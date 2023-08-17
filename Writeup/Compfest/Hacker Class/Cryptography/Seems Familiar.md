## Challenge Name: Seems Familiar
>Category: Cryptography

>Points: 316

>Solves: 34

### Challenge Description: 

Your friend has developed an AES-based enryption system in his spare time. That system is very limited and only able to use printable characters, and furthermore, two of four of its functions has yet to be fixed. Even though they are broken, he insisted the flag can be acquired through thorough analysis of the encryption itself. Feeling intrigued, you feel like you are able to get the flag.

```nc 34.101.174.85 10000```

Original Author: potsu

Artifact Files:
* [chall.py](https://ctf.compfest.id/files/8241b44ec3103e47586c9e2a9ed066d5/chall.py?token=eyJ1c2VyX2lkIjoxMCwidGVhbV9pZCI6bnVsbCwiZmlsZV9pZCI6MTN9.ZNyinA.TeLI-8eEKs0BTmQ-UpFV-wBhYrE)

### Approach

**1. Analyze the file**

Berikut adalah isi file ```chall.py``` :
```
from ast import Assert
import sys
import os
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from secret import FLAG

IV = os.urandom(AES.block_size)
KEY = os.urandom(AES.block_size)

class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

def get_flag():
    print("Sorry, the get_flag function is currently broken. Please try something else.")

def encrypt(msg = None):
    if msg == None:
        msg = input("message (in hex) = ")
    assert len(msg) % 2 == 0, f"Invalid Odd-length string of {msg} has been inputted."
    try:
        msg = binascii.unhexlify(msg.encode()) + FLAG
    except:
        raise AssertionError(f"{msg} is not a valid hex representation.")
    enc = AES.new(KEY, AES.MODE_ECB)
    cipher = enc.encrypt(pad(msg, 16))
    print("ciphertext (in hex): " + binascii.hexlify(cipher).decode())

#DEPRECATED
def decrypt():
    print("Sorry, the decrypt function is currently broken. Please try something else.")

def menu():
    print("1. Get encrypted flag")
    print("2. Encrypt a message")
    print("3. Decrypt a message")
    print("4. Exit")

def main():
    try:
        while True:
            menu()
            choice = input("> " )
            if choice == "1":
                get_flag()
            elif (choice == "2"):
                encrypt()
            elif (choice == "3"):
                decrypt()
            elif (choice == "4"):
                print("ending session.")
                break
            else:
                print("invalid input.")
    except Exception as e:
        print(repr(e))

if __name__ == "__main__":
    main()
```
Penjelasan tentang kode soal adalah sebagai berikut:
```
def main():
    try:
        while True:
            menu()
            choice = input("> " )
            if choice == "1":
                get_flag()
            elif (choice == "2"):
                encrypt()
            elif (choice == "3"):
                decrypt()
            elif (choice == "4"):
                print("ending session.")
                break
            else:
                print("invalid input.")
    except Exception as e:
        print(repr(e))

if __name__ == "__main__":
    main()
```
Bagian ini adalah logic utama program. Program akan melakukan infinite looping lalu menampilkan menu. Kemudian, program menerima input dari pengguna dan melakukan fungsi yang sesuai sesuai input:
1. Jika inputnya ```1```, maka akan memanggil fungsi ```get_flag()```
2. Jika inputnya ```2```, maka akan memanggil fungsi ```encrypt()```
3. Jika inputnya ```3```, maka akan memanggil fungsi ```decrypt()```
4. Jika inputnya ```4```, maka program akan berakhir.

Berikut adalah isi prompt di fungsi ```menu()```:
```
def menu():
    print("1. Get encrypted flag")
    print("2. Encrypt a message")
    print("3. Decrypt a message")
    print("4. Exit")
```  
Berikut adalah isi dari fungsi ```get_flag()```:
```
def get_flag():
    print("Sorry, the get_flag function is currently broken. Please try something else.")
```
Sepertinya kita tidak bisa menggunakan fungsi ini.

Selanjutnya adalah isi dari fungsi ```decrypt()```:
```
#DEPRECATED
def decrypt():
    print("Sorry, the decrypt function is currently broken. Please try something else.")
```
Sama seperti sebelumnya, fungsi ini tidak bisa digunakan.

Terakhir mari kita lihat fungsi ```encrypt()```:
```
def encrypt(msg = None):
    if msg == None:
        msg = input("message (in hex) = ")
    assert len(msg) % 2 == 0, f"Invalid Odd-length string of {msg} has been inputted."
    try:
        msg = binascii.unhexlify(msg.encode()) + FLAG
    except:
        raise AssertionError(f"{msg} is not a valid hex representation.")
    enc = AES.new(KEY, AES.MODE_ECB)
    cipher = enc.encrypt(pad(msg, 16))
    print("ciphertext (in hex): " + binascii.hexlify(cipher).decode())
```
Di fungsi ini, kita mengirimkan input berupa string yang merepresentasikan hex (misal ```4141``` yang merepresentasikan string **AA**). Terdapat pengecekan input untuk memastikan panjang inputnya genap. Kemudian, ```msg``` hasil input akan dijadikan array of binary dan dikonkatenasi dengan ```FLAG```, yang merupakan hal yang harus kita cari. Kemudian, dilakukan enkripsi menggunakan ```AES``` dengan mode ```ECB``` dengan file ```msg``` di-_pad_ agar pas kelipatan 16. Terakhir, hasil enkripsi-nya ditampikan.

**2. Find the Exploit**

Sekarang perlu kita pikirkan cara mendapatkan flagnya.

Setelah membaca-baca writeup tentang ```AES``` serta hint di discord, ternyata ada exploit bernama [Chosen Plaintext Attack](https://medium.com/@hva314/breaking-the-already-broken-aes-ecb-848b358cbc7).(Detail teori bisa dibaca di [sini](https://ctf101.org/cryptography/what-are-block-ciphers/#padding-oracle-attack)) Jadi mode ```ECB``` itu punya sifat yakni dia melakukan enkripsi per blok (biasanya 16 bytes) secara **INDEPENDEN**. Artinya perubahan karater di blok 1 tidak akan mempengaruhi hasil enkripsi di blok 2 selama panjang teks-nya sama. Dengan fakta ini, kita bisa melakukan bruteforce untuk mencari tiap karakter di flag satu-per-satu.

Misal di blok-1. Kita pertama mencari hasil enkripsi dari:
```
message = padding(15-len(flag)) + karakter pertama flag
```
Setelah mendapatkan hasil enkripsi flag ini, kita bruteforce dengan semua kemungkinan karakter flag({}A-Za-z0-9_!-) dengan payload berikut:
```
message = padding(15-len(flag)) + karakter yang dicoba
```
Sehingga pesan yang di-_encypt_ akan menjadi berikut:
```
message = padding(15-len(flag)) + karakter yang dicoba + flag
```
Namun perlu diingat, karena enkripsi-nya dilakukan per blok hanya ```padding(15-len(flag)) + karakter yang dicoba``` yang akan berada di blok 1.

Setelah didapatkan hasil enkripsi-nya, kita bandingkan dengan hasil enkripsi di awal sampai mendapatkan yang sama. Ulangi terus hingga dapat flagnya (bertemu karakter ```}```).

**3. Craft Payload**

Untuk mendapatkan flagnya, ku merancang script berikut:
```
import pwn
 
pwn.context.log_level = 'warn'

CONTEXT = 'local'

c:pwn.remote|pwn.process = None

def set_context(mode:str)->pwn.remote|pwn.process:
  #mode: 'local','remote'
  if(mode=='remote'):
    return pwn.remote("34.101.174.85",10000)
  else:
    return pwn.process(["python3","chall_sf.py"])

def send_payload(payload,block=0):
  #terima pesan awalnya
  c.recvuntil('> ')
  #masukkan input 2
  c.sendline('2')
  #masukkan input payload
  c.sendline(payload)
  #lihat ciphertext
  response = c.recvline()
  ciphertext = response.decode().split(" ")[-1].strip()
  return ciphertext[block*32:(block+1)*32]

def convert_to_hex_str(string:str)->bytes:
  hex_str = string.encode().hex()
  return bytes(hex_str,'utf-8')

if __name__=="__main__":
  FLAG_CHARACTERS = "{}-_!0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

  flags = ""
  #set connection
  c = set_context(CONTEXT)
  #loop terus sampai flag nya complete  (karakter terakhir == '}')
  while len(flags)==0 or  flags[-1]!='}':
    #block yang diperiksa
    block = len(flags) // 16
    #dapetin hash karakter terakhir
    payload = b"00" *  (16 * (block+1) -1 - len(flags)) 
    flag_ciphertext = send_payload(payload,block)
    print("cipher: ",flag_ciphertext)
    #loop semua karakter cari yang cocok
    for char in FLAG_CHARACTERS:
      try_payload = payload + convert_to_hex_str(flags) + convert_to_hex_str(char)
      tried_ciphertext = send_payload(try_payload,block)
      print("try: ",char,"result:",tried_ciphertext)
      if(flag_ciphertext==tried_ciphertext):
        flags += char
        print("FIND MATCH! Current Flag:",flags)
        break
  #jangan lupa tutup koneksinya
  c.close()
```
Berikut penjelasan tiap bagian kode:
- Pada bagian awal terdapat fungsi ```set_context()```:
```
CONTEXT = 'local'

c:pwn.remote|pwn.process = None

def set_context(mode:str)->pwn.remote|pwn.process:
  #mode: 'local','remote'
  if(mode=='remote'):
    return pwn.remote("34.101.174.85",10000)
  else:
    return pwn.process(["python3","chall_sf.py"])
```
Fungsi ini berguna untuk membuat koneksi baru, entah local atau remote.

- Selanjutnya ada fungsi ```send_payload()```:
```
def send_payload(payload,block=0):
  #terima pesan awalnya
  c.recvuntil('> ')
  #masukkan input 2
  c.sendline('2')
  #masukkan input payload
  c.sendline(payload)
  #lihat ciphertext
  response = c.recvline()
  ciphertext = response.decode().split(" ")[-1].strip()
  return ciphertext[block*32:(block+1)*32]
```
Fungsi ini menerima 2 input yakni ```payload``` yang akan dikirimkan serta ```block``` berapa yang akan dikembalikan. Alasan kita melakukan slicing pada blok adalah, kita hanya perlu memeriksa bagian cipher yang bisa kita kembalikan untuk mencari pasangan cipher yang sama. Program ini menerimpa data dari server berupa prompt aksi. Kemudian, karena hanya fungsi ```encrypt()``` saja yang kita akan akses, maka akan selalu mengirimkan response ```2``` ke server. Kemudian program mengirimkan ```payload``` ke server dan menerima responsenya. _Response_-nya akan dalam bentuk seperti ini:
```
ciphertext (in hex): XXXXXXX...
```
pesan yang sudah diterima ini akan kita decode lalu pisahkan dengan delimiter spasi. Karena kita tahu hasil enkripsinya ada di belakang, kita ambil elemen terakhir hasil pemisahan lalu kita bersihkan dari karakter whitespace. Terakhir, kita slicing dari indeks ```block*32``` hingga ```(block+1)*32```. Alasan pemilihan slicing ini adalah, setiap blok akan menghasilkan cipher sebanyak 32 bytes, sehingga yang kita lakukan adalah memotong 32 bytes bagian ciphertext untuk kita kembalikan.

- Kemudian ada fungsi ```convert_to_hex_str```:
```
def convert_to_hex_str(string:str)->bytes:
  hex_str = string.encode().hex()
  return bytes(hex_str,'utf-8')
```
Fungsi ini akan mengubah string (misal : **00**) menjadi string yang berisi representasi hexadecimalnya (misal: **00** menjadi **3030**). Hal ini dilakukan karena input program di server meminta masukan dalam bentuk string yang berisi representasi hexadecimal.

- Terakhir adalah alur utama program:
```
if __name__=="__main__":
  FLAG_CHARACTERS = "{}-_!0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

  flags = ""
  #set connection
  c = set_context(CONTEXT)
  #loop terus sampai flag nya complete  (karakter terakhir == '}')
  while len(flags)==0 or  flags[-1]!='}':
    #block yang diperiksa
    block = len(flags) // 16
    #dapetin hash karakter terakhir
    payload = b"00" *  (16 * (block+1) -1 - len(flags)) 
    flag_ciphertext = send_payload(payload,block)
    print("cipher: ",flag_ciphertext)
    #loop semua karakter cari yang cocok
    for char in FLAG_CHARACTERS:
      try_payload = payload + convert_to_hex_str(flags) + convert_to_hex_str(char)
      tried_ciphertext = send_payload(try_payload,block)
      print("try: ",char,"result:",tried_ciphertext)
      if(flag_ciphertext==tried_ciphertext):
        flags += char
        print("FIND MATCH! Current Flag:",flags)
        break
  #jangan lupa tutup koneksinya
  c.close()
```
Pertama-tama, kita siapkan string berisi semua kombinasi karakter flag yang mungkin beserta string kosong untuk menyimpan flag yang akan kita cari. Kemudian, kita inisialisasikan konteks koneksi. Selanjutnya, kita masuk looping utama.

Looping ini akan dilakukan terus selama kita belum mencapai karakter akhir flag (dari peraturan kita tahu bahwa flag **pasti** diakhiri oleh karakter **}**). Pertama, kita hitung indeks ```block``` yang akan kita cari dengan membagi panjang string dengan **16** (Dari soal kita tahu panjang blok nya adalah 16 bytes). Kemudian, kita buat payload awal untuk acuan dalam bruteforce. Payload yang dikirim adalah string "00" sebanyak (16 * (indeks blok + 1) -1 - panjang ```flag```). Penjelasan rumus ini ada di paragraf selanjutnya.

Jadi seperti kita tahu bahwa tiap blok panjangnya adalah ```16``` bytes, makanya kita akan melakukan pengecekan dengan payload kelipatan ```16```. Kelipatan ```16``` yang dipilihh bergantung sama nomor ```block``` nya. Semakin besar indeks ```block```, semakin besar kelipatannya. Namun karena indeks ```block``` dimulai dari 0, maka kita perlu menambahkan 1 sebelum mengalikan dengan ```16```. Selanjutnya, karena kita ingin menebak karakter terakhir di block, kita kurangi 1 lah jumlah payload yang dikirim sebagai ruang untuk karakter di flag yang akan dicari. Setelah itu, kita kurangi lagi dengan panjang flag karena semakin panjang flag yang kita tahu, semakin pendek padding yang kita butuhkan untuk memastikan karakter yang akan kita cari berada di akhir blok.

Setelah payload acuan dibentuk, kita kirimkan payload tersebut dan kita terima ciphertext nya. Setelah itu, mulai lah proses bruteforce.

Pada proses ini, kita melakukan iterasi untuk semua kemungkinan karakter yang ada di flag. Untuk tiap iterasi, kita buat payload dengan format berikut:
```
try_payload = payload + convert_to_hex_str(flags) + convert_to_hex_str(char)
```
```payload``` merupakan ```payload``` awal yang kita kirimkan untuk mencari cipher uji. ```flags``` adalah isi ```flags``` yang kita ketahui, sedangkan ```char``` adalah karakter yang kita masukkan untuk bruteforce. Jangan lupa konversikan ```flags``` dan ```char``` ke string yang berisi representasi hexadecimal dari mereka.

Setelah ini, payload dikirimkan dan kita lihat potongan cipher nya. Jika sama dengan potongan cipher uji, maka karakter ini tepat dan variabel ```flags``` dikonkatenasi dengan karakter ini. Jika tidak, iterasi akan berlanjut. Jangan lupa setelah flag nya berhasil didapat, koneksi di ```context``` perlu ditutup.

Jika masih bingung bagaimana metode ini bekerja berikut ilustrasinya:

Misalkan ```FLAG``` yang dicari adalah `FFFFFFFFFFFFFFFFFFFFFF`.

Pada pencarian cipher uji, anggap padding adalah ```00000000000000000000000000``` serta padding akhir adalah ```AAAAAAAAAAAAAAAA```. Text yang akan diencrypt akan menjadi berikut:
```
00000000000000000000000000FFFFFF FFFFFFFFFFFFFFFFAAAAAAAAAAAAAAAA
```
Lalu untuk iterasi, anggap karakter input adalah ```X``` yang memiliki representasi hexadecimal ```XX``` yang sama dengan ```FF``` serta ```flags``` yang sudah diketahui adalah `BB` yang memiliki representasi hex ```BBBB``` yang sama dengan ```FFFF```. Payload menjadi berikut:
```
00000000000000000000000000BBBBXX FFFFFFFFFFFFFFFFFFFFFFFFAAAAAAAA
```
Dari ilustrasi diatas, dengan memodifikasi input karakter di akhir blok, kita bisa menebak apa karater yang tepat.

**4. Get the Flag**

Karena di ```local``` tidak ada file ```secret```, kita tidak bisa mendapatkan flag nya. Namun jika ingin menguji di local, kita bisa memodifikasi kode nya sedikit:
```
# from secret import FLAG

FLAG  = b"COMPFEST{flag_g00d_fwf32egetrhtrhrthrhtjrthrthtrhrh}"
```
Sekarang coba kita jalankan:
```
...
try:  g result: feb0ac03bec2b6bf1af70110349f5373
try:  h result: 3c1d177f306b3165e8a65fecb9cc0d8c
FIND MATCH! Current Flag: COMPFEST{flag_g00d_fwf32egetrhtrhrthrhtjrthrthtrhrh
cipher:  75742f61f5da9fb87b8c323c72921a51
try:  { result: c0d45646b0ebde9c60be04bd7f715c11
try:  } result: 75742f61f5da9fb87b8c323c72921a51
FIND MATCH! Current Flag: COMPFEST{flag_g00d_fwf32egetrhtrhrthrhtjrthrthtrhrh}
```
Karena iterasinya lumayan banyak, hanya bagian akhir saja yang ku tampilkan. Tapi disini terlihat script nya bekerja dan flag yang didapat sama dengan yang di kode.

Sekarang mari kita coba jalankan ke server. Pertama ubah bagian berikut:
```
CONTEXT = 'local'
```
menjadi:
```
CONTEXT = 'remote'
```
Sekarang mari kita jalankan:
```
...
try:  } result: 391cb38712035d77713ca37f656db947
try:  - result: b9495cae8f5d5c8c707bff40491b210a
try:  _ result: 2642cd44ccbd373ab27c10a09afcb822
try:  ! result: 1b74d3e91f492c35d1201d109fe27914
try:  0 result: 0ecf3a592f3237fdce5d2ed1cd684162
try:  1 result: 4f5899bcd9fd4bd9e5da2111775db2a2
try:  2 result: f4cef5de9c04a06b3bbcfe21cc2e211b
try:  3 result: 752da0bf6c4dcd0a92de2c5b2c9f3d8d
try:  4 result: ecbde816b49edf951dc7a1214c495d0f
try:  5 result: a0990aabe8dcdf58a761d934f0c952f9
FIND MATCH! Current Flag: COMPFEST15{afdd2f3f203a7ee5055bbadb15302b9c1b81b78a747901fd3232dbd9ff479495
cipher:  9f72d563a049206dca1735f268327830
try:  { result: 4e697206ce719fcb7a6d6f68cd722caf
try:  } result: 9f72d563a049206dca1735f268327830
FIND MATCH! Current Flag: COMPFEST15{afdd2f3f203a7ee5055bbadb15302b9c1b81b78a747901fd3232dbd9ff479495}
```
Alhamdulillah dapat flag nya!
```
COMPFEST15{afdd2f3f203a7ee5055bbadb15302b9c1b81b78a747901fd3232dbd9ff479495}
```

### Reflections

Permulaan menarik untuk belajar vulnerability ASE di mode ECB karena enkripsi yang independen. Selain itu belajar meningkatkan kemampuan _pwntools_ , _scripting_ di Python, serta memperdalam pemahaman tentang encoding bytes.
  

---
[Back to home](../Readme.md)

