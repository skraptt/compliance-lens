"""Compliance Lens command line.

  python -m lens analyze demo/nordwind/profile.yaml --out runs/nordwind
  python -m lens analyze demo/nordwind/profile.yaml --dry-run          # print the prompts, no API call
  python -m lens analyze demo/nordwind/profile.yaml --mock-key demo/nordwind/answer_key.yaml   # offline pipeline test
  python -m lens eval runs/nordwind/findings.json demo/nordwind/answer_key.yaml

Needs ANTHROPIC_API_KEY for real runs.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

import yaml

from . import analyze, checklist, documents, evaluate, llm, report

ROOT = Path(__file__).resolve().parent.parent


def mock_transport(key: dict, doc_file: str):
    """A fake model that answers from the answer key (pipeline test, no API)."""
    expected = key["documents"].get(doc_file, {})

    def transport(payload):
        prompt = payload["messages"][0]["content"][1]["text"]
        keys = [line.split("key: ", 1)[1].strip() for line in prompt.splitlines() if line.startswith("- key: ")]
        findings = [{"check": k, "status": expected.get(k, {}).get("expected", "missing"), "paragraphs": [],
                     "evidence": "", "explanation": "mock"} for k in keys]
        return {"content": [{"type": "tool_use", "name": "record_findings", "input": {"findings": findings}}]}

    return transport


def replay_transport(responses: dict, doc_file: str):
    """Answer from saved model output ({doc_file: [findings]}), e.g. a run made elsewhere."""
    saved = {f["check"]: f for f in responses.get(doc_file, [])}

    def transport(payload):
        prompt = payload["messages"][0]["content"][1]["text"]
        keys = [line.split("key: ", 1)[1].strip() for line in prompt.splitlines() if line.startswith("- key: ")]
        return {"content": [{"type": "tool_use", "name": "record_findings",
                             "input": {"findings": [saved[k] for k in keys if k in saved]}}]}

    return transport


def cmd_analyze(a) -> int:
    prof_path = Path(a.profile)
    prof = yaml.safe_load(prof_path.read_text(encoding="utf-8"))
    cl = checklist.load(a.checklist)
    as_of = dt.date.fromisoformat(a.as_of) if a.as_of else dt.date.today()
    key = yaml.safe_load(Path(a.mock_key).read_text(encoding="utf-8")) if a.mock_key else None
    replay = json.loads(Path(a.replay).read_text(encoding="utf-8")) if a.replay else None
    model = "mock" if key else (a.replay_label or "replay") if replay else a.model

    run = {"company": prof["company"], "checklist_version": cl["meta"]["version"], "as_of": str(as_of),
           "model": model, "documents": []}
    for d in prof["documents"]:
        path = prof_path.parent / d["file"]
        paras = documents.load(path)
        checks = checklist.select(cl, prof["profile"], d["types"], today=as_of)
        n = sum(1 for c in checks if c.state == "run")
        print(f"{d['file']}: {len(paras)} paragraphs, {n} checks", file=sys.stderr)
        transport = mock_transport(key, d["file"]) if key else replay_transport(replay, d["file"]) if replay else None
        findings = analyze.analyse(d["file"], prof["company"], paras, checks, model=a.model,
                                   batch_size=a.batch_size, transport=transport, dry_run=a.dry_run,
                                   log=lambda m: print(m, file=sys.stderr))
        if a.dry_run:
            continue
        run["documents"].append({"file": d["file"], "types": d["types"], "findings": analyze.to_json(findings)})
    if a.dry_run:
        return 0

    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "findings.json").write_text(json.dumps(run, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "report.md").write_text(report.render(run), encoding="utf-8")
    print(f"wrote {out / 'findings.json'} and {out / 'report.md'}", file=sys.stderr)
    return 0


def cmd_eval(a) -> int:
    run = json.loads(Path(a.findings).read_text(encoding="utf-8"))
    key = yaml.safe_load(Path(a.key).read_text(encoding="utf-8"))
    print(evaluate.render(evaluate.score(run, key)))
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="lens")
    sub = p.add_subparsers(dest="cmd", required=True)
    an = sub.add_parser("analyze", help="check a company's documents")
    an.add_argument("profile")
    an.add_argument("--checklist", default=str(ROOT / "obligations/remit.yaml"))
    an.add_argument("--as-of", help="assessment date (YYYY-MM-DD), default today")
    an.add_argument("--model", default=llm.DEFAULT_MODEL)
    an.add_argument("--batch-size", type=int, default=20)
    an.add_argument("--out", default="runs/latest")
    an.add_argument("--dry-run", action="store_true")
    an.add_argument("--mock-key", help="answer key to use as a fake model")
    an.add_argument("--replay", help="JSON file with saved model findings per document")
    an.add_argument("--replay-label", help="model name to show in the report for a replayed run")
    an.set_defaults(func=cmd_analyze)
    ev = sub.add_parser("eval", help="score a run against an answer key")
    ev.add_argument("findings")
    ev.add_argument("key")
    ev.set_defaults(func=cmd_eval)
    a = p.parse_args(argv)
    return a.func(a)


if __name__ == "__main__":
    sys.exit(main())
