#-----------------------------------------------
# Test: Control Hazard
# Type: Branch if Equal
#------------------------------------------------

org 0x0000

ori $1, $zero, 0xF0
ori $2, $zero, 0x80
ori $3, $zero, 0x05
ori $4, $zero, 0x0A
ori $5, $zero, 0xFF
ori $6, $zero, 0xAA

cmp:	
	bne $3, $4, label
	or  $7, $zero, $5
	j exit
label:
	or  $7, $zero, $6
	addi $4, $4, -1
	j cmp

exit:	
	sw $7, 0($2)

halt
	
