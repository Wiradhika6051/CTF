	.arch armv8-a
	.file	"chall_1.c"
	.text
	.align	2
	.global	func
	.type	func, %function
func: //return  ((83 << wzr)//3) - input =  ((83 << 0)//3) - input =  (83 //3) - input =  27 - input, input = 27 (0000001b)
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
	.size	func, .-func
	.section	.rodata
	.align	3
.LC0:
	.string	"You win!"
	.align	3
.LC1:
	.string	"You Lose :("
	.text
	.align	2
	.global	main
	.type	main, %function
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
