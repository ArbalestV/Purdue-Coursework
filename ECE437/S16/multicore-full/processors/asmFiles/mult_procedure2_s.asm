	org  0x0000
	ori  $29,$0,0xFFFC
	ori  $2,$0,0x0003 #counter for number of operands
	ori  $3,$0,0x0002 #op1
	ori  $4,$0,0x0002 #op2
	ori  $5,$0,0x0003 #op3
	#ori  $6,$0,0x0015 op4
	push $3
	push $4
	push $5
	#push $6
	push $2
	jal  MULT_ALL
	ori  $15,$0,0x00F0
	sw   $10,0($15)
	halt
MULT_ALL:
	pop  $7
	ori  $2,$0,0x0001
	subu $7,$7,$2
START:
	beq  $0,$7,END2
	subu $7,$7,$2
	pop  $8
	pop  $9
	ori  $3,$0,0x0001
	ori  $10,$0,0x0000
MULT:
	beq  $0,$8,END
	addu $10,$10,$9
	subu $8,$8,$3
	j    MULT
END:
	push $10
	j    START
END2:
	pop  $10
	jr   $31
