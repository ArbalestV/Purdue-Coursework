	ori $1, $0, 0x001A
	ori $2, $0, 0x001A
	beq $1, $2, END
	ori $3, $0, 0x00FF
END:	halt
