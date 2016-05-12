`ifndef STORE_FORWARDING_IF_VH
 `define STORE_FORWARDING_IF_VH

 `include "cpu_types_pkg.vh"

interface store_forwarding_if;
   import cpu_types_pkg::*;

   logic dWEN_EX;
   regbits_t rt_EX, rd_M, rd_WB;
   logic [1:0] forwarding_required;


   modport sf (
	       input dWEN_EX, rt_EX, rd_M, rd_WB,
	       output forwarding_required
	       );

   modport tb (
	       input forwarding_required,
	       output dWEN_EX, rt_EX, rd_M, rd_WB
	       );

endinterface // store_forwarding_if
`endif //  `ifndef STORE_FORWARDING_IF_VH

