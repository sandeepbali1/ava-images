#!/usr/bin/env python3
"""Join and verify transfer parts without overwriting a destination."""
import hashlib, json, sys
from pathlib import Path
root = Path(__file__).resolve().parent
meta = json.loads((root / "parts.json").read_text())
if len(sys.argv) != 2:
    raise SystemExit("Usage: python join_zip.py NEW_OUTPUT_ZIP")
target = Path(sys.argv[1])
if target.exists():
    raise SystemExit("Refusing to overwrite existing destination")
for part in meta["parts"]:
    p = root / part["filename"]
    data = p.read_bytes()
    if len(data) != part["bytes"] or hashlib.sha256(data).hexdigest() != part["sha256"]:
        raise SystemExit("Part size/hash mismatch: " + p.name)
digest = hashlib.sha256()
size = 0
with target.open("xb") as output:
    for part in meta["parts"]:
        with (root / part["filename"]).open("rb") as source:
            while chunk := source.read(1024 * 1024):
                output.write(chunk)
                digest.update(chunk)
                size += len(chunk)
if size != meta["archive"]["bytes"] or digest.hexdigest() != meta["archive"]["sha256"]:
    raise SystemExit("Archive size/hash mismatch; output retained for diagnosis")
print(str(target))
