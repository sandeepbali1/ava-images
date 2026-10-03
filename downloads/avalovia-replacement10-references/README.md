# Avalovia references — replacement10

76 native reference PNGs (111,900,498 bytes). One ZIP_STORED archive is split into consecutive ordinary Git binary parts of at most 64 MiB. No Git LFS is used.

Download all files in this folder into one directory. Run with Python 3.11 or newer:

```sh
python3 join_zip.py
```

The script verifies every part and the reconstructed ZIP by byte count and SHA256, and refuses to overwrite an existing output. Optionally supply a new destination path as its first argument. Extract the verified ZIP with a standard ZIP tool.

`manifest.json` (also inside the ZIP) maps character IDs to original filenames, byte counts and SHA256 hashes. `parts.json` records the archive and ordered part hashes. The ZIP contains only the 76 mapped PNGs and its manifest. Native image bytes are preserved. No missing or unresolved source IDs.
