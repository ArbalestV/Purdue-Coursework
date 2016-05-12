`include "cpu_types_pkg.vh"
`include "control_unit_if.vh"

module control_unit (
		     control_unit_if.cu cuif
		     );
   import cpu_types_pkg::*;

   always_comb
     begin
	cuif.dR_REQ = 0;
	if ( (cuif.imemload[31:26] == 6'b110000) || (cuif.imemload[31:26] == 6'b100011)) //for LW or LL instruction only then read from memory
	  begin
	     cuif.dR_REQ = 1;
	  end
     end

   always_comb
     begin
	cuif.dW_REQ = 0;
	if ( (cuif.imemload[31:26] == 6'b101011)) //for SW only then write to memory
	  begin
	     cuif.dW_REQ = 1;
	  end
     end
  
   
   always_comb
     begin
	cuif.j = 0;
	cuif.jr = 0;
	cuif.jal = 0;
	cuif.beq = 0;
	cuif.bne = 0;
	cuif.halt = 0;
	cuif.RegDst = 0;
	cuif.ALUSrc = 0;//1 only for i-type
	cuif.MemToReg = 0;
	cuif.RegWrite = 0;
	cuif.ALUOp = ALU_SLL;
	cuif.ExtOp = 0;
	cuif.ShiftOp = 0;
	cuif.lui = 0;

	if (cuif.imemload[31:26] == 6'b000000) //R-type instruction
	  begin
	     cuif.RegDst = 1;//1 for r-type
	     cuif.RegWrite = 1;
	     cuif.ALUSrc = 0;

	     case(cuif.imemload[5:0])
	       6'b000000: //SLL
		 begin
		    cuif.ShiftOp = 1;
		    cuif.ALUOp = ALU_SLL;
		 end
	       6'b000010://SRL
		 begin
		    cuif.ShiftOp = 1;
		    cuif.ALUOp = ALU_SRL;
		 end
	       6'b001000://JR
		 begin
		    cuif.jr = 1;
		    cuif.RegWrite = 0;
		 end
	       6'b100000://ADD
		 begin
		    cuif.ALUOp = ALU_ADD;
		 end
	       6'b100001:
		 begin
		    cuif.ALUOp = ALU_ADD;
		 end
	       6'b100010://SUB
		 begin
		    cuif.ALUOp = ALU_SUB;
		 end
	       6'b100011:
		 begin
		    cuif.ALUOp = ALU_SUB;
		 end
	       6'b100100://AND
		 begin
		    cuif.ALUOp = ALU_AND;
		 end
	       6'b100101://OR
		 begin
		    cuif.ALUOp = ALU_OR;
		 end
	       6'b100110://XOR
		 begin
		    cuif.ALUOp = ALU_XOR;
		 end
	       6'b100111://NOR
		 begin
		    cuif.ALUOp = ALU_NOR;
		 end
	       6'b101010://SLT
		 begin
		    cuif.ALUOp = ALU_SLT;
		 end
	       6'b101011://SLTU
		 begin
		    cuif.ALUOp = ALU_SLTU;
		 end
	     endcase // case (cuif.imemload[0:5])
	  end // if (cuif.imemload[31:26] == 6'b000000)

	//now I-Type and J-Type
	else
	  begin
	     cuif.MemToReg = 0;
	     cuif.RegDst = 0;
	     cuif.RegWrite = 1;

	     case(cuif.imemload[31:26])
	       6'b000010://J
		 begin
		    cuif.j = 1;
		    cuif.RegWrite = 0;
		 end
	       6'b000011://jal
		 begin
		    cuif.jal = 1;
		 end
	       6'b111111://halt
		 begin
		    cuif.halt = 1;
		    cuif.RegWrite = 0;
		 end
	       //now i-type instructions
	       6'b000100://BEQ
		 begin
		    cuif.beq = 1;
		    cuif.ALUSrc = 0;
		    cuif.RegWrite = 0;
		    cuif.ALUOp = ALU_SUB;
		 end
	       6'b000101://bne
		 begin
		    cuif.bne = 1;
		    cuif.ALUSrc = 0;
		    cuif.RegWrite = 0;
		    cuif.ALUOp = ALU_SUB;
		 end
	       6'b001111://lui
		 begin
		    cuif.lui = 1;
		    cuif.ALUSrc = 1;
		    cuif.ALUOp = ALU_SLL;
		 end
	       6'b001000://addi
		 begin
		    cuif.ALUSrc = 1;
		    cuif.ExtOp = 1;
		    cuif.ALUOp = ALU_ADD;
		 end
	       6'b001001://addiu
		 begin
		    cuif.ALUSrc = 1;
		    cuif.ExtOp = 1;
		    cuif.ALUOp = ALU_ADD;
		 end
	       6'b001010://slti
		 begin
		    cuif.ALUSrc = 1;
		    cuif.ExtOp = 1;
		    cuif.ALUOp = ALU_SLT;
		 end
	       6'b001011://sltiu
		 begin
		    cuif.ALUSrc = 1;
		    cuif.ExtOp = 1;
		    cuif.ALUOp = ALU_SLT;
		 end
	       6'b001100://ANDI
		 begin
		    cuif.ALUOp = ALU_AND;
		    cuif.ALUSrc = 1;
		    cuif.ExtOp = 0;
		 end
	       6'b001101://ORI
		 begin
		    cuif.ALUOp = ALU_OR;
		    cuif.ALUSrc = 1;
		    cuif.ExtOp = 0;
		 end
	       6'b001110://xori
		 begin
		    cuif.ALUOp = ALU_XOR;
		    cuif.ALUSrc = 1;
		    cuif.ExtOp = 0;
		 end
	       6'b100011://lw
		 begin
		    cuif.ALUSrc = 1;
		    cuif.ALUOp = ALU_ADD;
		    cuif.MemToReg = 1;
		    cuif.ExtOp = 1;
		 end

	       6'b101011://sw
		 begin
		    cuif.ALUSrc = 1;
		    cuif.ALUOp = ALU_ADD;
		    cuif.MemToReg = 0;
		    cuif.ExtOp = 1;
		    cuif.RegWrite = 0;
		 end
	     endcase // case (cuif.imemload[31:26])
	  end // else: !if(cuif.imemload[31:26] == 6'b000000)
     end // always_comb
endmodule // control_unit














