## Challenge Name: Magikarp Ground Mission
>Category: General

>Points: 30

>Solves: 46k+

### Challenge Description: 

Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `b60940ca`
Additional details will be available after launching your challenge instance.

Artifact Files: -

### Approach

**1. Activate Instance**

Okee, ini jenis challenge yang unik karena kita perlu mengaktifkan instance baru dari halaman challenge. Mari kita aktifkan. (Pada saat penulisan writeup ini, instance nya sudah aktif).
![instance activated](Magikarp%20Ground%20Mission-1.JPG)
Setelah aktif, akan ada command ssh dan kita tinggal ssh ke instance nya saja.

**2. How to get the flag?**

Dalam pengerjaan challnge ini ku menggunakan webshell picoCTF. Pertama kita login ke webshell lalu menjalankan command ssh. Dalam kasusku command nya akan seperti ini:
```
ssh ctf-player@venus.picoctf.net -p 51986
```
Setelah itu akan muncul prompt untuk menambahkan ssh key. ketik ```yes```
```
The authenticity of host '[venus.picoctf.net]:51986 ([3.131.124.143]:51986)' can't be established.
ED25519 key fingerprint is SHA256:[REDACTED].
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[venus.picoctf.net]:51986' (ED25519) to the list of known hosts.
```
Lalu masukkan password yang diberikan di deskripsi soal.
```
ctf-player@venus.picoctf.net's password: 
```
Setelah memasukkan password yang benar, maka kita sudah terhubung ke instance.
```
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 5.4.0-1041-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@pico-chall$
```
Untuk melihay ada apa disini masukkan command ```ls```. Hasilnya akan sebagai berikut:
```
1of3.flag.txt  instructions-to-2of3.txt
```
Hmm ada 2 file. Mari kita buka file instruksi terlebih dahulu dengan command ```cat```.
```
Next, go to the root of all things, more succinctly `/`
```
Oh, ini mah buat ke part 2 flagnya kalau lihat dari nama file satunya wkwkwk.. mari kita buka file yang berisi potongan flag. Hasilnya:
```
picoCTF{xxsh_
```
Siip. Sekarang mari kita pergi ke part 2. Dari halaman instruksi sepertinya kita perlu pergi ke root. Command untuk pindah direktori adalah ```cd```. Untuk ke root masukkan command berikut:
```
cd /
```
Lalu kita lihat isi rootnya dengan ```ls```
```
2of3.flag.txt  dev   instructions-to-3of3.txt  media  proc  sbin  tmp
bin            etc   lib                       mnt    root  srv   usr
boot           home  lib64                     opt    run   sys   var
```
Nah ada part 2 nya. Mari kita buka
```
0ut_0f_\/\/4t3r_
```
Sip dapat. Sekarang kita lihat instruksi untuk ke part 3.
```
Lastly, ctf-player, go home... more succinctly `~`
```
Oh, tinggal pergi ke home. Seperti instruksinya kita tinggal ```cd``` saja ke home.
```
cd ~
```
Lalu kita lihat isinya dengan ```ls```
```
3of3.flag.txt  drop-in
```
Nah sip dah bagian terakhir. Eh ```drop-in``` apaan dah? Dah lah tar aja, mari kita buka part 3 nya.
```
c1754242}
```
Sebenarnya di titik ini flagnya dah dapet, tapi ku penasaran sama isi ```drop-in```. Mari kita buka!
```
cat drop-in
```
Didapat:
```
cat: drop-in: Is a directory
```
Owalah ini folder. Gapapa, kita bisa lihat isinya pake ls
```
ls drop-in
```
Didapat:
```
1of3.flag.txt  instructions-to-2of3.txt
```
Lah ini mah folder flag pertama. Yasudahlah, ini hasil akhir flag untuk challenge ini:
```
picoCTF{xxsh_0ut_0f_\/\/4t3r_c1754242}
```
Note: karena untuk menjalankan challenge ini perlu mengaktifkan instance, ada kemungkinan flag bisa berbeda-beda.
### Reflections
Permulaan bagus untuk belajar ssh dan cd, skill yang penting untung menjelajahi direktori. Belajar juga folder umum yang penting seperti root (/) dan home (~)
  

---
[Back to home](../Readme.md)
