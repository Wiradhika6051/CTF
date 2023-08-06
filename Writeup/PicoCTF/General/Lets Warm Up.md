## Challenge Name: Lets Warm Up
>Category: General

>Points: 50

>Solves: 89k+

### Challenge Description: 

If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

Artifact Files: -

### Approach

**1. How to get the flag?**

Oke dari deskripsinya kita suruh cari apa karakter ASCII dengan nilai hex 0x70. Dari searching di internet ketemu karakternya adalah 'p'
![bukti](Lets%20Warm%20Up-1.JPG)
Okee, dia bilang kan _word_ kan ya. Kita coba pikirkan kata yang diawali 'p', coba 'pico'.

Nah sekarang apa lagi yang perlu dilakukan? Coba kita buka hint.
![hint](Lets%20Warm%20Up-2.JPG)
Owalah langsung masukin aja. Mari kita masukkan.
```
picoCTF{pico}
```
![attempt 1](Lets%20Warm%20Up-3.PNG)
![failed](Lets%20Warm%20Up-4.JPG)
Yak gagal saudara.

Hmm harus gimana lagi ya?

Tunggu, ku kepikiran ide konyol. Kan di deskripsi cuma dikasih tahu yg 0x70 doang. Gimana kalau flagnya ini:
```
picoCTF{p}
```
Mari kita coba
![attempt 2](Lets%20Warm%20Up-5.PNG)
![success](Lets%20Warm%20Up-6.PNG)
Daann...sukses wkwkw...konyol juga flagnya.

Flag Real:
```
picoCTF{p}
```

### Reflections
Permulaan menarik untuk belajar konversi hex dan ASCII, namun challengenya cukup konyol dan membuat overthinking.
  
---
[Back to home](../Readme.md)
