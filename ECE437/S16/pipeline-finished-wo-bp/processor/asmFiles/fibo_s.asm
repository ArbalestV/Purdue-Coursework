org     0x0000
ori     $29, $0, 0xFFFC
ori $1, $0, 3 #this is where the argument is being set.
jal fib
halt
fib:
	bne $1, $0, ELSE1
	or $20, $0, $0
	jr $31
ELSE1:
	ori $2, $0, 1
	bne $1, $2, ELSE2
	ori $20,$0, 1
	jr $31
ELSE2:
	push $31
	addi $1, $1, -1
	jal fib
	addi $1, $1, 1
	or $3, $0, $20
	push $3
	addi $1, $1, -2
	jal fib
	addi $1, $1, 2
	or $4, $0, $20
	pop $3
	add $20, $3, $4
	pop $31
	jr $31
