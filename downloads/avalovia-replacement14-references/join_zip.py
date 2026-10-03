#!/usr/bin/env python3
"""Verify reference archive parts and reconstruct without overwriting files."""
import argparse
import hashlib
import json
from pathlib import Path


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=Path.cwd())
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    data = json.loads((base / 'parts.json').read_text())
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for archive in data['archives']:
        name = archive['filename']
        if Path(name).name != name:
            raise ValueError('Unsafe archive filename')
        destination = args.output_dir / name
        if destination.exists():
            raise FileExistsError(f'Refusing overwrite: {destination}')
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
    for archive in data['archives']:
        destination = args.output_dir / archive['filename']
        h = hashlib.sha256()
        with destination.open('xb') as output:
            for part in archive['parts']:
                with (base / part['filename']).open('rb') as source:
                    for chunk in iter(lambda: source.read(1024 * 1024), b''):
                        output.write(chunk)
                        h.update(chunk)
        if destination.stat().st_size != archive['bytes'] or h.hexdigest() != archive['sha256']:
            raise ValueError(f'Reconstruction verification failed: {destination}')
        print(f'Verified: {destination.name} ({archive["reference_count"]} references)')


if __name__ == '__main__':
    main()
