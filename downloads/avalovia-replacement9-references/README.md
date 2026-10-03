# Avalovia replacement9 reference originals

76 native reference PNGs, totaling 114,271,255 image bytes. Image bytes are unchanged. Only reference PNGs and their transfer manifest are inside the ZIP.

Download every file in this folder, including both `.part001` and `.part002` files, using Git or GitHub's raw-file download. These are ordinary Git files, not Git LFS objects. Keep the parts together with `parts.json` and `join_zip.py`.

Run with Python 3:

```sh
python3 join_zip.py --output-dir ./joined
```

The script verifies every part's byte count and SHA256, verifies the concatenated ZIP's byte count and SHA256, and refuses to overwrite an existing ZIP. Extract `joined/avalovia-replacement9-references.zip` with a standard ZIP tool into a new directory. Filenames remain `<character_id>_ref.png`.

`manifest.json`, also inside the ZIP, records each character ID, filename, byte count, and SHA256. `parts.json` records archive and part byte counts and SHA256 values. The first part is 64 MiB; the second contains the remaining bytes. No profiles or unrelated source files are included.
