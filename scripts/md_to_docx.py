"""Build the demo .docx files from their markdown sources.

Usage: python scripts/md_to_docx.py demo/nordwind/src demo/nordwind
"""
import sys
from pathlib import Path

import docx
from docx.shared import Pt


def convert(src: Path, dst: Path) -> None:
    d = docx.Document()
    d.styles["Normal"].font.name = "Calibri"
    d.styles["Normal"].font.size = Pt(11)
    for raw in src.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("# "):
            d.add_heading(line[2:], level=0)
        elif line.startswith("## "):
            d.add_heading(line[3:], level=1)
        else:
            d.add_paragraph(line)
    d.core_properties.title = src.stem.replace("-", " ").title()
    d.core_properties.author = "Nordwind Energy Trading GmbH (fictional)"
    d.save(str(dst))


if __name__ == "__main__":
    src_dir, out_dir = Path(sys.argv[1]), Path(sys.argv[2])
    for md in sorted(src_dir.glob("*.md")):
        out = out_dir / f"{md.stem}.docx"
        convert(md, out)
        print("wrote", out)
