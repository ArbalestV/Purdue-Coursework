`include "cpu_types_pkg.vh"
`include "caches_if.vh"
`include "datapath_cache_if.vh"
`include "cpu_ram_if.vh"

`timescale 1 ns / 1 ns
import cpu_types_pkg::*;

module icache_tb;
   parameter PERIOD = 10;
   logic CLK = 0;
   logic nRST;
   always #(PERIOD / 2) CLK++;
   caches_if cif();
   datapath_cache_if dcif();
   icache DUT (CLK, nRST, dcif, cif);
   test PROG(CLK, nRST, dcif, cif);
endmodule // icache_tb

program test (
	      input logic CLK,
	      output logic nRST,
	      datapath_cache_if dcif,
	      caches_if cif
	      );

   parameter PERIOD = 10;
   parameter delay = 3;
   initial 
     begin
	//System reset
	nRST = 1'b0;
	dcif.imemaddr = 32'h0000abcd;
	dcif.imemREN = 1'b1;
	cif.iwait = 1'b1;

	#(delay * 3);

	nRST = 1'b1; //reset off
	//ccif.iwait[0] = 1'b0;

	#(delay *3);

	cif.iwait = 1'b1;
	@(posedge CLK);
	//current state will be in update
	cif.iload = 32'h200abc68;//data to be loaded from ram

	#(delay);

	cif.iwait = 0;//after some time the iwait becomes 1 which means data can now be loaded from the ram into the frames
	@(posedge CLK);
	//now the current state should be the idle state and ihit should be 1. Check for the corresponding ccif signals

	assert(dcif.ihit == 1'b1  && dcif.imemload == 32'h200abc68)
	  $display("ihit is getting asserted and correct instruction loaded.");
	else
	  $display("Failed");

        @(posedge CLK);

	cif.iwait = 1;
        dcif.imemaddr = 32'h000000ff; //load another instruction

	//now it will again go to the update state at the next positive edge
	@(posedge CLK);
	cif.iload = 32'h00bbaabd;

	#(delay);

	cif.iwait = 0;
	@(posedge CLK);

	//now back at the idle state
	assert(dcif.ihit == 1 && dcif.imemload == 32'h00bbaabd)
	  $display("ihit is getting asserted and correct instruction loaded.");
	else
	  $display("Failed");

	@(posedge CLK);

	//check if for the same memory address ihit generated or not.
	cif.iwait = 1;
	dcif.imemaddr = 32'h0000abcd;
	#(delay);

	assert(dcif.ihit == 1'b1  && dcif.imemload == 32'h200abc68)
	  $display("ihit is getting asserted and correct instruction loaded for repeat instruction.");
	else
	  $display("Failed");

        @(posedge CLK);

	//check for same tag and same index but different byte offset
	cif.iwait = 1;
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

     end // initial begin
endprogram // test
   
	
	
	
			
