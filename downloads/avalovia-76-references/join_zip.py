from pathlib import Path
import hashlib,json,os
root=Path(__file__).resolve().parent
meta=json.loads((root/'parts.json').read_text())
out=root/meta['zip_filename']
if out.exists():
    raise SystemExit(f'File already exists: {out}; move it before joining.')
whole=hashlib.sha256()
total=0
temp=out.with_suffix('.joining')
try:
    with temp.open('xb') as dest:
        for part in meta['parts']:
            path=root/part['filename']
            digest=hashlib.sha256()
            count=0
            with path.open('rb') as source:
                while chunk:=source.read(1024*1024):
                    dest.write(chunk);digest.update(chunk);whole.update(chunk)
                    count+=len(chunk);total+=len(chunk)
            if count!=part['bytes'] or digest.hexdigest()!=part['sha256']:
                raise ValueError(f'Part integrity mismatch: {path.name}')
    if total!=meta['bytes'] or whole.hexdigest()!=meta['sha256']:
        raise ValueError('ZIP integrity mismatch')
    os.rename(temp,out)
except Exception:
    if temp.exists():temp.unlink()
    raise
print(f'Created and verified {out.name}: {total} bytes, {meta["reference_count"]} images')
