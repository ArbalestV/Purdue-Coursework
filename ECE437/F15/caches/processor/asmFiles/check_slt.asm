	ori $1, $0, 0x001B
	ori $2, $0, 0xFFFF
	slt $3, $1, $2
	slt $4, $2, $1
	halt
	
