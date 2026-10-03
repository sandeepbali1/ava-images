# Avalovia replacement11 reference originals

76 native reference PNGs, totaling 111,545,974 bytes. These four existing ZIP_STORED archives contain only the authoritative reference filenames and a minimal CSV manifest. Image bytes are preserved exactly.

Download all files in this folder. Run with Python 3:

```sh
python3 join_zip.py ./reconstructed
```

The script verifies every part and reconstructed archive using byte lengths and SHA256, then writes the four ZIPs. It refuses to overwrite any existing output. Extract the ZIPs into your chosen reference directory; each PNG has its original `ELV-xxxxxx_ref.png` filename. Each archive also contains its own `manifest.csv`, so extract archives into separate folders if you want to retain all four CSV files.

`manifest.json` maps all 76 character IDs to PNG filenames, byte counts, SHA256 hashes, and archives. `parts.json` describes archive hashes and consecutive binary parts. Parts are at most 64 MiB; these archives each fit in one part. Concatenation is lossless. Ordinary Git binary storage is used, with Git LFS filtering disabled for the part files.
