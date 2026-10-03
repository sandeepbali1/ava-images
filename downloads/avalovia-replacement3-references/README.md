# Avalovia replacement3 reference originals

72 native reference PNGs, totaling 107,779,129 image bytes. The three reused ZIP_STORED archives contain 28, 27, and 17 references respectively. Their combined archive size is 107,790,454 bytes.

Archive bytes are divided consecutively at a maximum of 64 MiB per binary part. Each existing archive is smaller than 64 MiB, so each has one part. These are ordinary Git files, not Git LFS pointers.

Download all files in this folder together, or clone the repository. Run:

```sh
python3 join_zip.py --output-dir reconstructed
```

The script verifies every part and reconstructed ZIP using byte counts and SHA256, and refuses to overwrite existing output files. Extract the three verified ZIPs into a new folder to obtain the original `ELV-xxxxxx_ref.png` filenames. Each ZIP contains a minimal CSV manifest; `manifest.json` supplies character IDs, filenames, byte counts, and SHA256 for all 72 images. `parts.json` supplies archive and ordered part metadata.

No image bytes have been transformed. Only reference PNGs and transfer manifests are inside the archives. Source originals are preserved.

Four previously submitted IDs have no mapped saved output and are excluded: ELV-003130, ELV-003199, ELV-015039, ELV-015070. They were not regenerated. No other mapped saved source files are missing.
