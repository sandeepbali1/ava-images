# Avalovia replacement8 reference images

76 native reference PNGs, totaling 111,134,740 image bytes. No image conversion was performed.

The three existing reference-only ZIP_STORED archives are preserved byte-for-byte as ordinary Git binary parts. Each archive is smaller than 64 MiB, so each has one part. No Git LFS is required. Download this entire folder, retaining the filenames, then run:

```sh
python3 join_zip.py --output-dir ./reconstructed
```

The script verifies every part and reconstructed archive against `parts.json` and refuses to overwrite any existing archive. Extract the resulting ZIP files with a standard ZIP utility to obtain the `<character_id>_ref.png` files. Each ZIP includes its original ID/filename/byte manifest.

`manifest.json` supplies the complete reference ID, filename, byte count, SHA256, and archive mapping for all 76 references. `parts.json` supplies archive and ordered part filenames, byte counts, and SHA256 hashes.
