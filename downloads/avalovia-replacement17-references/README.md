# Avalovia replacement17 reference originals

73 native reference PNGs, totaling 108,408,713 source bytes. No image transformations were applied. Three existing ZIP_STORED archives are preserved byte-for-byte, each divided into consecutive parts of at most 64 MiB. Each archive fits in one part.

Download all files in this folder together, then run:

```sh
python3 join_zip.py /path/to/new-output-directory
```

The script verifies each part and reconstructed ZIP using byte counts and SHA256, and refuses to overwrite existing ZIPs. Extract the three ZIPs into your reference destination. Each ZIP contains its assigned PNGs and a minimal manifest; archive membership is disjoint.

`manifest.json` lists all character IDs, original PNG filenames, byte counts, and SHA256 hashes. `parts.json` lists archive and part filenames, byte counts, hashes, and reference counts. Binary parts use ordinary Git, not Git LFS.
