#!/usr/bin/env python3
"""Verify and reconstruct archives without overwriting existing files."""
import hashlib,json,sys
from pathlib import Path
base=Path(__file__).resolve().parent
meta=json.loads((base/'parts.json').read_text())
target=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else base
for a in meta['archives']:
 if (target/a['filename']).exists():raise SystemExit('Refusing overwrite: '+str(target/a['filename']))
for a in meta['archives']:
 digest=hashlib.sha256();size=0
 for p in a['parts']:
  b=(base/p['filename']).read_bytes()
  if len(b)!=p['bytes'] or hashlib.sha256(b).hexdigest()!=p['sha256']:raise SystemExit('Part verification failed: '+p['filename'])
  digest.update(b);size+=len(b)
 if size!=a['bytes'] or digest.hexdigest()!=a['sha256']:raise SystemExit('Archive verification failed: '+a['filename'])
target.mkdir(parents=True,exist_ok=True)
for a in meta['archives']:
 with (target/a['filename']).open('xb') as f:
  for p in a['parts']:f.write((base/p['filename']).read_bytes())
 print('Reconstructed',a['filename'])
