`ifndef FORWARDING_UNIT_IF_VH
 `define FORWARDING_UNIT_IF_VH

 `include "cpu_types_pkg.vh"

interface forwarding_unit_if;
   import cpu_types_pkg::*;

   regbits_t rs_EX, rt_EX, wsel_M, wsel_WB;
   logic [1:0] forward_A, forward_B;
   logic       is_ITYPE;

   logic       is_bne_or_beq_M;
   

   //for lw in MEM stage
   logic       dREN_M; //check if there is a LW operation in the MEM stage.
   logic       bubble_lw_f; //this means that at this stage until memory access is complete do no forward. Also stall while the memory access is taking place until dhit signal is asserted at which time instead of moving into the MEM stage as you would normall, you stall for an extra clock cycle during which a bubble is inserted ino the MEM stage previously occupied by LW.
   //This signal name stands for bubble-during-load-opn-wrt-forwarding
   
   //Thus, the number of stall cycles in the EX stage = 1 + the no of cycles it takes to get dhit.



   logic       regWrite_M, regWrite_WB; //new signals while debugging all_s
   


   modport fu (
	       input rs_EX, rt_EX, wsel_M, wsel_WB, is_ITYPE, dREN_M, is_bne_or_beq_M, regWrite_M, regWrite_WB,
	       output bubble_lw_f, forward_A, forward_B
	       );
   
   modport tb (	     
	       input bubble_lw_f, forward_A, forward_B,
	       output rs_EX, rt_EX, wsel_M, wsel_WB, is_ITYPE, dREN_M, is_bne_or_beq_M, regWrite_M, regWrite_WB
	       );
endinterface // forwarding_unit_if

`endif //  `ifndef FORWARDING_UNIT_IF_VH

   
