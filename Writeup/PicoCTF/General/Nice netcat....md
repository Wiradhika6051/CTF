## Challenge Name: Nice netcat...
>Category: General

>Points: 15

>Solves: 93k+

Challenge Description: 
There is a nice program that you can talk to by using this command in a shell: ```$ nc mercury.picoctf.net 35652```, but it doesn't speak English...

Artifact Files:
-

### Approach
**1. Connect to the server**
Karena posisiku lagi di device windows tanpa wsl, maka challenge ini kukerjakan via webshell di web PicoCTF. Cara mengaksesnya sudah dijelaskan di writeup [Wave a flag](Wave%20a%20flag.md). 

Setelah masuk ke shell, masukkan command berikut:
```
nc mercury.picoctf.net 35652
```
Muncullah deretan angka random seperti berikut:
```
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
57 
98 
51 
98 
55 
51 
57 
50 
125 
10 

```
Angka-angka ini aneh tapi dari rentangnya yg kebanyakan diatas 50 namun dibawah 150, kemungkinan ini nilai desimal dari huruf latin yang menggunakan encoding ASCII. Mari kita coba konversi ke string menggunakan online converter ASCII to Text yang banyak tersedia di internet. Setelah dikonversi didapat hasil berikut:
![hasil](Nice%20netcat....jpg)
Didapatkan flag sebagai berikut:
```
picoCTF{g00d_k1tty!_n1c3_k1tty!_9b3b7392}
```

### Reflections
Permulaan bagus untuk belajar command ```nc```, encoding ASCII, serta googling mencari converter online.

---
[Back to home](../Readme.md)
