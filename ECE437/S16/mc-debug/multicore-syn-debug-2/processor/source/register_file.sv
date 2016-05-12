`include "cpu_types_pkg.vh"
`include "register_file_if.vh"
import cpu_types_pkg::*;
module register_file (
		      input logic CLK,
		      input logic nRST,
		      register_file_if.rf rfif
		      );
   word_t [31:0] rfile;
   always_ff @(negedge CLK or negedge nRST)
     begin
	if (!nRST)
	  begin
	     rfile <= '{default:0};
	  end
	else if (rfif.WEN && rfif.wsel)
	  begin
	     rfile[rfif.wsel] <= rfif.wdat;
	  end
     end // always_ff @
   assign rfif.rdat1 = rfile[rfif.rsel1];
   assign rfif.rdat2 = rfile[rfif.rsel2];
endmodule // register_file

     
    
