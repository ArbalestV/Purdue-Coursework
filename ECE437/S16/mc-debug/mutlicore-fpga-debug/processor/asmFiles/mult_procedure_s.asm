org 0x0000
ori $29, $0, 0xFFFC
#Load operands onto stack from main program (4 for now)
ori $10, $0, 3
push $10
ori $10, $0, 4
push $10
ori $10, $0, 4
push $10
ori $10, $0, 2
push $10
ori $10, $0, 2
push $10
#Set counters (number of variable - 1, iteration)
#ori $11, $0, 4 #iteration needed
#ori $12, $0, 0 #current iteration
#Instead of set counters, use stack (if only one value is in stack, then multall is done)
ori $11, $0, 0xFFF8
#result register
ori $13, $0, 0
#main loop
lp:
	beq $29, $11, end
	#jump to subroutine
	jal mult
	addiu $12, $12, 1
	j lp
end:
	#Save value from top of the stack
	pop $20
	halt

#mult subroutine. Use 4 registers (3,4,5,6)
mult:
	#Pop the values
	pop $3
	pop $4
	#Allocate registers for this function
	ori $5, $0, 0
	ori $6, $0, 0
mloop:
	beq $3, $5, mend
	addu $6, $6, $4
	addiu $5, $5, 1
	j mloop
mend:
	#Return on stack
	push $6
	#Return to main
	jr $31
	
