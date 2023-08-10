## Challenge Name: Serial Key
>Category: Reverse Engineering

>Points: 375

>Solves: 28

### Challenge Description: 

Classic reverse, classic serial key

```nc 34.101.174.85 10003```

Original Author: prajnapras19

Artifact Files:
* [soal](https://ctf.compfest.id/files/f915b06677a36b576a2613429ad62cdb/soal?token=eyJ1c2VyX2lkIjoxMCwidGVhbV9pZCI6bnVsbCwiZmlsZV9pZCI6N30.ZNM53g.3wVRvNQiQmhRXob2oOtsZ5wkKPE)

### Approach

**1. Decompiling Code**

Di challenge ini, kita diberikan binary yang merupakan binary yang sama dengan yang ada di server. Karena ku malas nganalisis satu-satu pakai gdb (spoiler alert: ujung-ujungnya tetep nganalisis juga), jadi ku pakai tool namanya [Ghidra](https://ghidra-sre.org/), tool buat pwn dan reverse engineering. Salah satu fitur unggulannya adalah decompiler, jadi code assembly di binary akan di-_convert_ ke pesudocode mirip bahasa C. Untuk cara menggunakannya ada di websitenya karena ada berbagai versi baik CLI maupun GUI, namun disini ku pakai versi GUI di Windows.

1. Pertama, jalankan ```ghidraRun.bat``` sampai muncul tampilan seperti ini.
![GUI ghidra](Serial%20Key-1.JPG)
2. Tekan File > New Project... untuk membuat project baru.
3. Drag and drop file ```soal``` ke GUI dan secara otomatis akan termuat.
4. Tekan nama file ```soal``` di list hingga tampilan menjadi seperti ini.
![soal Ghidra](Serial%20Key-2.JPG)
5. Untuk melihat daftar fungsi bisa dilihat di kolom sebelah kiri.
![function list](Serial%20Key-3.JPG)
6. Dari daftar fungsi, fungsi yang sepertinya unik dan ditulis penulis soal kemungkinan adalah ```main``` dan ```check```. Mari kita lihat pseudocode kedua fungsi tersebut. Untuk melakukan dekompilasi, tekan nama fungsi tersebut hingga tampilan menjadi seperti ini.
![decompiled](Serial%20Key-4.JPG)
Tab di sebelah kanan merupakan kode hasil dekompilasi. 

Namun perlu diingat, kode hasil dekompilasi memiliki nama variabel yang lumayan acak sehingga perlu kita kasih label. Untuk memberi label, tekan nama variabel terus klik kanan > Renama Variable seperti ini:
![rename variable](Serial%20Key-5.png)
Pada saat pembuatan writeup, hampir semua variabel sudah ku beri label. 

**2. Analisis Fungsi ```main```**

Hasil akhir pseudocode fungsi ```main``` yang sudah dilabeli adalah sebagai berikut:
```

undefined8 main(void)

{
  int isValid;
  FILE *f;
  long in_FS_OFFSET;
  int counter;
  undefined key [32];
  undefined flag [104];
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  setvbuf(stdout,(char *)0x0,2,0);
  counter = 0;
  do {
    if (99 < counter) {
      f = fopen("flag.txt","r");
      __isoc99_fscanf(f,&input_key,flag);
      printf("%s",flag);
exit:
      if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
        __stack_chk_fail();
      }
      return 0;
    }
    printf("Serial %d ==> ",(ulong)(counter + 1));
    __isoc99_scanf(&input_key);
    isValid = check(key);
    if (isValid == 0) {
      puts("Salah");
      goto exit;
    }
    counter = counter + 1;
  } while( true );
}
```
Fungsi ini akan melakukan infinite loop dan satu-satunya cara untuk menghentikannya ialah dengan return nilai. Pada awal loop ada sebuah variabel bernama ```counter``` yang memiliki nilai 0. Fungsi hanya akan ```return 0``` bila serial key salah atau nilai counter > 100 dan file flagnya ada. Jika nilai counter masih <= 100, program akan memanggil fungsi check yang mengembalikan suatu angka. Jika angka yang dikembalikan adalah 0, maka serial key salah dan program akan keluar. Namun jika bukan 0, maka nilai counter akan bertambah sebanyak 1.

**3. Analisis Fungsi ```check```**

Untuk fungsi ```check```, hasil dekompilasi yang sudah dilabeli adalah sebagai berikut:
```

undefined8 check(char *serial_key)

{
  size_t param_length;
  undefined8 isValid;
  void *pvVar1;
  char *pcVar2;
  long in_FS_OFFSET;
  int i;
  int j;
  int k;
  int m;
  int l;
  char *flag [6];
  char part_1;
  char part_2;
  char part_3;
  char part_4;
  long canary;
  char chara;
  int len;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  param_length = strlen(serial_key);
  if (param_length == 24) {
    for (i = 4; i < 24; i = i + 5) {
      if (serial_key[i] != '-') {
        isValid = 0;
        goto fail;
      }
    }
    for (j = 0; j < length; j = j + 1) {
      len = strncmp(*(char **)(serial + (long)j * 8),serial_key,24);
      if (len == 0) {
        isValid = 0;
        goto fail;
      }
    }
    for (k = 0; len = length, k < 24; k = k + 5) {
      for (m = k; m < k + 4; m = m + 1) {
        chara = serial_key[m];
        if (((chara < '0') || ('9' < chara)) && ((chara < 'A' || ('Z' < chara)))) {
          isValid = 0;
          goto fail;
        }
      }
      part_1 = serial_key[k];
      part_2 = serial_key[(long)k + 1];
      part_3 = serial_key[(long)k + 2];
      part_4 = serial_key[(long)k + 3];
      for (l = 0; l < k / 5; l = l + 1) {
        len = strncmp(flag[l],&part_1,4);
        if (len == 0) {
          isValid = 0;
          goto fail;
        }
      }
      pcVar2 = (char *)malloc(4);
      flag[k / 5] = pcVar2;
      pcVar2 = strdup(&part_1);
      flag[k / 5] = pcVar2;
    }
    pvVar1 = malloc(0x18);
    *(void **)(serial + (long)len * 8) = pvVar1;
    len = length;
    pcVar2 = strdup(serial_key);
    *(char **)(serial + (long)len * 8) = pcVar2;
    length = length + 1;
    isValid = 1;
  }
  else {
    isValid = 0;
  }
fail:
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return isValid;
}
```
Fungsi ```check``` ini lumayan susah dipahami sehingga ku harus melakukan analisis manual menggunakan ```gdb``` yang dapat diinstall di linux dengan command berikut (yes, ku ngerjain challenge ini bolak-balik Windows-Linux karena laptop dan OS Windows-nya tidak support WSL).
```
sudo apt-get update
sudo apt-get install gdb
```
Untuk menjalankan ```gdb```, masukkan command berikut:
```
gdb soal
```
Untuk melakukan disassembly fungsi, contoh saja ```check```, masukkan command berikut:
```
disass check
```
Yang akan menampilkan tampilan seperti berikut:
![disass gdb](Serial%20Key-6.png)
Selain itu, seperti di gambar, kita juga bisa menambahkan breakpoint dengan command:
```
b *ADDRESS
```
Jika ingin menjalankan aplikasi, tinggal masukkan:
```
run
```
Agar tampilannya lebih enak dilihat, masukkan:
```
layout asm
```
Tampilan gdb akan menjadi seperti berikut:
![layout asm](Serial%20Key-7.png)
Untuk menjalankan instruksi selanjutnya, masukkan:
```
ni
```
Jika ingin melihat isi semua register, masukkan:
```
i r
```
Atau jika hanya ingin melihat isi 1 register saja:
```
i r NAMA_REGISTER
```

Setelah melakukan analisis tambahan di gdb, ku mendapat konteks fungsi check yang akan dijabarkan sebagai berikur:

```
undefined8 check(char *serial_key)

{
  size_t param_length;
  undefined8 isValid;
  void *pvVar1;
  char *pcVar2;
  long in_FS_OFFSET;
  int i;
  int j;
  int k;
  int m;
  int l;
  char *flag [6];
  char part_1;
  char part_2;
  char part_3;
  char part_4;
  long canary;
  char chara;
  int len;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  param_length = strlen(serial_key);
  if (param_length == 24) {
    ...
  }
  else {
    isValid = 0;
  }
fail:
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return isValid;
}
```
Fungsi ini menerima 1 param, yakni string serial key, pertama , dicerk dulu panjang serial key nya, jika panjangnya 24, maka akan lanjut ke tahap berikutnya. Jika tidak, maka variabel isValid akan diberi nilai 0 dan di return. Seperti kita tahu, jika hasil return nya 0, maka serial key nya salah.

```
for (i = 4; i < 24; i = i + 5) {
  if (serial_key[i] != '-') {
    isValid = 0;
    goto fail;
  }
}
```
Setelah dipastikan panjagnya 24, selanjutnya dilakukan pengecekan separator. Dimulai dari indeks 4, untuk setiap 5 indeks berikutnya, karakternya harus merupakan separator ('-'). Berdasarkan data ini, kita bisa menerka bentuk serial key valid adalah sebagai berikut:
```
XXXX-XXXX-XXXX-XXXX-XXXX
```
Jika lolos pengecekan maka akan lanjut ke bagian berikut:
```
    for (j = 0; j < length; j = j + 1) {
      len = strncmp(*(char **)(serial + (long)j * 8),serial_key,24);
      if (len == 0) {
        isValid = 0;
        goto fail;
      }
    }
```
Bagian ini akan mengecek apakah ```serial_key``` yang diinput ada yang sama (duplikat) dengan semua serial key sebelumnya yang pernah diinput. ```serial``` adalah array of string yang berisi daftar serial key yang pernah diinput dan ```length``` adalah panjang ```serial```. Jika ada duplikat maka ```serial_key``` tidak valid. 

Jika ```serial_key``` unik, maka akan lanjut ke langkah berikutnya:
```
for (k = 0; len = length, k < 24; k = k + 5) {
  for (m = k; m < k + 4; m = m + 1) {
    chara = serial_key[m];
    if (((chara < '0') || ('9' < chara)) && ((chara < 'A' || ('Z' < chara)))) {
      isValid = 0;
      goto fail;
    }
  }
}
```
Bagian ini akan memeriksa apakah tiap karakter pada key yang bukan separator merupakan karakter angka 0-9 atau huruf A-Z. Jika bukan, maka serial key tidak valid. Berdasarkan info ini, format serial key adalah sebagai berikut:
```
XXXX-XXXX-XXXX-XXXX-XXXX
```
dengan ```X``` memenuhi regex ```[0-9A-Z]```.

Jika pengecekan sebelumnya sukses, maka akan lanjut ke langkah pengecekan terakhir:
```
part_1 = serial_key[k];
part_2 = serial_key[(long)k + 1];
part_3 = serial_key[(long)k + 2];
part_4 = serial_key[(long)k + 3];
for (l = 0; l < k / 5; l = l + 1) {
  len = strncmp(flag[l],&part_1,4);
  if (len == 0) {
    isValid = 0;
    goto fail;
  }
}
```
Jujur saja ku sempet bingung saat melihat dekompilasi ini dan baru ngerti bagian ini untuk apa setelah menganalisis menggunakan ```gdb```.

Jadi, bagian ini mengecek apakah setiap segmen pada serial key (XXXX) unik. Jadi format serial key yang valid ialah sebagai berikut:
```
XXXX-XXXX-XXXX-XXXX-XXXX
```
dengan aturan:
1. ```X``` memenuhi regex ```[0-9A-Z]```
2. Tiap serial key harus berbeda minimal satu karakter satu sama lain
3. Tiap karakter di satu segmen boleh sama atau berbeda satu sama lain
4. Tiap segmen pada satu serial key harus berbeda satu sama lain.

Jika serial key valid, maka serial key akan ditambahkan ke array ```serial``` serta variabel ```isValid``` akan memiliki nilai 1 yang menandakan serial key valid.
```
    ...
      pcVar2 = (char *)malloc(4);
      flag[k / 5] = pcVar2;
      pcVar2 = strdup(&part_1);
      flag[k / 5] = pcVar2;
    }
    pvVar1 = malloc(0x18);
    *(void **)(serial + (long)len * 8) = pvVar1;
    len = length;
    pcVar2 = strdup(serial_key);
    *(char **)(serial + (long)len * 8) = pcVar2;
    length = length + 1;
    isValid = 1;
```

**4. Merancang _Script_ dan Mendapatkan Flag**


### Reflections

Permulaan menarik untuk 
  
---
[Back to home](../Readme.md)
