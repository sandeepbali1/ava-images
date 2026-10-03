#!/usr/bin/env python3
"""Verify and join the archive parts without overwriting existing files."""
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
    root = Path(__file__).resolve().parent
    metadata = json.loads((root / 'parts.json').read_text())
    for archive in metadata['archives']:
        name = archive['filename']
        if Path(name).name != name:
            raise ValueError('Unsafe archive filename')
        if (args.output_dir / name).exists():
            raise FileExistsError('Refusing to overwrite: ' + str(args.output_dir / name))
        whole = hashlib.sha256()
        total = 0
        for part in archive['parts']:
            if Path(part['filename']).name != part['filename']:
                raise ValueError('Unsafe part filename')
            path = root / part['filename']
            if path.stat().st_size != part['bytes'] or digest(path) != part['sha256']:
                raise ValueError('Part verification failed: ' + path.name)
            with path.open('rb') as stream:
                for block in iter(lambda: stream.read(1024 * 1024), b''):
                    whole.update(block)
                    total += len(block)
        if total != archive['bytes'] or whole.hexdigest() != archive['sha256']:
            raise ValueError('Reconstruction verification failed: ' + name)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for archive in metadata['archives']:
        target = args.output_dir / archive['filename']
        with target.open('xb') as output:
            for part in archive['parts']:
                with (root / part['filename']).open('rb') as stream:
                    for block in iter(lambda: stream.read(1024 * 1024), b''):
                        output.write(block)
        if target.stat().st_size != archive['bytes'] or digest(target) != archive['sha256']:
            raise ValueError('Written archive verification failed: ' + target.name)
        print('Verified:', target.name)

if __name__ == '__main__':
    main()
