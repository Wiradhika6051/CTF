## Challenge Name: Rivest Shamir Adleman
>Category: Cryptography

>Points: 464

>Solves: 15

### Challenge Description: 

For the sake of maintaing security, the IT Dev team of Collective Inc. regularly changes their encryption system every sixth months. This time, they have made three new RSA-based encryption system and you are the one in charge testing them. They ask you to test these three algorithms by finding their vulnerabilities if possible with different test cases each round. Feeling intrigued, you accept their request filled with determination.

```nc 34.101.174.85 10004```

Original Author: potsu

Artifact Files:
* [chall.py](https://ctf.compfest.id/files/bad87d139d2137cf8a8fd6c243342125/chall.py?token=eyJ1c2VyX2lkIjoxMCwidGVhbV9pZCI6bnVsbCwiZmlsZV9pZCI6MTl9.ZNTSbQ.hgcGOPcif61G7YipMlwlsIPJ33A)

### Approach

**1. Analyze the file**

Berikut adalah isi file ```chall.py``` :
```
from Crypto.Util.number import GCD, getPrime, bytes_to_long
from sympy import nextprime
from random import choice
from secret import FLAG
import os

def modeA():
    n = getPrime(512)
    return n

def modeB():
    e = 3
    return e

def modeC(e):
    while True:
        p = getPrime(512)
        q = nextprime(nextprime(nextprime(p)))
        if GCD(e, (p-1)*(q-1)) == 1:
            break
    n = p*q
    return n

def setup():
    p = getPrime(512)
    q = getPrime(512)
    e = 65537
    return p, q, e

def main():
    print('Starting session.')
    flag = FLAG
    stages = 20
    modes = ['A', 'B', 'C']
    for i in range(stages):
        p, q, e = setup()
        n = p*q
        m = bytes_to_long(os.urandom(32))
        mode = choice(modes)
        if mode == 'A':
            n = modeA()
        elif mode == 'B':
            e = modeB()
        elif mode == 'C':
            n = modeC(e)
        else:
            raise AssertionError('Unknown Mode')

        c = pow(m, e, n)
        print(f'mode = {mode}')
        print(f'n = {n}')
        print(f'e = {e}')
        print(f'c = {c}')

        inp = input("Your answer: ")
        if not inp.isnumeric():
            raise AssertionError('Input is not integer.')
        
        if int(inp) == m:
            print('Correct!')
        else:
            print('Wrong answer!')
            break

    if i == (stages - 1):
        print(f'Congrats! Here\'s your flag: {flag}')
    else:
        print(f'Sorry you have failed at round {i + 1}')
    print('Ending session.')

if __name__ == '__main__':
    try:
        main()
    except:
        print('An error has occured.')
```
Penjelasan tentang kode soal adalah sebagai berikut:
```
def main():
    print('Starting session.')
    flag = FLAG
    stages = 20
    modes = ['A', 'B', 'C']
    for i in range(stages):
        p, q, e = setup()
        n = p*q
        m = bytes_to_long(os.urandom(32))
        mode = choice(modes)
        if mode == 'A':
            n = modeA()
        elif mode == 'B':
            e = modeB()
        elif mode == 'C':
            n = modeC(e)
        else:
            raise AssertionError('Unknown Mode')

        c = pow(m, e, n)
        print(f'mode = {mode}')
        print(f'n = {n}')
        print(f'e = {e}')
        print(f'c = {c}')

        inp = input("Your answer: ")
        if not inp.isnumeric():
            raise AssertionError('Input is not integer.')
        
        if int(inp) == m:
            print('Correct!')
        else:
            print('Wrong answer!')
            break

    if i == (stages - 1):
        print(f'Congrats! Here\'s your flag: {flag}')
    else:
        print(f'Sorry you have failed at round {i + 1}')
    print('Ending session.')

if __name__ == '__main__':
    try:
        main()
    except:
        print('An error has occured.')
```
Bagian ini merupakan bagian utama program. Program pertama akan membaca ```FLAG``` dari file python di local server, lalu melakukan looping sebanyak ```stages```, dalam hal ini adalah **20**. Di tiap stage, akan dilakukan pemilihan mode di stage tersebut secara acak, apakah **A**, **B**, atau **C**. Terlepas dari mode yang dipilih, akan dilakukan inisialisasi awal nilai ```p```,```q```, dan ```e``` melalui fungsi ```setup()```, serta inisialisasi nilai ```n``` dan ```m```. Kemudian, dilakukan inisialisasi lanjutan berdasarkan mode-nya. Jika modenya adalah **A**, nilai ```n``` akan diperbaharui dengan nilai keluaran fungsi ```modeA()```. Jika modenya adalah **B**, nilai ```e``` akan diperbaharui dengan nilai keluaran fungsi ```modeB()```. Terkahir, jika modenya adalah **C**, nilai ```n``` akan diperbaharui dengan nilai keluaran fungsi ```modeC(e)```.

Setelah proses inisialisasi selesai, dilakukan proses perhitungan untuk mendapatkan ciphertext (```c```). Selanjutnya, nilai ```mode```, ```n```, ```e```, dan ```c``` akan ditampilkan ke pengguna.

Langkah selanjutnya, program akan menerima input plaintext (```m```) yang di-_generate_ di stage ini. Jika tebakan benar, maka akan lanjut ke stage berikutnya. Jika gagal, maka akan keluar dari loop.

Jika pengguna bisa menyelesaikan semua stage, maka flag akan ditampilkan ke layar.

Berikut adalah isi dari fungsi ```setup()```:
```
def setup():
    p = getPrime(512)
    q = getPrime(512)
    e = 65537
    return p, q, e
```
Fungsi ini akan menghasilkan nilai ```p``` dan ```q```, yang merupakan bilangan prima sepanjang 512 bit / 64 bytes.  Selain itu, akan dikembalikan juga nilai ```e``` yakni konstanta dengan nilai **65537**.

Selanjutnya adalah fungsi ```modeA()```:
```
def modeA():
    n = getPrime(512)
    return n
```
Fungsi ini akan mengembalikan nilai ```n``` berupa bilangan prima 512-bit. Sebenarnya dari sini, terlihat bahwa ```modeA()``` memiliki exploit, yakni ```n``` merupakan bilangan prima. Cara exploit nya akan dijelaskan di bagian pembuatan ```script```.

Selanjutnya adalah fungsi ```modeB()```:
```
def modeB():
    e = 3
    return e
```
Fungsi ini akan mengembalikan nilai ```e``` dengan nilai konstan yakni **3**. Dari sini bisa terlihat bahwa ```modeB()``` rentang dengan serangan yang memanfaatkan fakta bahwa eksponen publik (```e```) kecil.

Terakhir adalah fungsi ```modeC()```:
```
def modeC(e):
    while True:
        p = getPrime(512)
        q = nextprime(nextprime(nextprime(p)))
        if GCD(e, (p-1)*(q-1)) == 1:
            break
    n = p*q
    return n
```
Fungsi ini akan meng-_generate_ nilai ```n``` dengan terlebih dahulu meng-_generate_ nilai ```p``` dan ```q```. Jika kita perhatikan ada fakta menarik,yakni ```q``` merupakan bilangan prima ketiga setelah ```p```. Karena ```p``` cukup besar (512-bit), jarak ```p``` dan ```q``` tidak terlalu jauh relatif ke ```n``` dimana persamaan berikut akan terpenuhi:
```
|p-q| < n ^ (1/4)
```
Hal ini bisa menjadi exploit untuk mendapatkan ```p``` dan ```q```.

**2. Craft Payload and Get the Flag**

Untuk langkah selanjutnya, kita akan membuat script untuk mendapatkan flag. Kita bahas untuk setiap mode:

1. Mode A. Pada mode ini kita akan mengeksploitasi vulnerability yakni ```n``` merupakan bilangan prima. Kode untuk menyelesaikannya adalah sebagai berikut:
```
#vulnerability p = prime
def solve_A(N,c):
  e = 65537
  phi_p = N-1
  d = inverse(e,phi_p)
  m = pow(c,d,N)
  print("Plaintext (m): ",m)
  return m
```
Karena kita tahu ```n``` adalah prima, maka faktornya hanyalah ```p``` saja. Karena faktornya cuma p, nilai ```phi_n``` akan menjadi:
```
phi_n = p-1...(1)
```
karena ```n```==```p```, maka persamaan akan menjadi:
```
phi_n = phi_p = n-1...(2)
```
Jika kita sudah mendapat ```phi_n```, kita bisa mendapatkan kunci privat (```d```) dengan persamaan:
```
d = 1+ k* (phi_p)/ e ...(3)
```
Atau kita bisa tinggal menggunakan fungsi ```inverse()``` bawaan library ```Crypto```. 

Jika ```d```, sudah didapatkan, tinggal pangkatkan ```ciphertext``` dengan ```d```, lalu hasilnya dimodulo dengan ```n``` (persamaan dekripsi RSA) dan didapatkan plaintext-nya.

Side info: fungsi ```pow()``` bisa menerima argumen ke 3, yakni nilai modulo sehingga pemanggilan berikut:
```
pow(a,b,c)
```
sama dengan
```
(a ** b) % c
```

2. Mode B. Pada mode ini kita akan mengeksploitasi vulnerability yakni ```e``` nya sangat kecil (e <<< N) sehingga pada sebagian besar kasus, p ** e akan lebih kecil dari N dan efek modulo tidak akan terasa. Kode untuk menyelesaikannya adalah sebagai berikut:
```
#vulnerability e kecil (e=3)
def solve_B(c):
  m = cbrt(c)
  print("Plaintext (m): ",m)
  return m
```
```cbrt()``` adalah fungsi bawaan library ```sympy``` untuk menghitung akar pangkat 3 yang lebih efisien dalam hal waktu ibandingkan menggunakan ```pow()```. Alasan kita mencari akar pangkat 3 adalah dari data yang kita tahu, pada sebagian besar kasus:
```
p ** e < n
```
Sehingga persamaan enkripsinya akan menjadi berikut:
```
c = p **e ...(4)
```
Dalam kasus ini untuk mendapatkan plaintext, persamaannya adalah:
```
p = c ** (1/e) ...(5)
```
Karena ```e``` = 3, maka persamaannya akan menjadi:
```
p = c ** (1/3) ...(6)
```
Atau dengan kata lain adalah plaintext adalah akar pangkat 3 dan ciphertext.

3. Mode C. Pada mode ini kita akan mengeksploitasi vulnerability yakni nilai ```p``` dan ```q``` yang cukup berdekatan, yakni memenuhi persamaan:
```
|p-q| < n ^ (1/4)...(7)
```
Kita bisa melakukan eksploit dengan menggunakan **fermat attack**. Kode untuk melakukan serangannya adalah sebagai berikut:
```
#fermat attack (p dan q deketan, |p-1|<N^1/4)
def solve_C(N,c):
  e = 65537
  #cari p dan q dengane near consecutive prime exploit menggunakan fermat attack (|p-q| < N ^ 1/4)
  a,_ = gmpy2.iroot(N,2)
  while a*a - N <0:
    a +=1
  b = int(a*a - N)
  sqrt_b,_ = gmpy2.iroot(b,2)
  p = int(a - sqrt_b)
  q = N//p
  phi_p = (p-1) * (q-1)
  d = inverse(e,phi_p)
  m = pow(c,d,N)
  print("Plaintext (m): ",m)
  return m
```
Cara melakukannya adalah sebagai berikut:
1. Kita melakukan aproksimasi untuk mendapatkan ```p``` dengan mencari akar pangkat 2 dari ```n```.
2. Kemudian kita hitung nilai:
```
a*a-n
```
Jika nilainya kurang dari 0, inkremen ```a```. (Sebenarnya setelah kubaca-baca lagi, di bagian ```while``` harusnya ada pengecekan apakah ```a*a-n``` itu _perfect square_ (hasil pangkat dua bilangan, misalnya 16 itu _perfect square_ karena merupakan hasil dari 4 **2), tapi kebetulan di server tembus jadi yaudah wkwkw).

3. Jika sudah didapat nilai **a** yang memenuhi, hitung ```a*a-n``` lalu dikonversi ke integer dan hasilnya di-_assign_ ke variabel ```b```.

4. Selanjutnya, karena diasumsikan ```b``` itu _perfect square_, maka cari nilai akar dari ```b``` lalu assign ke variabel bernama ```sqrt_b```. Fungsi ```gmpy.iroot(b,2)``` berguna untuk mencari akar pangkat 2 dari b dengan lebih efisien. Fungsi ini bawaan library **gmpy**.

5. Nilai ```p``` bisa didapatkan dengan mengurangi **a** dengan **sqrt_b**, lalu hasilnya dijadikan integer.

6. Nilai ```q``` bisa didapatkan dengan membagi ```n``` dengan ```p```, lalu hasilnya dijadikan integer. (Operator **//** itu operator pembagian di python yang hasilnya tetap integer meski pembagiannya bersisa).

7. Karena ```p``` dan ```q``` sudah didapay, tinggal mendapatkan ```phi_n``` dengan rumus: (note: di kode typo malah jadi ```phi_p``` tapi ku dah mager ngubahnya)
```
phi_n = (p-1) * (q-1)...(8)
```

8. Jika ```phi_n``` sudah didapat, mendapatkan ```d``` tinggal melakukan inverse modulo antara ```e``` dengan ```phi_n```. Lalu setelah ```d``` didapat, tinggal lakukan proses dekripsi RSA biasa dan didapat _plaintext_-nya.

### Reflections

Permulaan menarik untuk 
  

---
[Back to home](../Readme.md)
