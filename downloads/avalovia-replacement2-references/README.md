# Avalovia replacement2 reference downloads

76 native reference PNGs, totaling 113,032,716 bytes, in four ZIP_STORED archives of 19 references each. Original image bytes and character-ID filenames are preserved. Each ZIP also contains its minimal filename and byte-count CSV manifest.

Download every file in this folder using Git or GitHub's **Raw / Download raw file** option for each binary part. These are ordinary Git files, not Git LFS pointers. Each archive is smaller than 64 MiB and therefore has one consecutive part, `.part001`.

With Python 3 installed, run:

```sh
python3 join_zip.py --output-dir reconstructed
```

The script checks every part's size and SHA256, reconstructs the four ZIP files, and checks their complete sizes and SHA256 values. It refuses to overwrite existing output ZIPs. After successful verification, extract the ZIPs with your normal ZIP application. Each archive includes `manifest.csv`; extract into separate folders if retaining each CSV.

`parts.json` records archive and part filenames, byte counts, and SHA256 hashes. `manifest.json` maps each reference ID to its filename, byte count, SHA256, and archive. Archives contain only reference PNGs and the minimal transfer manifest; no profiles or unrelated files are included.
