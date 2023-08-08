## Challenge Name: morphgura
>Category: Just Do It

>Points: 100

>Solves: 64

### Challenge Description: 

Creator: Lily

Artifact Files:
* [waduh.png](https://ctf.compfest.id/files/f94db33cebdbbb6e8f5a7d06ccc142b5/waduh.png?token=eyJ1c2VyX2lkIjoxMCwidGVhbV9pZCI6bnVsbCwiZmlsZV9pZCI6M30.ZNGSWg.CKRkBI7-5wedoNowixjRRbLgX4M)

### Approach

**1. Analyze the file**

Tidak usah basa basi, langsung unduh aja filenya, atau kalau mau pake commandline bisa dengan command berikut:
```
wget -c https://ctf.compfest.id/files/f94db33cebdbbb6e8f5a7d06ccc142b5/waduh.png?token=eyJ1c2VyX2lkIjoxMCwidGVhbV9pZCI6bnVsbCwiZmlsZV9pZCI6M30.ZNGSWg.CKRkBI7-5wedoNowixjRRbLgX4M
```
Jika nama filenya random misal:
```
'waduh.png?token=eyJ1c2VyX2lkIjoxMCwidGVhbV9pZCI6bnVsbCwiZmlsZV9pZCI6M30.ZNGSWg.CKRkBI7-5wedoNowixjRRbLgX4M'
```
Rename menggunakan ```mv```:
```
mv 'waduh.png?token=eyJ1c2VyX2lkIjoxMCwidGVhbV9pZCI6bnVsbCwiZmlsZV9pZCI6M30.ZNGSWg.CKRkBI7-5wedoNowixjRRbLgX4M' waduh.png
```
Sekarang mari kita buka filenya.
![Mr.Waduh](Just%20Do%20It-1.png)
Hanya gambar Mr.Waduh yang menjadi meme viral (~~apakah panitnya member sungut lele?~~). 

**2. Ekstrak File**

Seperti biasa, kalau ini soal Forensic, maka kita harus suudzon ada yang tersembunyi dari gambar ini. Mari kita cek menggunakan ```binwalk```.
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 500 x 590, 8-bit/color RGBA, non-interlaced
449620        0x6DC54         Zip archive data, encrypted at least v1.0 to extract, compressed size: 43, uncompressed size: 31, name: ???.txt
449821        0x6DD1D         End of Zip archive, footer length: 22
```
Kan bener ada file ```zip```. Langsung saja kita ekstrak dan lihat isinya.
```
6DC54.zip  '???.txt'*
```
Coba kita unzip.
```
unzip 6DC54.zip
```
Diperoleh:
```
Archive:  6DC54.zip
[6DC54.zip] ???.txt password: 
```
Lah diminta password dong. coba kita masukkan **waduh**.
```
password incorrect--reenter: 
```
Incorrect dong. coba ```justdoit```
```
password incorrect--reenter: 
```
Masih gafal. Hmm..apa password-nya ada di metadata? Coba kita pake ```exiftool```.
```
ExifTool Version Number         : 12.40
File Name                       : 6DC54.zip
Directory                       : .
File Size                       : 223 bytes
File Modification Date/Time     : 2023:08:08 09:25:00+07:00
File Access Date/Time           : 2023:08:08 09:26:18+07:00
File Inode Change Date/Time     : 2023:08:08 09:25:00+07:00
File Permissions                : -rw-rw-r--
File Type                       : ZIP
File Type Extension             : zip
MIME Type                       : application/zip
Zip Required Version            : 10
Zip Bit Flag                    : 0x0009
Zip Compression                 : None
Zip Modify Date                 : 2023:08:03 22:25:04
Zip CRC                         : 0x0212f0f2
Zip Compressed Size             : 43
Zip Uncompressed Size           : 43
Zip File Name                   : ???.txt
```
Tidak ada yang menarik. Coba kita lihat metadata di ```waduh.png```
```
ExifTool Version Number         : 12.40
File Name                       : waduh.png
Directory                       : .
File Size                       : 439 KiB
File Modification Date/Time     : 2023:08:07 20:33:49+07:00
File Access Date/Time           : 2023:08:07 20:34:06+07:00
File Inode Change Date/Time     : 2023:08:07 20:33:49+07:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 500
Image Height                    : 590
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Warning                         : [minor] Trailer data after PNG IEND chunk
Image Size                      : 500x590
Megapixels                      : 0.295
```
Tidak ada yang menarik.

**3. Bruteforce the Zip and Get the Flag**

Mau gak mau kita harus pake bruteforce. Kita bisa coba pakai tool bernama ```John The Ripper``` yang bisa diunduh dengan command berikut:
```
snap install john-the-ripper
```
Selain itu, kita perlu mengunduh converter untuk zip agar bisa dibruteforce bernama ```zip2john```. Namun jika mengunduh menggunakan command diatas, ```zip2john``` sudah terinstall secara otomatis.

Setelah diunduh, kita perlu mendapatkan hash dari file zip. Untuk mendapatkannya, gunakan command berikut:
```
john-the-ripper.zip2john 6DC54.zip > zip.hash
```
Diperoleh:
```
ver 1.0 efh 5455 efh 7875 6DC54.zip/???.txt PKZIP Encr: 2b chk, TS_chk, cmplen=43, decmplen=31, crc=0212F0F2 ts=B322 cs=b322 type=0
```
zip.hash adalah file yang berisi hash dari file. Untuk memulai bruteforce jalankan command berikut:
```
john-the-ripper zip.hash
```
Didapat:
```
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 8 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, 'h' for help, almost any other key for status
Almost done: Processing the remaining buffered candidate passwords, if any.
0g 0:00:00:00 DONE 1/3 (2023-08-08 09:45) 0g/s 684400p/s 684400c/s 684400C/s Txt6dc541900..Tzip1900
Proceeding with wordlist:/snap/john-the-ripper/current/run/password.lst
Enabling duplicate candidate password suppressor
trymenow         (6DC54.zip/???.txt)     
1g 0:00:00:00 DONE 2/3 (2023-08-08 09:45) 3.225g/s 1493Kp/s 1493Kc/s 1493KC/s 102362..capita1
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```
Sip kita dapat passwordnya. Passwordnya adalah ```trymenow```. Coba kita masukkan.
```
Archive:  6DC54.zip
[6DC54.zip] ???.txt password: 
replace ???.txt? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
 extracting: ???.txt 
```
Alhamdulillah jalan. Mari kita lihat isi file ```???.txt```.
```
COMPFEST15{brRuuTeF0rc33touch}
```
Dapat flagnya!

### Reflections

Permulaan yang lumayan membingungkan. Tapi lumayan bisa belajar ```binwalk``` dan bruteforce menggunakan ```John The Ripper``` (kalau kata para peserta lain sih namanya ```joni``` wkkwwk).

---
[Back to home](../Readme.md)
