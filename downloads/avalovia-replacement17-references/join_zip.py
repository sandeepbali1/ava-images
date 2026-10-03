#!/usr/bin/env python3
"""Verify and reconstruct reference ZIPs; never overwrite existing files."""
import hashlib,json,pathlib,sys
root=pathlib.Path(__file__).resolve().parent
index=json.loads((root/'parts.json').read_text())
dest=pathlib.Path(sys.argv[1]).resolve() if len(sys.argv)>1 else root
for a in index['archives']:
 if pathlib.Path(a['filename']).name!=a['filename']:raise SystemExit('Unsafe archive filename')
 if (dest/a['filename']).exists():raise SystemExit('Refusing overwrite: '+str(dest/a['filename']))
 for p in a['parts']:
  if pathlib.Path(p['filename']).name!=p['filename']:raise SystemExit('Unsafe part filename')
  b=(root/p['filename']).read_bytes()
  if len(b)!=p['bytes'] or hashlib.sha256(b).hexdigest()!=p['sha256']:raise SystemExit('Part verification failed: '+p['filename'])
dest.mkdir(parents=True,exist_ok=True)
for a in index['archives']:
 digest=hashlib.sha256();size=0
 with (dest/a['filename']).open('xb') as f:
  for p in a['parts']:
   b=(root/p['filename']).read_bytes();f.write(b);digest.update(b);size+=len(b)
 if size!=a['bytes'] or digest.hexdigest()!=a['sha256']:raise SystemExit('Archive verification failed: '+a['filename'])
 print('Verified:',a['filename'])
