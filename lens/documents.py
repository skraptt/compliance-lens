"""Read a procedure document into numbered paragraphs.

Each paragraph gets a stable id (P1, P2, ...) so findings can point back to it; the Word
add-in will use the same ids to highlight paragraphs. The section number a paragraph
starts with ("4.2") is kept separately for readable reports.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

SECTION = re.compile(r"^(\d+(?:\.\d+)*)\s+")


@dataclass
class Paragraph:
    pid: str
    text: str
    section: str | None
    heading: bool

    @property
    def label(self) -> str:
        return self.section or self.pid


def _from_lines(lines: list[tuple[str, bool]]) -> list[Paragraph]:
    out = []
    for text, heading in lines:
        text = " ".join(text.split())
        if not text:
            continue
        m = SECTION.match(text)
        out.append(Paragraph(pid=f"P{len(out) + 1}", text=text, section=m.group(1) if m else None, heading=heading))
    return out


def load(path: str | Path) -> list[Paragraph]:
    path = Path(path)
    if path.suffix.lower() == ".docx":
        import docx  # python-docx

        d = docx.Document(str(path))
        return _from_lines([(p.text, p.style.name.lower().startswith(("heading", "title"))) for p in d.paragraphs])
    if path.suffix.lower() in (".md", ".txt"):
        lines = []
        for raw in path.read_text(encoding="utf-8").splitlines():
            heading = raw.startswith("#")
            lines.append((raw.lstrip("#").strip(), heading))
        return _from_lines(lines)
    raise ValueError(f"unsupported file type: {path.suffix}")


def render(paragraphs: list[Paragraph]) -> str:
    """Paragraphs as the model sees them: one per line, prefixed with their id."""
    return "\n".join(f"[{p.pid}]{' (heading)' if p.heading else ''} {p.text}" for p in paragraphs)
