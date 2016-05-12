/****************************************************
 * Module: forwarding_unit.sv
 * Date  : 10/4/15
 * ECE437 Section 6
 * *************************************************/

`include "forwarding_unit_if.vh"
`include "cpu_types_pkg.vh"

module forwarding_unit
  (
   forwarding_unit_if.fu fuif
   );

   import cpu_types_pkg::*;
 
   always_comb
     begin
	//forwardA logic first
	if ( fuif.op_M == JAL && fuif.ex_regRs == 31 ) 
	  begin
	     fuif.ForwardA = 3'b100;
	  end
	else if (fuif.op_WB == JAL && fuif.ex_regRs == 31)
	  begin
	     fuif.ForwardA = 3'b011;	     
	  end
	else if (fuif.mem_RegWrite && (fuif.mem_regRd != 0 && (fuif.mem_regRd == fuif.ex_regRs)))
	  begin
	     fuif.ForwardA = 3'b010;
	  end
	else if (fuif.wb_RegWrite && (fuif.wb_regRd != 0 && (fuif.wb_regRd == fuif.ex_regRs)))
	  begin
	     fuif.ForwardA = 3'b001;
	  end
	/*
	else if (fuif.mem_regRd != 0 && (fuif.mem_regRd == fuif.ex_regRs))
	  begin
	     fuif.forwardA = 3'b010;
	  end
	else if (fuif.wb_regRd != 0 && (fuif.wb_regRd == fuif.ex_regRs))
	  begin
	     fuif.forwardA = 3'b001;
	  end
	*/
	else 
	  begin
	     fuif.ForwardA = 3'b000;
	  end // else: !if(fuif.wb_RegWrite && (fuif.wb_regRd != 0 && (fuif.wb_regRd == fuif.ex_regRs)))
	
	//forwardB logic now
	if ( ~fuif.isIType && fuif.op_M == JAL && fuif.ex_regRt == 31 ) 
	  begin
	     fuif.ForwardB = 3'b100;
	  end
	else if (~fuif.isIType && fuif.op_WB == JAL && fuif.ex_regRt == 31)
	  begin
	     fuif.ForwardB = 3'b011;	     
	  end
	else if (~fuif.isLUI_EX && ~fuif.isIType && fuif.mem_RegWrite && (fuif.mem_regRd != 0 && (fuif.mem_regRd == fuif.ex_regRt)))
	  begin
	     fuif.ForwardB = 3'b010;
	  end
	else if (~fuif.isLUI_EX && ~fuif.isIType && fuif.wb_RegWrite && (fuif.wb_regRd != 0 && (fuif.wb_regRd == fuif.ex_regRt)))
	  begin
	     fuif.ForwardB = 3'b001;
	  end

	//handle branches separately from itype
	else if (fuif.is_branch && (fuif.mem_regRd != 0 && (fuif.mem_regRd == fuif.ex_regRt) ) )
	  begin
	     fuif.ForwardB = 3'b010;
	  end
	else if (fuif.is_branch && (fuif.wb_regRd != 0 && (fuif.wb_regRd == fuif.ex_regRt) ) )
	  begin
	     fuif.ForwardB = 3'b001;
	  end
	//end of handling branches separately from itype
	else
	  begin
	     fuif.ForwardB = 3'b000;
	  end
     end // always_comb
   
   always_comb
     begin
	fuif.stCntl = 2'b0;
	if (fuif.dWEN && (fuif.mem_regRd == fuif.ex_regRt) ) begin
	   fuif.stCntl = 2'b01;
	end
	if (fuif.dWEN && (fuif.wb_regRd == fuif.ex_regRt ) ) begin
	   fuif.stCntl = 2'b10;
	end
     end
   always_comb
     begin
	fuif.stCntl2 = 1'b0;
	if ( (fuif.dWEN && (fuif.mem_regRd == fuif.ex_regRs)) ||
	     (fuif.dREN && (fuif.wb_regRd == fuif.ex_regRs)) ) begin
	   fuif.stCntl2 = 1'b1;
	end		      
     end
   
endmodule
