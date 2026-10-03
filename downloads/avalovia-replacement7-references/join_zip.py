#!/usr/bin/env python3
"""Verify and join ordinary binary parts without overwriting any file."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
meta = json.loads((root / 'parts.json').read_text())
target = root / meta['archive']['filename']
if target.exists():
    raise SystemExit(f'Refusing to overwrite {target}')
for part in meta['parts']:
    path = root / part['filename']
    if path.stat().st_size != part['bytes']:
        raise SystemExit(f'Size mismatch: {path.name}')
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    if digest.hexdigest() != part['sha256']:
        raise SystemExit(f'SHA256 mismatch: {path.name}')
digest = hashlib.sha256()
size = 0
with target.open('xb') as output:
    for part in meta['parts']:
        with (root / part['filename']).open('rb') as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b''):
                output.write(block)
                digest.update(block)
                size += len(block)
if size != meta['archive']['bytes'] or digest.hexdigest() != meta['archive']['sha256']:
    raise SystemExit('Reconstruction verification failed; output retained for diagnosis.')
print(f'Verified {target.name}: {size} bytes, {meta["reference_count"]} references')
