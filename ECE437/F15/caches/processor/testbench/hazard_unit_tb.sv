`include "cpu_types_pkg.vh"
`timescale 1 ns / 1 ns
import cpu_types_pkg::*;
module hazard_unit_tb;
   parameter PERIOD = 10;
   hazard_unit_if huif();
   test #(.PERIOD (PERIOD)) PROG (
				 .huif
				  );
`ifndef MAPPED
   hazard_unit DUT(huif);
`else
   hazard_unit DUT(
		   .\huif.ex_memread (huif.ex_memread),
		   .\huif.ex_memwrite (huif.ex_memwrite),
		   .\huif.nop (huif.nop),
		   .\huif.de_regRs (huif.de_regRs),
		   .\huif.de_regRt (huif.regRt),
		   .\huif.ex_regRd (huif.ex_regRd),
		   .\huif.ex_regRt (huif.ex_regRt),
		   .\huif.ex_wsel (huif.ex_wsel)
		   );
`endif // !`ifndef MAPPED
endmodule // hazard_unit_tb
program test (
	      hazard_unit_if.tb huif
	      );
   parameter PERIOD = 10;
   parameter delay = 3;
   initial begin
      
      huif.ex_wsel = 5'b11001;
      huif.de_regRs = 5'b11000;
      huif.ex_regRd = 5'b10101;  
      //check for load and store hazard
      huif.ex_memread = 1;
      huif.ex_memwrite = 0;
      huif.de_regRt = 5'b00110;
      huif.ex_regRt = 5'b00110;
      #(delay *2 );
      huif.de_regRt = 5'b10001;
      #(delay * 2);
      huif.ex_memread = 0;
      huif.ex_memwrite = 1;
      huif.de_regRt = 5'b00110;
      huif.ex_regRt = 5'b00110;
      #(delay *2 );
      huif.de_regRt = 5'b10001;
      #(delay * 2);
      
      huif.ex_memread = 1;
      huif.ex_memwrite = 0;
      huif.de_regRs = 5'b00110;
      huif.ex_regRt = 5'b00110;
      #(delay *2 );
      huif.de_regRs = 5'b10001;
      #(delay * 2);
      huif.ex_memread = 0;
      huif.ex_memwrite = 1;
      huif.de_regRs = 5'b00110;
      huif.ex_regRt = 5'b00110;
      #(delay *2 );
      huif.de_regRs = 5'b10001;
      #(delay * 2);
      huif.ex_memwrite = 0;
      
      //r-type hazard
      huif.ex_regRd = 5'b11001;
      huif.ex_wsel = 5'b10101;
      huif.de_regRs = 5'b10101;
      huif.de_regRt = 5'b10000;
      #(delay * 3);
      huif.ex_wsel = 5'b10001;
      #(delay * 3);
      huif.ex_wsel = 5'b10100;
      huif.de_regRt = 5'b10100;
      #(delay * 3);
      huif.ex_wsel = 5'b00001;
      #(delay * 3);
      
      //r-type hazard II
      huif.ex_regRd = 5'b10101;
      huif.de_regRt = 5'b10101;
      #(delay * 3);
      huif.ex_regRd = 5'b10001;
      #(delay * 3);
      huif.ex_regRd = 5'b10101;
      huif.de_regRs = 5'b10101;
      huif.de_regRt = 5'b00011;
      #(delay * 3);
      huif.ex_regRd = 5'b00101;
      huif.de_regRs = 5'b10101;
      #(delay * 3);

      //r-type hazard III
      huif.mem_regRd = 5'b10101;
      huif.de_regRs = 5'b10001; //nop == 0      
      huif.de_regRt = 5'b10001; //nop == 0
      #(delay * 3);
      huif.de_regRs = 5'b10101; //nop == 1
      #(delay * 3);
      huif.de_regRs = 5'b10001;      
      huif.de_regRt = 5'b10101; //nop == 1      
      #(delay * 3);
      
      
   end // initial begin
endprogram // test
   

