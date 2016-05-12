//`include "cpu_types_pkg.vh"
module program_counter #(parameter PC_INIT = 0)(
		       //input PC_INIT,
		       input logic 	   CLK, nRST, pc_EN,
		       input logic [31:0]  pc_in,
		       output logic [31:0] pc_out
		       );
   //import cpu_types_pkg::*;
   //parameter PC_INIT = 0;
   always_ff @(posedge CLK, negedge nRST)
     begin
	if (!nRST)
	  begin
	     //pc_out <= 32'b0;
	     pc_out <= PC_INIT;
	  end
	else
	  begin
	     if (pc_EN == 1'b1)
	       begin
		  pc_out <= pc_in;
	       end
	  end
     end // always_ff @
endmodule // program_counter

