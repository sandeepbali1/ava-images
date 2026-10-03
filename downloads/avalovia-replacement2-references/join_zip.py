#!/usr/bin/env python3
"""Verify every part and reconstruct original ZIP archives without overwriting."""
import argparse
import hashlib
import json
from pathlib import Path

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=Path.cwd())
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    archives = json.loads((base / 'parts.json').read_text())['archives']
    for archive in archives:
        name = archive['filename']
        if Path(name).name != name:
            raise ValueError('Unsafe archive filename')
        target = args.output_dir / name
        if target.exists():
            raise FileExistsError(f'Refusing to overwrite {target}')
        total = 0
        for part in archive['parts']:
            name = part['filename']
            if Path(name).name != name:
                raise ValueError('Unsafe part filename')
            path = base / name
            if path.stat().st_size != part['bytes'] or digest(path) != part['sha256']:
                raise ValueError(f'Part verification failed: {name}')
            total += part['bytes']
        if total != archive['bytes']:
            raise ValueError('Archive byte count mismatch')
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for archive in archives:
        target = args.output_dir / archive['filename']
        with target.open('xb') as output:
            for part in archive['parts']:
                with (base / part['filename']).open('rb') as source:
                    for block in iter(lambda: source.read(1024 * 1024), b''):
                        output.write(block)
        if target.stat().st_size != archive['bytes'] or digest(target) != archive['sha256']:
            raise ValueError(f'Reconstruction verification failed: {target}')
        print(f'Verified {target.name}: {archive["reference_count"]} references')

if __name__ == '__main__':
    main()
