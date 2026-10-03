# Avalovia reference archive — 76 images

These are ordinary Git files. The 112,890,422-byte ZIP is split into two parts because GitHub blocks individual repository files larger than 100 MiB.

Download both `.part001` and `.part002` files, `parts.json`, and `join_zip.py` into one folder. On each file page, use **Download raw file** to save the actual file.

Run this in that folder with Python 3.8 or later:

```sh
python join_zip.py
```

On macOS/Linux you can use `python3 join_zip.py`; on Windows you can use `py join_zip.py`.

The script verifies both part hashes and the reconstructed ZIP, then creates `Avalovia-cloud-replacement-1-all-76-references.zip`. Extract it to get the 76 original reference PNGs and `manifest.json`.

ZIP SHA-256: `81a2cd3507d6bbc5fc5984f2e73bbea820d6cb5285f5a3cc62f4913201c89c4e`

The original PNG filenames and bytes are preserved. The included image manifest records character IDs, original source paths, sizes, and SHA-256 hashes.
