# Avalovia old cloud4 reference originals

827 mapped reference PNGs, totaling 1,207,394,575 bytes. These are preserved original image bytes, with one canonical `<character_id>_ref.png` per saved identity. No profiles, prompts, raw generated-name duplicates, credentials, or uncertain outputs are included.

The 27 existing ZIP_STORED archives were verified against the authoritative saved identity mapping using byte counts and SHA256 only. Each archive is split consecutively at a 64 MiB boundary; these archives are smaller than that boundary, so each has one part. All 27 parts are ordinary Git binary files, not Git LFS pointers.

Download every file in this folder. With Python 3, run:

```sh
python3 join_zip.py --output-dir reconstructed
```

The script checks every part's size and SHA256, reconstructs the ZIP files in manifest order, verifies each reconstructed file's size and SHA256, and refuses to overwrite any existing output. Existing outputs must be left intact; choose a fresh directory for another run. Extract the verified archives into a fresh destination with your ZIP tool. Each archive includes a minimal ID/filename/bytes manifest.

`manifest.json` records the complete reference ID/filename/bytes/SHA256 mapping. `parts.json` records archive and part filenames, sizes and SHA256 values, exact unresolved IDs, and missing-source information. No saved source files were missing. The 27 unresolved submitted identities remain excluded and must not be regenerated.
