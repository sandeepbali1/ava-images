# Avalovia primary Library recovery references

336 distinct existing reference originals in 18 byte-preserved source ZIP archives. These are recovered exports, not newly generated images. No profiles are included.

Each archive is stored as one `.zip.part001` file under 64 MiB. Download the parts and `parts.json`, then run:

```sh
python3 join_zip.py /path/to/new-output-directory
```

The output directory must not exist. The script verifies every part and reconstructed archive by size and SHA-256, and refuses overwrites. It does not extract or inspect images. Extract the ZIP files using your normal ZIP tool. The ZIPs retain original reference metadata and export support files.

`id-manifest.json` maps each character ID to its original PNG filename, archive member, byte count, SHA-256 and source archive/file ID. `parts.json` lists source archives and transfer parts with exact sizes and hashes.
