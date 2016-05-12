
  #------------------------------------------------------------------
  # R-type Instruction (ALU) Test Program
  #------------------------------------------------------------------

  org 0x0000
  ori   $1,$zero,0xD269
  ori   $2,$zero,0x37F1

  ori   $21,$zero,0x80
  ori   $22,$zero,0xF0

# Now running all R type instructions
  or    $3,$1,$2
  jal	Next
  j     STORE

BBB:   ori $16, $zero, 0x1
  ori $17, $zero, 0x1
  beq $16, $17, Continue

Oops:  slti $1, $16, 0
       sltiu $13, $16, 999
       JR $31
Continue:   sll   $11,$1,4
  bne $16, $zero, Oops

Next:  and   $4,$1,$2
  andi  $5,$1,0xF
  addu  $6,$1,$2
  addiu $7,$3,0x8740
  j     BBB
  
  
# Store them to verify the results
STORE:  sw    $13,0($22)		#M[R[22] + 0] <= R[13]
  sw    $3,0($21)		#M[R[21] + 0] <= R[3]
  sw    $4,4($21)
  sw    $5,8($21)
  sw    $6,12($21)		#works
  sw    $7,16($21)		#Does not work
  sw    $8,20($21)
  sw    $9,24($21)
  sw    $10,28($21)
  sw    $11,32($21)
  #sw    $12,36($21)
  halt  # that's all
