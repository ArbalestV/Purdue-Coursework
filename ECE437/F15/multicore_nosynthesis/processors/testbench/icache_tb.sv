`include "cpu_types_pkg.vh"
`include "cache_control_if.vh"
`include "datapath_cache_if.vh"
`include "cpu_ram_if.vh"

`timescale 1 ns / 1 ns
import cpu_types_pkg::*;

module icache_tb;
   parameter PERIOD = 10;
   logic CLK = 0;
   logic nRST;
   always #(PERIOD / 2) CLK++;
   cache_control_if ccif();
   datapath_cache_if dcif();
   icache DUT (CLK, nRST, dcif, ccif);
   test PROG(CLK, nRST, dcif, ccif);
endmodule // icache_tb

program test (
	      input logic CLK,
	      output logic nRST,
	      datapath_cache_if dcif,
	      cache_control_if ccif
	      );

   parameter PERIOD = 10;
   parameter delay = 3;
   initial 
     begin
	//System reset
	nRST = 1'b0;
	dcif.imemaddr = 32'h0000abcd;
	dcif.imemREN = 1'b1;
	ccif.iwait[0] = 1'b1;
	#(delay * 3);
	nRST = 1'b1; //reset off
	//ccif.iwait[0] = 1'b0;
	#(delay *3);
	ccif.iwait[0] = 1'b1;
	@(posedge CLK);
	//current state will be in update
	ccif.iload[0] = 32'h200abc68;//data to be loaded from ram
	#(delay);
	ccif.iwait[0] = 0;//after some time the iwait becomes 1 which means data can now be loaded from the ram into the frames
	@(posedge CLK);
	//now the current state should be the idle state and ihit should be 1. Check for the corresponding ccif signals
	assert(dcif.ihit == 1'b1  && dcif.imemload == 32'h200abc68)
	  $display("ihit is getting asserted and correct instruction loaded.");
	else
	  $display("Failed");
        @(posedge CLK);
	ccif.iwait[0] = 1;
        dcif.imemaddr = 32'h000000ff; //load another instruction
	//now it will again go to the update state at the next positive edge
	@(posedge CLK);
	ccif.iload[0] = 32'h00bbaabd;
	#(delay);
	ccif.iwait[0] = 0;
	@(posedge CLK);
	//now back at the idle state
	assert(dcif.ihit == 1 && dcif.imemload == 32'h00bbaabd)
	  $display("ihit is getting asserted and correct instruction loaded.");
	else
	  $display("Failed");
	@(posedge CLK);
	//check if for the same memory address ihit generated or not.
	ccif.iwait[0] = 1;
	dcif.imemaddr = 32'h0000abcd;
	#(delay);
	assert(dcif.ihit == 1'b1  && dcif.imemload == 32'h200abc68)
	  $display("ihit is getting asserted and correct instruction loaded for repeat instruction.");
	else
	  $display("Failed");
        @(posedge CLK);
	//check for same tag and same index but different byte offset
	ccif.iwait[0] = 1;
	dcif.imemaddr = 32'h000000fc;
	#(delay);
	assert(dcif.ihit == 1 && dcif.imemload == 32'h00bbaabd)
	  $display("ihit is getting asserted and correct instruction loaded for same tag, idx with different byte offset.");
	else
	  $display("Failed");
	@(posedge CLK);
	dcif.imemaddr = 32'h0000abcc;
	#(delay);
	assert(dcif.ihit == 1'b1  && dcif.imemload == 32'h200abc68)
	  $display("ihit is getting asserted and correct instruction loaded for same tag, idx with different byte offset.");
	else
	  $display("Failed");
        @(posedge CLK);
	#(delay);
	
	/*
	dcif.imemaddr = 32'h000000ff;
	#(delay * 6); //to observe the effects
	nRST = 1'b1;
	ccif.iwait[0] = 1;
	@(posedge CLK);
	//first read == miss
	dcif.imemREN = 1;
	dcif.imemaddr = 32'h000000ff;
	@(posedge CLK);
	ccif.iwait[0] = 0;
	ccif.iload[0] = 100;
	assert(ccif.iREN == 1'b1 && ccif.iaddr == 32'h000000ff)
	  $display("Test case 1 passed");
	else
	  $display("Test case 1 failed.");
	@(posedge CLK);
	@(posedge CLK);
	#(delay);
	assert(dcif.imemload == 100 && dcif.ihit == 1'b1)
	  $display("Test case 2 passed");
	else
	  $display("Test case 2 failed.");
	@(posedge CLK);
	#(delay);
	ccif.iwait[0] = 0;
	ccif.iload[0] = 200;
	assert(dcif.ihit == 1'b0)
	  $display("Test case 3 passed");
	else
	  $display("Test case 3 failed.");
	@(posedge CLK);
	@(posedge CLK);
	assert(dcif.imemload == 200 && dcif.ihit == 1'b1)
	  $display("Test case 4 passed");
	else
	  $display("Test case 4 failed.");
	dcif.imemaddr = 32'h000000ff;
	ccif.iwait[0] = 1;
	@(posedge CLK);
	@(posedge CLK);
	assert(dcif.imemload == 100 && dcif.ihit == 1'b1)
	  $display("Test case 5 passed.");
	else
	  $display("Test case 5 failed.");
	dcif.imemaddr = 32'h000000ff;
	ccif.iwait[0] = 1;
	ccif.iload[0] = 700;
	@(posedge CLK);
	ccif.iwait[0] = 0;
	@(posedge CLK);
	assert(dcif.imemload == 700 && dcif.ihit == 1'b1)
	  $display("Test case 6 passed.");
	else
	  $display("Test case 6 failed.");
	 */	
     end // initial begin
endprogram // test
   
	
	
	
			
