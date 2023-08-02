## Challenge Name: Transformation
Category: Reverse Engineering
Points: 20
Solves: 37k+

Challenge Description: 
I wonder what this really is... [enc](https://mercury.picoctf.net/static/dd6004f51362ff76f98cb8c699510f23/enc) 

```''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])```

Artifact Files:
* [enc](https://mercury.picoctf.net/static/dd6004f51362ff76f98cb8c699510f23/enc)

### Approach
**1. Analisi filenya**
mari kita buka file ```enc```, baik menggunakan notepad atau menggunakan command ```cat```.
```
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽
```
Apa ini? Kok banyak Hanzi!? apa flagnya suruh tinggal translate wkwkwk..
Eh tapi keknya enggak deh, ada Hanggeul jadi keknya flagnya bukan tinggal translate Bahasa Mandarin (:sadge:).

**2. Analisis Kode**
Karena ini soal reverse engineering, seperti namanya, sepertinya ada yang perlu di-reverse. Di petunjuk soal ada kode aneh, mari kita analisis.
```
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```
Sepertinya kode ini digunakan untuk menghasilkan teks yang ada di file ```env```. Dari kode ini, sepertinya si string flag diproses tiap 2 karakter (karena biasanya flag CTF dalam ASCII, kita asumsikan 1 karakter pasti 1 byte). Karakter pertama di shift kiri 1 byte, lalu diconvert ke integer menggunakan ord() lalu hasilnya ditambah dengan nilai desimal karakter kedua. Terakhir, hasil penjumlahannya dijadikan karakter kembali.

Tunggu sebentar, ini seperti hal yang familiar. Anggap si karakter pertama 0x60 dan karakter kedua 0x61. Setelah dijumlah hasil nya akan menjadi 0x6160. Fix ini tinggal tempel tempel aja.

Tapi kok jadi unicode? Welp ternyata fungsi [chr()](https://www.w3schools.com/python/ref_func_chr.asp) emang bisa menghasilkan unicode. Jadi unicode di file tadi hasil pembentukan dua karakter dari flag. Tinggal yang diperlukan yakni mengekstrak karakter-karakter tersebut dari unicode ini.

**3. Decode Characters**
Untuk percobaan pertama mari tinggal kita balikkan fungsinya. Dari sintaksnya jelas ini adalah kode python bisa dilihat dari loopingnya yang menggunakan ```for i in range(0, len(flag), 2)``` .Berarti yang kita perlukan berarti tinggal shift kiri 1 byte buat dapetin karakter pertama dan AND dengan 0xff untuk mendapatkan karakter kedua. Kode nya sebagai berikut:
```
with open('enc',"r") as r:
    enc = r.read()
    print("".join([f"{chr(ord(enc[i])>>8)}{chr(ord(enc[i])&0xff)}" for i in range(len(enc))]))
```
Mari kita coba run:
```
Traceback (most recent call last):
  File "XXX\transformation.py", line 17, in <module>
    enc = r.read()
  File "XXX\Python\Python310\lib\encodings\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 1: character maps to <undefined>
```
Lah gagal!?

Setelah kulakukan searching, ternyata kalau ada karakter unicode sebaiknya dibaca menggunakan "rb", atau dibaca sebagai byte untuk kemudian diencoding lagi di program. Oke lah mari kita coba ulang. Ini kode revisinya:
```
with open('enc',"rb") as r:
    enc = r.read()
    print("".join([f"{chr(ord(enc[i])>>8)}{chr(ord(enc[i])&0xff)}" for i in range(len(enc))]))
```
Dan kita jalankan ulang:
```
Traceback (most recent call last):
  File "XXX\transformation.py", line 18, in <module>
    print("".join([f"{chr(ord(enc[i])>>8)}{chr(ord(enc[i])&0xff)}" for i in range(len(enc))]))
  File "XXX\transformation.py", line 18, in <listcomp>
    print("".join([f"{chr(ord(enc[i])>>8)}{chr(ord(enc[i])&0xff)}" for i in range(len(enc))]))
TypeError: ord() expected string of length 1, but int found
```
Lah gagal !?, hmm mungkin karena dibacanya per byte, tiap elemen dianggap bilangan heksadesimal yang mengakibatkan ini dianggap sebagai integer. Sepertinya perlu diconvert ke string dulu. Mari kita coba ubah menjadi:
```
with open('enc',"rb") as r:
    enc = r.read()
    print("".join([f"{chr(ord(chr(enc[i]))>>8)}{chr(ord(chr(enc[i]))&0xff)}" for i in range(len(enc))]))
```
Dan kita jalankan ulang:
```
ç©æ¯ää»ã
        ¶å½¢æ¥´ç¥®ç´ã´æ½¦å¼¸å¼°æ¤æ¤ã¤·æ
½
```
Sekarang jadi string gak jelas dong. Tapi at least gak crash. 

Tunggu dulu, bukankah waktu mencari soal kenapa membaca file dengan "r" crash dan sebaiknya menggunakan "rb" disebut bahwa setelah dibaca, datanya bisa di decode sesuai kebutuhan? kenapa kita tidak coba encode dulu. Lagipula ku baru sadar kalo dari kode di deskripsi soal, unicodenya minimal dua byte sedangkan yang kita proses malah per 1 byte wkkw.

Setelah mencari ku menemukan bahwa di python kita bisa mengkonversi byte mencari string unicode menggunakan fungsi [decode()](https://www.tutorialspoint.com/python/string_decode.htm). Mari kita terapkan fungsi tersebut di kode:
```
with open('enc',"rb") as r:
    enc = r.read()
    decoded_string = enc.decode()
    print("".join([f"{chr(ord(chr(enc[i]))>>8)}{chr(ord(chr(enc[i]))&0xff)}" for i in range(len(decoded_string))]))
```
Lalu kita jalankan:
```
ç©æ¯ää»ã
        ¶å½¢æ
```
Masih string tidak jelas saudara...Hmm apakah karena unicode tetap melakukan enumerasi per byte ya jika menggunakan indeks?

Coba kalau kita enumerasi per karakter pakai ```for in```
```
with open('enc',"rb") as r:
    enc = r.read()
    decoded_string = enc.decode()
    print("".join([f'{chr(ord(char) >> 8)}{chr(ord(char) & 0xff)}' for char in decoded_string]))
```
Mari kita jalankan:
```
picoCTF{16_bits_inst34d_of_8_0ddcd97a}
```
Alhamdulillah dapat juga flagnya!! Saatnya kita submit


### Reflections
Permulaan bagus untuk belajar reverse engineering, meski jujur ku sempe kekecoh sampai berjam-jam. Beberapa soal web exploitation malah ada yang lebih gampang dari ini dan poinnya lebih besar jadi kerasa kek kurang worth it wkwk. Jadi belajar soal encoding dan konversi byte ke string dan sebaliknya.

---
[Back to home](../Readme.md)
