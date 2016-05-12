
	org 0x0000
	
	ori   $1, $zero, 0x0000
	ori   $2, $zero, 0x0080
	ori   $3, $zero, 0x0003
	ori   $4, $zero, 0x0004
	push  $3
	push  $4
	jal   funct
	pop   $3
	sw    $3, 0($2)
	halt
	
funct:	
	pop $5
	pop $6
	add $7, $5, $6
	push $7
	jr $31
