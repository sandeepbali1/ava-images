#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,tempfile,os
root=Path(__file__).resolve().parent
index=json.loads((root/'parts.json').read_text())
def check(path,record):
 h=hashlib.sha256(); size=0
 with path.open('rb') as f:
  for chunk in iter(lambda:f.read(1024*1024),b''):
   h.update(chunk); size+=len(chunk)
 if size!=record['bytes'] or h.hexdigest()!=record['sha256']:
  raise SystemExit('Byte verification failed: '+path.name)
archive=index['archive']; dest=root/archive['filename']
if dest.exists(): raise SystemExit('Refusing overwrite: '+str(dest))
for part in index['parts']: check(root/part['filename'],part)
fd,tmp=tempfile.mkstemp(prefix='.join-',dir=root)
tmp=Path(tmp)
try:
 with os.fdopen(fd,'wb') as out:
  for part in index['parts']:
   with (root/part['filename']).open('rb') as f:
    for chunk in iter(lambda:f.read(1024*1024),b''): out.write(chunk)
  out.flush(); os.fsync(out.fileno())
 check(tmp,archive)
 os.link(tmp,dest)
 print('Verified archive: '+str(dest))
finally:
 tmp.unlink(missing_ok=True)
