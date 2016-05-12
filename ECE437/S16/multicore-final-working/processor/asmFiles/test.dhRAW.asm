	org 0x0000
	
	ori $1, $zero, 0x0004
	ori $2, $zero, 0x0003
	ori $8, $zero, 0x00F0
	#nop
	#nop
	#nop
	#nop
	add $3, $1, $2       #Register 3 written
	add $4, $3, $1       #First operand depends on instr 1
	add $5, $2, $3       #Second operand depends on instr 1
	add $6, $1, $2       #First and Second operand depends on instr 1
	#nop
	#nop
	#nop
	#nop
	sw $3, 0($8)
	sw $4, 4($8)
	sw $5, 8($8)
	sw $6, 12($8)
	halt
