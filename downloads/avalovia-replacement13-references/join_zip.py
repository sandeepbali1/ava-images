#!/usr/bin/env python3
"""Verify archive parts and copy/join into a separate directory; never overwrite."""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    archives = json.loads((root / 'parts.json').read_text())['archives']
    args.destination.mkdir(parents=True, exist_ok=True)
    for archive in archives:
        target = args.destination / archive['filename']
        if target.exists():
            raise FileExistsError(f'Refusing to overwrite {target}')
    for archive in archives:
        whole = hashlib.sha256()
        size = 0
        for part in archive['parts']:
            data = (root / part['filename']).read_bytes()
            if len(data) != part['bytes'] or hashlib.sha256(data).hexdigest() != part['sha256']:
                raise ValueError(f"Part verification failed: {part['filename']}")
            whole.update(data)
            size += len(data)
        if size != archive['bytes'] or whole.hexdigest() != archive['sha256']:
            raise ValueError(f"Archive verification failed: {archive['filename']}")
    for archive in archives:
        target = args.destination / archive['filename']
        with target.open('xb') as output:
            for part in archive['parts']:
                with (root / part['filename']).open('rb') as source:
                    while block := source.read(1024 * 1024):
                        output.write(block)
        print(target)


if __name__ == '__main__':
    main()
