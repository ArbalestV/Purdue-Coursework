	ori $29, $0, 0xFFFC

	#store current day in reg 15
	ori $15, $0, 0x0014
	#store current month in reg 16
	ori $16, $0, 0x0008
	#store current year in reg 17
	ori $17, $0, 0x07DF
	#store the variable 30 in reg 18
	ori $18, $0, 0x001E
	addi $16, $16, -1
	#store the variable 365 in reg 19
	ori $19, $0, 0x016D
	#store the variable 2000 ini reg 20
	ori $20, $0, 0x07D0
	subu $17, $17, $20

	


	push $17
	push $19
	push $16
	push $18


	ori $26, $0, 0xFFFC #to compare the stack pointer with the beginning
CMP:	beq $29, $26, EXIT
	
MULT:	pop $2 #second variable
	pop $1 #first variable
	ori $4, $1, 0x0000 #store the initial value of first operant in $4
	addi $5, $2, -1 #the no. of iterations
	or $3, $0, $5 #the counter is in register 3

	beq $2, $0, ZERO #when zero is multiplied (2nd operand)
	j ZERO1 #if second operand is not 0, check if 1st operant is 0
	
ZERO:	ori $1, $0, 0x0000 #if 0 is the second multiplicand then store 0
	j DONE #if either operand is 0, then answer is found and so exit
	
ZERO1:	beq $1, $0, ZERO #if the first multiplicant is zero then store 0
	
LOOP:	add $1, $1, $4
	addi $3, $3, -1
	bne $3, $0, LOOP

DONE:	add $15, $15, $1 #reg 15 will store the final output
	j CMP

EXIT:	or $1, $0, $15 #store the final result in reg 1
	halt
	


	
