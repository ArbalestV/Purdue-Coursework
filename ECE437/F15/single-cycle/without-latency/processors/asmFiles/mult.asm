	ori $29, $0, 0xFFFC
	ori $1, $0, 0x001A
	ori $2, $0, 0x00FF
	push $1
	push $2
	pop $2 #second variable
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

DONE:	push $1
	halt
	
 
