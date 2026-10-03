# Avalovia fresh cloud3 references

Three native reference PNG originals: ELV-000235, ELV-000673, ELV-001055.

Download all files in this folder together. Run `python3 join_zip.py` from this folder (or invoke it by its path). It verifies every part and the reconstructed archive, and refuses to overwrite an existing archive. Extract the resulting ZIP with your usual ZIP tool.

`manifest.json` records each reference filename, ID, byte count and SHA256. The ZIP contains only the three reference PNGs and its original minimal manifest. `parts.json` records the archive and consecutive binary parts, each at most 64 MiB. Image bytes are unchanged. These are ordinary Git files, not Git LFS objects.
