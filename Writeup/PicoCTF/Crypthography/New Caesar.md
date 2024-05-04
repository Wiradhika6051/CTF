## Challenge Name: New Caesar
> Category: Cryptography

> Points: 60

> Solves: 7,012

### Challenge Description: 

We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) ```mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj``` [new_caesar.py](https://mercury.picoctf.net/static/43182e6d4527ef0916b2ce43883227b7/new_caesar.py)


Artifact Files: 
* [new_caesar.py](https://mercury.picoctf.net/static/43182e6d4527ef0916b2ce43883227b7/new_caesar.py)

### Approach

**1. Analyze the Code**  
Dari namanya, sepertinya ini adalah soal _cipher_ _caesar_ yang dimodifikasi. Berikut alur utamanya:
```py
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
...
flag = "redacted"
key = "redacted"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print(enc)
```
Dari asersi, diketahui bahwa _key_-nya merupakan _string_ dengan 1 karakter dan karakter tersebut merupakan salah satu dari 16 karakter huruf kecil awal (a hingga p). _Flag_ akan dijadikan masukan ke fungsi ``b16_encode()``, lalu tiap karakter dari _string_ hasil _encoding_ akan dijadikan masukan ke fungsi ``shift()`` bersama dengan ``key``, lalu hasilnya akan di-_append_ ke _string_ yang berisi hasil enkripsi.

Untuk fungsi ```b16_encode()```, berikut adalah kodenya:
```py
def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		print(ord(c),binary,int(binary[:4], 2),int(binary[4:], 2))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc
```
Setiap karakter pada _flag_ akan dikonversi menjadi representasi biner 8-bit. Kemudian representasi tersebut akan dipecah per 4-bit untuk dijadikan indeks dalam mendapatkan karakter dari _list_ ```ALPHABET```.

Untuk fungsi ```shift()```, berikut adalah kodenya:
```py
def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]
```
Inti fungsi ini adalah geser karakter sebanyak selisih nilai ASCII karakter tersebut dengan _key_.

**2. Develop Decoder**  
Agar kita bisa mendapatkan _flag_, kita perlu membuat _decoder_. Untuk kode penuh _decoder_ terdapat di _file_ [new_caesar_decrypt.py](Artifacts/new_caesar_decrypt.py).
```py
LOWERCASE_OFFSET = ord("a")
ALPHABET = 'abcdefghijklmnop'
.....
ciphertext = input("Enter ciphertext:")
keys = list(ALPHABET)
## Key nya 1 karakter antara a sampai p
# assert all([k in ALPHABET for k in key])
# assert len(key) == 1 
#coba semua kemungkinan key
for key in keys:
	plain = ""
	for i, c in enumerate(ciphertext):
		plain += reverse_shift(c, key)
	flag = b16_decode(plain)
	print(f"Key: {key}. Flag: {flag}")
```
Ide utamanya adalah membalikkan proses enkripsi. Namun karena kita tidak tahu _key_-nya, dilakukan _brute force_ untuk mencoba semua kemungkinan _key_ untuk dipilih hasil yang paling masuk akal. Untuk setiap kemungkinak _key_, akan dilakukan iterasi tiap karakter untuk di _unshift_. Setelah itu, hasil akhirnya akan di-_decode_ dari bentuk **base16** ke _plaintext_.

Berikut adalah kode untuk melakukan _unshift_:
```py
def reverse_shift(c, k):
	term1 =  ALPHABET.index(c)  - ord(k) + 2* LOWERCASE_OFFSET
	for n in range(2):
		term2 = n * (len(ALPHABET))
		if(ord(ALPHABET[0]) <= (term1 + term2) <= ord(ALPHABET[-1])):
			return chr(term1 + term2)
```
Penurunan persamaan untuk _unshift_ terdapat di komentar di atas fungsi. Alasan di bagian terakhir dilakukan pengecekan nilai ASCII adalah dikarenakan di persamaan aslinya terdapat modulo, kita tidak tahu berapa angka sebenarnya dari karakter tersebut dan harus menebaknya. Namun kita tahu bahwa nilai tersebut pasti diantara ``a`` dan ``p`` karena yang di-_shift_ merupakan hasil _encoding_ **base16**.

Berikut adalah kode untuk melakukan _decoding_:
```py
def b16_decode(cipher):
	plain = ""
	for i in range(0,len(cipher),2):
		index_lower = ALPHABET.index(cipher[i])
		index_upper = ALPHABET.index(cipher[i+1])
		binary = "{0:08b}".format((index_lower<<4) + index_upper)
		plain += chr(int(binary,2))
	return plain
```
Intinya melakukan proses yang terbalik dengan _encoding_ dengan merekonstruksi nilai biner karakter asal untuk dikonversi menjadi karakter asal tersebut.

**3. Get the Flag**  
Langsung saja kita jalankan programnya dan diperoleh hasil sebagai berikut:
```
Enter ciphertext:mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj  
µÌËÇÊÈÊÊËÉ
Key: b. Flag: ºÉ¤ÉÊ
                   ¤»º¶
¹·¹¹¹º¶¸

Key: c. Flag: ©¸¸¹sy{vwªx©{u¥t{wz¨w¦u¨u}¨¨©xv{}¥§tw
Key: d. Flag: §¨bhjefgcjfifddlcf
Key: e. Flag: qQqWYTUVYSRYUXU
                             SS[VTY[
RU
Key: f. Flag: v
`
@`FHCDwEvHBrAHDGuDsBuBJuuvECHJrtAD
Key: g. Flag: et_tu?_5723f4e71a0736d3b1d19dde4279ac03
Key: h. Flag: TcNcd.N$&!"U#T& P/&"%S"Q S (SST#!&(PR/"
Key: i. Flag: CR=RS↔=‼§►◄D↕C§▼O▲§◄¶B◄@▼B▼↨BBC↕►§↨OA▲◄
♦♥1?♫1♫♠112☺☼♦♠>0AB♀,☻♦☼3☺2♦♫>
Key: k. Flag: !01ûóþÿ"ð!óý-üóÿò ÿ.ý ýõ  !ðþóõ-/üÿ
Key: l. Flag: ►/
/ ê
àâíî◄ï►âì∟ëâîá▼î↔ì▼ìä▼▼►ïíâä∟▲ëî
ÚÝy: m. Flag: ☼▲ù▲▼ÙùßÑÜÝÞ☼ÑÛ♂ÚÑÝÐ♫Ý♀Û♫ÛÓ♫♫☼ÞÜÑÓ♂
♫ÈèÎÀËÌÿÍþÀÊúÉÀÌÏýÌûÊýÊÂýýþÍËÀÂúüÉÌ
Key: o. Flag: íü×üý·×½¿º»î¼í¿¹é¸¿»¾ì»ê¹ì¹±ììí¼º¿±éë¸»
Key: p. Flag: ÜëÆëì¦Æ¬®©ªÝ«Ü®¨Ø§®ª­ÛªÙ¨Û¨ ÛÛÜ«©® ØÚ§ª
```
Dari hasil tersebut, hampir semuanya berisi karakter _gibberish_ kecuali untuk kunci **g**. Oleh karena itu, diperoleh _flag_-nya adalah:
```
picoCTF{et_tu?_5723f4e71a0736d3b1d19dde4279ac03}
```
### Reflections
Permulaan menarik untuk belajar dasar cipher caesar yang sudah dimodifikasi sedikit.