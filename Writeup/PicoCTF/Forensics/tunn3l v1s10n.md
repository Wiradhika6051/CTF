## Challenge Name: tunn3l v1s10n
>Category: Forensics

>Points: 40

>Solves: 13k+

### Challenge Description: 

We found this [file](https://mercury.picoctf.net/static/06a5e4ab22ba52cd66a038d51a6cc07b/tunn3l_v1s10n). Recover the flag.

Artifact Files:
* [tunn3l_v1s10n](https://mercury.picoctf.net/static/06a5e4ab22ba52cd66a038d51a6cc07b/tunn3l_v1s10n)

### Approach

**1. Analisis File**

Pertama kita unduh gambarnya, terlihat file ini tidak memiliki ekstensi. Karena ku sedang tidak di windows dan tidak terinstall wsl, maka tidak bisa menggunakan _command_ ```file```. Sebagai alternatif, mari kita cek manual menggunakan [file signature](https://en.wikipedia.org/wiki/List_of_file_signatures). Caranya menggunakan hex editor seperti ```HxD``` di windows.
![file signature](tunn3l%20v1s10n-1.JPG)
Disini terlihat dua byte pertamanya yang membentuk hex yang sama dengan kata ```BM```. Coba kita cari ini file apa dengan data dari wikipedia.
![BMP file](tunn3l%20v1s10n-2.JPG)
ternyata ini file ```BMP``` (Bitmap Project) yang digunakan untuk menyimpan gambar. 

**2. Fixing the Header**

Sekarang mari kita buka menggunakan aplikasi pembuka gambar, misal ```GIMP```.
![failed](tunn3l%20v1s10n-3.JPG)
Lach error!!?

Setelah kucari-cari, ternyata file headernya bermasalah. Coba kita lihat struktur file ```BMP``` itu seperti apa [di sini](https://en.wikipedia.org/wiki/BMP_file_format)

Dari sini kita tahu bahwa secara umu, struktur data ```BMP``` itu sebagai berikut:
1. Bitmap File Header
2. DIB Header
3. Data

Bitmap File Header memiliki struktur sebagai berikut:
| Tujuan         | Ukuran  |
|----------------|---------|
| File Signature | 2 bytes |
| File Size      | 4 bytes |
| Reserved 1     | 2 bytes |
| Reserved 2     | 2 bytes |
| Offset Data    | 4 bytes |

Sedangkan untuk DIB Header, strukturnya bergantung _file signature_-nya. Karena _file signature_ file ini adalah **BM**, kemungkinan tipe header-nya adalah **BITMAPINFOHEADER** yang memiliki struktur berikut:
| Tujuan                         | Ukuran  |
|--------------------------------|---------|
| DIB Header Size                | 4 bytes |
| Bitmap Width                   | 4 bytes |
| Bitmap Height                  | 4 bytes |
| Number of Color Panes          | 2 bytes |
| Bits per pixel                 | 2 bytes |
| Compression Method             | 4 bytes |
| Image Size                     | 4 bytes |
| Horizontal Resolution          | 4 bytes |
| Vertical Resolution            | 4 bytes |
| Number of Color in Color Panel | 4 bytes |
| Number of Important Color      | 4 bytes |

Sekarang mari kita lihat Bitmap File Header untuk file ini. Berikut isi Bitmap File Header:
```
42 4D 8E 26 2C 00 00 00 00 00 BA D0 00 00
```
Dari tabel di atas, berikut penjelasan isi header-nya (default arsitektur CPU sekarang adalah little endian, jadi nilai hex ini direpresentasikan dengan little endian):
| Tujuan         | Ukuran  | Nilai (hex) | Deskripsi Nilai|
|----------------|---------|-------------|----------------|
| File Signature | 2 bytes |   42 4D     |      BM        |
| File Size      | 4 bytes | 8E 26 2C 00 |    2893443     |
| Reserved 1     | 2 bytes |   00 00     |      0         |
| Reserved 2     | 2 bytes |   00 00     |      0         |
| Offset Data    | 4 bytes | BA D0 00 00 |    53434       |

Dari sini terlihat sekilas tidak ada yang aneh sampai terlihat offset ke data nya mencapai 53 KB, yang mana offset ke data adalah panjang bitmap file header ditambah panjang DIB header. Seperti yang kita tahu panjang bitmap file header adalah **14** bytes dan panjang DIB header adalah **40** bytes sehingga seharusnya _field_ ini memiliki nilai **54** atau **0x36** dalam hex.

Untuk mengubahnya di **HxD**, tinggal edit saja bytes pada indeks 10 hingga 13 menjadi:
```
36 00 00 00
```
Seperti ini:
![edit bytes #1](tunn3l%20v1s10n-4.JPG)
lalu tekan Save (CTRL +S).

Sekarang mari kita coba buka gambarnya kembali
![still failed](tunn3l%20v1s10n-5.JPG)
Terlihat header-nya masih bermasalah.

Hmm coba kita cek DIB Header-nya. Berikut isinya:
```
BA D0 00 00 6E 04 00 00 32 01 00 00 01 00 18 00 00 00 00 00 58 26 2C 00 25 16 00 00 25 16 00 00 00 00 00 00 00 00 00 00
```
Dari tabel di atas, berikut penjelasan isi header-nya:
| Tujuan                         | Ukuran  | Nilai (hex) | Deskripsi Nilai |
|--------------------------------|---------|-------------|-----------------|
| DIB Header Size                | 4 bytes | BA D0 00 00 | 3514            |
| Bitmap Width                   | 4 bytes | 6E 04 00 00 | 1134            |
| Bitmap Height                  | 4 bytes | 32 01 00 00 | 306             |
| Number of Color Panes          | 2 bytes | 01 00       | 1               |
| Bits per pixel                 | 2 bytes | 18 00       | 24              |
| Compression Method             | 4 bytes | 00 00 00 00 | 0               |
| Image Size                     | 4 bytes | 58 26 2C 00 | 2893400         |
| Horizontal Resolution          | 4 bytes | 25 16 00 00 | 5669            |
| Vertical Resolution            | 4 bytes | 25 16 00 00 | 5669            |
| Number of Color in Color Panel | 4 bytes | 00 00 00 00 | 0               |
| Number of Important Color      | 4 bytes | 00 00 00 00 | 0               |

Dari tabel ini terlihat ada hal yang aneh yakni attribute ```DIB Header Size``` yang semestinya bernilai **40** malah bernilai **3514**. Ayo kita ubah menjadi representasi hexadecimal dari **40** yakni **0x28**
![change DIB header size](tunn3l%20v1s10n-6.JPG)
Sekarang coba kita buka lagi
![finally opened](tunn3l%20v1s10n-7.JPG)
Alhamdulillah terbuka, namun sayangnya tidak ada flag. Hmm dimana ya?

Kalau kita perhatikan, gambar ini seperti terpotong. Sepertinya kita perlu memainkan atribut **Bitmap Width** dan **Bitmap Height** untuk mendapatkan flag-nya.

**3. Find the Right Size and Get the Flag**

Supaya gambarnya benar, coba kita utak-atik resolusinya. Pada keadaan sekarang resolusinya adalah **1134x306**. Coba kita utak-atik width-nya terlebih dahulu.
- **1440x306**. Karena reolusi standar yang terdekat dari **1134** adalah **1440**, coba kita ganti properti **bitmap width** menjadi **1440** atau **0x5A0** dalam hexadecimal.
![change width](tunn3l%20v1s10n-8.JPG)
Coba kita buka lagi
![broken image](tunn3l%20v1s10n-9.JPG)
Terlihat gambarnya jadi berantakan. Berarti width-nya kurang dari **1440**.
- **1200x306**. Kita coba ke kelipatan 100 terdekat. Ubah nilai properti **bitmap width** menjadi **0x4B0** dalam hexadecimal. Berikut hasilnya:
![broken image#2](tunn3l%20v1s10n-10.JPG)
- **1150x306**. Kita coba ke kelipatan 50 terdekat. Ubah nilai properti **bitmap width** menjadi **0x47E** dalam hexadecimal. Berikut hasilnya:
![broken image#3](tunn3l%20v1s10n-11.JPG)
- **1140x306**. Kita coba ke kelipatan 10 terdekat. Ubah nilai properti **bitmap width** menjadi **0x474** dalam hexadecimal. Berikut hasilnya:
![broken image#4](tunn3l%20v1s10n-12.JPG)
- **1135x306**. Kita coba ke kelipatan 5 terdekat. Ubah nilai properti **bitmap width** menjadi **0x46F** dalam hexadecimal. Berikut hasilnya:
![broken image#5](tunn3l%20v1s10n-13.JPG)
- **1134x480**. Karena memperbesar width membuat gambar jadi rusak sedangkan kita tahu gambar ini terpotong, bagaimana kalau mengubah height?. Ubah nilai properti **bitmap height** menjadi **480** atau  **0x1E0** dalam hexadecimal. Kembalikan juga properti **bitmap width** ke **1134**. Berikut hasilnya:
![no flag](tunn3l%20v1s10n-14.JPG)
- **1134x720**. Karena belum nemu flag-nya, coba kita tingkatkan ketinggian gambar **720** atau **0x2D0** dalam hexadecimal. Berikut hasilnya:
![no flag#2](tunn3l%20v1s10n-15.JPG)
- **1134x1080**. Karena belum nemu flag-nya, coba kita tingkatkan ketinggian gambar **1080** atau **0x438** dalam hexadecimal. Berikut hasilnya:
![flag](tunn3l%20v1s10n-16.JPG)

Aha, flagnya ketemu. Flagnya adalah:
```
picoCTF{qu1t3_a_v13w_2020}
```

### Reflections
Permulaan menarik untuk belajar file signature dan header di file, terutama **BMP**. Selain itu jadi belajar ngedit binary langsung.
  

---
[Back to home](../Readme.md)
