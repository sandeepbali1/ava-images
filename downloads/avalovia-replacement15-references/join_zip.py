#!/usr/bin/env python3
"""Verify and reconstruct archives without overwriting existing files."""
import argparse
import hashlib
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output-dir', type=Path, default=Path.cwd())
parser.add_argument('--verify-only', action='store_true')
args = parser.parse_args()
root = Path(__file__).resolve().parent
catalog = json.loads((root / 'parts.json').read_text())

def safe_name(name):
    if Path(name).name != name or name in ('.', '..'):
        raise ValueError('Unsafe filename')
    return name

for archive in catalog['archives']:
    name = safe_name(archive['filename'])
    if not args.verify_only and (args.output_dir / name).exists():
        raise FileExistsError(f'Refusing overwrite: {args.output_dir / name}')
    digest = hashlib.sha256()
    size = 0
    for part in archive['parts']:
        data = (root / safe_name(part['filename'])).read_bytes()
        if len(data) != part['bytes'] or hashlib.sha256(data).hexdigest() != part['sha256']:
            raise ValueError(f'Part verification failed: {part["filename"]}')
        digest.update(data)
        size += len(data)
    if size != archive['bytes'] or digest.hexdigest() != archive['sha256']:
        raise ValueError(f'Archive verification failed: {name}')

if not args.verify_only:
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for archive in catalog['archives']:
        target = args.output_dir / archive['filename']
        with target.open('xb') as output:
            for part in archive['parts']:
                output.write((root / part['filename']).read_bytes())
        if target.stat().st_size != archive['bytes'] or hashlib.sha256(target.read_bytes()).hexdigest() != archive['sha256']:
            raise ValueError(f'Reconstruction verification failed: {target}')
print(f'Verified {len(catalog["archives"])} archives containing {catalog["reference_count"]} references.')
