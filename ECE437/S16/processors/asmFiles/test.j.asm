	org 0x0000
	ori $1, $0, 0x0010
	ori $2, $0, 0x00F8
	ori $3, $2, 0x57CA
	j store
afterstore:	slt $10, $4, $2
		lui $2, 0xA9
		j exit
store:	sw $3, 20($2)
	and $4, $2, $3
	j afterstore
exit:	halt
