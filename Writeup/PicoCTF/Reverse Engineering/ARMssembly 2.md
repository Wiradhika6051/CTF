## Challenge Name: ARMssembly 2
>Category: Reverse Engineering

>Points: 90

>Solves: 2,253

### Challenge Description: 

What integer does this program print with argument ```3297082261```? File: [chall_2.S](https://mercury.picoctf.net/static/397a4b46a393eda0777f925f1a866f90/chall_2.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})


Artifact Files:
* [chall_2.S](https://mercury.picoctf.net/static/397a4b46a393eda0777f925f1a866f90/chall_2.S)

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

Untuk membantu menganalisis program ini, ku menambahkan catatan di file ```chall_2.S``` yang bisa diakses [di sini](Artifact/chall_2.S). Cattaan diawali simbol ```//``` pada tiap baris.

Pada program ini terdapat sebuah fungsi utama seperti berikut:
```asm
main:
	stp	x29, x30, [sp, -48]! //*(sp-48) = x29, *[sp-40] = x30
	add	x29, sp, 0 // x29 += sp
	str	w0, [x29, 28] // *(x29+28) = w0
	str	x1, [x29, 16] // *(x29+16) = x1
	ldr	x0, [x29, 16] //x0 = *(x29+16)
	add	x0, x0, 8 //x0 += 8
	ldr	x0, [x0] // x0 = *x0 -> input
	bl	atoi //konversi input jadi integer
	bl	func1 //panggil func1
	str	w0, [x29, 44] // *(x29+44) = w0
	adrp	x0, .LC0 //
	add	x0, x0, :lo12:.LC0
	ldr	w1, [x29, 44] //w1 = *(x29+44) //variabel %ld (hasil eksekusi )
	bl	printf //print "Result: %ld\n"
	nop
	ldp	x29, x30, [sp], 48
	ret
```
secara ringkas, program ini akan menerima masukan berupa sebuah _integer_ yang akan dijadikan masukan ke fungsi ```func1```, lalu hasil fungsi tersebut akan dicetak ke layar.

Berikut adalah kode untuk fungsi ```func1```:
```asm
func1:
	sub	sp, sp, #32 // sp -=32
	str	w0, [sp, 12] // *(sp+12) = w0 -> input
	str	wzr, [sp, 24] // *(sp+24) = wzr = 0 -> a
	str	wzr, [sp, 28] // *(sp+28) = wzr = 0 -> b
	b	.L2 //jump ke .L2
.L3:
	ldr	w0, [sp, 24] // w0 = *(sp+24) //w0 = a
	add	w0, w0, 3 //w0 += 3 //a += 3
	str	w0, [sp, 24] //*(sp+24) = w0 
	ldr	w0, [sp, 28] //w0 = *(sp+28) //w0 = b
	add	w0, w0, 1 //w0 += 1 //b +=1
	str	w0, [sp, 28] //*(sp+28) = w0
.L2:
	ldr	w1, [sp, 28] //w1 = *(sp+28) //w1 = b
	ldr	w0, [sp, 12] //w0 = *(sp+12) //w0 = input
	cmp	w1, w0 // w0-w1, jika w1 > w0, maka akan negatif dan kena carry flag
	bcc	.L3 //bcc -> branch if carry (flag) clear, tldr loncat ke .L3 jika w1 <= w0 , if(b <= input)
	ldr	w0, [sp, 24] // w0 = *(sp+24) //w0 = a
	add	sp, sp, 32 // sp+=32
	ret //return a
```
Jika dikonversi ke dalam program **C**, berikut adalah kodenya:
```c
int func1(int input){
	int a=0,b=0;
	while(b<=input){
		a+=3;
		b+=1;
	}
	return a;
}
```
Secara ringkas, fungsi ini akan mengembalikan nilai sebesar 3 kali nilai ``input``.

**3. Mendapatkan Flag**  
Dari penjelasan kode di bagian sebelumnya, kita tahu bahwa fungsi ``func1``akan mengembalikan nilai sebesar 3 kali nilai ``input``. Karena masukan untuk soal ini adalah ```3297082261```, maka keluaran fungsi ```func1``` adalah ```9891246783``` yang bernilai ```0x0002 4D90 72BF``` dalam representasi heksadesimal. Namun, Karena _flag_-nya dalam format heksadesimal 32-bit, hanya 4 _byte_ terbawah saja yang digunakan sehingga _flag_-nya adalah:
```
picoCTF{4d9072bf}
```


### Reflections

Eksplorasi lebih mendalam tentang assembly ARM serta belajar tentang operator **bcc**.

---
[Back to home](../Readme.md)
