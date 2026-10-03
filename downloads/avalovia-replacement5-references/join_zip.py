#!/usr/bin/env python3
"""Verify and reconstruct the reference archives without overwriting files."""
import argparse, hashlib, json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=Path.cwd())
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    index = json.loads((base / 'parts.json').read_text())
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for archive in index['archives']:
        target = args.output_dir / archive['filename']
        if target.exists():
            raise FileExistsError(f'Refusing to overwrite: {target}')
    for archive in index['archives']:
        for part in archive['parts']:
            source = base / part['filename']
            digest = hashlib.sha256()
            size = 0
            with source.open('rb') as f:
                for block in iter(lambda: f.read(1024 * 1024), b''):
                    digest.update(block)
                    size += len(block)
            if size != part['bytes'] or digest.hexdigest() != part['sha256']:
                raise ValueError(f'Part verification failed: {source.name}')
    for archive in index['archives']:
        target = args.output_dir / archive['filename']
        digest = hashlib.sha256()
        size = 0
        with target.open('xb') as out:
            for part in archive['parts']:
                with (base / part['filename']).open('rb') as source:
                    for block in iter(lambda: source.read(1024 * 1024), b''):
                        out.write(block)
                        digest.update(block)
                        size += len(block)
        if size != archive['bytes'] or digest.hexdigest() != archive['sha256']:
            raise ValueError(f'Reconstruction verification failed: {target}')
        print(f'Verified {target.name}: {archive["reference_count"]} references')

if __name__ == '__main__':
    main()
