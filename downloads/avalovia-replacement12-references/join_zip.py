#!/usr/bin/env python3
"""Verify binary parts and reconstruct ZIPs without overwriting files."""
import argparse, hashlib, json, pathlib

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=pathlib.Path, default=pathlib.Path.cwd())
    args = parser.parse_args()
    root = pathlib.Path(__file__).resolve().parent
    metadata = json.loads((root / 'parts.json').read_text())
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for archive in metadata['archives']:
        destination = args.output_dir / archive['filename']
        if destination.exists():
            raise FileExistsError(f'Refusing overwrite: {destination}')
        for part in archive['parts']:
            path = root / part['filename']
            if path.stat().st_size != part['bytes'] or digest(path) != part['sha256']:
                raise ValueError(f'Part verification failed: {path.name}')
    for archive in metadata['archives']:
        destination = args.output_dir / archive['filename']
        h = hashlib.sha256()
        size = 0
        with destination.open('xb') as output:
            for part in archive['parts']:
                with (root / part['filename']).open('rb') as source:
                    for block in iter(lambda: source.read(1024 * 1024), b''):
                        output.write(block)
                        h.update(block)
                        size += len(block)
        if size != archive['bytes'] or h.hexdigest() != archive['sha256']:
            raise ValueError(f'Archive verification failed: {destination.name}')
        print(f'Verified {destination.name}: {archive["reference_count"]} references')

if __name__ == '__main__':
    main()
