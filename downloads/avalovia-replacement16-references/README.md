# Avalovia replacement16 reference images

74 native reference PNGs, totaling 108,652,498 bytes. Originals are preserved byte-for-byte in four existing ZIP_STORED archives. Each archive is split at a maximum of 64 MiB; these archives each fit in one part. These are ordinary Git binary files, not Git LFS pointers.

Download this entire folder, keeping filenames unchanged. Run with Python 3:

```sh
python3 join_zip.py
```

The script verifies each part and reconstructed ZIP against `parts.json`, and refuses to overwrite any existing ZIP. Extract the four resulting ZIPs to a destination of your choice. Each ZIP includes a minimal manifest for its own references; extract the PNGs without overwriting another archive's embedded `manifest.json`.

The folder-level `manifest.json` provides the complete character ID, native filename, byte count, and SHA256 mapping for all 74 images. `parts.json` records each archive and consecutive part's filename, size, and SHA256. No image decoding or image changes were used in preparing this transfer.
