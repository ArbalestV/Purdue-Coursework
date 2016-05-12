#first sltiu
	ori $5, $0, 0x1000 #write locations in memory
	ori $1, $0, 0x001B #+ve
	ori $2, $0, 0xFFFA #-ve
	sltiu $3, $2, 0x001B
	sltiu $4, $1, 0xFFFA
	sw $3, 0($5)
	sw $4, 4($5)
	halt
