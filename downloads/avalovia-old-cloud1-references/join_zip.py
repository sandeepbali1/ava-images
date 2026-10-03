#!/usr/bin/env python3
"""Reconstruct byte-verified ZIP archives; never overwrite existing outputs."""
import hashlib
import json
from pathlib import Path
import sys

base = Path(__file__).resolve().parent
manifest = json.loads((base / 'parts.json').read_text())
out = Path(sys.argv[1]) if len(sys.argv) == 2 else base / 'reconstructed'
out.mkdir(parents=True, exist_ok=True)
for archive in manifest['archives']:
    target = out / archive['filename']
    if target.exists():
        raise SystemExit(f'Refusing overwrite: {target}')
    for part in archive['parts']:
        path = base / part['filename']
        h = hashlib.sha256()
        size = 0
        with path.open('rb') as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b''):
                size += len(chunk)
                h.update(chunk)
        if size != part['bytes'] or h.hexdigest() != part['sha256']:
            raise SystemExit(f'Part verification failed: {path}')
for archive in manifest['archives']:
    target = out / archive['filename']
    h = hashlib.sha256()
    size = 0
    with target.open('xb') as dest:
        for part in archive['parts']:
            ph = hashlib.sha256()
            ps = 0
            with (base / part['filename']).open('rb') as src:
                for chunk in iter(lambda: src.read(1024 * 1024), b''):
                    dest.write(chunk)
                    size += len(chunk)
                    ps += len(chunk)
                    h.update(chunk)
                    ph.update(chunk)
            if ps != part['bytes'] or ph.hexdigest() != part['sha256']:
                raise SystemExit(f'Part changed during reconstruction: {part["filename"]}')
    if size != archive['bytes'] or h.hexdigest() != archive['sha256']:
        raise SystemExit(f'Archive verification failed: {target}')
    print(f'Verified {target.name}: {size} bytes')
