"""Draw the add-in icons (a teal lens ring) as PNGs, standard library only.

Usage: python scripts/make_icons.py addin/assets
"""
import struct
import sys
import zlib
from pathlib import Path

TEAL = (15, 110, 110)


def png(size: int) -> bytes:
    rows = []
    c = (size - 1) / 2
    outer, inner = size * 0.40, size * 0.26
    for y in range(size):
        row = bytearray([0])  # filter: none
        for x in range(size):
            d = ((x - c) ** 2 + (y - c) ** 2) ** 0.5
            # anti-aliased ring plus a short handle to the lower right
            ring = max(0.0, min(1.0, outer + 0.5 - d)) * max(0.0, min(1.0, d - inner + 0.5))
            hx, hy = x - c, y - c
            on_handle = hx > outer * 0.55 and hy > outer * 0.55 and abs(hx - hy) < size * 0.09 and hx < size * 0.48
            a = 1.0 if on_handle else ring
            row += bytes((*TEAL, int(255 * a)))
        rows.append(bytes(row))
    raw = zlib.compress(b"".join(rows), 9)

    def chunk(tag, data):
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0)) + chunk(b"IDAT", raw) + chunk(b"IEND", b"")


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "addin/assets")
    out.mkdir(parents=True, exist_ok=True)
    for s in (16, 32, 64, 80, 128):
        (out / f"icon-{s}.png").write_bytes(png(s))
        print("wrote", out / f"icon-{s}.png")
