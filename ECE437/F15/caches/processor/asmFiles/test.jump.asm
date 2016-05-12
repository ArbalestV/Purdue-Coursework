	org 0x0000

	j T1
	nop
	nop
	nop
T1:	j T3
	nop
	nop
	nop
	nop
	nop
T2:	j EXIT
	nop
	nop
	nop
	nop
	nop
T3:	nop
	nop
	j T2
EXIT:	halt
	

