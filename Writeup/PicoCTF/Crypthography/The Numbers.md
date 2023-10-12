## Challenge Name: The Numbers
> Category: Cryptography

> Points: 50

> Solves: 53,965

### Challenge Description: 

The [numbers](https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png)... what do they mean?


Artifact Files: 
* [the_numbers.png](https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png)

### Approach

**1. Analyze the Image**  
Jadi di soal ini dikasih sebuah gambar yang bau-baunya berisi ~~nomor togel~~ sebuah pesan misterius seperti ini.
![nomor togel](images/The%20Numbers-1.JPG)
Ada yang menarik disini, terlihat ada karakter **{**, **}**, dan sebelum karakter **{** ada 5 buah angka. Hmm...seperti sebuah _flag_. Jika benar ini _flag_, 5 angka pertamanya semestinya bisa dikonversi menjadi "picoCTF". 

Bentar, huruf "p" kan huruf ke-16 di alfabet, begitupun huruf "i" huruf ke-9 di alfabet. Sepertinya ~~nomor togel~~ angka-angka ini menunjukkan urutan karakter di alfabet deh.

**2. Get the Flag**  
Yasudah kita ganti saja tiap angka dengan karakter di alfabet di posisi ke-sekian (dimulai dari posisi 1). Didapat _flag_-nya:
```
picoCTF{thenumbersmason}
```
Note: setelah di-_submit_, ternyata pengecekan _flag_ untuk _challenge_ ini _case insensitive_, jadi jika _submit_ _flag_ seperti:
```
PICOCTF{THENUMBERSMASON}
```
Itu juga valid.

### Reflections
Permulaan menarik untuk melakukan dekripsi pesan kriptik tanpa konteks.