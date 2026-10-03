# Avalovia replacement18 reference originals

73 native reference PNGs, 107,520,796 image bytes, preserved unchanged. Three existing ZIP_STORED archives are provided as consecutive binary parts of at most 64 MiB. These archives each fit in one part. No Git LFS is used.

Download all files in this folder together, then run:

```sh
python3 join_zip.py
```

The script checks every part and reconstructed archive against `parts.json` and refuses to overwrite existing ZIPs. Extract the three ZIP files into your chosen destination. Each archive contains reference PNGs and a minimal manifest. The folder-level `manifest.json` records each reference ID, filename, byte size, SHA256 and containing archive. Originals remain unchanged.
