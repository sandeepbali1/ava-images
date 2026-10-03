# Avalovia fresh cloud4 references

Three native reference PNGs: ELV-000568, ELV-000956, ELV-019930. Total reference bytes: 4,306,118. Originals are preserved byte-for-byte. No profiles are included.

Download every file in this folder into one directory, then run `python3 join_zip.py`. The script checks each part and the reconstructed ZIP using SHA-256, and refuses to overwrite an existing ZIP. Extract the verified ZIP with your ZIP utility.

The ZIP is split into consecutive parts of up to 64 MiB; this source needs one part. `parts.json` records archive and part sizes/hashes. `manifest.json` records reference IDs, filenames, byte counts and SHA-256 hashes. The reused archive contains the same references and its original ID/filename/byte manifest. Binary parts use ordinary Git, not Git LFS.
