## Challenge Name: Tab, Tab, Attack
>Category: General

>Points: 20

>Solves: 57k+

### Challenge Description: 

Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/fe16c756149cfa85f23e73cd9dbd6a25/Addadshashanammu.zip)

Artifact Files:
* [Addadshashanammu.zip](https://mercury.picoctf.net/static/fe16c756149cfa85f23e73cd9dbd6a25/Addadshashanammu.zip)

### Approach

ide:
1. download pake wget
2. analisis file 
4. download unzip pake sudo apt-get install unzip, di webshell dah ada
5. ekstrak pake unzip : unzip file.zip
6. cd \tab sampe dapet


**1. Analisis File**

Untuk challenge ini aku selesaikan via WebShell.

Pertama kubuka webshell lalu ku download file ```Addadshashanammu.zip``` dengan command:
```
wget https://mercury.picoctf.net/static/fe16c756149cfa85f23e73cd9dbd6a25/Addadshashanammu.zip
```
Lalu kita analisis filenya menggunakan:
```
file Addadshashanammu.zip
```
Diperoleh:
```
Addadshashanammu.zip: Zip archive data, at least v1.0 to extract, compression method=store
```
Oke jadi jelas ini file zip. Sekarang bagaimana cara unzipnya pakai linux?

Setelah ku search, ku menemukan [ini](https://askubuntu.com/questions/86849/how-to-unzip-a-zip-file-from-the-terminal). Jadi, untuk unzip nya kita bisa pakai program ```unzip``` yang bisa diunduh dengan cara berikut:
```
sudo apt-get install unzip
```
Untuk unzipnya bisa dengan command:
```
unzip Addadshashanammu.zip
```
diperoleh:
```
Archive:  Addadshashanammu.zip
   creating: Addadshashanammu/
   creating: Addadshashanammu/Almurbalarammi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
  inflating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet 
```
Woah banyak banget subdirektori nya. Sepertinya bakal nguli. Tunggu jadi inget sesuatu di deskripsi challenge:
```
Using tabcomplete in the Terminal will add years to your life,
```
Sepertinya kita bakal main tab tab an.

**2. Traversing subdirectory**
Kita perlu traverse sampai ujung pertama kita cd ke direktori hasil ekstrak.
```
cd Addadshashanammu
```
Setelah masuk, coba kita list isinya menggunakan:
```
ls
```
Didapat:
```
Almurbalarammi
```
Kalau kalian menggunakan shell yang ada warnanya, bakal kelihatan ini warna untuk direktori. Dari deskripsinya kita bakal main tab-tab an. Coba kita cd lagi 
```
cd
```
lalu kita tab dan...
```
cd Almurbalarammi/
```
wuh keautocomplete dong!!! Coba kita tab lagi
```
cd Almurbalarammi/Ashalmimilkala/
```
Woah!! keautocomplete lagi. Mari kita spam!
```
cd Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
```
Wah...udah gak bisa lagi. Keknya udah nyampai direktori terakhir. Yowislah mari kita pindah kesana dulu.

Lalu kita lihat isinya.
```
ls
```
Didapat:
```
fang-of-haynekhtnamet
```
cuma ada 1 file doang. (Kalau ini di shell berwarna bakal kelihatan ini file).

**3. Get the flag**
Sekarang bagaimana cara mendapatkan string dari file ini? coba lihat dulu deh ini file apaan. Tentu saja pake tab dong. Tidak perlu mempersulit hidup.
```
file fang-of-haynekhtnamet 
```
Didapat:
```
fang-of-haynekhtnamet: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=5fffe70019957f0a27a70bb886b2cfb9f9b21d6e, not stripped
```
Sepertinya ini file binary executable. Coba kita run. Jangan lupa pakai tab wkwkw
```
./fang-of-haynekhtnamet
```
Dan didapat:
```
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_76266e38}
```
Flagnya ketemu!! Alhamdulillah.
```
picoCTF{l3v3l_up!_t4k3_4_r35t!_76266e38}
```
### Reflections
Lumayan belajar tentang tab autocomplete di shell jadi mempermudah hidup.

---
[Back to home](../Readme.md)
