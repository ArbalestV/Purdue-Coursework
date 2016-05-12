`include "cpu_types_pkg.vh"
`timescale 1 ns / 1 ns
import cpu_types_pkg::*;
module control_unit_tb;
   parameter PERIOD = 10;
   //always #(PERIOD / 2) CLK++;
   control_unit_if cuif();
   test #(.PERIOD (PERIOD)) PROG (
				  .cuif
				  );
`ifndef MAPPED
   control_unit DUT(cuif);
`else
   control_unit DUT(
		    .\cuif.imemload (cuif.imemload),
		    .\cuif.j (cuif.j),
		    .\cuif.jr (cuif.jr),
		    .\cuif.jal (cuif.jal),
		    .\cuif.beq (cuif.beq),
		    .\cuif.halt (cuif.halt),
		    .\cuif.RegDst (cuif.RegDst),
		    .\cuif.ALUSrc (cuif.ALUSrc),
		    .\cuif.MemToReg (cuif.MemToReg),
		    .\cuif.RegWrite (cuif.RegWrite),
		    .\cuif.ALUOp (cuif.ALUOp),
		    .\cuif.ExtOp (cuif.ExtOp),
		    .\cuif.ShiftOp (cuif.ShiftOp),
		    .\cuif.lui (cuif.lui),
		    .\cuif.dR_REQ (cuif.dR_REQ),
		    .\cuif.dW_REQ (cuif.dW_REQ)
		    );
`endif // !`ifndef MAPPED
endmodule // control_unit_tb
program test (
	      control_unit_if.tb cuif
	      );
   parameter PERIOD = 10;
   parameter delay = 3;
   logic [OP_W - 1 : 0] opcode;
   logic [REG_W - 1 : 0] rs, rt, rd;
   logic [IMM_W - 1 : 0] imm;
   logic [ADDR_W - 1 : 0] jumpaddr;
   logic [SHAM_W - 1 : 0] shiftamt;
   logic [FUNC_W - 1 : 0] funct;
   logic [1 : 0] 	  instrType;
   assign cuif.imemload = (instrType == 0)? {opcode, rs, rt, rd, shiftamt, funct} :
							(instrType == 1)? {opcode, rs, rt, imm} : {opcode, jumpaddr};
   initial begin
      //r-type SLL
      opcode = RTYPE;
      instrType = 0;
      rs = 23;
      rt = 20;
      rd = 1;
      shiftamt = 3;
      funct = SLL;
      #(delay * 2);
      //r-type SRL
      //opcode = RTYPE;
      shiftamt = 4;
      funct = SRL;
      #(delay * 2);
      //r-type jr
      funct = JR;
      #(delay * 2);
      //r-type add
      funct = ADD;
      #(delay * 2);
      //rtype addu
      funct = ADDU;
      #(delay * 2);
      //r-type sub
      funct = SUB;
      #(delay * 2);
      //rtype subu
      funct = SUBU;
      #(delay * 2);
      //rtype and
      funct = AND;
      #(delay * 2);
      //r-type or
      funct = OR;
      #(delay * 2);
      //rtype xor
      funct = XOR;
      #(delay * 2);
      //rtype nor
      funct = NOR;
      #(delay * 2);
      //rtype slt
      funct = SLT;
      #(delay * 2);
      //rtype sltu
      funct = SLTU;
      #(delay * 2);

      #(PERIOD);
      //now j type
      instrType = 2;
      opcode = J;
      jumpaddr = 3;
      #(delay * 2);
      //jal
      opcode = JAL;
      #(delay * 2);
      
      //i-type
      instrType = 1;
      imm = 4;
      //halt
      opcode = HALT;
      #(delay * 2);
      //beq
      opcode = BEQ;
      #(delay * 2);
      //bne
      opcode = BNE;
      #(delay * 2);
      //lui
      opcode = LUI;
      #(delay * 2);
      //addi
      opcode = ADDI;
      #(delay * 2);
      //addiu
      opcode = ADDIU;
      #(delay * 2);
      //slti
      opcode = SLTI;
      #(delay * 2);
      //sltiu
      opcode = SLTIU;
      #(delay * 2);
      //andi
      opcode = ANDI;
      #(delay * 2);
      //ori
      opcode = ORI;
      #(delay * 2);
      //xori
      opcode = XORI;
      #(delay * 2);
      //lw
      opcode = LW;
      #(delay * 2);
      //sw
      opcode = SW;
      #(delay * 2);
      

   end // initial begin
endprogram // test
   
      
      
		   
