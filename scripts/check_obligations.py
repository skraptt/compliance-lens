"""Check an obligation file and render a review sheet.

Usage: python scripts/check_obligations.py obligations/remit.yaml [--review out.md] [--taxonomy path/to/behaviours.yaml]
"""
import argparse
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

SECTIONS = {
    "obligations": ["id", "area", "title", "legal_basis", "binding", "applies_to", "status", "documents", "requirement", "checks"],
    "adjacent_regimes": ["id", "framework", "title", "legal_basis", "binding", "applies_to", "documents", "requirement", "checks"],
    "good_practice": ["id", "area", "title", "applies_to", "documents", "practice", "checks", "sources"],
}
BASES = ("law", "guidance", "good_practice")
BADGE = {"law": "LAW", "guidance": "ACER", "good_practice": "GOOD PRACTICE"}


def check(doc, behaviours=None):
    errors = []
    flags = set(doc.get("addressees", {}))
    doc_types = set(doc.get("document_types", {}))
    seen = set()
    for section, required in SECTIONS.items():
        for item in doc.get(section, []):
            oid = item.get("id", "?")
            for key in required:
                if not item.get(key):
                    errors.append(f"{oid}: missing {key}")
            if oid in seen:
                errors.append(f"{oid}: duplicate id")
            seen.add(oid)
            if section != "good_practice" and item.get("binding") not in ("law", "guidance"):
                errors.append(f"{oid}: binding must be law or guidance")
            if section == "obligations":
                if item.get("status") not in ("in_force", "upcoming"):
                    errors.append(f"{oid}: status must be in_force or upcoming")
                if item.get("status") == "upcoming" and not item.get("applies_from"):
                    errors.append(f"{oid}: upcoming obligation needs applies_from")
            for a in item.get("applies_to", []):
                if a not in flags:
                    errors.append(f"{oid}: unknown addressee '{a}'")
            for d in item.get("documents", []):
                if d not in doc_types:
                    errors.append(f"{oid}: unknown document type '{d}'")
            cids = [c.get("id") for c in item.get("checks", [])]
            if len(cids) != len(set(cids)):
                errors.append(f"{oid}: duplicate check ids")
            for c in item.get("checks", []):
                if c.get("basis") not in BASES:
                    errors.append(f"{oid}.{c.get('id')}: bad basis '{c.get('basis')}'")
                if not c.get("text"):
                    errors.append(f"{oid}.{c.get('id')}: empty text")
                w = c.get("when")
                if w and w not in flags and not re.match(r"^date >= \d{4}-\d{2}-\d{2}$", str(w)):
                    errors.append(f"{oid}.{c.get('id')}: bad when '{w}'")
            if section == "good_practice" and any(c.get("basis") == "law" for c in item.get("checks", [])):
                errors.append(f"{oid}: good-practice item has a law check")
            if behaviours is not None:
                for b in item.get("related_behaviours", []):
                    if b not in behaviours:
                        errors.append(f"{oid}: unknown behaviour '{b}'")
    return errors


def stats(doc):
    out = []
    for section in SECTIONS:
        items = doc.get(section, [])
        bases = Counter(c["basis"] for i in items for c in i.get("checks", []))
        out.append(f"{section}: {len(items)} items, {sum(bases.values())} checks "
                   f"({', '.join(f'{k} {v}' for k, v in sorted(bases.items()))})")
    return "\n".join(out)


def render_item(item, section):
    head = f"### {item['id']} · {item['title']}"
    meta = []
    if item.get("legal_basis"):
        meta.append("*" + ", ".join(item["legal_basis"]) + "*")
    if item.get("binding"):
        meta.append(item["binding"])
    meta.append("applies to: " + ", ".join(item["applies_to"]))
    meta.append("documents: " + ", ".join(item["documents"]))
    if item.get("applies_from"):
        meta.append(f"**applies from {item['applies_from']}**")
    lines = [head, " · ".join(meta), "", (item.get("requirement") or item.get("practice")).strip(), "", "Checks:"]
    for c in item["checks"]:
        when = f" _(only if {c['when']})_" if c.get("when") else ""
        lines.append(f"- [ ] `{c['id']}` **[{BADGE[c['basis']]}]** {c['text']}{when}")
    refs = item.get("guidance") or item.get("sources")
    if refs:
        lines += ["", "Sources: " + "; ".join(refs)]
    if item.get("notes"):
        lines += ["", "> " + " ".join(str(item["notes"]).split())]
    lines += ["", "Reviewer comments:", "", "---", ""]
    return lines


def review_sheet(doc):
    m = doc["meta"]
    lines = [
        f"# Review sheet: REMIT checklist v{m['version']}",
        "",
        f"Status **{m['status']}** · sources fetched {m['sources_fetched']} · ACER Guidance edition {m['acer_guidance_edition']}",
        "",
        "Badges: **[LAW]** missing = gap · **[ACER]** missing = \"ACER expects\" · **[GOOD PRACTICE]** missing = recommendation only.",
        "Tick each check you agree with; write corrections next to anything wrong.",
        "",
        "```",
        stats(doc),
        "```",
        "",
    ]
    titles = {"obligations": "Part A — REMIT obligations", "adjacent_regimes": "Part B — Adjacent regime (MAR)", "good_practice": "Part C — Good practice (non-binding)"}
    for section in SECTIONS:
        lines += [f"# {titles[section]}", ""]
        area = None
        for item in doc.get(section, []):
            a = item.get("area") or item.get("framework")
            if a != area:
                area = a
                lines += [f"## {a.replace('_', ' ').title()}", ""]
            lines += render_item(item, section)
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("file")
    p.add_argument("--review")
    p.add_argument("--taxonomy")
    args = p.parse_args()
    doc = yaml.safe_load(Path(args.file).read_text(encoding="utf-8"))
    behaviours = None
    if args.taxonomy:
        behaviours = {b["id"] for b in yaml.safe_load(Path(args.taxonomy).read_text(encoding="utf-8"))["behaviours"]}
    errors = check(doc, behaviours)
    print(stats(doc))
    for e in errors:
        print("ERROR", e)
    if args.review:
        Path(args.review).write_text(review_sheet(doc), encoding="utf-8")
        print("review sheet ->", args.review)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
