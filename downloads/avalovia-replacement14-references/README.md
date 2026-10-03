# Avalovia replacement14 reference images

75 native reference PNGs, totaling 108,697,574 bytes. Original bytes are preserved in four ZIP_STORED archives. No profiles or unrelated files are included.

Download every file in this folder, or clone the repository using ordinary Git. Git LFS is not required. Each archive is divided into consecutive parts of at most 64 MiB; these four archives each fit in one part.

Reconstruct and verify the ZIP files with Python 3:

```sh
python3 join_zip.py --output-dir ./reconstructed
```

The script verifies each part's length and SHA-256, verifies reconstructed archive lengths and SHA-256, and refuses to overwrite any existing output archive. After success, extract the four ZIP files with your usual archive utility into an empty destination folder. Each ZIP contains reference PNGs and a minimal manifest; its internal manifest describes only that archive.

The folder's `manifest.json` is the complete authoritative mapping of character IDs, native filenames, byte counts, SHA-256 hashes, and containing archive. `parts.json` records archive and part lengths and hashes. Preserve this folder's complete manifest when combining the extracted images.
