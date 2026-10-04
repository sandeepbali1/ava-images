# Avalovia fresh cloud 1 reference download

Contains exactly 3 original reference PNGs: ELV-000321, ELV-000746, and ELV-001118. No profiles are included.

The ZIP is 4,499,622 bytes, below the 64 MiB part limit, so splitting was unnecessary. Download the ZIP directly, or download all files in this folder and run:

```sh
python3 join_zip.py /path/to/new-avalovia-cloud1.zip
```

The script checks sizes and SHA-256 hashes and refuses to overwrite a destination. Extract the verified ZIP with your usual ZIP tool. `id-manifest.json` records each original filename, character ID, size, and hash. `parts.json` records the archive and transfer part sizes and hashes. The ZIP also contains the original minimal manifest.
