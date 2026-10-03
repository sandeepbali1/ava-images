# Avalovia replacement20 reference downloads

73 native reference PNGs, totaling 105,559,647 bytes. The original PNG bytes and character filenames are preserved. No profiles or unrelated files are included.

Three original ZIP_STORED archives are supplied as consecutive binary parts of at most 64 MiB each. Each archive fits in one part. This folder uses ordinary Git, not Git LFS.

Download every file in this folder together, or clone the repository, then run:

```sh
python3 join_zip.py --verify-only
python3 join_zip.py --output-dir reconstructed
```

The script checks every part and reconstructed archive against `parts.json` and refuses to overwrite existing output ZIPs. Extract the three reconstructed ZIPs into your chosen destination using a ZIP utility. Each contains native `ELV-xxxxxx_ref.png` files and a minimal `manifest.csv`; those per-archive CSV names may overlap, so preserve them separately if desired.

`manifest.json` lists each reference's character ID, filename, byte count, and SHA256. `parts.json` lists archive and part filenames, byte counts, SHA256 values, and reference counts. The source mapping and archive entries were checked by byte hashing without opening or decoding images. All 73 mapped references are included; no unresolved source IDs.
