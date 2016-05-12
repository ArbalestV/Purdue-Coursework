org 0x0000
ori $29, $0, 0xFFFC
#Main program for approximated number of days from 2000
#Days = Current day + 30 * (Current month - 1) + 365 * (Current year - 2000)
#Using January 6, 2016 as current date
ori $20, $0, 6 #Day -> will be used as result register 
ori $11, $0, 1 #Month
ori $12, $0, 2016 #Year
ori $13, $0, 1 #month to be subtracted
ori $14, $0, 2000 #year to be subtracted

#subtractions
subu $11, $11, $13
subu $12, $12, $14

#Calculation
ori $15, $0, 30 #month coefficient
ori $16, $0, 365 #year coefficient
push $15
push $11
jal mult
pop $17
addu $20, $20, $17
push $16
push $12
jal mult
pop $17
addu $20, $20, $17
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
