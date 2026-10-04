# Avalovia historical Library recovery references

46 distinct existing historical/recovered reference PNGs from three source archives. These are not newly generated and are separate from the 1,137-reference primary recovery. They are not attributed to any remaining primary or oldcloud2 counts.

The original mixed archive is not published. Its one profile image and profile metadata were excluded from the reference-only replacement, preserving all 18 reference PNGs byte for byte. The other two archives retain their original bytes (11 and 17 references).

Each archive is stored as one `.zip.part001` file under 64 MiB. Download all files in this folder, then run:

```sh
python3 join_zip.py /path/to/new-output-directory
```

The output directory must not exist. The script verifies parts and reconstructed archives by byte count and SHA-256 and refuses overwrites. It does not extract or inspect images. Extract the resulting ZIPs using your usual ZIP tool.

`id-manifest.json` records every character ID, filename, byte count, SHA-256, archive member and source provenance. `parts.json` records source and published archive hashes, sizes, and the excluded profile count. Original source archives remain preserved locally.
