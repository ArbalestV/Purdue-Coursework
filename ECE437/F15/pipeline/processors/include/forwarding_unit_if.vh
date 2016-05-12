`ifndef FORWARDING_UNIT_IF_VH
`define FORWARDING_UNIT_IF_VH

`include "cpu_types_pkg.vh"

interface forwarding_unit_if;
   
   import cpu_types_pkg::*;
   
   //declarations
   regbits_t de_regRt, ex_regRt, ex_regRs, mem_regRd, wb_regRd;
   logic     mem_RegWrite, wb_RegWrite, dWEN, dREN;
   logic [2:0] ForwardA, ForwardB;
   logic       isLUI_EX, isIType, stCntl2;
   logic [1:0] stCntl/*, stCntl2*/;   
   opcode_t  op_M, op_WB;

   logic       is_branch;
   
   
   //ports
   modport fu (
	       input  de_regRt, ex_regRt, ex_regRs, mem_regRd, wb_regRd, mem_RegWrite, wb_RegWrite, isLUI_EX, dWEN, dREN, op_M, op_WB, isIType, is_branch,
	       output ForwardA, ForwardB, stCntl, stCntl2
	       );
   modport tb (
	       input  ForwardA, ForwardB, stCntl, stCntl2,
	       output de_regRt, ex_regRt, ex_regRs, mem_regRd, wb_regRd, mem_RegWrite, wb_RegWrite, isLUI_EX, dWEN, dREN, op_M, op_WB, isIType, is_branch
	       );
   
endinterface

`endif
