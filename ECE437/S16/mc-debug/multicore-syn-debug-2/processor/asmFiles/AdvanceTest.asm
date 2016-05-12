
  #------------------------------------------------------------------
  # R-type Instruction (ALU) Test Program
  #------------------------------------------------------------------

  org 0x0000
  ori   $1,$zero,888
  ori   $2,$zero,200
  ori   $3,$zero,300
  ori   $4,$zero,400
  ori   $5,$zero,500
  ori   $6,$zero,600
  ori   $7,$zero,884
  ori   $8,$zero,256
  ori   $9,$zero,512
  ori   $10,$zero,892


# Now running all R type instructions
  sw    $1,0($6)
  sw    $2,0($7)
  sw    $3,0($8)
  sw    $4,0($9)
  sw    $5,0($10)
  
# Now load the values and starts testing
  lw    $11,0($6)
  sll   $21, $11, 2
  add   $22, $11, $21

  lw    $11,0($6)
  srl   $21, $11, 2
  add   $23, $21, $11

  lui   $24, 8
  add   $25, $24, $23

  lw    $12,0($7)
  lui   $24, 8
  add   $26, $24, $12
  
  lui   $27, 9
  lw    $13,0($8)
  add   $28, $27, $13
  lw    $14,0($9)
  lw    $15,0($10)

  sw    $15, 0($1)
  sw    $12, 0($2)
  sw    $11, 0($3)
  lui   $28, 2
  sw    $28, 0($4)
  sw    $21, 0($5)
  sw    $22, 4($6)
  sw    $24, 4($7)
  sw    $25, 8($8)
  sw    $26, 8($9)
  sw    $27, 8($10)
  
  lw    $11,0($6)
  sw    $11, 0($11)


  halt  # that's all
