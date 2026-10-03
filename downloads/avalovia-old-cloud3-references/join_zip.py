#!/usr/bin/env python3
"""Verify every binary part and reconstruct the native reference ZIP."""
import argparse
import hashlib
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, help='Destination ZIP; must not exist')
parser.add_argument('--verify-only', action='store_true', help='Verify without writing')
args = parser.parse_args()
base = Path(__file__).resolve().parent
index = json.loads((base / 'parts.json').read_text())
target = args.output or base / index['archive']['filename']
if not args.verify_only and target.exists():
    parser.error(f'Refusing to overwrite: {target}')
whole = hashlib.sha256()
total = 0
output = None if args.verify_only else target.open('xb')
try:
    for part in index['parts']:
        name = part['filename']
        if Path(name).name != name:
            raise ValueError('Invalid part filename')
        digest = hashlib.sha256()
        size = 0
        with (base / name).open('rb') as source:
            for block in iter(lambda: source.read(8 * 1024 * 1024), b''):
                digest.update(block)
                whole.update(block)
                size += len(block)
                if output:
                    output.write(block)
        if size != part['bytes'] or digest.hexdigest() != part['sha256']:
            raise ValueError(f'Part verification failed: {name}')
        total += size
    if total != index['archive']['bytes'] or whole.hexdigest() != index['archive']['sha256']:
        raise ValueError('Reconstructed archive verification failed')
finally:
    if output:
        output.close()
print(f'Verified {len(index["parts"])} parts, {total} bytes, SHA256 {whole.hexdigest()}')
if output:
    print(f'Created {target}')
