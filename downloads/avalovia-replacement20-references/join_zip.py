#!/usr/bin/env python3
"""Verify all parts and reconstruct original ZIPs without overwriting files."""
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
    parser.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    data = json.loads((base / 'parts.json').read_text())
    for archive in data['archives']:
        target = args.output_dir / archive['filename']
        if not args.verify_only and target.exists():
            raise SystemExit(f'Refusing to overwrite {target}')
        combined = hashlib.sha256()
        total = 0
        for part in archive['parts']:
            path = base / part['filename']
            if path.stat().st_size != part['bytes'] or digest(path) != part['sha256']:
                raise SystemExit(f'Part verification failed: {path.name}')
            with path.open('rb') as stream:
                for block in iter(lambda: stream.read(1024 * 1024), b''):
                    combined.update(block)
                    total += len(block)
        if total != archive['bytes'] or combined.hexdigest() != archive['sha256']:
            raise SystemExit(f'Archive verification failed: {archive["filename"]}')
    if args.verify_only:
        print('All parts and reconstructed archive hashes verified.')
        return
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for archive in data['archives']:
        target = args.output_dir / archive['filename']
        with target.open('xb') as destination:
            for part in archive['parts']:
                with (base / part['filename']).open('rb') as stream:
                    for block in iter(lambda: stream.read(1024 * 1024), b''):
                        destination.write(block)
        if target.stat().st_size != archive['bytes'] or digest(target) != archive['sha256']:
            raise SystemExit(f'Reconstruction verification failed: {target}')
        print(f'Reconstructed and verified {target}')


if __name__ == '__main__':
    main()
