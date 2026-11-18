"""Markdown report from findings."""
from __future__ import annotations

PROBLEM = ("contradicts", "missing", "partial")

GROUPS = [
    ("Conflicts with REMIT", lambda f: f["basis"] == "law" and f["status"] == "contradicts"),
    ("Gaps (required by law, missing)", lambda f: f["basis"] == "law" and f["status"] == "missing"),
    ("Weak points (required by law, only partly covered)", lambda f: f["basis"] == "law" and f["status"] == "partial"),
    ("ACER expects", lambda f: f["basis"] == "guidance" and f["status"] in PROBLEM),
    ("Recommendations (good practice)", lambda f: f["basis"] == "good_practice" and f["status"] in PROBLEM),
]
ORDER = {"contradicts": 0, "missing": 1, "partial": 2}


def _line(f: dict) -> list[str]:
    where = f" · §{', §'.join(f['sections'])}" if f["sections"] else ""
    out = [f"- **{f['check']}** {f['check_text']}{where}  "]
    if f["explanation"]:
        out.append(f"  {f['explanation']}  ")
    if f["evidence"]:
        out.append(f"  > {f['evidence']}  ")
    out.append(f"  _{f['item_title']} — {', '.join(f['legal_basis']) or 'non-binding'}_")
    return out


def document_report(name: str, findings: list[dict]) -> str:
    prim = [f for f in findings if f["primary"] and f["status"] not in ("upcoming", "not_applicable")]
    sec = [f for f in findings if not f["primary"] and f["status"] in PROBLEM]
    upcoming = sorted({(f["item_id"], f["item_title"], f["explanation"]) for f in findings if f["status"] == "upcoming"})
    covered = [f for f in prim if f["status"] == "covered"]

    count = lambda pred: sum(1 for f in prim if pred(f))
    lines = [
        f"## {name}",
        "",
        f"{len(prim)} checks · **{count(GROUPS[0][1])} conflicts** · **{count(GROUPS[1][1])} gaps** · "
        f"{count(GROUPS[2][1])} weak points · {count(GROUPS[3][1])} ACER expectations · "
        f"{count(GROUPS[4][1])} recommendations · {len(covered)} covered",
        "",
    ]
    for title, pred in GROUPS:
        group = sorted((f for f in prim if pred(f)), key=lambda f: ORDER.get(f["status"], 9))
        if not group:
            continue
        lines += [f"### {title}", ""]
        for f in group:
            lines += _line(f)
        lines.append("")
    if sec:
        lines += ["### May be covered in another document", ""]
        lines += [f"- {f['check']} ({f['status']}) {f['check_text']}" for f in sec]
        lines.append("")
    if upcoming:
        lines += ["### Not yet in force", ""]
        lines += [f"- {i} {t} — {why}" for i, t, why in upcoming]
        lines.append("")
    if covered:
        lines += ["<details><summary>Covered</summary>", ""]
        lines += [f"- {f['check']} §{', §'.join(f['sections']) or '—'} {f['check_text']}" for f in covered]
        lines += ["", "</details>", ""]
    return "\n".join(lines)


def render(run: dict) -> str:
    head = [
        f"# Compliance Lens report — {run['company']}",
        "",
        f"Checklist v{run['checklist_version']} · assessed as of {run['as_of']} · model {run['model']}",
        "",
        "Automated first-pass review. It reads only the documents supplied and is not legal advice; a lawyer should confirm each finding.",
        "",
    ]
    return "\n".join(head + [document_report(d["file"], d["findings"]) for d in run["documents"]])
