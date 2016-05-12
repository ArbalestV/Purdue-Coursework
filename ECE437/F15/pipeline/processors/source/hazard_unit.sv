/********************************************
 * David Larson
 * Pranjit Kalita
 * ECE 437 Section 6
 * Module: hazard_unit.sv
 *******************************************/

//includes
`include "cpu_types_pkg.vh"
`include "hazard_unit_if.vh"
import cpu_types_pkg::*;
//packages

module hazard_unit
(
  hazard_unit_if.hu huif
);

   //huif.flush_ex
   //huif.mem_regRd
   //huif.mem_regRd
  always_comb
    begin
       huif.nop = 1'b0;       
       if ( (huif.ex_memread || huif.ex_memwrite) && ((huif.ex_regRt == huif.de_regRt) ||
				(huif.ex_regRt == huif.de_regRs)    )) begin
	  huif.nop = 1'b1;
       end // ld data hazard
       if ( huif.ex_wsel == huif.de_regRs || huif.ex_wsel == huif.de_regRt ) begin
	  huif.nop = 1'b1;
       end // r-type data hazard in ex stage
       if ( huif.ex_regRd == huif.de_regRt || huif.ex_regRd == huif.de_regRs ) begin
	  huif.nop = 1'b1;
       end // r-type data hazard in ex stage
       if ( huif.mem_regRd == huif.de_regRt || huif.mem_regRd == huif.de_regRs ) begin
	  huif.nop = 1'b1;			 
       end // r-type data hazard in memstage
    end
endmodule // hazard_unit
