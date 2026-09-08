#!/usr/bin/env python3
"""Sanity-check config/glove80.keymap: every layer must have exactly 80 bindings
and every combo key position must be < 80. Cheap to run before pushing."""
import re
import sys
from pathlib import Path

KEYMAP = Path(__file__).resolve().parent.parent / "config" / "glove80.keymap"
EXPECTED = 80
ROWS = [10, 12, 12, 12, 18, 16]

src = KEYMAP.read_text()
src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)      # block comments
src = re.sub(r"//[^\n]*", "", src)                    # line comments
src = src.replace("&trans", "___").replace("&none", "XXX")

ok = True
keymap = src[src.index('compatible = "zmk,keymap"'):]
for m in re.finditer(r"(\w+)\s*\{\s*bindings\s*=\s*<(.*?)>\s*;", keymap, flags=re.S):
    name, body = m.group(1), m.group(2)
    lines = [l for l in body.splitlines() if l.strip()]
    per_row = [len(re.findall(r"&\w+|___|XXX", l)) for l in lines]
    total = sum(per_row)
    status = "ok " if total == EXPECTED and per_row == ROWS else "BAD"
    if status == "BAD":
        ok = False
    print(f"{status} {name:<14} {total:>3} keys  rows={per_row}")

for m in re.finditer(r"(?<!-)key-positions\s*=\s*<([^>]*)>", src):
    pos = [int(p) for p in m.group(1).split()]
    if any(p >= EXPECTED for p in pos):
        ok = False
        print(f"BAD combo position out of range: {pos}")

sys.exit(0 if ok else 1)
