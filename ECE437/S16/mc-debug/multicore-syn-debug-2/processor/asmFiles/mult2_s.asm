org     0x0000
ori     $29, $0, 0xFFFC
#Load operands.
#Data from main program to stack. Load in random data for this program
jal	mult
sw	$12,0($29)
halt
mult:
	#Pop the values
	ori $11,$0,2
	ori $10,$0,10
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
	jr  $31
