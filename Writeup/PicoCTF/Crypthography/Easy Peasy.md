## Challenge Name: Easy Peasy
> Category: Cryptography

> Points: 40

> Solves: 7,593

### Challenge Description: 

A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{})  
```nc mercury.picoctf.net 36449``` [otp.py](https://mercury.picoctf.net/static/2cebaadd44657a7b22ddff3d0401775f/otp.py)


Artifact Files: 
* [otp.py](https://mercury.picoctf.net/static/2cebaadd44657a7b22ddff3d0401775f/otp.py)

### Approach

**1. Analyze the File**

Di challenge ini kita diberikan file ```otp.py``` yang bisa diunduh [di sini](https://mercury.picoctf.net/static/2cebaadd44657a7b22ddff3d0401775f/otp.py) atau bisa juga dilihat di repositori [ini](Artifacts/otp.py).

Jika kita perhatikan ada bagian menarik.
```
def encrypt(key_location):
	ui = input("What data would you like to encrypt? ").rstrip()
	if len(ui) == 0 or len(ui) > KEY_LEN:
		return -1

	start = key_location
	stop = key_location + len(ui)

	kf = open(KEY_FILE, "rb").read()

	if stop >= KEY_LEN:
		stop = stop % KEY_LEN
		key = kf[start:] + kf[:stop]
	else:
		key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))

	print("Here ya go!\n{}\n".format("".join(result)))

	return key_location
```
Pada bagian ini, key yang dipakai akan kembali ke indeks 0 jika sudah mencapai akhir key. Artinya, key yang dipakai akan berulang bila input yang kita masukkan banyak. Ini berarti, kita bisa mendapatkan key yang digunakan untuk mengenripsi flag.

Selain itu, karena operasi enkripsi hanya dengan operasi ```XOR```, kita bisa mendapatkan flag dan melakukan dekripsi dengan mudah karena ```XOR``` bersifat reversibel. Selain itu, pada operasi ```XOR``` terdapat sifat identitas yakni jika suatu bits di-```XOR``` dengan **0**, maka akan menghasilkan bits itu sendiri. Jadi untuk mendapatkan key, tinggal kirimkan payload berupa byte NULL (0x0), lalu key-nya kita ```XOR```-kan dengan hasil enkripsi flag di awal program untuk mendapatkan flag-nya.

**2. Make Script and Get the Flag**

Untuk script-nya bisa dilihat [di sini](Artifacts/Easy%20Peasy_Solver.py). Untuk script ini ada 4 bagian utama:
1. Mendapatkan flag yang di-_encrypt_.
```
  #dapetin 2 pesan input pertama
  c.recvuntil(b"flag!\n")
  #dapetin flag yang diencrypt
  encrypted_flag = c.recvline().rstrip()
```
Bagian ini akan menerima respons dari server berupa nilai _flag_ yang sudah di-_encrypt_, lalu dihilangkan karakter _newline_ (\n) dari hasil responsenya untuk kemudian disimpan sebagai array of binaries.

2. Mengirimkan data _filler_ untuk mencapai posisi _key_ _flag_.
```
  #tunggu promp input muncul
  c.recvuntil(b"to encrypt? ")
  #masukin filler untuk mencapai lokasi mask flag-nya
  c.sendline(b'\x00' * (KEY_LEN-len(encrypted_flag)//2))
```
Karena respons _key_ yang di-_encrypt_ berupa representasi hexadecimal tiap elemen, maka panjang responsnya akan dua kali panjang _key_-nya. Oleh karena itu, panjang _key_ sebenarnya adalah setengah dari panjang response _key_-yang di-_encrypt_. Untuk itu, dikirimkan filler sepanjang panjang key total dikurangi panjang _flag_ agar pointer _key_ bergerak ke posisi _key_ yang digunakan untuk mengenkripsi _flag_.

3. Mengirimkan data _mask_ untuk mendapatkan _flag_ dan menyimpannya:
```
  #tunggu promp input muncul
  c.recvuntil(b"to encrypt? ")
  #masukin payload key-nya
  c.sendline(b'\x00' * (len(encrypted_flag)//2))
  # skip tulisan
  c.recvline()
  #dapetin responsenya
  flag_key = c.recvline().rstrip()
```
Di bagian ini, kita akan mengirimkan _mask_ sepanjang _flag_ untuk mendapatkan _key_ untuk mendekripsi _flag_.

4. Mendapatkan _flag_.
```
  #decrypt using xor operation
  flag = []
  #decode
  for i in range(0,len(encrypted_flag),2):
    enc_flag_hex = bytes_to_hex(encrypted_flag[i:i+2])
    key_hex = bytes_to_hex(flag_key[i:i+2])
    flag.append(f"{chr(enc_flag_hex ^ key_hex)}")
  print("This is the flag: picoCTF{" +"".join(flag) + "}")
```
Pada bagian ini, dilakukan operasi ```XOR``` antara _flag_ yang dienkripsi dengan _key_. Proses enkripsi dilakukan dengan memotong dua byte di _flag_ dan di _key_, lalu konversi string yang dipotong tersebut ke dalam bilangan hexadecimal yang direpresentasikan string tersebut, dilakukan operasi ```XOR```, lalu hasilnya dijadikan ```char``` **ASCII**. Hasil akhirnya lalu di-_concat_ menjadi flag.

Setelah dijalankan didapat seperti berikut:
```
This is the flag: picoCTF{75302b38697a8717f0faee9c0fd36a57}
```
Didapat _flag_-nya:
```
picoCTF{75302b38697a8717f0faee9c0fd36a57}
```

### Reflections
Permulaan menarik untuk belajar bahayanya menggunakan key yang static dan berpola.
  

---
[Back to home](../Readme.md)
