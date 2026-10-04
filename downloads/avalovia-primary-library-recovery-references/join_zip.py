#!/usr/bin/env python3
"""Verify and reconstruct archives into a new directory; never overwrite."""
import hashlib,json,sys
from pathlib import Path
root=Path(__file__).resolve().parent
if len(sys.argv)!=2:raise SystemExit('Usage: python3 join_zip.py NEW_OUTPUT_DIRECTORY')
meta=json.loads((root/'parts.json').read_text())
def check(path,item):
 h=hashlib.sha256();size=0
 with path.open('rb') as f:
  while b:=f.read(1024*1024):h.update(b);size+=len(b)
 if size!=item['bytes'] or h.hexdigest()!=item['sha256']:raise SystemExit('Size/hash mismatch: '+path.name)
for a in meta['archives']:
 for p in a['parts']:
  if Path(p['filename']).name!=p['filename']:raise SystemExit('Unsafe part name')
  check(root/p['filename'],p)
 if Path(a['archive']['filename']).name!=a['archive']['filename']:raise SystemExit('Unsafe archive name')
out=Path(sys.argv[1]);out.mkdir(exist_ok=False)
for a in meta['archives']:
 target=out/a['archive']['filename']
 with target.open('xb') as f:
  for p in a['parts']:
   with (root/p['filename']).open('rb') as source:
    while b:=source.read(1024*1024):f.write(b)
 check(target,a['archive'])
print('Verified and reconstructed',len(meta['archives']),'archives in',out)
