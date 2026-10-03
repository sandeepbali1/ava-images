#!/usr/bin/env python3
"""Reconstruct the reference ZIP with byte verification; never overwrite."""
import hashlib,json,sys
from pathlib import Path
base=Path(__file__).resolve().parent
meta=json.loads((base/'parts.json').read_text())
target=Path(sys.argv[1]) if len(sys.argv)>1 else base/meta['archive']['filename']
if target.exists():raise SystemExit(f'Refusing to overwrite: {target}')
for r in meta['parts']:
 p=base/r['filename']
 if p.stat().st_size!=r['bytes'] or hashlib.file_digest(p.open('rb'),'sha256').hexdigest()!=r['sha256']:
  raise SystemExit(f'Part verification failed: {p.name}')
h=hashlib.sha256();size=0
with target.open('xb') as dst:
 for r in meta['parts']:
  with (base/r['filename']).open('rb') as src:
   while block:=src.read(1024*1024):dst.write(block);h.update(block);size+=len(block)
if size!=meta['archive']['bytes'] or h.hexdigest()!=meta['archive']['sha256']:
 raise SystemExit('Archive verification failed; incomplete output retained for investigation.')
print(f'Verified {target}: {size} bytes, {meta["reference_count"]} references')
