# Avalovia replacement4 references

76 native reference PNGs, preserved byte-for-byte. No profiles or unrelated files are included.

Download all files in this folder together. The ZIP is stored as consecutive ordinary Git binary parts, each at most 64 MiB; Git LFS is not used.

Run with Python 3:

```sh
python3 join_zip.py
```

The script verifies each part and the reconstructed ZIP against `parts.json` and refuses to overwrite an existing output. An optional first argument selects the output ZIP path. Extract the verified ZIP using your ZIP utility into a new directory.

`manifest.csv` records each character ID, original filename, byte length, and SHA256. The same manifest is included inside the ZIP. `parts.json` records archive and part byte lengths and hashes. Archive entries were verified against the authoritative saved-source mapping by byte hashing only.
