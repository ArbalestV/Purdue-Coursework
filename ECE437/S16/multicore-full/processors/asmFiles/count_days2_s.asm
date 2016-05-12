	org  0x0000
	ori  $29,$0,0xFFFC
	ori  $2,$0,0x0006 #day
	ori  $3,$0,0x0001 #month
	ori  $4,$0,0x07E0 #year
	ori  $5,$0,0x0001
	subu $3,$3,$5
	ori  $5,$0,0x001E
	push $5
	push $3
	jal  MULT_P
	pop  $3
	ori  $5,$0,0x07D0
	subu $4,$4,$5
	ori  $5,$0,0x016D
	push $5
	push $4
	jal  MULT_P
	pop  $4
	addu $3,$3,$4
	addu $2,$2,$3
	halt
MULT_P:
	pop  $11
	pop  $12
	ori  $10,$0,0x0000
	ori  $8,$0,0x0001
MULT:
	beq  $0,$11,END
	addu $10,$10,$12
	subu $11,$11,$8
	j    MULT
END:
	push $10
	jr   $31
