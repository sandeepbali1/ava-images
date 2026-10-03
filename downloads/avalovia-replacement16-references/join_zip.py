#!/usr/bin/env python3
"""Verify and reconstruct archives without overwriting existing files."""
import hashlib
import json
from pathlib import Path

base = Path(__file__).resolve().parent
metadata = json.loads((base / 'parts.json').read_text())

def verify(data, record):
    if len(data) != record['bytes'] or hashlib.sha256(data).hexdigest() != record['sha256']:
        raise ValueError('Byte count or SHA256 mismatch: ' + record['filename'])

# Check every part and complete archive before writing any output.
for archive in metadata['archives']:
    target = base / archive['filename']
    if target.exists():
        raise FileExistsError('Refusing to overwrite: ' + str(target))
    digest = hashlib.sha256()
    size = 0
    for part in archive['parts']:
        data = (base / part['filename']).read_bytes()
        verify(data, part)
        digest.update(data)
        size += len(data)
    if size != archive['bytes'] or digest.hexdigest() != archive['sha256']:
        raise ValueError('Archive reconstruction mismatch: ' + archive['filename'])

for archive in metadata['archives']:
    target = base / archive['filename']
    with target.open('xb') as output:
        for part in archive['parts']:
            data = (base / part['filename']).read_bytes()
            verify(data, part)
            output.write(data)
    verify(target.read_bytes(), archive)
    print('Verified:', target.name)
