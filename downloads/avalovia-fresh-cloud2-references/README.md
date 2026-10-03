# Avalovia fresh cloud2 reference originals

Three native reference PNGs: ELV-000355, ELV-000777, ELV-001140.
Original image bytes are preserved. No profiles are included.

Download all files in this folder together, then run:

```sh
python3 join_zip.py
```

The script checks each part and the reconstructed ZIP against the byte counts
and SHA256 hashes in `parts.json`. It refuses to overwrite an existing ZIP.
Extract the resulting ZIP using your usual ZIP utility.

Parts are consecutive chunks of at most 64 MiB stored in ordinary Git, without
Git LFS. This source fits in one part. `manifest.json` maps each character ID to
its reference filename, original byte count and SHA256. The reused ZIP also
contains its original minimal ID/filename/byte manifest.
