#!/usr/bin/env python3
"""Verify ordinary Git parts and reconstruct archives without overwriting files."""
import argparse,hashlib,json
from pathlib import Path

def digest(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--output-dir',type=Path,default=Path.cwd())
 args=parser.parse_args();base=Path(__file__).resolve().parent
 data=json.loads((base/'parts.json').read_text())
 args.output_dir.mkdir(parents=True,exist_ok=True)
 for a in data['archives']:
  if (args.output_dir/a['filename']).exists():raise SystemExit('Refusing overwrite: '+a['filename'])
  total=0;h=hashlib.sha256()
  for p in a['parts']:
   source=base/p['filename']
   if source.stat().st_size!=p['bytes'] or digest(source)!=p['sha256']:raise SystemExit('Invalid part: '+p['filename'])
   with source.open('rb') as f:
    for b in iter(lambda:f.read(1024*1024),b''):h.update(b);total+=len(b)
  if total!=a['bytes'] or h.hexdigest()!=a['sha256']:raise SystemExit('Invalid archive reconstruction: '+a['filename'])
 for a in data['archives']:
  out=args.output_dir/a['filename']
  with out.open('xb') as f:
   for p in a['parts']:
    with (base/p['filename']).open('rb') as src:
     for b in iter(lambda:src.read(1024*1024),b''):f.write(b)
  if out.stat().st_size!=a['bytes'] or digest(out)!=a['sha256']:raise SystemExit('Output verification failed: '+a['filename'])
  print('Verified:',out)
if __name__=='__main__':main()
