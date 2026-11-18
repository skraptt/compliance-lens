"""Score a run against an answer key."""
from __future__ import annotations

from collections import Counter

STATUSES = ("covered", "partial", "missing", "contradicts")


def score(run: dict, key: dict) -> dict:
    rows = []
    for d in run["documents"]:
        expected = key["documents"].get(d["file"], {})
        got = {f["check"]: f for f in d["findings"] if f["primary"] and f["status"] in STATUSES}
        for check, exp in expected.items():
            f = got.get(check)
            status = f["status"] if f else "absent"
            basis = f["basis"] if f else "?"
            ok = status == exp["expected"] or status in exp.get("accept", [])
            rows.append({"doc": d["file"], "check": check, "expected": exp["expected"], "got": status,
                         "ok": ok, "basis": basis, "planted": bool(exp.get("planted"))})

    def acc(sel):
        sel = list(sel)
        return (sum(r["ok"] for r in sel), len(sel))

    problem = lambda s: s in ("partial", "missing", "contradicts")
    tp = sum(1 for r in rows if problem(r["expected"]) and problem(r["got"]))
    fp = sum(1 for r in rows if not problem(r["expected"]) and problem(r["got"]))
    fn = sum(1 for r in rows if problem(r["expected"]) and not problem(r["got"]))
    planted = [r for r in rows if r["planted"]]
    return {
        "rows": rows,
        "accuracy": acc(rows),
        "accuracy_law": acc(r for r in rows if r["basis"] == "law"),
        "problem_precision": tp / (tp + fp) if tp + fp else 1.0,
        "problem_recall": tp / (tp + fn) if tp + fn else 1.0,
        "planted_found": (sum(1 for r in planted if problem(r["got"])), len(planted)),
        "planted_exact": acc(planted),
        "confusion": Counter((r["expected"], r["got"]) for r in rows),
    }


def render(s: dict) -> str:
    a, n = s["accuracy"]
    al, nl = s["accuracy_law"]
    pf, pn = s["planted_found"]
    pe, _ = s["planted_exact"]
    lines = [
        f"status accuracy        {a}/{n} ({a / n:.0%})" if n else "no rows",
        f"  on law checks        {al}/{nl} ({al / nl:.0%})" if nl else "",
        f"problem precision      {s['problem_precision']:.0%}   (flagged problems that are real)",
        f"problem recall         {s['problem_recall']:.0%}   (real problems that were flagged)",
        f"planted errors found   {pf}/{pn}   (exact status {pe}/{pn})",
        "",
        "expected -> got        count",
    ]
    for (e, g), c in sorted(s["confusion"].items()):
        if e != g:
            lines.append(f"  {e:<11} -> {g:<11} {c}")
    wrong = [r for r in s["rows"] if not r["ok"]]
    if wrong:
        lines += ["", "mismatches:"]
        lines += [f"  {r['doc'][:28]:<28} {r['check']:<20} expected {r['expected']:<11} got {r['got']}{'  [planted]' if r['planted'] else ''}" for r in wrong]
    return "\n".join(l for l in lines if l is not None)
