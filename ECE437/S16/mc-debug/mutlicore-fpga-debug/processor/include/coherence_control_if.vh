t`ifndef COHERENCE_CONTROL_IF_VH
 `define COHERENCE_CONTROL_IF_VH

 `include "cpu_types_pkg.vh"

interface coherence_control_if;
   import cpu_types_pkg::*;

   logic ccwrite_0, ccwrite_1;
   logic cctrans_0, cctrans_1;
   logic ccwait_0, ccwait_1;
   logic ccinv_0, ccinv_1;
   word_t ccsnoopaddr;


   modport cc (
	       input ccwrite_0, ccwrite_1, cctrans_0, cctrans_1,
	       output ccwait_0, ccwait_1, ccinv_0, ccinv_1, ccsnoopaddr
	       );

   modport tb (
	       input ccwait_0, ccwait_1, ccinv_0, ccinv_1, ccsnoopaddr,
	       output ccwrite_0, ccwrite_1, cctrans_0, cctrans_1	       
	       );
endinterface // coherence_control_if

`endif //  `ifndef COHERENCE_CONTROL_IF_VH

   
