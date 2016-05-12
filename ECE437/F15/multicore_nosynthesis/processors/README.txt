TODO: 

RTL
[ ] finish RTL -- branch
Hazard Unit
[X] implement PC logic using branch target 
[X] add to hazard unit for other data hazards (R-type stuff)
[X] add structural hazards (dmemread | dmemwrite)
[X] add branch hazards
[ ] testbench
Datapath
[X] move branch unit to EX
[X] add new signals to hazard unit



LOG: 

9/29
I've added the first pass at the hazard unit and the branch unit. 

The hazard unit is only looking for LW data hazards i.e. LW $r1 -> ADD $s $r1 $t0

The branch unit computes checks for a branch condition and computes the branch target without the use of the alu. This means that only one bubble is necessary instead of three.

We might need to compute the jump target within the PC logic as well

9/30
Completed logic for R-type hazards in hazard unit
talked through rest of project with John

-David
