`include "cpu_types_pkg.vh"
`include "forwarding_unit_if.vh"
import cpu_types_pkg::*;
module forwarding_unit (
			forwarding_unit_if.fu fuif
			);
   
   assign fuif.bubble_lw_f = fuif.dREN_M && 
			     ( ( (fuif.is_ITYPE == 1'b0) && ((fuif.rt_EX == fuif.wsel_M) || (fuif.rs_EX == fuif.wsel_WB)) )
			       ||
			       ( (fuif.rs_EX == fuif.wsel_M) || (fuif.rs_EX == fuif.wsel_WB) )); //the specific condition(s) where this particular bubble is needed.
   
   assign fuif.forward_A = (fuif.rs_EX == fuif.wsel_M && fuif.rs_EX != 0 && fuif.regWrite_M != 0) ? 2'b01 : ( (fuif.rs_EX == fuif.wsel_WB && fuif.rs_EX != 0 && fuif.regWrite_WB != 0) ? 2'b10 : 2'b00);
   assign fuif.forward_B = (fuif.is_ITYPE == 1'b1 && (fuif.is_bne_or_beq_M == 1'b0)) ? 2'b00 : ( (fuif.rt_EX == fuif.wsel_M && fuif.rt_EX != 0 && fuif.regWrite_M != 0) ? 2'b01 : ( (fuif.rt_EX == fuif.wsel_WB && fuif.rt_EX != 0 && fuif.regWrite_WB != 0) ? 2'b10 : 2'b00) );
endmodule // forwarding_unit
