#!/usr/bin/env python3
"""Verify ordered parts and reconstruct the reference ZIP without overwriting."""
import hashlib,json,pathlib,sys
root=pathlib.Path(__file__).resolve().parent
meta=json.loads((root/'parts.json').read_text())
out=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else root/meta['archive']['filename']
if out.exists():raise SystemExit(f'Refusing to overwrite: {out}')
def chunks(p):
 with p.open('rb') as f:
  while b:=f.read(1024*1024):yield b
whole=hashlib.sha256();total=0
for part in meta['parts']:
 p=root/part['filename'];h=hashlib.sha256();size=0
 for b in chunks(p):h.update(b);whole.update(b);size+=len(b)
 if size!=part['bytes'] or h.hexdigest()!=part['sha256']:raise SystemExit(f'Part verification failed: {p.name}')
 total+=size
if total!=meta['archive']['bytes'] or whole.hexdigest()!=meta['archive']['sha256']:raise SystemExit('Archive verification failed')
with out.open('xb') as f:
 for part in meta['parts']:
  for b in chunks(root/part['filename']):f.write(b)
h=hashlib.sha256();size=0
for b in chunks(out):h.update(b);size+=len(b)
if size!=meta['archive']['bytes'] or h.hexdigest()!=meta['archive']['sha256']:raise SystemExit('Written archive verification failed')
print(f'Verified {out}: {meta["reference_count"]} references, {size} archive bytes')
