#!/usr/bin/env python3
"""Verify and reconstruct archives beside this script; refuse overwrites."""
import hashlib
import json
from pathlib import Path

base = Path(__file__).resolve().parent
catalog = json.loads((base / 'parts.json').read_text())
for archive in catalog['archives']:
    target = base / archive['filename']
    if target.exists():
        raise SystemExit(f'Refusing overwrite: {target.name}')
    total = 0
    digest = hashlib.sha256()
    for part in archive['parts']:
        path = base / part['filename']
        data = path.read_bytes()
        if len(data) != part['bytes'] or hashlib.sha256(data).hexdigest() != part['sha256']:
            raise SystemExit(f'Invalid part: {path.name}')
        total += len(data)
        digest.update(data)
    if total != archive['bytes'] or digest.hexdigest() != archive['sha256']:
        raise SystemExit(f'Invalid reconstruction: {target.name}')
    with target.open('xb') as dest:
        for part in archive['parts']:
            with (base / part['filename']).open('rb') as source:
                while chunk := source.read(1024 * 1024):
                    dest.write(chunk)
    if target.stat().st_size != archive['bytes'] or hashlib.sha256(target.read_bytes()).hexdigest() != archive['sha256']:
        raise SystemExit(f'Reconstruction verification failed: {target.name}')
    print(f'Verified {target.name}')
