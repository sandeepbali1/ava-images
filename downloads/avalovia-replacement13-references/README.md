# Avalovia replacement 13 references

75 native reference PNGs in four independent ZIP archives. Original filenames and PNG bytes are preserved. Each ZIP also contains its minimal ID, filename, and byte-count manifest. No image decoding or visual analysis was performed during transfer.

| Archive | References | Bytes |
| --- | ---: | ---: |
| avalovia-replacement13-part01-of04.zip | 20 | 29119400 |
| avalovia-replacement13-part02-of04.zip | 19 | 28188834 |
| avalovia-replacement13-part03-of04.zip | 19 | 28066364 |
| avalovia-replacement13-part04-of04.zip | 17 | 25337642 |

Download all four ZIP files using GitHub's raw/download action, then extract each into your chosen reference directory. These ZIPs are independent archives, not segments of one ZIP; do not concatenate them. All archives are below 64 MiB, so no splitting was needed.

`references.json` records each source ID, filename, size, SHA256, and archive. `source-ids.txt` lists all 75 IDs. `parts.json` records archive and part sizes and SHA256s. Unresolved IDs: none.

Optionally download `join_zip.py` and `parts.json` beside the four archives and run:

```sh
python3 join_zip.py /path/to/new-output-directory
```

The helper verifies all archive/part hashes before copying the independent ZIPs. It refuses to overwrite any destination archive. Preserve existing reference files when extracting.
