	.arch armv8-a
	.file	"chall.c"
	.text
	.align	2
	.global	func1
	.type	func1, %function
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
	mov	w1, w0 //w1 = w0, ->w1 = nilai arg 2
	mov	w0, w19 //w0 = w19 -> w0 = nilai arg 1
	bl	func1 //call func1
	mov	w1, w0 //w1 = w0 -> w1 simpan hasil operasinya
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	printf
	mov	w0, 0
	ldr	x19, [sp, 16]
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
