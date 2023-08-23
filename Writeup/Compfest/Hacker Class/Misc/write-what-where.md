## Challenge Name: write-what-where
>Category: Misc

>Points: 498

>Solves: 4

### Challenge Description: 

bukan pwn kok. mari mengasah skill perdukunan ctf :D  
```nc 34.101.174.85 10069```

Artifact Files:
-

### Approach

**1. Analyze Challenge**

Karena di deskripsi gak ada info ini challenge ngapain, kita coba langsung konekin aja.
```
USER@HOST:PATH$ nc 34.101.174.85 10069
Enter a command (or 'exit' to quit): 


```
Kita suruh masukin command. Coba kalau ```exit```.
```
exit
Exiting...

USER@HOST:PATH$ 
```
Setelah **Eciting...** perlu tekan enter, tapi intinya bikin keluar koneksi.

Hmm ini seperti shell. Coba kita join lagi lalu masukkin ```ls```.
```
USER@HOST:PATH$ nc 34.101.174.85 10069
Enter a command (or 'exit' to quit): 
ls
Enter a command (or 'exit' to quit): 
```
Lah gak ada _response_-nya dong. Coba kita lihat current working directory pake ```pwd```:
```
pwd
Enter a command (or 'exit' to quit): 
```
Kosong juga dong... Coba kalau ```cat```, bisa gak.
```
cat
Error: bash: cat: command not found
Enter a command (or 'exit' to quit): 
```
Menarik, kalau error dia tampilin hasilnya tapi kalau enggak dia sembunyikan. Berarti coba-coba command yang bisa nampilin isi file ke stderror.

**2. Get the Flag**

Setelah ku coba-coba, ku nemu command namanya ```source``` yang ngasih error kalau cara makainya salah.
```
USER@HOST:PATH$ nc 34.101.174.85 10069
Enter a command (or 'exit' to quit): 
source
Error: bash: line 0: source: filename argument required
source: usage: source filename [arguments]

```
Setelah kucari di internet, command ```source``` berguna untuk membaca dan mengeksekusi isi file (biasanya berisi command), lalu dijadikan argumen ke shell scrpt. Ada hal menarik di sini, isi file yang dibaca diasumsikan adalah command. Bagaimana kalau isinya bukan command? harusnya ngasih error gak sih? Menarik ini bisa buat dapetin _flag_-nya.

Sekarang tinggal cari _flag_-nya dimana. Biasanya di challenge macam ini, _flag_-nya ada di file ```flag.txt```. Mari kita coba:
```
USER@HOST:PATH$ nc 34.101.174.85 10069
Enter a command (or 'exit' to quit): 
source flag.txt
Error: flag.txt: line 1: COMPFEST15{M3nGas4h_sK1LL_DuKuN_g3s}: command not found
Enter a command (or 'exit' to quit): 

```
Alhamdulillah dapat _flag_-nya:
```
COMPFEST15{M3nGas4h_sK1LL_DuKuN_g3s}
```

**EXTRA**

Special thanks for this [writeup](https://ctftime.org/writeup/25802) by **ryan-cd** from team **meraxes** for giving inspiration about how this challenge could be done.

### Reflections

Permulaan menarik untuk belajar mengenai fitur di UNIX Shell, belajar tentang ```stdout``` dan ```stderr```, redirect output ke file lain, serta belajar command baru semacam ```source```.
  

---
[Back to home](../Readme.md)
