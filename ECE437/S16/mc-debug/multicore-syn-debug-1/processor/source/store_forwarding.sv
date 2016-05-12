`include "cpu_types_pkg.vh"
`include "store_forwarding_if.vh"
import cpu_types_pkg::*;

module store_forwarding (
			 store_forwarding_if.sf sfif
			 );

   //1 -> forward from MEM stage
   //2 -> forward from WB stage
   //0 -> no forwarding
   assign sfif.forwarding_required = ( (sfif.dWEN_EX == 1'b0) ? 2'b00 : ( (sfif.rt_EX == sfif.rd_M) ? 2'b01 : ( (sfif.rt_EX == sfif.rd_WB) ? 2'b10 : 2'b00)));
endmodule // store_forwarding

