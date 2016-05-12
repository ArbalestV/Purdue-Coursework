`include "cpu_types_pkg.vh"
`timescale 1 ns / 1 ns
import cpu_types_pkg::*;
module hazard_detection_unit_tb;
   parameter PERIOD = 10;
   hazard_detection_unit_if hduif();
   test #(.PERIOD (PERIOD)) PROG 
   (
    .hduif
   );

`ifndef MAPPED
   hazard_detection_unit DUT(hduif);
`else
   hazard_detection_unit DUT(
		   .\hduif.ex_dR_REQ (hduif.ex_dR_REQ),
		   .\hduif.ex_regRt (hduif.ex_regRt),
		   .\hduif.de_regRs (hduif.de_regRs),
		   .\hduif.de_regRt (hduif.de_regRt),
		   .\hduif.stall (hduif.stall)
		   );
`endif // !`ifndef MAPPED
endmodule // hazard_detection_unit_tb

program test
(
 hazard_detection_unit_if.tb hduif
);
   parameter PERIOD = 10;


   initial
     begin
	//TEST 1
	hduif.ex_dR_REQ = 1'b1;
	hduif.ex_regRt = 5;
	hduif.de_regRs = 5;
	hduif.de_regRt = 5;
	
	#(PERIOD/2)
	if (hduif.stall == 1'b1)
	  $display("Test 1 Passed!");
	else
	  $error("Test 1 Failed!");
	#(PERIOD/2)

	//TEST 2
	hduif.de_regRs = 4;
	#(PERIOD/2)
	if (hduif.stall == 1'b1)
	  $display("Test 2 Passed!");
	else
	  $error("Test 2 Failed!");
	#(PERIOD/2)

	//TEST 3
	hduif.de_regRt = 4;
	#(PERIOD/2)
	if (hduif.stall == 0'b1)
	  $display("Test 3 Passed!");
	else
	  $error("Test 3 Failed!");
	#(PERIOD/2)
	
	//TEST 4
	hduif.ex_regRt = 4;
	#(PERIOD/2)
	if (hduif.stall == 1'b1)
	  $display("Test 4 Passed!");
	else
	  $error("Test 4 Failed!");
	#(PERIOD/2)
	
	//TEST 5
	hduif.ex_dR_REQ = 1'b0;
	#(PERIOD/2)
	if (hduif.stall == 0'b1)
	  $display("Test 4 Passed!");
	else
	  $error("Test 4 Failed!");
	#(PERIOD/2)
	hduif.ex_dR_REQ = 1'b1;
	
     end
endprogram // test
   
