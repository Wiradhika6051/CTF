## Challenge Name: speeds and feeds
>Category: Reverse Engineering

>Points: 50

>Solves: 12,586

### Challenge Description: 

There is something on my shop network running at ```nc mercury.picoctf.net 28067```, but I can't tell what it is. Can you?


Artifact Files:
-

### Approach
**1. Analisi Respons**  
Langsung saja kita lihat ada apa sih di ```mercury.picoctf.net:28067```
![result](images/speeds%20and%20feeds-2.JPG)
Ada sebuah daftar perintah misterius disini. Sebelum kita cari tahu ini apaan, kita simpan dulu di lokal dengan perintah:
```
nc mercury.picoctf.net 28067 > command.txt
```
![hasil](images/speeds%20and%20feeds-3.JPG)
Untuk suatu alasan, memang bakal _stuck_ kek gini. Langsung saja _disconnect_ dengan ```CTRL+C```, lalu buka _file_-nya.
![file](images/speeds%20and%20feeds-4.JPG)

**2.Find the Language**  
Menggunakan mesin pencari, diperoleh bahasa apa yang digunakan kode tersebut.
![result](images/speeds%20and%20feeds-5.JPG)
Bahasa tersebtu adalah **G-Code**, yang ternyata digunakan untuk mesin _spindle_ dan _3d printing_ ternyata wkwk..

**3. Decode the Command and Get the Flag**  
Karena ku mager buat _decode_ manual, cari aja interpreter _online_ di mesin pencari. Setelah mencari di internet, didapat website bernama [ncviewer](https://ncviewer.com/) yang dapat memvisualisasikan menginterpretasi dan memvisualisasikan perintah **G-Code** yang dimasukkan. Langsung saja kita salin kode yang sudah disimpan tadi ke **ncviewer**.
![flag](images/speeds%20and%20feeds-1.JPG)
Wah ternyata ada _flag_-nya.
```
picoCTF{num3r1cal_c0ntr0l_84d2d117}
```


### Reflections
Permulaan menarik buat nyobain bahasa-bahasa aneh kayak **G-Code**. Meskipun terlihat aneh ini ternyata bahasa buat _3d modelling_ macam **Blender**. Sama _challenge_ ini berguna juga meningkatkan _skill googling_ buat nyari interpreter yang udah ada.

---
[Back to home](../Readme.md)
