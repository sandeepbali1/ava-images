#!/usr/bin/env python3
"""Verify and reconstruct the old cloud4 archives without overwriting files."""
import argparse
import hashlib
import json
from pathlib import Path

def measure(path):
    digest = hashlib.sha256()
    size = 0
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            size += len(block)
            digest.update(block)
    return size, digest.hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    data = json.loads((root / 'parts.json').read_text())
    targets = []
    for archive in data['archives']:
        name = archive['filename']
        if Path(name).name != name:
            raise SystemExit('Unsafe archive filename')
        target = args.output_dir / name
        if target.exists() or target.is_symlink():
            raise SystemExit(f'Refusing overwrite: {target}')
        targets.append(target)
        for part in archive['parts']:
            if Path(part['filename']).name != part['filename']:
                raise SystemExit('Unsafe part filename')
            if measure(root / part['filename']) != (part['bytes'], part['sha256']):
                raise SystemExit(f'Part verification failed: {part["filename"]}')
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for archive, target in zip(data['archives'], targets):
        digest = hashlib.sha256()
        size = 0
        with target.open('xb') as output:
            for part in archive['parts']:
                part_digest = hashlib.sha256()
                part_size = 0
                with (root / part['filename']).open('rb') as source:
                    for block in iter(lambda: source.read(1024 * 1024), b''):
                        output.write(block)
                        digest.update(block)
                        size += len(block)
                        part_digest.update(block)
                        part_size += len(block)
                if (part_size, part_digest.hexdigest()) != (part['bytes'], part['sha256']):
                    raise SystemExit(f'Part changed during reconstruction: {target}')
        if (size, digest.hexdigest()) != (archive['bytes'], archive['sha256']):
            raise SystemExit(f'Archive verification failed: {target}')
        if measure(target) != (archive['bytes'], archive['sha256']):
            raise SystemExit(f'Written archive verification failed: {target}')
        print(f'Verified {target.name}: {size} bytes')

if __name__ == '__main__':
    main()
