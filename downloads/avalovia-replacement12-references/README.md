# Avalovia replacement12 reference images

51 native reference PNGs, totaling 74,958,874 bytes. These files preserve the original image bytes. No image decoding or modification was performed.

The two existing ZIP_STORED archives are provided as consecutive binary parts of at most 64 MiB each. Each archive fits in one part. These are ordinary Git files; Git LFS is not used.

Download this entire directory, then run with Python 3:

```sh
python3 join_zip.py --output-dir ./joined
```

The script verifies each part's byte count and SHA256, reconstructs the ZIPs in listed order, checks the archive byte count and SHA256, and refuses to overwrite existing ZIPs. Extract both ZIPs to access all 51 PNGs. Each archive includes its own minimal manifest; keep those manifests separate when extracting into one destination if desired.

`manifest.json` contains the authoritative character ID, PNG filename, byte count, and SHA256 for every reference. `parts.json` records archive and part names, byte counts, SHA256 values, and reference counts. Archive 1 contains 28 references; archive 2 contains 23. The byte hashes of every archived PNG were compared with the saved source mapping before publication.
