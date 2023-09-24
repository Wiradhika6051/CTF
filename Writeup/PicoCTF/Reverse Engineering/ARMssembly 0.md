## Challenge Name: ARMssembly 0
>Category: Reverse Engineering

>Points: 40

>Solves: 6,239

### Challenge Description: 

What integer does this program print with arguments ```4004594377``` and ```4110761777```? File: [chall.S](https://mercury.picoctf.net/static/006961dc756fc3f418b0dbe0a42dcee8/chall.S)
Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

Artifact Files:
* [chall.S](https://mercury.picoctf.net/static/006961dc756fc3f418b0dbe0a42dcee8/chall.S)

### Approach

//return angka terbesar
//karena 4110761777 lebih besar dari 4004594377, maka return 4110761777 atau 0xF5053F31 dalam hex

**1. Sekilas Tentang ARM Assembly**

Karena di soal ada baris seperti ini:
```
	.arch armv8-a
```
Jelas ini adalah assembly untuk processor ARM. Karena ARM menggunakan arsitektur RISC sedangkan x86 yang biasa digunakan menggunakan arsitektur CISC, maka sintaks dan instruksi yang digunakan akan berbeda juga.

Berikut adalah referensi yang bisa dipakai untuk memahami assembly ARM:
1. https://azeria-labs.com/writing-arm-assembly-part-1/
2. https://diveintosystems.org/book/C9-ARM64/index.html

**2. Analisis Program**

Untuk membantu menganalisis program ini, ku menambahkan catatan di file ```chall.S``` yang bisa diakses [di sini](Artifact/chall.S). Cattaan diawali simbol ```//``` pada tiap baris.

Pada program ini terdapat 3 bagian utama:
1. Memproses masukan
```
main:
	stp	x29, x30, [sp, -48]! //*(sp-48) = x29, *(sp-40) = x30 
	add	x29, sp, 0  //x29 = sp + 0
	str	x19, [sp, 16] //*(sp + 16) = x19
	str	w0, [x29, 44] //w0 -> x0 tapi lower 32 bits, x0 itu 64 bits. *(x29+44) = w0
	str	x1, [x29, 32] //*(x29+32) = x1
	ldr	x0, [x29, 32] // x0 = *(x29+32)
	add	x0, x0, 8 //x0 += 8
	ldr	x0, [x0] // x0 = *(x0)
	bl	atoi //call atoi -> convert string to int, convert arg 1
	mov	w19, w0 //w19 = w0 ->w19 = nilai arg 1
	ldr	x0, [x29, 32] //x0 = *(x29+32)
	add	x0, x0, 16 //x0 += 16
	ldr	x0, [x0] //x0 = *(x0)
	bl	atoi //call atoi -> convert arg 2
```
Pada bagian ini, input pertama dan kedua (asumsikan input didapat dari _command line argument_) akan dibaca dari _stack_ lalu dikonversi menjadi angka dengan fungsi ```atoi()```. instruksi ```bl``` digunakan untuk memanggil fungsi. Parameter fungsi disimpan di register dengan parameter pertama disimpan di register ```x0```, parameter kedua di register ```x1```, dst. register ```x0``` dapat memuat 64 bits (8 bytes), sedangkan register ```w0``` merupakan setengah bawah register ```x0``` yang dapat menyimpan 32 bits (4 bytes).

2. Melakukan operasi dengan parameter _input_ di fungsi ```func1```.
```
func1:
	sub	sp, sp, #16 // sp -= 16
	str	w0, [sp, 12] //*(sp+12) = w0 //arg 1
	str	w1, [sp, 8] //*(sp+8) = w1 //arg 2
	ldr	w1, [sp, 12] //w1 = *(sp+12) //arg 1
	ldr	w0, [sp, 8] //w0 = *(sp+8) //arg 2
	cmp	w1, w0 //w1 - w0 -> bandingkan arg 1 dan arg 2
	bls	.L2 // w1<=w0 ? jumlp ke L2 -> arg1 <= arg2
	ldr	w0, [sp, 12] //w0 = *(sp+12) ->arg 1 awal
	b	.L3 // jump ke L3 -> return arg1
.L2:
	ldr	w0, [sp, 8] //w0 = *(sp+8) //arg 2 -> return arg 2
.L3:
	add	sp, sp, 16 //sp += 16
	ret //return , in short ini program return nilai terbesar diantara dua angka
main:
  ...
	mov	w1, w0 //w1 = w0, ->w1 = nilai arg 2
	mov	w0, w19 //w0 = w19 -> w0 = nilai arg 1
	bl	func1 //call func1
```
parameter _input_ 1 dan 2 masing-masing akan disimpan di ```w0``` dan ```w1```. Di fungsi ```func1```, kedua nilai ini akan dibandingkan. Jika parameter _input_ 1 lebih kecil atau sama dengan (<=) parameter _input_ 2, maka fungsi ```func1``` akan mengembalikan parameter _input_ 2, jika tidak, maka akan mengembalikan parameter _input_ 1. Hal ini berarti fungsi ini mengembalikan nilai terbesar diantara dua angka.

3. Mencetak angka yang terpilih.
```
	mov	w1, w0 //w1 = w0 -> w1 simpan hasil operasinya
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	printf
	mov	w0, 0
	ldr	x19, [sp, 16]
	ldp	x29, x30, [sp], 48
	ret
```
Pada bagian ini, angka yang terpilih akan disimpan di register ```w0```, lalu dijadikan parameter ke fungsi ```printf()``` untuk dicetak ke layar. Terakhir, program akan mengeksekusi instruksi ```ret``` dan program pun akan berakhir.

**3. Mendapatkan Flag**

Dari penjelasan di atas, kita jadi tahu bahwa yang akan dicetak oleh program adalah angka terbesar antara ```4004594377``` dan ```4110761777``` yang mana bisa ditebak bahwa angka yang lebih besar adalah ```4110761777```. Untuk mendapatkan _flag_-nya, angka ```4110761777``` kita konversikan menjadi bilangan heksadesimal tanpa notasi ```0x``` lalu kita selipkan di dalam string ```picoCTF{}```. Setelah dikonversi didapat representasi heksadesimal dari ```4110761777``` adalah ```F5053F31``` sehingga _flag_-nya adalah:
```
picoCTF{F5053F31}
```
### Reflections

Menarik jadi bisa belajar arsitektur ARM yang sedikit berbeda dengan x86.

---
[Back to home](../Readme.md)
