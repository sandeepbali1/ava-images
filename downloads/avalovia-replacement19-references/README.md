# Avalovia references — replacement19

73 native reference PNGs, totaling 108,569,326 image bytes, in three ZIP_STORED archives. Originals are preserved byte-for-byte. Only reference PNGs and their ID/filename/byte manifests are inside the archives.

Download every file in this folder together. Binary parts use ordinary Git, not Git LFS. Each archive is split into consecutive parts of at most 64 MiB; these three existing archives each fit in one part.

Run with Python 3.8 or newer:

```sh
python join_zip.py --output-dir reconstructed
```

The script verifies all part sizes and SHA256 hashes, reconstructs each ZIP, verifies the reconstructed archive, and refuses to overwrite existing output files. Extract the resulting ZIPs into your desired image directory. Each contains a `manifest.csv`; retain or rename those per-archive manifests as needed when extracting into one directory.

`parts.json` records the archive and part names, sizes, SHA256 hashes, and reference counts. The folder-level `manifest.csv` maps all 73 character IDs to original PNG filenames, byte sizes, and SHA256 hashes. No image decoding or re-encoding was performed. There are no missing source IDs in this source set.
