## Challenge Name: Mod 26
> Category: Cryptography

> Points: 10

> Solves: 159k+

Challenge Description: 
Cryptography can be easy, do you know what ROT13 is? 
`cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}`

Artifact Files: -

### Approach

**1. Find the encryption algorithm**

Dari deskripsi challenge nya bisa menjadi petunjuk. Kemungkinan besar menggunakan ROT13. Mari kita cari tahu tentang ROT13.
[ROT 13](https://id.wikipedia.org/wiki/ROT13)

Intinya tiap huruf digeser 13 , lalu dimodulo 26 jadi huruf baru

**2. How to decode it**
Sudah banyak decoder ROT13 online. Kita bisa langsung pakai saja.
Contoh [website](https://cryptii.com/pipes/rot13-decoder)

Salin cipher ke kolom ciphertext dan didapatkan flagnya
![flag](Mod%2026-1.JPG)

The flag is:
```
picoCTF{next_time_I'll_try_2_rounds_of_rot13_Aphnytiq}
```

### Reflections
Permulaan bagus untuk belajar cryptography, belajar algoritma cryptography sederhana macam ROT13
  

---
[Back to home](../Readme.md)
