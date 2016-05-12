`ifndef CONTROL_UNIT_IF_VH
`define CONTROL_UNIT_IF_VH

`include "cpu_types_pkg.vh"

interface control_unit_if;
   //import types
   import cpu_types_pkg::*;

   word_t imemload;
   logic j, jr, jal;
   logic beq, bne;
   logic halt;
   logic RegDst;
   logic ALUSrc;
   logic MemToReg;
   logic RegWrite;
   aluop_t ALUOp;
   logic ExtOp;
   logic ShiftOp;
   logic lui;
   logic dR_REQ, dW_REQ;
   logic datomic;   

   //cu ports
   modport cu(
	      input imemload,
	      output j, jr, jal, beq, bne, halt, RegDst, ALUSrc, MemToReg, RegWrite, ALUOp, ExtOp, ShiftOp, lui, dR_REQ, dW_REQ, datomic
	      );

   //cu tb
   modport tb(
	      input j, jr, jal, beq, bne, halt, RegDst, ALUSrc, MemToReg, RegWrite, ALUOp, ExtOp, ShiftOp, lui, dR_REQ, dW_REQ, datomic,
	      output imemload
	      );
   
endinterface // control_unit_if
`endif //  `ifndef CONTROL_UNIT_IF_VH

	      
