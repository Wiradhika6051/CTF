## Challenge Name: Matryoshka doll
>Category: Forensics

>Points: 30

>Solves: 31k+

### Challenge Description: 

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/f6cc2560a70b1ea811c151accba5390f/dolls.jpg)

Artifact Files:
* [dolls.jpg](https://mercury.picoctf.net/static/f6cc2560a70b1ea811c151accba5390f/dolls.jpg)

### Approach

**1. Analisis Gambar**

Pertama-tama, unduh dulu gambarnya. Bisa download langsung atau pake ```wget```.
```
wget https://mercury.picoctf.net/static/f6cc2560a70b1ea811c151accba5390f/dolls.jpg
```
![gambar](Matryoshka%20doll-1.JPG)
Sekilas hanya gambar boneka dari eropa timur yang bisa rekursif...

Weit, rekursif!!? Jangan bilang ada file yang tersembunti disini. Bentar pastikan dulu ini memang gambar.
```
file dolls.jpg
```
Hasil:
```
dolls.jpg: PNG image data, 594 x 1104, 8-bit/color RGBA, non-interlaced
```
Benar ternyata. Berarti sekarang lanjut ke langkah selanjutnya.

**2. Recursively Unwrap Until You Reach the Flag**

Untuk memastikan apakah ada file tersembunyi, gunakan program bernama [binwalk](https://github.com/ReFirmLabs/binwalk). Setelah dipasang, pertama kita cek isi filenya menggunakan command:
```
binwalk dolls.jpg
```
Diperoleh:
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378955, uncompressed size: 383936, name: base_images/2_c.jpg
651613        0x9F15D         End of Zip archive, footer length: 22
```
Kan bener ada file ```zip``` didalamnya. Untuk mengektrak file tersembunyi, gunakan command:
```
binwalk -e dolls.jpg
```
Diperoleh:
```

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378955, uncompressed size: 383936, name: base_images/2_c.jpg
651613        0x9F15D         End of Zip archive, footer length: 22
```
Bila kita cek menggunakan ```ls```:
```
README.txt            _waduh.png.extracted        dolls.jpg
_dolls.jpg.extracted  bkcrack-1.5.0-Linux         rawr.docx
_rawr.docx.extracted  bkcrack-1.5.0-Linux.tar.gz  waduh.png
```
Terlihat ada folder baru bernama ```_dolls.jpg.extracted```. Coba kita masuk ke sana dan lihat isinya.
```
4286C.zip  base_images
```
ada file zip awal yang direname oleh ```binwalk``` dan folder bernama ```base_images```. Mari kita lihat isi folder ini.
```
2_c.jpg
```
Ternyata ada file gambar lagi. Karena kita dari awal sudah suudzon, mari kita lanjutkan suudzon tadi. Ini gambar sepertinya ada file tersembunyi.
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 526 x 1106, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
187707        0x2DD3B         Zip archive data, at least v2.0 to extract, compressed size: 196041, uncompressed size: 201443, name: base_images/3_c.jpg
383803        0x5DB3B         End of Zip archive, footer length: 22
383914        0x5DBAA         End of Zip archive, footer length: 22
```
Kan bener...

Sudah, tidak usah basa-basi lagi langsung saja kita ekstrak dan lihat isi folder hasil ekstraksinya.
```
2DD3B.zip  base_images
```
Ternyata ada file ```zip``` awal dan folder bernama ```base_images```. Jika dugaanku benar...
```
3_c.jpg
```
Kan bener ada gambar lagi. Mari kita cek apakah masih ada yang disembunyikan...
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 428 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
123606        0x1E2D6         Zip archive data, at least v2.0 to extract, compressed size: 77649, uncompressed size: 79806, name: base_images/4_c.jpg
201421        0x312CD         End of Zip archive, footer length: 22
```
Kan ada...yasudahlah, lanjutkan rutinitas dan lihat isi foldernya.
```
1E2D6.zip  base_images
```
Ya Allah, ada folder lagi dong. Mari kita lihat isinya.
```
4_c.jpg
```
Ku curiga ini file punya rahasia di dalamnya.
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 320 x 768, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
79578         0x136DA         Zip archive data, at least v2.0 to extract, compressed size: 62, uncompressed size: 81, name: flag.txt
79784         0x137A8         End of Zip archive, footer length: 22
```
Nah, at least ini keknya ```zip``` terakhir. Yasudahlah langsung kita extract saja. Bismillah.
```
136DA.zip  flag.txt
```
Alhamdulillah udah mau nyampe flag. Langsung kita buka saja isinya.
```
picoCTF{ac0072c423ee13bfc0b166af72e25b61}
```

### Reflections

Permulaan yang menarik (meski nguli) buat belajar ```binwalk``` dan mencari file tersembunyi dalam file.

---
[Back to home](../Readme.md)
