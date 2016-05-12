	ori $1, $0, 0x001A
	ori $2, $0, 0x001A
	jal ADD1
	ori $3, $0, 0x00FF
	halt
ADD1:	addi $4, $1, 1
	jr $31
