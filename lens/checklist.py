"""Select the checks that apply to a company and a document.

A check is run against a document when its item applies to the company profile and the
document is tagged with one of the item's document types. The first entry in `documents`
is the item's primary document; findings on other documents are reported as
"may be covered elsewhere" rather than as gaps.
"""
from __future__ import annotations

import datetime as dt
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

SECTIONS = ("obligations", "adjacent_regimes", "good_practice")
ALWAYS = {"any_person"}


@dataclass
class Check:
    item_id: str
    check_id: str
    basis: str            # law | guidance | good_practice
    text: str
    section: str          # obligations | adjacent_regimes | good_practice
    item_title: str
    legal_basis: list[str]
    requirement: str
    primary: bool         # this document is the item's primary document
    state: str = "run"    # run | upcoming | not_applicable
    reason: str = ""
    sources: list[str] = field(default_factory=list)

    @property
    def key(self) -> str:
        return f"{self.item_id}.{self.check_id}"


def load(path: str | Path) -> dict:
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


def _applies(item: dict, flags: set[str]) -> bool:
    return any(a in flags or a in ALWAYS for a in item.get("applies_to", []))


def _when_ok(when, flags: set[str], today: dt.date) -> tuple[bool, str]:
    if not when:
        return True, ""
    m = re.match(r"^date >= (\d{4}-\d{2}-\d{2})$", str(when))
    if m:
        start = dt.date.fromisoformat(m.group(1))
        return today >= start, f"applies from {start}"
    return when in flags, f"only if {when}"


def select(checklist: dict, profile: dict, doc_types: list[str], today: dt.date | None = None) -> list[Check]:
    """Checks for one document, in checklist order."""
    today = today or dt.date.today()
    flags = {k for k, v in profile.items() if v}
    out: list[Check] = []
    for section in SECTIONS:
        for item in checklist.get(section, []):
            docs = item.get("documents", [])
            if not set(docs) & set(doc_types) and "CM" not in doc_types:
                continue
            if not _applies(item, flags):
                continue
            primary = bool(docs) and (docs[0] in doc_types or "CM" in doc_types)
            upcoming = item.get("status") == "upcoming" and item.get("applies_from") and today < dt.date.fromisoformat(str(item["applies_from"]))
            for c in item.get("checks", []):
                ok, why = _when_ok(c.get("when"), flags, today)
                state, reason = "run", ""
                if upcoming:
                    state, reason = "upcoming", f"applies from {item['applies_from']}"
                elif not ok:
                    state, reason = ("upcoming", why) if why.startswith("applies from") else ("not_applicable", why)
                out.append(Check(
                    item_id=item["id"], check_id=c["id"], basis=c["basis"], text=c["text"],
                    section=section, item_title=item["title"],
                    legal_basis=item.get("legal_basis", []),
                    requirement=" ".join(str(item.get("requirement") or item.get("practice", "")).split()),
                    primary=primary, state=state, reason=reason,
                    sources=item.get("guidance") or item.get("sources") or [],
                ))
    return out
