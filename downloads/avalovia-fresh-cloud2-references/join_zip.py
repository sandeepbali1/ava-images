#!/usr/bin/env python3
"""Verify and join archive parts without overwriting an existing file."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
metadata = json.loads((root / 'parts.json').read_text())
archive = metadata['archive']
destination = root / archive['filename']
if destination.exists():
    raise SystemExit(f'Refusing to overwrite {destination}')
whole = hashlib.sha256()
size = 0
for part in metadata['parts']:
    data = (root / part['filename']).read_bytes()
    if len(data) != part['bytes'] or hashlib.sha256(data).hexdigest() != part['sha256']:
        raise SystemExit(f'Part verification failed: {part["filename"]}')
    whole.update(data)
    size += len(data)
if size != archive['bytes'] or whole.hexdigest() != archive['sha256']:
    raise SystemExit('Archive verification failed')
with destination.open('xb') as output:
    for part in metadata['parts']:
        data = (root / part['filename']).read_bytes()
        if len(data) != part['bytes'] or hashlib.sha256(data).hexdigest() != part['sha256']:
            raise SystemExit('Part changed during reconstruction')
        output.write(data)
if hashlib.sha256(destination.read_bytes()).hexdigest() != archive['sha256']:
    raise SystemExit('Reconstruction verification failed')
print(f'Verified archive: {destination}')
