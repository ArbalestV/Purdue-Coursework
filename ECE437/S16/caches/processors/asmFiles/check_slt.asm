	ori $1, $0, 0x001B
	ori $2, $0, 0xFFFF
	slt $3, $1, $2
	slt $4, $2, $1
	sltu $5, $2, $1
	sltu $6, $1, $2
	ori $7, $0, 0x1000
	ori $8, $0, 0x1004
	ori $9, $0, 0x1008
	ori $10, $0, 0x100c
	sw $3, 0($7)
	sw $4, 4($7)
	sw $5, 8($8)
	sw $6, 0($10)
	halt
	
