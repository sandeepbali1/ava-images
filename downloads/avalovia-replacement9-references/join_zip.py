#!/usr/bin/env python3
"""Verify and join archive parts without overwriting any existing file."""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    metadata = json.loads((root / 'parts.json').read_text())
    archive = metadata['archive']
    destination = args.output_dir / archive['filename']
    if destination.exists():
        raise FileExistsError(f'Refusing to overwrite {destination}')
    combined = hashlib.sha256()
    total = 0
    for part in metadata['parts']:
        path = root / part['filename']
        digest = hashlib.sha256()
        size = 0
        with path.open('rb') as stream:
            while block := stream.read(1024 * 1024):
                digest.update(block)
                combined.update(block)
                size += len(block)
        if size != part['bytes'] or digest.hexdigest() != part['sha256']:
            raise ValueError(f'Part verification failed: {path.name}')
        total += size
    if total != archive['bytes'] or combined.hexdigest() != archive['sha256']:
        raise ValueError('Reconstructed archive verification failed')
    args.output_dir.mkdir(parents=True, exist_ok=True)
    written = hashlib.sha256()
    size = 0
    with destination.open('xb') as output:
        for part in metadata['parts']:
            with (root / part['filename']).open('rb') as stream:
                while block := stream.read(1024 * 1024):
                    output.write(block)
                    written.update(block)
                    size += len(block)
    if size != archive['bytes'] or written.hexdigest() != archive['sha256']:
        raise ValueError(f'Output verification failed; incomplete output retained: {destination}')
    print(f'Verified {destination}: {size} bytes, {metadata["reference_count"]} references')


if __name__ == '__main__':
    main()
