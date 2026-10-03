# Avalovia references — old cloud3

This source contains 2,991 native reference PNGs (4,390,346,947 bytes), preserved without image decoding or modification. The ZIP uses ZIP_STORED and ZIP64. Its consecutive binary parts are at most 64 MiB each and are ordinary Git files, not Git LFS objects.

Download every `.partNNN` file and `parts.json` into the same directory as `join_zip.py`. Run with Python 3:

```sh
python3 join_zip.py --verify-only
python3 join_zip.py --output avalovia-old-cloud3-references.zip
```

The script verifies every part and the reconstructed archive against byte counts and SHA256 hashes. It refuses to overwrite an existing destination. If verification fails after a destination has been created, that partial destination must be moved aside manually before another attempt. Extract the verified ZIP using a ZIP64-compatible archive application; each image retains its canonical `ELV-NNNNNN_ref.png` filename.

`manifest.json`, also included inside the ZIP, maps every character ID to its filename, byte count and SHA256. `parts.json` identifies the archive and ordered parts. The archive contains only reference PNGs and its transfer manifest.

Nine submitted identities had no retained native output and remain unresolved, excluded without regeneration: ELV-005116, ELV-005125, ELV-005139, ELV-005150, ELV-005167, ELV-005207, ELV-005219, ELV-005226, ELV-005236.
