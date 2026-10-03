# Avalovia replacement6 reference images

76 original native reference PNGs, totaling 111,701,152 bytes. These are stored in four ZIP_STORED archives, represented by consecutive binary parts of at most 64 MiB. Each of these archives fits in one part. No Git LFS is used.

Download every file in this folder into one directory, then run:

```sh
python3 join_zip.py
```

The script verifies each part's byte count and SHA256, reconstructs all four ZIP archives, and verifies their byte counts and SHA256. It refuses to overwrite any existing destination archive. Extract the verified ZIPs into a new directory to access the reference PNGs. Each archive includes a minimal manifest for its images.

`parts.json` records archive and part filenames, byte counts, SHA256, and reference counts. `source-manifest.json` maps every character ID to its PNG filename, byte count, SHA256, and containing archive. All PNG bytes are preserved unchanged. Only reference images and transfer manifests are included.
