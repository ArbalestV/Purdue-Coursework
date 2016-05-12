`include "cpu_types_pkg.vh"
`include "caches_if.vh"
`include "datapath_cache_if.vh"
`include "cpu_ram_if.vh"

`timescale 1 ns / 1 ns
import cpu_types_pkg::*;

module dcache_tb;
   parameter PERIOD = 10;
   logic CLK = 0;
   logic nRST;
   always #(PERIOD / 2) CLK++;
   caches_if cif();
   datapath_cache_if dcif();
   dcache DUT (CLK, nRST, dcif, cif);
   test PROG (CLK, nRST, dcif, cif);
endmodule // dcache_tb


   program test (
		 input logic CLK,
		 output logic nRST,
		 datapath_cache_if dcif,
		 caches_if cif
		 );

   parameter PERIOD = 10;
   parameter delay = 3;
   logic [4:0] 		      testcase;
   
   initial
     begin
	//System reset
	nRST = 1'b0;
	//dcif.dmemaddr = 32'h0000abcd;
	dcif.dmemREN = 1'b1;
	dcif.dmemstore = 32'h0046fe89;
	dcif.dmemWEN = 1'b0;
	dcif.halt = 1'b0;
	cif.dwait = 1'b1;
	
	#(delay * 3);
	nRST = 1'b1; //reset off
	@(posedge CLK);
	dcif.dmemaddr = 32'h0000abcd;
	
//TESTCASE 1------------------------------------------------------------------------------------------------------------------------------
	//now, a dhit = 0 will be generated at the idle state
	testcase = 5'b00001;
	$display("TEST 1");
	$display("In test case 1. Reading data from memory for the first time.");
	
	$display("In the IDLE state.");	
	#(delay);
	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero");
	else
	  $display("Failed! dhit should not be one.");  
	
	@(posedge CLK);
	
	//now the current state will be in the fetch0 state
	$display("In the FETCH0 state.");
	#(delay);
	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero.");
	else
	  $display("Failed! dhit should be zero.");
	
	assert(cif.dREN == 1 && cif.dWEN == 0)
	  $display("Correct! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	else
	  $display("Failed! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	
	assert(cif.daddr == 32'h0000abcd)
	  $display("Correct! Value to be read from the memory is right.");
	else
	  $display("Failed! Value to be read from the memory is wrong.");
	

	@(posedge CLK);
	
	//now the current state will still be in the fetch 0 state
	$display("Still in the FETCH0 state.");
	cif.dload = 32'h000077ff;
	cif.dwait = 0; //make it 0 to go to the next fetch1 state
	
	@(posedge CLK);
	
	//now the current state will be in the Fetch1 state
	$display("In the FETCH1 state.");	
	cif.dwait = 1; //make dwait to be 1 again since we are fetching in the fetch 1 state
	#(delay);
	
	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero.");
	else
	  $display("Failed! dhit should be zero.");
	
	assert(cif.dREN == 1 && cif.dWEN == 0)
	  $display("Correct! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	else
	  $display("Failed! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	
	assert(cif.daddr == 32'h0000abc9)
	  $display("Correct! Value to be read from the memory is right.");
	else
	  $display("Failed! Value to be read from the memory is wrong.");
	
	@(posedge CLK);
	
	//now the current state will still be in the fetch 1 state
	$display("Still in the FETCH1 state.");
	cif.dload = 32'h000077fd;
	cif.dwait = 0; //make it 0 to go to the next fetch1 state
	#(delay);
	
	@(posedge CLK);
	
	//now the current state will be in the IDLE state and dhit will be 1
	$display("Now back to the IDLE state after fetching from the memory.");
	#(delay);
	
	assert(dcif.dhit == 1)
	  $display("Correct! dhit should be 1.");
	else
	  $display("Failed! dhit should not be 0.");
	
	assert(dcif.dmemload == 32'h000077ff)
	  $display("Correct! The correct data value is sent to the datapath.");
	else
	  $display("Failed! The incorrect data value is sent to the datapath.");
	
	assert(cif.dREN == 0 && cif.dWEN == 0)
	  $display("Correct! Nothing needs to be written to or read from the RAM.");
	else
	  $display("Failed! No read from or write to the RAM should take place now.");
	
	cif.dwait = 1'b1; //since always in IDLE state the dwait value should be 1

	//TESTCASE 2-----------------------------------------------------------------------------------------------------------
	testcase = 5'b00010;
	@(posedge CLK); //the second test case
	
	//will wait for one clock cycle before the next data address is generated from the datapath
	dcif.dmemREN = 1; //to simulate the behavior of the datapath
	dcif.dmemaddr = 32'h0000ffe3;
	
	//@(posedge CLK); 
	$display("TEST 2");
	$display("In test case 2. Reading data from memory for the second time.");
	$display("In the IDLE state.");	
	#(delay);
	
	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero");
	else
	  $display("Failed! dhit should not be one.");  
	
	@(posedge CLK);
	
	//now the current state will be in the fetch0 state
	$display("In the FETCH0 state.");
	#(delay);
	
	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero.");
	else
	  $display("Failed! dhit should be zero.");
	
	assert(cif.dREN == 1 && cif.dWEN == 0)
	  $display("Correct! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	else
	  $display("Failed! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	
	assert(cif.daddr == 32'h0000ffe3)
	  $display("Correct! Value to be read from the memory is right.");
	else
	  $display("Failed! Value to be read from the memory is wrong.");
	
	@(posedge CLK);
	
	//now the current state will still be in the fetch 0 state
	$display("Still in the FETCH0 state.");
	cif.dload = 32'habc677ff;
	cif.dwait = 0; //make it 0 to go to the next fetch1 state
	
	@(posedge CLK);
	
	//now the current state will be in the Fetch1 state
	$display("In the FETCH1 state.");	
	cif.dwait = 1; //make dwait to be 1 again since we are fetching in the fetch 1 state
	#(delay);
	
	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero.");
	else
	  $display("Failed! dhit should be zero.");
	
	assert(cif.dREN == 1 && cif.dWEN == 0)
	  $display("Correct! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	else
	  $display("Failed! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	
	assert(cif.daddr == 32'h0000ffe7)
	  $display("Correct! Value to be read from the memory is right.");
	else
	  $display("Failed! Value to be read from the memory is wrong.");
	
	@(posedge CLK);
	
	//now the current state will still be in the fetch 1 state
	$display("Still in the FETCH1 state.");
	cif.dload = 32'hf6e2ab4c;
	cif.dwait = 0; //make it 0 to go to the next fetch1 state
	#(delay);
	
	@(posedge CLK);
	
	//now the current state will be in the IDLE state and dhit will be 1
	$display("Now back to the IDLE state after fetching from the memory.");
	#(delay);
	
	assert(dcif.dhit == 1)
	  $display("Correct! dhit should be 1.");
	else
	  $display("Failed! dhit should not be 0.");
	
	assert(dcif.dmemload == 32'habc677ff)
	  $display("Correct! The correct data value is sent to the datapath.");
	else
	  $display("Failed! The incorrect data value is sent to the datapath.");
	
	assert(cif.dREN == 0 && cif.dWEN == 0)
	  $display("Correct! Nothing needs to be written to or read from the RAM.");
	else
	  $display("Failed! No read from or write to the RAM should take place now.");
	
	cif.dwait = 1'b1; //since always in IDLE state the dwait value should be 1


	@(posedge CLK);
	
	//will wait for one clock cycle before the next data address is generated from the datapath
	dcif.dmemREN = 1; //to simulate the behavior of the datapath
	dcif.dmemaddr = 32'h0000abcf; //this has the same index, tag as 32'b0000abcd already found in the cache. The block offset is also the same, so check for the exact same dmemload as the first case
	
	//TESTCAE 3--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	testcase = 5'b00011;
	$display("TEST 3");
	$display("Test Case 3. Here we will be requesting a data read from a previously loaded cache block. Block offset = 1");
	$display("Starting from the IDLE state.");
	#(delay);
	
	assert(dcif.dhit == 1)
	  $display("Correct! dhit should be 1.");
	else
	  $display("Failed! dhit should not be 0.");
	
	assert(dcif.dmemload == 32'h000077ff)
	  $display("Correct! The correct data value is sent to the datapath.");
	else
	  $display("Failed! The incorrect data value is sent to the datapath.");
	
	assert(cif.dREN == 0 && cif.dWEN == 0)
	  $display("Correct! Nothing needs to be written to or read from the RAM.");
	else
	  $display("Failed! No read from or write to the RAM should take place now.");

	@(posedge CLK);
	//will wait for one clock cycle before the next data address is generated from the datapath
	
	dcif.dmemREN = 1; //to simulate the behavior of the datapath
	dcif.dmemaddr = 32'h0000abcb; //this has the same index, tag as 32'b0000abcd already found in the cache. The block offset is also the same, so check for the exact same dmemload as the first case
	
	//TESTCASE 4 ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	testcase = 5'b00100;
	$display("TEST 4");	
	$display("Test Case 4. Here we will be requesting a data read from a previously loaded cache block. Block offset = 0");
	$display("Starting from the IDLE state.");
	#(delay);
	
	assert(dcif.dhit == 1)
	  $display("Correct! dhit should be 1.");
	else
	  $display("Failed! dhit should not be 0.");
	
	assert(dcif.dmemload == 32'h000077fd)
	  $display("Correct! The correct data value is sent to the datapath.");
	else
	  $display("Failed! The incorrect data value is sent to the datapath.");
	
	assert(cif.dREN == 0 && cif.dWEN == 0)
	  $display("Correct! Nothing needs to be written to or read from the RAM.");
	else
	  $display("Failed! No read from or write to the RAM should take place now.");
	 
	@(posedge CLK);
	//will wait for one clock cycle before the next data address is generated from the datapath
	dcif.dmemREN = 1; //to simulate the behavior of the datapath
	dcif.dmemaddr = 32'h0000f9e4;

	//TESTCASE 5 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	testcase = 5'b00101;
	$display("TEST 5");
	$display("In test case 5. Here we will be requesting a data read from a previously loaded cache block. But the lru will be used.");
	$display("In the IDLE state.");	
	#(delay);
	
	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero");
	else
	  $display("Failed! dhit should not be one.");  
	
	@(posedge CLK);
	
	//now the current state will be in the fetch0 state
	$display("In the FETCH0 state.");
	#(delay);
	
	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero.");
	else
	  $display("Failed! dhit should be zero.");
	
	assert(cif.dREN == 1 && cif.dWEN == 0)
	  $display("Correct! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	else
	  $display("Failed! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	
	assert(cif.daddr == 32'h0000f9e4)
	  $display("Correct! Value to be read from the memory is right.");
	else
	  $display("Failed! Value to be read from the memory is wrong.");
	
	@(posedge CLK);
	
	//now the current state will still be in the fetch 0 state
	$display("Still in the FETCH0 state.");
	cif.dload = 32'hadf6789f;
	cif.dwait = 0; //make it 0 to go to the next fetch1 state
	
	@(posedge CLK);
	
	//now the current state will be in the Fetch1 state
	$display("In the FETCH1 state.");	
	cif.dwait = 1; //make dwait to be 1 again since we are fetching in the fetch 1 state
	#(delay);
	
	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero.");
	else
	  $display("Failed! dhit should be zero.");
	
	assert(cif.dREN == 1 && cif.dWEN == 0)
	  $display("Correct! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	else
	  $display("Failed! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	
	assert(cif.daddr == 32'h0000f9e0)
	  $display("Correct! Value to be read from the memory is right.");
	else
	  $display("Failed! Value to be read from the memory is wrong.");
	
	@(posedge CLK);
	
	//now the current state will still be in the fetch 1 state
	$display("Still in the FETCH1 state.");
	cif.dload = 32'hfae4f56e;
	cif.dwait = 0; //make it 0 to go to the next fetch1 state
	#(delay);
	
	@(posedge CLK);
	
	//now the current state will be in the IDLE state and dhit will be 1
	$display("Now back to the IDLE state after fetching from the memory.");
	#(delay);
	
	assert(dcif.dhit == 1)
	  $display("Correct! dhit should be 1.");
	else
	  $display("Failed! dhit should not be 0.");
	
	assert(dcif.dmemload == 32'hadf6789f)
	  $display("Correct! The correct data value is sent to the datapath.");
	else
	  $display("Failed! The incorrect data value is sent to the datapath.");
	
	assert(cif.dREN == 0 && cif.dWEN == 0)
	  $display("Correct! Nothing needs to be written to or read from the RAM.");
	else
	  $display("Failed! No read from or write to the RAM should take place now.");
	
	cif.dwait = 1'b1; //since always in IDLE state the dwait value should be 1


	
	@(posedge CLK);
	
	//will wait for one clock cycle before the next data address is generated from the datapath
	dcif.dmemREN = 1; //to simulate the behavior of the datapath
	dcif.dmemaddr = 32'h0000f9e4;
	
	//TESTCASE 6 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	testcase = 5'b00110;
	$display("TEST 6");
	$display("Test Case 6. Here we will be requesting a data read from a previously loaded cache block. Block offset = 1");
	$display("Starting from the IDLE state.");
	#(delay);
	
	assert(dcif.dhit == 1)
	  $display("Correct! dhit should be 1.");
	else
	  $display("Failed! dhit should not be 0.");
	
	assert(dcif.dmemload == 32'hadf6789f)
	  $display("Correct! The correct data value is sent to the datapath.");
	else
	  $display("Failed! The incorrect data value is sent to the datapath.");
	
	assert(cif.dREN == 0 && cif.dWEN == 0)
	  $display("Correct! Nothing needs to be written to or read from the RAM.");
	else
	  $display("Failed! No read from or write to the RAM should take place now.");
	
	
	@(posedge CLK);
	dcif.dmemREN = 1; //to simulate the behavior of the datapath
	dcif.dmemaddr = 32'h0000f9e1;
	
	//TESTCASE 7 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	testcase = 5'b00111;
	$display("TEST 7");
	$display("Test Case 7. Here we will be requesting a data read from a previously loaded cache block. Block offset = 0");
	$display("Starting from the IDLE state.");
	#(delay);
	
	assert(dcif.dhit == 1)
	  $display("Correct! dhit should be 1.");
	else
	  $display("Failed! dhit should not be 0.");
	
	assert(dcif.dmemload == 32'hfae4f56e)
	  $display("Correct! The correct data value is sent to the datapath.");
	else
	  $display("Failed! The incorrect data value is sent to the datapath.");
	
	assert(cif.dREN == 0 && cif.dWEN == 0)
	  $display("Correct! Nothing needs to be written to or read from the RAM.");
	else
	  $display("Failed! No read from or write to the RAM should take place now.");
	
	

	@(posedge CLK);
	dcif.dmemREN = 0; //to check if it behaves properly
	dcif.dmemWEN = 0;

	
	@(posedge CLK);
	//now will check writes
	//first write will be to a cache location that is not found
	dcif.dmemREN = 0;
	dcif.dmemWEN = 1;
	dcif.dmemaddr = 32'h0023acd9; //block offset = 0, index = 3
	dcif.dmemstore = 32'habcd3f58;
	
	//TESTCASE 8 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	testcase = 5'b01000;
	$display("TEST 8");
	$display("In test case 8. Writing to the cache for the first time. Data not found.");
	$display("In the IDLE state.");	
	#(delay);
	
	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero");
	else
	  $display("Failed! dhit should not be one.");
	
	@(posedge CLK);
	
	//now the current state will be in the fetch0 state
	$display("In the FETCH0 state.");
	#(delay);
	
	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero.");
	else
	  $display("Failed! dhit should be zero.");
	
	assert(cif.dREN == 1 && cif.dWEN == 0)
	  $display("Correct! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	else
	  $display("Failed! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	
	assert(cif.daddr == 32'h0023acd9)
	  $display("Correct! Value to be read from the memory is right.");
	else
	  $display("Failed! Value to be read from the memory is wrong.");
	
	@(posedge CLK);
	
	//now the current state will still be in the fetch 0 state
	$display("Still in the FETCH0 state.");
	cif.dload = 32'habc678ef;
	cif.dwait = 0; //make it 0 to go to the next fetch1 state
	
	@(posedge CLK);
	
	//now the current state will be in the Fetch1 state
	$display("In the FETCH1 state.");	
	cif.dwait = 1; //make dwait to be 1 again since we are fetching in the fetch 1 state
	#(delay);
	
	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero.");
	else
	  $display("Failed! dhit should be zero.");
	
	assert(cif.dREN == 1 && cif.dWEN == 0)
	  $display("Correct! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	else
	  $display("Failed! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	
	assert(cif.daddr == 32'h0023acdd)
	  $display("Correct! Value to be read from the memory is right.");
	else
	  $display("Failed! Value to be read from the memory is wrong.");
	
	@(posedge CLK);
	
	//now the current state will still be in the fetch 1 state
	$display("Still in the FETCH1 state.");
	cif.dload = 32'hf665dc4f;
	cif.dwait = 0; //make it 0 to go to the next fetch1 state
	#(delay);
	
	@(posedge CLK);
	
	//now the current state will be in the IDLE state and dhit will be 1
	$display("Now back to the IDLE state after fetching from the memory.");
	#(delay);
	
	assert(dcif.dhit == 1)
	  $display("Correct! dhit should be 1.");
	else
	  $display("Failed! dhit should not be 0.");

	assert(cif.dREN == 0 && cif.dWEN == 0)
	  $display("Correct! Nothing needs to be written to or read from the RAM.");
	else
	  $display("Failed! No read from or write to the RAM should take place now.");

	cif.dwait = 1'b1; //since always in IDLE state the dwait value should be 1
	



	@(posedge CLK);
	dcif.dmemREN = 1;
	dcif.dmemWEN = 0;
	dcif.dmemaddr = 32'h00b0ee4a;
	//now, a dhit = 0 will be generated at the idle state

	//TESTCASE 9 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	testcase = 5'b01001;
	$display("TEST 9");
	$display("In test case 9. Reading data from memory for the first time so that it could be written to later.");
	$display("In the IDLE state.");	
	#(delay);
	
	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero");
	else
	  $display("Failed! dhit should not be one.");  
	
	@(posedge CLK);
	//now the current state will be in the fetch0 state
	$display("In the FETCH0 state.");
	#(delay);
	
	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero.");
	else
	  $display("Failed! dhit should be zero.");
	
	assert(cif.dREN == 1 && cif.dWEN == 0)
	  $display("Correct! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	else
	  $display("Failed! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	
	assert(cif.daddr == 32'h00b0ee4a)
	  $display("Correct! Value to be read from the memory is right.");
	else
	  $display("Failed! Value to be read from the memory is wrong.");
	
	@(posedge CLK);
	
	//now the current state will still be in the fetch 0 state
	$display("Still in the FETCH0 state.");
	cif.dload = 32'h030078ff;
	cif.dwait = 0; //make it 0 to go to the next fetch1 state
	
	@(posedge CLK);
	
	//now the current state will be in the Fetch1 state
	$display("In the FETCH1 state.");	
	cif.dwait = 1; //make dwait to be 1 again since we are fetching in the fetch 1 state
	#(delay);
	
	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero.");
	else
	  $display("Failed! dhit should be zero.");
	
	assert(cif.dREN == 1 && cif.dWEN == 0)
	  $display("Correct! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	else
	  $display("Failed! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	
	assert(cif.daddr == 32'h00b0ee4e)
	  $display("Correct! Value to be read from the memory is right.");
	else
	  $display("Failed! Value to be read from the memory is wrong.");
	
	@(posedge CLK);
	
	//now the current state will still be in the fetch 1 state
	$display("Still in the FETCH1 state.");
	cif.dload = 32'h9c1077fd;
	cif.dwait = 0; //make it 0 to go to the next fetch1 state
	#(delay);
	
	@(posedge CLK);
	
	//now the current state will be in the IDLE state and dhit will be 1
	$display("Now back to the IDLE state after fetching from the memory.");
	#(delay);
	
	assert(dcif.dhit == 1)
	  $display("Correct! dhit should be 1.");
	else
	  $display("Failed! dhit should not be 0.");
	
	assert(dcif.dmemload == 32'h030078ff)
	  $display("Correct! The correct data value is sent to the datapath.");
	else
	  $display("Failed! The incorrect data value is sent to the datapath.");
	
	assert(cif.dREN == 0 && cif.dWEN == 0)
	  $display("Correct! Nothing needs to be written to or read from the RAM.");
	else
	  $display("Failed! No read from or write to the RAM should take place now.");
	
	cif.dwait = 1'b1; //since always in IDLE state the dwait value should be 1

	
	@(posedge CLK);
	
	//in this test case we will write into an already existing block in the cache
	dcif.dmemWEN = 1;
	dcif.dmemREN = 0;
	dcif.dmemaddr = 32'h00b0ee4c; //index = 1, block offset = 1
	dcif.dmemstore = 32'h4567cda2;
	//we will check for dhit == 1
	
	//TESTCASE 10 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	testcase = 5'b01010;
	$display("TEST 10");
	$display("In test case 10. Writing to an existing cache block.");
	$display("At the IDLE state where we should be getting a dhit to write to memory.");
	#(delay);
	
	assert(dcif.dhit == 1)
	  $display("Correct! dhit should be 1.");
	else
	  $display("Failed! dhit should not be 0.");

	assert(cif.dREN == 0 && cif.dWEN == 0)
	  $display("Correct! Nothing needs to be written to or read from the RAM.");
	else
	  $display("Failed! No read from or write to the RAM should take place now.");

	cif.dwait = 1'b1; //since always in IDLE state the dwait value should be 1

	@(posedge CLK);	
	
	//in this test case we will write into an already existing block in the cache
	dcif.dmemWEN = 1;
	dcif.dmemREN = 0;
	dcif.dmemaddr = 32'h0000abc9; //index = 1, block offset = 1
	dcif.dmemstore = 32'haaaa7bfe;
	//we will check for dhit == 1
	
	//TESTCASE 11 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	testcase = 5'b01011;
	$display("TEST 11");
	$display("In test case 11. Writing to an existing cache block (same index so that we can test the replacement policy next.");
	$display("At the IDLE state where we should be getting a dhit to write to memory.");
	#(delay);
	
	assert(dcif.dhit == 1)
	  $display("Correct! dhit should be 1.");
	else
	  $display("Failed! dhit should not be 0.");

	assert(cif.dREN == 0 && cif.dWEN == 0)
	  $display("Correct! Nothing needs to be written to or read from the RAM.");
	else
	  $display("Failed! No read from or write to the RAM should take place now.");

	cif.dwait = 1'b1; //since always in IDLE state the dwait value should be 1
	





	@(posedge CLK);
	//now will check the replacement policy
	dcif.dmemREN = 1;
	dcif.dmemWEN = 0;
	dcif.dmemaddr = 32'h0000e2ca; //now will not find the data but there will be a dirty set. By the way the lru is 1
	//now, a dhit = 0 will be generated at the idle state
 
	//TESTCASE 12 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	testcase = 5'b01100;
	$display("TEST 12");
	$display("In test case 12. Will be checking the write back policy here. Index = 1, Dirty Bit = 1, Block offset = 0. LRU = 1.");
	$display("In the IDLE state.");	
	#(delay);

	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero");
	else
	  $display("Failed! dhit should not be one.");


	

	//the extra states will be exclusively of dirty bit
	@(posedge CLK);
	
	//now the current state will be in the fetch0 state
	$display("In the WB0 state.");
	#(delay);
	
	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero.");
	else
	  $display("Failed! dhit should be zero.");
	
	assert(cif.dREN == 0 && cif.dWEN == 1)
	  $display("Correct! dREN should be 0 & dWEN should be 1 since we will be writing to RAM.");
	else
	  $display("Failed! dREN should be 0 & dWEN should be 1 since we will be writing to RAM.");
	
	/*assert(cif.dstore == 32'h030078ff)
	  $display("Correct! Value to be written to the memory is right.");
	else
	  $display("Failed! Value to be written to the memory is wrong.");
	*/
	@(posedge CLK);
	
	//now the current state will still be in the fetch 0 state
	$display("Still in the WB0 state.");
	//cif.dload = 32'h030078ff;
	cif.dwait = 0; //make it 0 to go to the next fetch1 state
	
	@(posedge CLK);
	
	//now the current state will be in the Fetch1 state
	$display("In the WB1 state.");	
	cif.dwait = 1; //make dwait to be 1 again since we are fetching in the fetch 1 state
	#(delay);
	
	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero.");
	else
	  $display("Failed! dhit should be zero.");
	
	assert(cif.dREN == 0 && cif.dWEN == 1)
	  $display("Correct! dREN should be 0 & dWEN should be 1 since we will be fetching from RAM.");
	else
	  $display("Failed! dREN should be 0 & dWEN should be 1 since we will be fetching from RAM.");
	
	/*
	assert(cif.dstore == 32'h4567cda2)
	  $display("Correct! Value to be written to the memory is right.");
	else
	  $display("Failed! Value to be written to the memory is wrong.");
	*/
	
	@(posedge CLK);
	
	//now the current state will still be in the fetch 1 state
	$display("Still in the WB1 state.");
	//cif.dload = 32'h9c1077fd;
	cif.dwait = 0; //make it 0 to go to the next fetch0 state


	
	@(posedge CLK);
	//now the current state will be in the fetch0 state
	cif.dwait = 1; //going from WB1 to FETCH0 state	
	$display("In the FETCH0 state.");
	#(delay);

	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero.");
	else
	  $display("Failed! dhit should be zero.");

	assert(cif.dREN == 1 && cif.dWEN == 0)
	  $display("Correct! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	else
	  $display("Failed! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");

	assert(cif.daddr == 32'h0000e2ca)
	  $display("Correct! Value to be read from the memory is right.");
	else
	  $display("Failed! Value to be read from the memory is wrong.");	

	@(posedge CLK);

	//now the current state will still be in the fetch 0 state
	$display("Still in the FETCH0 state.");
	cif.dload = 32'hfabc347f;
	cif.dwait = 0; //make it 0 to go to the next fetch1 state

	@(posedge CLK);

	//now the current state will be in the Fetch1 state
	$display("In the FETCH1 state.");	
	cif.dwait = 1; //make dwait to be 1 again since we are fetching in the fetch 1 state
	#(delay);

	assert(dcif.dhit == 0)
	  $display("Correct! dhit should be zero.");
	else
	  $display("Failed! dhit should be zero.");

	assert(cif.dREN == 1 && cif.dWEN == 0)
	  $display("Correct! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");
	else
	  $display("Failed! dREN should be 1 & dWEN should be 0 since we will be fetching from RAM.");

	assert(cif.daddr == 32'h0000e2ce)
	  $display("Correct! Value to be read from the memory is right.");
	else
	  $display("Failed! Value to be read from the memory is wrong.");

	@(posedge CLK);

	//now the current state will still be in the fetch 1 state
	$display("Still in the FETCH1 state.");
	cif.dload = 32'h9e7631ad;
	cif.dwait = 0; //make it 0 to go to the next fetch1 state
	#(delay);

	@(posedge CLK);

	//now the current state will be in the IDLE state and dhit will be 1
	$display("Now back to the IDLE state after fetching from the memory.");
	#(delay);

	assert(dcif.dhit == 1)
	  $display("Correct! dhit should be 1.");
	else
	  $display("Failed! dhit should not be 0.");

	assert(dcif.dmemload == 32'hfabc347f)
	  $display("Correct! The correct data value is sent to the datapath.");
	else
	  $display("Failed! The incorrect data value is sent to the datapath.");

	assert(cif.dREN == 0 && cif.dWEN == 0)
	  $display("Correct! Nothing needs to be written to or read from the RAM.");
	else
	  $display("Failed! No read from or write to the RAM should take place now.");
	cif.dwait = 1'b1; //since always in IDLE state the dwait value should be 1
	

	
	
	@(posedge CLK);

	//the final test case. just to check the halt signal
	dcif.dmemREN = 1;
	dcif.halt = 1;
	$display("In the process of checking for halt and correspondingly flush now.");
	#(delay);

	assert(dcif.dhit == 0)
	  $display("Correct! Now as soon as we see a halt signal the dhit value should be 0.");
	 else
	   $display("Failed! dhit should not be 1 whenever halt = 1.");	

	@(posedge CLK);

	//at this clock edge, the state changes to flush
	@(posedge CLK);

	//at this clock edge, the flushing signal = 1 gets generated and the next_state becomes WB0
	@(posedge CLK);

	//at this state, the WB0 becomes the current state and the first block gets written to memory
	$display("Now in the WB0 state.");
	cif.dwait = 1;

	@(posedge CLK);

	$display("Still in the WB0 state.");
	cif.dwait = 0;

	//this would mean WB1 in the next state -> next clock edge
	@(posedge CLK);

	//at this state, the WB1 becomes the current state and the second block gets written to memory
	$display("Now in the WB1 state.");
	cif.dwait = 1;

	@(posedge CLK);

	$display("Still in the WB1 state.");
	cif.dwait = 0;
	//this would mean FLUSH in the next state -> next clock edge, and flushing signal  = 0. Also the dirty bit will get set to 0


	//the second dirty bit gets cleared
	@(posedge CLK);
	//at this clock edge, the state changes to flush
	@(posedge CLK);
	//at this clock edge, the flushing signal = 1 gets generated and the next_state becomes WB0
	@(posedge CLK);
	//at this state, the WB0 becomes the current state and the first block gets written to memory
	$display("Now in the WB0 state.");
	cif.dwait = 1;
	@(posedge CLK);
	$display("Still in the WB0 state.");
	cif.dwait = 0;
	//this would mean WB1 in the next state -> next clock edge
	@(posedge CLK);
	//at this state, the WB1 becomes the current state and the second block gets written to memory
	$display("Now in the WB1 state.");
	cif.dwait = 1;
	@(posedge CLK);
	$display("Still in the WB1 state.");
	cif.dwait = 0;
	//this would mean FLUSH in the next state -> next clock edge, and flushing signal  = 0. Also the dirty bit will get set to 0
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);
	@(posedge CLK);

	
	
	

	
     end // initial begin
endprogram // test
   
