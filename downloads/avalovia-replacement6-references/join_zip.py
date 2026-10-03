#!/usr/bin/env python3
"""Verify and reconstruct these reference archives without overwriting files."""
import hashlib
import json
from pathlib import Path

base = Path(__file__).resolve().parent
metadata = json.loads((base / 'parts.json').read_text())

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

for archive in metadata['archives']:
    target = base / archive['filename']
    if target.exists():
        raise FileExistsError(f'Refusing overwrite: {target.name}')
    for part in archive['parts']:
        path = base / part['filename']
        if path.stat().st_size != part['bytes'] or digest(path) != part['sha256']:
            raise ValueError(f'Part verification failed: {path.name}')

for archive in metadata['archives']:
    target = base / archive['filename']
    h = hashlib.sha256()
    count = 0
    with target.open('xb') as output:
        for part in archive['parts']:
            with (base / part['filename']).open('rb') as stream:
                for block in iter(lambda: stream.read(1024 * 1024), b''):
                    output.write(block)
                    h.update(block)
                    count += len(block)
    if count != archive['bytes'] or h.hexdigest() != archive['sha256']:
        raise ValueError(f'Archive verification failed: {target.name}')
    print(f'Verified {target.name}: {archive["reference_count"]} references')
