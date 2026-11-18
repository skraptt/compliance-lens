"""Check one document against the applicable checks."""
from __future__ import annotations

from dataclasses import asdict, dataclass

from . import documents, llm
from .checklist import Check

STATUSES = ("covered", "partial", "missing", "contradicts")

SYSTEM = """You are an experienced EU energy-regulation lawyer reviewing a company's internal compliance procedure against a REMIT checklist.

For each check, decide what the document says and give one status:
- covered: the document clearly states what the check asks for.
- partial: the document addresses the point but incompletely, vaguely, or only by implication.
- missing: the document does not address the point.
- contradicts: the document states something inconsistent with the check or with the requirement behind it (for example a longer deadline, a narrower scope, an excluded group, a shorter retention period, or a practice the law prohibits).

Rules:
- Judge only the text of this document. Do not assume that other documents cover the point.
- A rule that is stricter than required counts as covered (for example a shorter deadline).
- Read the requirement behind each check: a document can contradict the requirement even when it does not use the same words.
- Cite the ids of the paragraphs you rely on (e.g. "P12"). For missing, cite none.
- evidence: a short verbatim quote (at most 30 words) from the cited paragraph; empty for missing.
- explanation: at most 40 words, in English, saying what is present or absent and why it matters; for contradicts, state the conflict precisely.
- Return every check exactly once, using its key."""

TOOL = {
    "name": "record_findings",
    "description": "Record the assessment of each check against the document.",
    "input_schema": {
        "type": "object",
        "properties": {
            "findings": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "check": {"type": "string", "description": "check key, e.g. REMIT-DIS-04.c4"},
                        "status": {"type": "string", "enum": list(STATUSES)},
                        "paragraphs": {"type": "array", "items": {"type": "string"}},
                        "evidence": {"type": "string"},
                        "explanation": {"type": "string"},
                    },
                    "required": ["check", "status", "paragraphs", "evidence", "explanation"],
                },
            }
        },
        "required": ["findings"],
    },
}

BASIS_LABEL = {"law": "LAW", "guidance": "ACER expectation", "good_practice": "good practice"}


@dataclass
class Finding:
    check: str
    status: str            # covered | partial | missing | contradicts | upcoming | not_applicable
    basis: str
    primary: bool
    item_id: str
    item_title: str
    check_text: str
    legal_basis: list
    paragraphs: list
    sections: list
    evidence: str
    explanation: str


def _context(doc_name: str, company: str, paras: list[documents.Paragraph]) -> str:
    return f"Company: {company}\nDocument: {doc_name}\n\n<document>\n{documents.render(paras)}\n</document>"


def _prompt(checks: list[Check]) -> str:
    lines = ["Assess these checks against the document above.\n"]
    for c in checks:
        lines.append(
            f"- key: {c.key}\n  basis: {BASIS_LABEL[c.basis]}\n  check: {c.text}\n"
            f"  obligation: {c.item_title} ({', '.join(c.legal_basis) or 'non-binding'})\n"
            f"  requirement: {c.requirement}"
        )
    return "\n".join(lines)


def batches(items: list, size: int) -> list[list]:
    return [items[i:i + size] for i in range(0, len(items), size)]


def analyse(doc_name: str, company: str, paras: list[documents.Paragraph], checks: list[Check], *,
            model: str = llm.DEFAULT_MODEL, batch_size: int = 20, transport=None, dry_run: bool = False,
            log=print) -> list[Finding]:
    by_pid = {p.pid: p for p in paras}
    context = _context(doc_name, company, paras)
    to_run = [c for c in checks if c.state == "run"]
    results: dict[str, dict] = {}

    for batch in batches(to_run, batch_size):
        prompt = _prompt(batch)
        if dry_run:
            log(f"--- system ---\n{SYSTEM}\n--- cached context ---\n{context}\n--- prompt ---\n{prompt}")
            return []
        pending = batch
        for attempt in range(2):
            out = llm.call_tool(system=SYSTEM, cached_context=context, prompt=_prompt(pending), tool=TOOL,
                                model=model, transport=transport)
            wanted = {c.key for c in pending}
            for f in out.get("findings", []):
                if f.get("check") in wanted and f.get("status") in STATUSES:
                    results[f["check"]] = f
            pending = [c for c in pending if c.key not in results]
            if not pending:
                break
            log(f"  {len(pending)} checks unanswered, asking again")
        for c in pending:
            log(f"  warning: no answer for {c.key}")

    findings = []
    for c in checks:
        if c.state != "run":
            findings.append(Finding(c.key, c.state, c.basis, c.primary, c.item_id, c.item_title, c.text,
                                    c.legal_basis, [], [], "", c.reason))
            continue
        r = results.get(c.key)
        if not r:
            continue
        pids = [p for p in r.get("paragraphs", []) if p in by_pid]
        findings.append(Finding(
            c.key, r["status"], c.basis, c.primary, c.item_id, c.item_title, c.text, c.legal_basis,
            pids, [by_pid[p].label for p in pids], r.get("evidence", ""), r.get("explanation", ""),
        ))
    return findings


def to_json(findings: list[Finding]) -> list[dict]:
    return [asdict(f) for f in findings]
