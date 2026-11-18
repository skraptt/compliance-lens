"""Offline tests: no API key or network needed. Run: python -m unittest discover tests"""
import datetime as dt
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from lens import analyze, checklist, documents, evaluate  # noqa: E402

CL = checklist.load(ROOT / "obligations/remit.yaml")
PROFILE = yaml.safe_load((ROOT / "demo/nordwind/profile.yaml").read_text(encoding="utf-8"))
KEY = yaml.safe_load((ROOT / "demo/nordwind/answer_key.yaml").read_text(encoding="utf-8"))
AS_OF = dt.date(2026, 11, 18)


class TestChecklist(unittest.TestCase):
    def test_profile_filters_addressees(self):
        checks = checklist.select(CL, PROFILE["profile"], ["IIP"], today=AS_OF)
        items = {c.item_id for c in checks}
        self.assertIn("REMIT-DIS-04", items)           # mp_disclosing
        self.assertNotIn("REMIT-INS-02", items)        # not an Art 3(4)(b) operator
        self.assertNotIn("REMIT-STR-01", items)        # not a PPAT/PPET (and wrong document)

    def test_upcoming_items_are_not_run(self):
        checks = checklist.select(CL, PROFILE["profile"], ["TRP"], today=AS_OF)
        rep04 = [c for c in checks if c.item_id == "REMIT-REP-04"]
        self.assertTrue(rep04 and all(c.state == "upcoming" for c in rep04))
        later = checklist.select(CL, PROFILE["profile"], ["TRP"], today=dt.date(2027, 2, 1))
        self.assertTrue(all(c.state == "run" for c in later if c.item_id == "REMIT-REP-04"))

    def test_date_gated_check(self):
        checks = {c.key: c for c in checklist.select(CL, PROFILE["profile"], ["TRP"], today=AS_OF)}
        self.assertEqual(checks["REMIT-REP-06.c2"].state, "upcoming")
        self.assertEqual(checks["REMIT-REP-06.c1"].state, "run")

    def test_primary_document(self):
        checks = {c.key: c for c in checklist.select(CL, PROFILE["profile"], ["MCP"], today=AS_OF)}
        self.assertTrue(checks["REMIT-MAN-01.c1"].primary)
        self.assertFalse(checks["REMIT-INS-01.c1"].primary)   # primary document is IIP

    def test_answer_key_matches_runnable_primary_checks(self):
        for d in PROFILE["documents"]:
            run = {c.key for c in checklist.select(CL, PROFILE["profile"], d["types"], today=AS_OF)
                   if c.state == "run" and c.primary}
            self.assertEqual(run, set(KEY["documents"][d["file"]]), d["file"])


class TestDocuments(unittest.TestCase):
    def test_docx_and_md_agree(self):
        a = documents.load(ROOT / "demo/nordwind/inside-information-policy.docx")
        b = documents.load(ROOT / "demo/nordwind/src/inside-information-policy.md")
        self.assertEqual([p.text for p in a], [p.text for p in b])
        self.assertEqual(next(p for p in a if p.section == "4.2").text[:3], "4.2")


class TestPipeline(unittest.TestCase):
    def fake_model(self, statuses):
        def transport(payload):
            prompt = payload["messages"][0]["content"][1]["text"]
            keys = [l.split("key: ", 1)[1] for l in prompt.splitlines() if l.startswith("- key: ")]
            return {"content": [{"type": "tool_use", "name": "record_findings", "input": {"findings": [
                {"check": k, "status": statuses.get(k, "missing"), "paragraphs": ["P3", "P999"], "evidence": "x",
                 "explanation": "y"} for k in keys]}}]}
        return transport

    def test_every_check_answered_once_and_bad_paragraphs_dropped(self):
        paras = documents.load(ROOT / "demo/nordwind/market-conduct-policy.docx")
        checks = checklist.select(CL, PROFILE["profile"], ["MCP", "ALG"], today=AS_OF)
        out = analyze.analyse("x", "Nordwind", paras, checks, transport=self.fake_model({}), batch_size=7, log=lambda m: None)
        self.assertEqual(len(out), len(checks))
        ran = [f for f in out if f.status in analyze.STATUSES]
        self.assertTrue(ran and all(f.paragraphs == ["P3"] for f in ran))

    def test_retry_for_unanswered_checks(self):
        calls = []

        def flaky(payload):
            calls.append(1)
            prompt = payload["messages"][0]["content"][1]["text"]
            keys = [l.split("key: ", 1)[1] for l in prompt.splitlines() if l.startswith("- key: ")]
            keys = keys[:1] if len(calls) == 1 else keys      # first call answers only one check
            return {"content": [{"type": "tool_use", "name": "record_findings", "input": {"findings": [
                {"check": k, "status": "covered", "paragraphs": [], "evidence": "", "explanation": ""} for k in keys]}}]}

        paras = documents.load(ROOT / "demo/nordwind/market-conduct-policy.docx")
        checks = [c for c in checklist.select(CL, PROFILE["profile"], ["MCP"], today=AS_OF) if c.state == "run"][:5]
        out = analyze.analyse("x", "Nordwind", paras, checks, transport=flaky, log=lambda m: None)
        self.assertEqual(len(calls), 2)
        self.assertEqual(len(out), 5)

    def test_mock_run_scores_perfectly_and_report_renders(self):
        with tempfile.TemporaryDirectory() as tmp:
            cmd = [sys.executable, "-m", "lens", "analyze", "demo/nordwind/profile.yaml", "--as-of", "2026-11-18",
                   "--mock-key", "demo/nordwind/answer_key.yaml", "--out", tmp]
            subprocess.run(cmd, cwd=ROOT, check=True, capture_output=True)
            run = json.loads(Path(tmp, "findings.json").read_text(encoding="utf-8"))
            s = evaluate.score(run, KEY)
            self.assertEqual(s["accuracy"][0], s["accuracy"][1])
            self.assertEqual(s["planted_found"][0], s["planted_found"][1])
            rep = Path(tmp, "report.md").read_text(encoding="utf-8")
            self.assertIn("Conflicts with REMIT", rep)
            self.assertIn("REMIT-DIS-04.c4", rep)

    def test_eval_counts_mistakes(self):
        run = {"documents": [{"file": "transaction-reporting-procedure.docx", "findings": [
            {"check": "REMIT-REP-02.c2", "status": "covered", "basis": "law", "primary": True},   # planted, missed
            {"check": "REMIT-REP-02.c1", "status": "partial", "basis": "law", "primary": True},   # accepted alternative
        ]}]}
        s = evaluate.score(run, KEY)
        rows = {r["check"]: r for r in s["rows"]}
        self.assertFalse(rows["REMIT-REP-02.c2"]["ok"])
        self.assertTrue(rows["REMIT-REP-02.c1"]["ok"])


if __name__ == "__main__":
    unittest.main()
