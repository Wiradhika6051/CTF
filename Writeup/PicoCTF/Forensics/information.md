## Challenge Name: information
>Category: Forensics

>Points: 10

>Solves: 77k+

Challenge Description: 
Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/a614a27d4cb251d04c7d2f3f3f76a965/cat.jpg)

Artifact Files:
* [cat.jpg](https://mercury.picoctf.net/static/a614a27d4cb251d04c7d2f3f3f76a965/cat.jpg)

### Approach
**1. Analisis Gambar**

Pertama kita download file nya lalu kita buka.
![cat.jpg](information-1.jpg)
Tidak ada sesuatu yang mencurigakan seperti pola flag atau semacamnya. Iya benar di layar ada kode apache spark yang ada hex nya, tapi bukan pola format ctf.

Mari kita analisis jenis filenya.
```
file cat.jpg
```
Didapat:
```
cat.jpg: JPEG image data, JFIF standard 1.02, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2560x1598, components 3
```
Hanya file JPEG biasa tanpa hal yang SUS (mencurigakan).

**2. Analisis Metadata**

Karena di filenya tidak ada hal yang mencurigakan dan soal ini poinnya rendah, kemungkinan bukan tentang stegano aneh aneh. Berarti target selanjutnya adalah metadata. Di hint 1 juga dikasih petunjuk buat cek metadata. Berhubung lagi di Windows, mari kita buka metadata nya lewat file detail. Caranya dengan klik kanan file -> Properties -> Details.
![file detail](information-2.JPG)
![file detail 2](information-3.JPG)
![file detail 3](information-4.JPG)

Dari metadata ini tidak ada hal yang aneh. Namun perlu diingat metadata di details ini tidak semuanya ditampilkan dan masih ada yang tersembunyi.

**3. Menggunakan ExifTools**
Untuk mendapatkan semua metadata, kita bisa menggunakan ExifTools yang bisa diunduh dari [sini](https://exiftool.org/install.html).
Setelah didownload dan diinstall sesuai OS, kita bisa menjalankan Exiftools menggunakan command berikut di windows:
```
.\exiftool.exe  cat.jpg
```
atau command berikut di UNIX-based OS:
```
./exiftool cat.jpg
```
Didapat hasil sebagai berikut:
```
ExifTool Version Number         : 12.64
File Name                       : cat.jpg
Directory                       : .
File Size                       : 878 kB
Zone Identifier                 : Exists
File Modification Date/Time     : 2023:08:01 09:45:03+07:00
File Access Date/Time           : 2023:08:01 16:48:44+07:00
File Creation Date/Time         : 2023:08:01 15:53:36+07:00
File Permissions                : -rw-rw-rw-
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```
Dari metadata disini, ada dua properti yang menucrigakan dan terlihat seperti hex yang bisa jadi merupakan flag, yakni **Current IPTC DIgest** serta **Lisence** . Mari kita coba masukkan ke submisi. Pertama untuk **Current IPTC DIgest**:
![attempt 1](information-5.JPG)
Ternyata ini bukan flagnya. Sekarang mari kita coba untuk **Lisenced**:
![attempt 2](information-6.JPG)
Ternyata bukan juga :sadge:

Hmm, apa hex ini perlu diconvert ya? tapi kemana? mari kita coba-coba di website [ini](https://gchq.github.io/CyberChef/)
- **to Base64**
  - **Current IPTC DIgest**
  ![hasil 1](information-7.JPG)
  - **Lisence**
  ![hasil 2](information-8.JPG)
- **from Base64**
  - **Current IPTC DIgest**
  ![hasil 3](information-9.JPG)
  - **Lisence**
  ![hasil 4](information-10.JPG)
Aha, flagnya ketemu. Flagnya adalah:
```
picoCTF{the_m3tadata_1s_modified}
```

### Reflections
Permulaan bagus untuk belajar forensic, belajar tools seperti Exiftools dan explore metadata.
  

---
[Back to home](../Readme.md)
