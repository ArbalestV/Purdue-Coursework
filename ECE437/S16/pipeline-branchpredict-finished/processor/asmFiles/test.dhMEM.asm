#------------------------------------------------
# Test: Data Hazard
# Type: Read after LoadWord
#------------------------------------------------

org 0x0000

ori $1, $zero, 0xF0
ori $2, $zero, 0x80
ori $3, $zero, 0x31
ori $4, $zero, 0x32
ori $5, $zero, 0x34
ori $6, $zero, 0x38

#nop
#nop
#nop
#nop

lw  $7, 0($1)
#nop
#nop
#nop
add $7, $7, $7

#nop
#nop
#nop
#nop

lw  $8, 0($1)
#nop
#nop
add $8, $8, $8

#nop
#nop
#nop
#nop
	
lw  $9, 0($1)
#nop
add $9, $9, $9

#nop
#nop
#nop
#nop

lw  $10, 0($1)
add $10, $10, $10
	
#nop
#nop
#nop
#nop
	
sw $7, 0($2)
sw $8, 4($2)
sw $9, 8($2)
sw $10, 12($2)
halt

org 0x00F0
cfw 0x0001
cfw 0x0002
cfw 0x0004
