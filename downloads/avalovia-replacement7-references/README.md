# Avalovia replacement7 references

76 original native reference PNGs (111,609,454 image bytes), preserved unchanged.
The ZIP_STORED archive is split into two consecutive ordinary Git binary parts,
each at most 64 MiB. Git LFS is not used.

Download both `.part` files, `parts.json`, and `join_zip.py` into one folder.
Run `python3 join_zip.py` there. The script verifies each part's size and SHA256,
joins them in order, verifies the resulting archive, and refuses to overwrite
an existing ZIP. Then extract `avalovia-replacement7-references.zip` with your
usual ZIP utility.

`manifest.json` (also inside the ZIP) lists character IDs, original filenames,
byte counts, and SHA256 hashes. `parts.json` records archive and part hashes.
Only mapped reference PNGs and the transfer manifest are inside the archive.
