## Challenge Name: Mind your Ps and Qs
> Category: Cryptography

> Points: 20

> Solves: 27k+

### Challenge Description: 

In RSA, a small ```e``` value can be problematic, but what about ```N```? Can you decrypt this? [values](https://mercury.picoctf.net/static/3cfeb09681369c26e3f19d886bc1e5d9/values)

Artifact Files:
* [values](https://mercury.picoctf.net/static/3cfeb09681369c26e3f19d886bc1e5d9/values)

### Approach

**1. Analisis Artifak**

Pertama-tama kita unduh dulu artifaknya lalu kita cek jenis filenya. (Untuk downloadnya bisa download langsung atau pake ```wget```)
```
file values
```
Diperoleh:
```
values: ASCII text
```
Oh berarti ini file teks biasa. Mari kita buka.
```
cat values
```
Diperoleh:
```
Decrypt my super sick RSA:
c: 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n: 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e: 65537
```
Owalah..ini data yang dikasih ke kita untuk disolve, ada **ciphertext**,**n**, dan **e**.

**2. Decrypt the Flag**

Untuk bisa melakukan dekripsi, kita perlu belajar basic RSA. Untuk referensi aku ambil dari [sini](https://ctf101.org/cryptography/what-is-rsa/).

Tujuan kita adalah men-_decrypt_ ciphertext (c) menjadi message (m). Di challenge ini kita hanya diberikan **n** (perkalian dua faktor prima) dan **e** (kunci enkripsi / kunci publik). Untuk bisa men-_decrypt_ ciphertext, kita memerlukan **d** (kunci privat / kunci dekripsi).

Sekarang bagaimana caranya mendapatkan **d**?

Dari referensi yang sudah disebutkan sebelumnya, kunci privat diperoleh dengan mencari angka prima yang memenuhi persamaan berikut:
```
d x e mod λ(n) = 1 ...(1)
```
dimana **e** adalah kunci publik dan **λ(n)** diperoleh dari persamaan:
```
λ(n) = lcm(p-1, q-1) ...(2)
``` 
Dimana **lcm()** adalag fungsi untuk mencari faktor persekutuan terbesar antara dua angka, serta **p** dan **q** adalah dua faktor prima acak yang dipilih untuk membangkitkan kunci publik dan privat.

Persamaan (1) bisa diubah bentuknya menjadi:
```
d = (1 + k * λ(n))/ e ...(3)
```
Dan persamaan (3) bisa disubstitusi dengan persamaan (2) menjadi:
```
d = (1 + k * lcm(p-1, q-1))/ e ...(4)
```
Karena kita sudah mengetahui nilai **e**, yang kita perlukan untuk bisa mencari **d** adalah mengetahui **p** dan **q**.

Sekarang bagaimana mendapatkan kedua faktor tersebut. Lalu apa gunanya **n**?

Sabar bro 'n sis. Jika kita baca referensinya, kita jadi tahu kalo nilai **n** itu bisa diperoleh dengan mengalikan **p** dan **q**. Artinya untuk bisa mendapatkan **p** dan **q**, kita perlu memfaktorkan **n**.

Tapi **n** kan panjang banget? Gimana faktorinnya? Kalo pake cara faktorisasi yang pohon-pohon mah udah mah lieur lama lagi.

Gunakanlah teknologi namanya _searching_ (gak, ku gak mau promosi in, lagian udah pada tahu lah website apa yang biasa dipakai buat nyari di internet). Kita cari factorizer online.

Welp...factorizer online gak kuat buat ngecari faktor buat **n** yang kita punya.

Setelah baca baca writeup untuk challenge sejenis, ku menemukan writeup yang ditulis oleh [Jarvis OJ](https://www.ctfwriteup.com/crypto/jarvis-oj-crypto-rsa-series). Ternyata ada website namanya [FactorDB](http://factordb.com/) untuk mencari faktor dari **n** yang cukup besar. Mari kita coba.

![factorDB](Mind%20your%20Ps%20and%20Qs-1.JPG)
Dapet dong. Diperoleh faktor untuk **p** dan **q** nya yakni:
```
p = 1617549722683965197900599011412144490161
q = 475693130177488446807040098678772442581573
```
Karena **p** dan **q** nya sudah dapat, mari kita cari **d**. Karena ku malas hitung, mari kita gunakan **Python saja**. Mari kita buat scriptnya dengan bantuan library **Crypto**. Untuk menginstallnya gunakan command berikut:
```
pip install pycryptodome
```
Dan karena di library ini sudah ada fungsi untuk mencari **d** (Basically rumus di poin (4) itu nyari inverse modulo dari **e**), tinggal gunakan saja fungsi ```inverse()```. Scriptnya adalah sebagai berikut:
```
from Crypto.Util.number import inverse
from math import lcm

#input data yang kita punya
p = 1617549722683965197900599011412144490161
q = 475693130177488446807040098678772442581573
e = 65537

#cari lambda_n
lambda_n = lcm(p-1,q-1)

#cari d
d = inverse(e,lambda_n)

print(f"Private key(d): {d}")
```
Mari kita jalankan:
```
Private key(d): 5309780120616927090141248812381294101574332745185110447018575329469639081235633
```
Okee kita dapat private key nya. Untuk mendapatkan **plaintext**, kita tinggal decrypt menggunakan private key. Sebelum private key bisa digunakan, kita perlu membuat objeknya terlebih dahulu. Berikut scriptnya:
```
from Crypto.Util.number import inverse,long_to_bytes
from math import lcm
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.Padding import pad

#input data yang kita punya
p = 1617549722683965197900599011412144490161
q = 475693130177488446807040098678772442581573
e = 65537
N = 769457290801263793712740792519696786147248001937382943813345728685422050738403253
ciphertext = 8533139361076999596208540806559574687666062896040360148742851107661304651861689

#cari lambda_n
lambda_n = lcm(p-1,q-1)

#cari d
d = inverse(e,lambda_n)
print(f"Private key(d): {d}")

#plaintext
plaintext = pow(ciphertext,d,N) 

#decrypt messagenya
print(f"Decrypted Message: {long_to_bytes(plaintext)}")
```
Alasan kenapa plaintext nya perlu dikonversi ke bytes adalah karena ciphertext-nya berupa angka dan tentu saja sangat gak berguna kalau kita dapat plaintextnya berupa angka juga, makanya perlu dikonversi jadi array of byte biar seenggaknya kelihatan flagnya. Mari kita coba!
```
Private key(d): 5309780120616927090141248812381294101574332745185110447018575329469639081235633
Decrypted Message: b'picoCTF{sma11_N_n0_g0od_45369387}'
```
Dapat flagnya! Flagnya adalah:
```
picoCTF{sma11_N_n0_g0od_45369387}
```
### Reflections
Permulaan menarik untuk belajar RSA dan library Crypto di Python meski awalnya sempet bingung cara ngefaktoring angka yang besar.
  

---
[Back to home](../Readme.md)
