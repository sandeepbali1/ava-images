#!/usr/bin/env python3
"""Verify and reconstruct the reference ZIP archives without overwriting files."""
import argparse
import hashlib
import json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    archives = json.loads((root / 'parts.json').read_text())['archives']
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for archive in archives:
        target = args.output_dir / archive['filename']
        if target.exists():
            raise SystemExit(f'Refusing overwrite: {target}')
        full_hash = hashlib.sha256()
        full_size = 0
        for part in archive['parts']:
            sha = hashlib.sha256()
            size = 0
            with (root / part['filename']).open('rb') as source:
                while block := source.read(1024 * 1024):
                    sha.update(block)
                    full_hash.update(block)
                    size += len(block)
            if size != part['bytes'] or sha.hexdigest() != part['sha256']:
                raise SystemExit(f'Part verification failed: {part["filename"]}')
            full_size += size
        if full_size != archive['bytes'] or full_hash.hexdigest() != archive['sha256']:
            raise SystemExit(f'Archive verification failed: {archive["filename"]}')
    for archive in archives:
        target = args.output_dir / archive['filename']
        sha = hashlib.sha256()
        size = 0
        with target.open('xb') as destination:
            for part in archive['parts']:
                with (root / part['filename']).open('rb') as source:
                    while block := source.read(1024 * 1024):
                        destination.write(block)
                        sha.update(block)
                        size += len(block)
        if size != archive['bytes'] or sha.hexdigest() != archive['sha256']:
            raise SystemExit(f'Reconstruction failed: {target}; file retained for diagnosis')
        print(f'Verified: {target.name} ({archive["reference_count"]} references)')

if __name__ == '__main__':
    main()
