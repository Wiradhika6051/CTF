## Challenge Name: Glory of the Garden
>Category: Forensics

>Points: 50

>Solves: 48,240

### Challenge Description: 

This [garden](https://jupiter.challenges.picoctf.org/static/4153422e18d40363e7ffc7e15a108683/garden.jpg) contains more than it seems.

Artifact Files:
* [garden.jpg](https://jupiter.challenges.picoctf.org/static/4153422e18d40363e7ffc7e15a108683/garden.jpg)

### Approach
**1. Analisis Gambar**   
Langsung saja kita unduh gambarnya dan kita buka
![gambar](Glory%20of%20the%20Garden-1.JPG)
Terlihat hanya ada gambar biasa. Karena ini soal forensik, sepertinya informasinya disembunyikan di gambar.

**2. Analisis Metadata**   
Pertama-tama, coba kita lihat metadata-nya menggunakan [exiftool](https://exiftool.org/). Setelah diunduh, jalankan _command_ berikut:
```
exiftool garden.jpg
```
Dan didapat:
```
C:\XXX\Forensics>exiftool garden.jpg
ExifTool Version Number         : 12.64
File Name                       : garden.jpg
Directory                       : .
File Size                       : 2.3 MB
Zone Identifier                 : Exists
File Modification Date/Time     : 2023:09:28 10:18:44+07:00
File Access Date/Time           : 2023:09:28 14:06:06+07:00
File Creation Date/Time         : 2023:09:28 10:18:16+07:00
File Permissions                : -rw-rw-rw-
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Linotronic
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 1998:02:09 06:49:00
Profile File Signature          : acsp
Primary Platform                : Microsoft Corporation
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : Hewlett-Packard
Device Model                    : sRGB
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Hewlett-Packard
Profile ID                      : 0
Profile Copyright               : Copyright (c) 1998 Hewlett-Packard Company
Profile Description             : sRGB IEC61966-2.1
Media White Point               : 0.95045 1 1.08905
Media Black Point               : 0 0 0
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Device Mfg Desc                 : IEC http://www.iec.ch
Device Model Desc               : IEC 61966-2.1 Default RGB colour space - sRGB
Viewing Cond Desc               : Reference Viewing Condition in IEC61966-2.1
Viewing Cond Illuminant         : 19.6445 20.3718 16.8089
Viewing Cond Surround           : 3.92889 4.07439 3.36179
Viewing Cond Illuminant Type    : D50
Luminance                       : 76.03647 80 87.12462
Measurement Observer            : CIE 1931
Measurement Backing             : 0 0 0
Measurement Geometry            : Unknown
Measurement Flare               : 0.999%
Measurement Illuminant          : D65
Technology                      : Cathode Ray Tube Display
Red Tone Reproduction Curve     : (Binary data 2060 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 2060 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 2060 bytes, use -b option to extract)
Image Width                     : 2999
Image Height                    : 2249
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2999x2249
Megapixels                      : 6.7
```
Tidak ada yang menarik. Berarti _flag_-nya bukan disini.

**3. Mencari _flag_ di Gambar**   
Coba kita cari, jangan-jangan _flag_-nya dalam bentuk _string_ di gambar. Karena ku sedang di windows yang gak ada WSL, ku gunakan _command_ alternatif untuk ```grep``` di windows yakni ```Select-String```. Untuk mencari _flag_, kita gunakan _command_ berikut:
```
Select-String -Path .\garden.jpg -Pattern "picoCTF"
```
Berikut hasil eksekusinya:
```
PS C:\XXX\Forensics> Select-String -Path .\garden.jpg -Pattern "picoCTF"

garden.jpg:13403:↑�<�j~k��V�y9���S�� 1�u▼�¶������������Ӳ�⌂��Here is a flag "picoCTF{more_than_m33ts_the_3y33dd2eEF5}"
```
Mantap dapat _flag_-nya!
```
picoCTF{more_than_m33ts_the_3y33dd2eEF5}
```

### Reflections
Permulaan bagus untuk belajar nyari _flag_ di file dan menggunakan _command_ untuk mencari _string_ di _file_.

---
[Back to home](../Readme.md)




