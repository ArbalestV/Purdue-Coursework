org     0x0000
ori     $29, $0, 0xFFFC
#Load operands.
#Data from main program to stack. Load in random data for this program
ori	$10, $0, 4
ori	$11, $0, 5
#Push before mult subroutine
push	$10
push	$11
#subroutine
mult:
	#Pop the values
	pop $11
	pop $10
	#Allocate registers for this function
	ori $12, $0, 0
	ori $13, $0, 0
loop:
	beq $13, $11, end
	addu $12, $12, $10
	addiu $13, $13, 1
	j loop
end:
	#Return on stack
	push $12
	halt
