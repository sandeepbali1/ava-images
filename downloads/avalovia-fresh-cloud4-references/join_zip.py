#!/usr/bin/env python3
"""Verify and reconstruct the reference archive without overwriting files."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
info = json.loads((root / 'parts.json').read_text())
target = root / info['archive']['filename']
if target.exists():
    raise SystemExit(f'Refusing overwrite: {target}')

def digest(path):
    h = hashlib.sha256()
    size = 0
    with path.open('rb') as stream:
        while block := stream.read(1024 * 1024):
            h.update(block)
            size += len(block)
    return size, h.hexdigest()

for part in info['parts']:
    if digest(root / part['filename']) != (part['bytes'], part['sha256']):
        raise SystemExit(f'Part verification failed: {part["filename"]}')
h = hashlib.sha256()
size = 0
with target.open('xb') as output:
    for part in info['parts']:
        with (root / part['filename']).open('rb') as stream:
            while block := stream.read(1024 * 1024):
                output.write(block)
                h.update(block)
                size += len(block)
if (size, h.hexdigest()) != (info['archive']['bytes'], info['archive']['sha256']):
    raise SystemExit('Reconstruction verification failed; output preserved for inspection.')
print(f'Verified {target.name}: {size} bytes')
