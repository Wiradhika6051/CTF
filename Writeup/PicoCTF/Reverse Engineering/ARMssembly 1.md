## Challenge Name: ARMssembly 1
>Category: Reverse Engineering

>Points: 70

>Solves: 3,017

### Challenge Description: 

For what argument does this program print `win` with variables `83`, `0` and `3`? File: [chall_1.S](https://mercury.picoctf.net/static/b4fd1dabc9dec63c37180b5b05783b55/chall_1.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

Artifact Files:
* [chall_1.S](https://mercury.picoctf.net/static/b4fd1dabc9dec63c37180b5b05783b55/chall_1.S) 

### Approach

**1. Referensi untuk ARM Assembly**

Karena di soal ada baris seperti ini:
```
	.arch armv8-a
```
Jelas ini adalah assembly untuk processor ARM. Karena ARM menggunakan arsitektur RISC sedangkan x86 yang biasa digunakan menggunakan arsitektur CISC, maka sintaks dan instruksi yang digunakan akan berbeda juga.

Berikut adalah referensi yang bisa dipakai untuk memahami assembly ARM:
1. https://azeria-labs.com/writing-arm-assembly-part-1/
2. https://diveintosystems.org/book/C9-ARM64/index.html
3. https://developer.arm.com/documentation/dui0801/f/A32-and-T32-Instructions

**2. Analisis Program**

Untuk membantu menganalisis program ini, ku menambahkan catatan di file ```chall_1.S``` yang bisa diakses [di sini](Artifact/chall_1.S). Cattaan diawali simbol ```//``` pada tiap baris.

Pada program ini terdapat 3 bagian utama:
1. Memproses masukan
```nasm
main:
	stp	x29, x30, [sp, -48]! //*(sp-48) = x29, *[sp-40] = x30
	add	x29, sp, 0 // x29 = sp + 0
	str	w0, [x29, 28] // *(x29+28) = w0
	str	x1, [x29, 16] // *(x29+16) = x1
	ldr	x0, [x29, 16] //x0 = *(x29+16)
	add	x0, x0, 8 // x0 += 8
	ldr	x0, [x0] // x0 = *x0 -> input
	bl	atoi //call atoi to conver input to integer
	str	w0, [x29, 44] //*(x29+44) = w0 -> simpan return
	ldr	w0, [x29, 44] //w0 = *(x29+44)
	bl	func //call func
```
Pada bagian ini, masukan dari pengguna akan diubah menjadi _integer_ untuk kemudian dijadikan sebagai parameter ke fungsi ```func```.

2. Melakukan operasi dengan parameter _input_ di fungsi ```func```.
```nasm
func: 
	sub	sp, sp, #32 //sp -= 32
	str	w0, [sp, 12] //*(sp+12) = w0
	mov	w0, 83 //w0 = 83
	str	w0, [sp, 16] //*(sp+16) = w0
	str	wzr, [sp, 20] //*(sp+20) = wzr (wzr=0, register ini nilainyta selalu 0)
	mov	w0, 3 //w0 = 3
	str	w0, [sp, 24] //*(sp+24) = w0
	ldr	w0, [sp, 20] //w0 = *(sp+20)
	ldr	w1, [sp, 16] //w1 = *(sp+16)
	lsl	w0, w1, w0 // w0 = w1 << w0
	str	w0, [sp, 28] // *(sp+28) = w0
	ldr	w1, [sp, 28] //w1 = *(sp+28)
	ldr	w0, [sp, 24] // w0 = *(sp+24)
	sdiv	w0, w1, w0 //sdiv -> signed div, w0 = w1 // w0
	str	w0, [sp, 28] //*(sp+28) = w0
	ldr	w1, [sp, 28] //w1 = *(sp+28)
	ldr	w0, [sp, 12] //w0 = *(sp+12)
	sub	w0, w1, w0 //w0 = w1-w0
	str	w0, [sp, 28] //*(sp+28) = w0
	ldr	w0, [sp, 28] //w0 = *(sp+28)
	add	sp, sp, 32 // sp +=32
	ret
```
parameter _input_ akan dijadikan masukkan ke operasi matematik. Setelah dilakukan penyederhanaan diperoleh operasi yang dilakukan:
```
27 - input
```

3. Memeriksa apakah sukses atau gagal
```nasm
.LC0:
	.string	"You win!"
	.align	3
.LC1:
	.string	"You Lose :("
	.text
	.align	2
	.global	main
	.type	main, %function
  .....
	cmp	w0, 0 
	bne	.L4 //if w0 (return) != 0 (bne -> branch not equal)
	adrp	x0, .LC0 //w0 ==0
	add	x0, x0, :lo12:.LC0 //print sesuatu (You win)
	bl	puts
	b	.L6
.L4:
	adrp	x0, .LC1
	add	x0, x0, :lo12:.LC1
	bl	puts //print sesuatu ( You Lose)
.L6:
	nop
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
```
Pada bagian ini, hasil keluaran dari fungsi ```func``` akan diperiksa. Jika nilainya 0 maka akan mencetak ```You win!``` sedangkan bila tidak maka akan mencetal ```You Lose!```.

**3. Mendapatkan Flag**

Dari penjelasan di atas, kita jadi tahu jika ingin mendapatkan ```You win!```, kita harus memasukkan angka sehingga persamaan:
```
27-input
```
menghasiljan **0**. Oleh karena itu, **input** harus bernilai **27**. Karena jawaban harus dalam heksadesimal 32-bit, maka _flag_-nya adalah:
```
picoCTF{0000001b}
```
### Reflections

Eksplorasi lebih mendalam tentang assembly ARM serta belajar tentang _logical shift_ di ARM.

---
[Back to home](../Readme.md)
