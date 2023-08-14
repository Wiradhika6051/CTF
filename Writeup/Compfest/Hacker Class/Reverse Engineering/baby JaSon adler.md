## Challenge Name: baby JaSon adler
>Category: Reverse Engineering

>Points: 337

>Solves: 32

### Challenge Description: 

Most people say that babies are hard to understand. But that’s not the case for baby Jason. everyone can understand him easily.

Author: Lily

Artifact Files:
* [adler](https://ctf.compfest.id/files/9f55a73620594ea3774fbab53c598722/adler?token=eyJ1c2VyX2lkIjoxMCwidGVhbV9pZCI6bnVsbCwiZmlsZV9pZCI6NX0.ZNjD7Q.zFTZwGkiJhWmfrUYH8IX_igoTro)
* [enc.txt](https://ctf.compfest.id/files/a1452d7db5bde0d5c289fc59d1e35718/enc.txt?token=eyJ1c2VyX2lkIjoxMCwidGVhbV9pZCI6bnVsbCwiZmlsZV9pZCI6Nn0.ZNjD7Q.2HRKoapQpA5G20RmpySu9_F-Akc)

### Approach

**1. Analyze the Code**

Pada challenge ini kita diberi dua buah file yakni ```enc.txt``` dan ```adler```. Berikut isi ```enc.txt```:
```
DàİŶƻȎɢʓˈ̓͸ϚлѯҧӝՀո֩؍قٶگܒݴޭߣࠗࡼࢰऒॆॻমৢੈભଐୄ୵ப௟ు౳೔ആഺ൬ිชฺຝ໔༈ཫྡဃံၧႝᄃᄹᅱᆤሊቁእዖገጽ᎟᐀ᐳᑩᓦD×ųȐʦ̱ωѰӵ՛؋ڻݒࠕࢪख঄ਝસଡஶ౏ಸഥශຆ༡ྐ࿺႓ᄬᇂቘ዁ጩ᎐ᐪᓵᖽᙔᚹᜟញᠠᢴ᥇᧚ᩀ᪦ᬾᯜ᱄᳗ᵱᷜṳἌᾤ‹₝℄↠∼⊪⌕⎮⑋ⓦ╻◞♅⛜➟⠳⢜⥏
```
Hanya karakter unicode acak.  

Berikut adalah isi file ```adler```:
```
enc=[];holder1=[];holder2=[];fl4g.split("").map((x,y)=>{!y?holder1[y]=x.charCodeAt(0)+1:holder1[y]=((x.charCodeAt(0)+holder1[y-1])%(2**9<<16))});holder1.map((zZ,hh)=>{!hh?holder2[hh]=holder1[hh]:holder2[hh]=(zZ+holder1[hh-1])%(2**9<<8)});enc=holder1.concat(holder2);enc.map((wkwk,zz)=>{enc[zz]=String.fromCharCode(wkwk)});enc=enc.join("")
```
Dengan menggunakan formatter di **vscode**, berikut adalah kode file ```adler```:
```
enc = [];
holder1 = [];
holder2 = [];
fl4g.split("").map((x, y) => {
  !y
    ? (holder1[y] = x.charCodeAt(0) + 1)
    : (holder1[y] = (x.charCodeAt(0) + holder1[y - 1]) % ((2 ** 9) << 16));
});
holder1.map((zZ, hh) => {
  !hh
    ? (holder2[hh] = holder1[hh])
    : (holder2[hh] = (zZ + holder1[hh - 1]) % ((2 ** 9) << 8));
});
enc = holder1.concat(holder2);
enc.map((wkwk, zz) => {
  enc[zz] = String.fromCharCode(wkwk);
});
enc = enc.join("");
```
Terlihat bahwa file ```adler``` adalah kode **javascript**. Diasumsikan ada variabel bernama ```fl4g``` yang merupakan flag challenge ini. ```fl4g``` lalu displit menjadi array of character lalu dilakukan proses mapping:
1. Jika di indeks 0, maka menambahkan entri baru pada variabel ```holder1``` di indeks 0 dengan nilai integer unicode dari karakter di indeks tersebut ditambah 1.
2. Jika di indeks selain 0 (i), maka menambahkan entri baru pada variabel ```holder1``` di indeks tersebut dengan nilai interger unicode karakter di indeks tersebut ditambah nilai di array ```holder1``` pada indekse (i-1) lalu dimodulus dengan **(2 ** 9) << 16**.

Setelah looping ini kelar, maka kita akan lanjutkan ke tahap 2 yakni array ```holder1``` akan diiterasi:
1. Jika di indeks 0, maka menambahkan entri baru pada variabel ```holder2``` di indeks 0 dengan nilai elemen ```holder1``` di indeks 0
2. Jika di indeks selain 0 (i), maka menambahkan entri baru pada variabel ```holder2``` di indeks tersebut dengan nilai di array ```holder1``` pada indekse i ditambah nilai di array ```holder1``` pada indekse (i-1) lalu dimodulus dengan **(2 ** 9) << 8**.

Kemudian, ```holder1``` akan di-_concat_ dengan ```holder2``` lalu disimpan di variabel ```enc```. Terakhir, tiap elemen di ```enc``` akan di-_join_ dan menghasilkan string.

**2. Mencari Celah**

Dari data hasil analisis kode di bagian sebelumnya, kita tahu bahwa file ```enc.txt``` merupakan hasil akhir operasi program di file ```adler```. Berarti sekarang kita perlu memikirkan bagaimna me-_reverse_ program ini agar mendapt flag semula.

Dari kode kita tahu bahwa isi file ```adler``` merupakan gabungan ```holder1``` dan ```holder2```. Selain itu, jika kita perhatikan, isi ```holder2``` bergantung pada isi ```holder1``` saja dan karena modulusnya lumayan besar, bisa kita asumsikan modulus ini tidak berpengaruh. Artinya adalah, jika kita tahu isi ```holder2```, maka ```holder1``` bisa didapat.

Sekarang mari kita analisis untuk ```holder1```, dari output kita tahu bahwa isi ```holder1``` ada di dalam file. Hal ini berarti kita bisa skip kode _reverse engineering_ untuk ```holder2``` dan langsung saja mulai melakukan _reverse engineering_ via ```holder1```. Selain itu juga, elemen ke-0 ```holder1``` bisa langsung dibalikkan saja flow programnya untuk mendapatkan flag di indeks ke-0. Jika flag di indeks ke-0 sudah diketahui, maka proses _reverse engineering_ akan semudah membalikkan telapak tangan. 

**4. Merancang _Script_**

Untuk melakukan _reverse engineering_, kita bisa membuat script menggunakan bahasa **python** (welp, javascript rada rempong buat baca file , harus pake ```node```. Meanwhile python udah built-in untuk File I/O). Berikut adalah kode-nya:
```
#baca isi file as binary terus di decode ke utf-8
with open("enc.txt","rb") as f:
    adler_text = f.read().decode()
    print("Read text:",adler_text)

    #karena len(holder1)==len(holder2), maka split jadi 2
    holder1 = adler_text[:len(adler_text)//2]
    print("holder1: ",holder1)

    #pastikan sizenya benar
    assert len(holder1)==len(adler_text)//2

    #reverse holder1 jadi flag
    flag = ""
    for i in range(len(holder1)):
      #kalau indeksnya 0
      if i==0:
         flag += chr(ord(holder1[i]) - 1)
      #buat sisanya
      else:
        #asumsikan karakter terakhir cukup kecil sehingga memenuhi holder1[-1] < ((2 ** 9) << 16)
        flag += chr(ord(holder1[i]) - ord(holder1[i-1]))
    
    #print flag
    print(f"Flag: {flag}")
  
```
Di kode ini, pertama kita baca filenya sebagai binary lalu di-decode. Alasannya adalah karena default encoding teks adalah **UTF-8**, hal ini bisa membuat python bingung jika membacanya sebagai teks biasa, apakah encoding-nya pakai **UTF-8**, **UTF-16**, dsb. 

Setelah dibaca, kita bagi teksnya menjadi dua lalu ambil potongan awal. Bagian awal ini merupakan konten dari variabel ```holder1```.

Setelah itu, kita menyiapkan variabel string kosong bernama ```flag``` lalu kita lakukan iterasi pada isi variabel ```holder1```. Jika indeksnya 0, kita konkatenasi string ```flag``` dengan karakter yang memiliki nilai unicode sama dengan nilai unicode karakter di ```holder1``` pada indeks 0 dikurangi 1. Jika indeksnya selain itu , sebut saja ```i```, kita konkatenasi string ```flag``` dengan karakter yang memiliki nilai unicode sama dengan nilai unicode karakter di ```holder1``` pada indeks ```i``` dikurangi dengan nilai unicode karakter di ```holder1``` pada indeks ```i-1```. Terakhir, kita cetak flagnya.

**5. Mendapatkan _Flag_**

Berikut hasil eksekusi program:
```
PS C:\Users\Anugrah  Wiradhika F\Documents\CTF\CTF\Writeup\Compfest\Hacker Class\Reverse Engineering> python '.\baby JaSon adler.py'
Read text: DàİŶƻȎɢʓˈ̓͸ϚлѯҧӝՀո֩؍قٶگܒݴޭߣࠗࡼࢰऒॆॻমৢੈભଐୄ୵ப௟ు౳೔ആഺ൬ිชฺຝ໔༈ཫྡဃံၧႝᄃᄹᅱᆤሊቁእዖገጽ᎟᐀ᐳᑩᓦD×ųȐʦ̱ωѰӵ՛؋ڻݒࠕࢪख঄ਝસଡஶ౏ಸഥශຆ༡ྐ࿺႓ᄬᇂቘ዁ጩ᎐ᐪᓵᖽᙔᚹᜟញᠠᢴ᥇᧚ᩀ᪦ᬾᯜ
᱄᳗ᵱᷜṳἌᾤ‹₝℄↠∼⊪⌕⎮⑋ⓦ╻◞♅⛜➟⠳⢜⥏
holder1:  DàİŶƻȎɢʓˈ̓͸ϚлѯҧӝՀո֩؍قٶگܒݴޭߣࠗࡼࢰऒॆॻমৢੈભଐୄ୵ப௟ు౳೔ആഺ൬ිชฺຝ໔༈ཫྡဃံၧႝᄃᄹᅱᆤሊቁእዖገጽ᎟᐀ᐳᑩᓦ
Flag: COMPFEST15{5ba486c81d549cb964e4b4534fec4155b2a242f80c74c6b316f683f7d125ba36}
```
Alhamdulillah kita dapat flag-nya;
```
COMPFEST15{5ba486c81d549cb964e4b4534fec4155b2a242f80c74c6b316f683f7d125ba36}
```
### Reflections

Latihan yang bagus untuk belajar me-_reverse_ program, belajar tentang hash ```adler```, serta mengasah kemampuan scripting di python.
  
---
[Back to home](../Readme.md)
