# Avalovia references — replacement15

74 native reference PNGs, totaling 106,635,267 image bytes. The four existing ZIP_STORED archives are preserved as ordinary Git binary parts. Each archive fits in one part; the part size limit is 64 MiB. No Git LFS is used.

Download this entire folder, including all `.part001` files, `parts.json`, and `join_zip.py`. Using Python 3:

```sh
python3 join_zip.py --verify-only
python3 join_zip.py --output-dir ./reconstructed
```

The script checks part and archive sizes and SHA256 hashes and refuses to overwrite any existing output archive. Extract all four reconstructed ZIP files into your chosen image directory. Each ZIP contains reference PNGs and its minimal ID/filename/byte manifest; the manifest filename is repeated across archives, so retain manifests separately if desired.

`source-manifest.json` lists each unique character ID, filename, byte count, and SHA256 of the original PNG. `parts.json` records archive and part sizes and SHA256 hashes. Image bytes were checked without image decoding or visual inspection. Originals remain preserved in the source environment.
