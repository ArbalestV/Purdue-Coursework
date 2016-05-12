/********************************************
 * David Larson
 * Pranjit Kalita
 * ECE 437 Section 6
 * Module: branch_unit.sv
 *******************************************/

//includes
`include "cpu_types_pkg.vh"
`include "branch_unit_if.vh"

//packages

module branch_unit
(
 branch_unit_if.bu buif
 );
   
  import cpu_types_pkg::*;
  /*  Declarations
  logic        br, flush_de;
  word_t       rs, rt;
  opcode_t     instrOp;
  logic [15:0] imm, brTgt;
  */
  word_t temp_branch_tgt1, temp_branch_tgt2;
   assign temp_branch_tgt1 = {{16{buif.imm[15]}}, buif.imm};
   assign temp_branch_tgt2 = temp_branch_tgt1 << 2; //shift left by 2
  //assign buif.brTgt = buif.imm; //TODO: extend to correct length
   assign buif.brTgt = temp_branch_tgt2;
   //now the branch target has been assigned, this has to be added to pc+4 value in the EX latch 
  always_comb
    begin
       buif.br = 1'b0;
       buif.flush_de = 1'b0;
       if ( buif.instrOp == /*BEQ*/6'b000100 && buif.rs == buif.rt ) begin
	  buif.br = 1'b1;
	  buif.flush_de = 1'b1;
       end
       if ( buif.instrOp == /*BNE*/6'b000101 && buif.rs != buif.rt ) begin
	  buif.br = 1'b1;
	  buif.flush_de = 1'b1;
       end
    end // always_comb begin
   
endmodule // branch_unit
