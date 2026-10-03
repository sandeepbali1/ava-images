# Avalovia replacement5 reference originals

76 native reference PNGs, totaling 112,382,703 bytes, preserved without image transformation.

This folder contains three existing ZIP_STORED archives split into consecutive binary parts of at most 64 MiB. Each archive fits in one part. The archives contain 28, 28, and 20 distinct references, respectively, plus a minimal manifest. These are ordinary Git files, not Git LFS pointers.

Download this entire folder, then run with Python 3:

```sh
python3 join_zip.py --output-dir ./reconstructed
```

The script checks every part's byte count and SHA256, reconstructs each ZIP in order, checks its archive hash, and refuses to overwrite an existing output. Extract the resulting ZIPs into separate empty folders using your usual ZIP utility. Each PNG keeps its original `ELV-xxxxxx_ref.png` filename.

`manifest.json` maps each reference ID to its filename, byte count, and SHA256. `parts.json` records archive and part sizes and hashes. The original archive manifests are unchanged; use the folder-level manifest for per-image hashes.
