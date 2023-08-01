## Challenge Name: Wave a Flag
Category: General
Points: 10
Solves: 114k+

Challenge Description: 
Can you invoke help flags for a tool or binary? 
[This program](https://mercury.picoctf.net/static/cfea736820f329083dab9558c3932ada/warm) has extraordinarily helpful information...

Artifact Files:
* [Binary Program](https://mercury.picoctf.net/static/cfea736820f329083dab9558c3932ada/warm)

### Approach

**1. Analyze the content**

Karena ini challenge bau-baunya binary exploitation dan ku lagi di windows yang gak ada wsl, ku pake webshell di website PicoCTF yang bisa diakses di sebelah kanan layar
![webshell toolbar](Wave%20a%20flag-1.JPG)
Setelah ditekan maka kita perlu masukkan username dan password PicoCTF:
![login](Wave%20a%20flag-2.JPG)
Lalu, kita perlu download file yang diperlukan dengan command:
```
wget https://mercury.picoctf.net/static/cfea736820f329083dab9558c3932ada/warm
```
Lalu kita lihat info tentang filenya menggunakan command:
```
file warm
```
Didapat informasi seperti berikut:
```
warm: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=3aa19b2a9cc4e093d64025eab8f510679b523455, with debug_info, not stripped
```
Terlihat ini adalah file binary ELF 64-bit biasa. Mari kita coba run menggunakan command:
```
./warm
```
Oh tidak dapat error:
```
-bash: ./warm: Permission denied
```
Benar juga, kita perlu kasih permission menggunakan command;
```
chmod +x warm
```
Sekarang mari kita jalankan lagi:
```
./warm
```
Didapat tulisan:
```
Hello user! Pass me a -h to learn what I can do!
```
Mari kita coba jalankan ulang dengan flag -h
```
./warm -h
```
Didapat hasil:
```
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_30e77291}
```
Alhamdulillah ketemu flagnya. Didapat flagnya:
```
picoCTF{b1scu1ts_4nd_gr4vy_30e77291}
```

### Reflections
Jadi inget soal yg Python Wrangling. Lumayan belajar pake shell dan `wget`. Karena masih permulaan jadi lebih ke belajar basic shell dan binary.

---
[Back to home](../Readme.md)
