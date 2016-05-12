`include "cpu_types_pkg.vh"
`include "alu_if.vh"
import cpu_types_pkg::*;
module alu (
	    alu_if.aluports alpts
	    );
   word_t compare;
   
   always_comb begin

      alpts.portO = 0;
      alpts.nFlag = 0;
      alpts.zFlag = 0;
      alpts.oFlag = 0;
      
      //case statement to perform alu operations;
      case (alpts.aluOP)
	ALU_SLL:
	  begin
	     alpts.portO = (alpts.portA << alpts.portB);
	  end
	ALU_SRL:
	  begin
	     alpts.portO = (alpts.portA >> alpts.portB);
	  end
	ALU_AND:
	  begin
	     alpts.portO = (alpts.portA & alpts.portB);
	  end
	ALU_OR:
	  begin
	     alpts.portO = (alpts.portA | alpts.portB);
	  end
	ALU_XOR:
	  begin
	     alpts.portO = (alpts.portA ^ alpts.portB);
	  end
	ALU_NOR:
	  begin
	     alpts.portO = ~(alpts.portA | alpts.portB);
	  end
	ALU_ADD:
	  begin
	     alpts.portO = ($signed(alpts.portA) + $signed(alpts.portB));
	  end
	ALU_SUB:
	  begin
	     alpts.portO = ($signed(alpts.portA) - $signed(alpts.portB));
	  end
	ALU_SLT:
	  begin
	     alpts.portO = ($signed(alpts.portA) < $signed(alpts.portB));
	  end
	ALU_SLTU:
	  begin
	     alpts.portO = (alpts.portA < alpts.portB);
	  end
	default:
	  begin
	     alpts.portO = 0;
	     alpts.nFlag = 0;
	     alpts.zFlag = 0;
	     alpts.oFlag = 0;
	  end
      endcase // case (alpts.aluOP)
      //now, let us try to check and set the flags based on the outputs;
      if (alpts.portO == 0)
	begin
	   alpts.zFlag = 1;
	end
      else
	begin
	   alpts.zFlag = 0;
	end
      
      if (
	  (
	   (
	    (alpts.portO[31] == 1'b1 && (alpts.portA[31] == 1'b0 && alpts.portB[31] == 1'b0)) ||
	    (alpts.portO[31] == 1'b0 && (alpts.portA[31] == 1'b1 && alpts.portB[31] == 1'b1))
	    ) 
	   && alpts.aluOP == 2)
	  ||
	  (
	   (
	    (alpts.portO[31] == 1'b1 && (alpts.portA[31] == 1'b0 && alpts.portB[31] == 1'b1)) ||
	    (alpts.portO[31] == 1'b0 && (alpts.portA[31] == 1'b1 && alpts.portB[31] == 1'b0))
	    ) 
	   && alpts.aluOP == 3)
	   )
	begin
	   alpts.oFlag = 1;
	end
      else
	begin
	   alpts.oFlag = 0;
	end // else: !if(...

      if (alpts.portO[31] == 1'b1)
	begin
	   alpts.nFlag = 1;
	end
      else
	begin
	   alpts.nFlag = 0;
	end
   end // always_comb
   
endmodule // alu


	
	   
      
      
	   
