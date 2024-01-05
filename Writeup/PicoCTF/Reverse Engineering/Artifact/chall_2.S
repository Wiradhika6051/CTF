	.arch armv8-a
	.file	"chall_2.c"
	.text
	.align	2
	.global	func1
	.type	func1, %function
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
	.size	func1, .-func1
	.section	.rodata
	.align	3
.LC0:
	.string	"Result: %ld\n"
	.text
	.align	2
	.global	main
	.type	main, %function
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
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits


//func1 in c:
//int func1(int input){
//	int a=0,b=0;
//	while(b<=input){
//		a+=3;
//		b+=1;
//	}
//	return a;
//}