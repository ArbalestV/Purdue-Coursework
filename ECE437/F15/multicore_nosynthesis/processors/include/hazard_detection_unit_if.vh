`ifndef HAZARD_DETECTION_UNIT_IF_VH
`define HAZARD_DETECTION_UNIT_IF_VH

`include "cpu_types_pkg.vh"

interface hazard_detection_unit_if;

   import cpu_types_pkg::*;

   //declarations
   logic stall;
   regbits_t ex_regRt, de_regRs, de_regRt;
   logic ex_dR_REQ, ex_dW_REQ, de_dR_REQ, de_dW_REQ;

   //ports
   modport hdu (
		input ex_dR_REQ, ex_regRt, de_regRs, de_regRt, ex_dW_REQ, de_dR_REQ, de_dW_REQ,
		output stall
		);
   modport tb (
	       input stall,
	       output ex_dR_REQ, ex_regRt, de_regRs, de_regRt, ex_dW_REQ, de_dR_REQ, de_dW_REQ
	       );

endinterface // hazard_detection_unit_if
`endif //  `ifndef HAZARD_DETECTION_UNIT_IF_VH

