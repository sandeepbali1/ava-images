# Avalovia old cloud1 reference originals

1,992 saved native reference PNGs, preserved byte-for-byte in 96 ZIP_STORED archives. Only reference PNGs and minimal ID/filename/byte manifests are inside the archives. `parts.json` supplies SHA-256 hashes for every reference, archive and consecutive binary part, and lists eight unresolved IDs with no saved original.

Download this whole folder using ordinary Git (no Git LFS). Each archive is smaller than 64 MiB, so each has one numbered part. Run:

```sh
python3 join_zip.py /path/to/new-output-directory
```

The script verifies all part and reconstructed archive byte counts and SHA-256 hashes. It refuses to overwrite an existing output archive. Extract the verified ZIPs with your preferred ZIP utility. Original filenames map directly to character IDs in `parts.json` and the embedded manifests.
