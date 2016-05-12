	ori $29, $0, 0xFFFC
	
	#get all the data values in regs 1-5
MAIN:	ori $1, $0, 0x0005
	ori $2, $0, 0x0002
	ori $3, $0, 0x002A
	ori $4, $0, 0x0010
	ori $5, $0, 0x0003


	ori $15, $0, 0xFFF8 #to compare the stack pointer with if it has only one element
	
	#push all the data values from regs 1-5 in the stack
	push $1
	push $2
	push $3
	push $4
	push $5
	
	jal MULT #multiply the first two operands from the stack

CMP:	beq $29, $15, EXIT #if only one element in stack=>all operands multiplied=>EXIT
	j MULT #if more than 1 element in stack=>multiply the next operand
	
	

MULT:	pop $2 #second variable
	pop $1 #first variable
	ori $16, $1, 0x0000 #store the initial value of 1st operant in $16
	addi $17, $2, -1 #the no. of iterations
	or $18, $0, $17 #the counter is in register 18

	beq $2, $0, ZERO #when 0 is multiplied (2nd operand)
	j ZERO1 #if second operand is not 0, check if 1st operant is 0

ZERO:	ori $1, $0, 0x0000 #if 0 is the second multiplicant the store 0
	j DONE #if either operand is 0, then answer is found and so exit

ZERO1:	beq $1, $0, ZERO #if the first multiplicand is zero then store 0

LOOP:	add $1, $1, $16
	addi $18, $18, -1
	bne $18, $0, LOOP

DONE:	push $1 #now the top element of the stack is the computed value
	jr $31 #to go to the next instruction after MULT function

EXIT:	pop $1 #store the final result in reg 1
	halt
