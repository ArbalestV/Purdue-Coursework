`include "cpu_types_pkg.vh"
`include "coherence_control_if.vh"
`include "cache_control_if.vh"
`include "coherence_memory_if.vh"

`timescale 1 ns / 1 ns
import cpu_types_pkg::*;

module coherence_control_tb;
   
   parameter PERIOD = 10;
   logic CLK = 0;
   logic nRST;

   always #(PERIOD / 2) CLK++;

   coherence_control_if cohif();
   coherence_memory_if cmif();
   
   caches_if cif0();
   caches_if cif1();
   cache_control_if #(.CPUS(2)) ccif(cif0, cif1);
   
   coherence_control DUT (CLK, nRST, cohif, cmif, ccif);
   test PROG (CLK, nRST, cohif, cmif, ccif);

endmodule // coherence_controller_tb

program test(
	     input logic CLK,
	     output logic nRST,
	     coherence_control_if cohif,
	     coherence_memory_if cmif,
	     cache_control_if ccif
	     );

   parameter PERIOD = 10;

   initial
     begin
	//system reset
	nRST = 1'b0;
	cohif.cctrans_0 = 1'b0;
	cohif.cctrans_1 = 1'b0;
	cohif.ccwrite_0 = 1'b0;
	cohif.ccwrite_1 = 1'b0;

	#(PERIOD)
	
	nRST = 1'b1;
	
	@(posedge CLK);
	
	//Test 1 - D0 requests a read
	cohif.cctrans_0 = 1'b1;
	cohif.cctrans_1 = 1'b0;
	cmif.dmemaddr_0 = 32'b0;
	cmif.dmemaddr_1 = 32'b1;
	cmif.cacheBlock0 = 32'h20;
	cmif.cacheBlock1 = 32'h40;
		
	@(posedge CLK);
	@(posedge CLK);

	$display("T1 = only D0 requests read");
	
	//cohif.ccwait_1 should be asserted since it is the servicer
	assert(cohif.ccwait_1 == 1)
	  $display("T1 - Correct! ccwait_1 should be asserted!");
        else
          $display("T1 - Failed! ccwait_1 should not be 0");

	assert(cohif.ccsnoopaddr == 32'b1)
	  $display("T1 - Correct! ccsnoopaddr should be 32'b1");
	else
	  $display("T1 - Failed! ccsnoopaddr should be 32'b1");
	
	
	assert(cohif.ccinv_1 == 0)
	  $display("T1 - Correct! ccinv_1 should be 0 since D0 is not requesting write permissions!");
        else
          $display("T1 - Failed! ccinv_1 should not be 1 for read requests");

	ccif.dwait[0] = 1'b1;

	@(posedge CLK);
	@(posedge CLK);			
	@(posedge CLK);
	@(posedge CLK);

	nRST = 1'b0;
	#(PERIOD)
	nRST = 1'b1;

	//TEST 2 - D0 requests write permissions
	cohif.cctrans_0 = 1'b1;
	cohif.cctrans_1 = 1'b0;
	cohif.ccwrite_0 = 1'b1;
	cohif.ccwrite_1 = 1'b0;
	cmif.dmemaddr_0 = 32'h32;
	cmif.dmemaddr_1 = 32'h12;
	cmif.cacheBlock0 = 32'h20;
	cmif.cacheBlock1 = 32'h40;
		
	@(posedge CLK);
	@(posedge CLK);

	$display("T2 = only D0 requests write");
	
	assert(cohif.ccwait_1 == 1)
	  $display("T2 - Correct! ccwait_1 should be asserted!");
        else
          $display("T2 - Failed! ccwait_1 should not be 0");

	assert(cohif.ccsnoopaddr == cmif.dmemaddr_1)
	  $display("T2 - Correct! ccsnoopaddr should be 32'h32");
	else
	  $display("T2 - Failed! ccsnoopaddr should be 32'h32");
	

	assert(cohif.ccinv_1 == 1)
	  $display("T2 - Correct! ccinv_1 should be 1 since D0 is requesting write permissions!");
        else
          $display("T2 - Failed! ccinv_1 should not be 0 for write requests");

	ccif.dwait[1] = 1'b1;

	@(posedge CLK);
	@(posedge CLK);			
	@(posedge CLK);
	@(posedge CLK);

	nRST = 1'b0;
	#(PERIOD)
	nRST = 1'b1;

	//TEST 3 - D0 & D1 request read permissions
	cohif.cctrans_0 = 1'b1;
	cohif.cctrans_1 = 1'b1;
	cohif.ccwrite_0 = 1'b0;
	cohif.ccwrite_1 = 1'b0;
	cmif.dmemaddr_0 = 32'h22;
	cmif.dmemaddr_1 = 32'h10;
	cmif.cacheBlock0 = 32'h30;
	cmif.cacheBlock1 = 32'h50;
	
	@(posedge CLK);
	@(posedge CLK);

	$display("T3 = D0 and D1 request reads at same time");
	
	assert(cohif.ccwait_1 == 1)
	  $display("T3 - Correct! ccwait_1 should be asserted!");
        else
          $display("T3 - Failed! ccwait_1 should not be 0");

	assert(cohif.ccsnoopaddr == cmif.dmemaddr_1)
	  $display("T3 - Correct! ccsnoopaddr should be 32'h10");
	else
	  $display("T3 - Failed! ccsnoopaddr should be 32'h10");
	
	assert(cohif.ccinv_1 == 0)
	  $display("T3 - Correct! ccinv_1 should be 0 since D0 is requesting read permissions!");
        else
          $display("T3 - Failed! ccinv_1 should not be 1 for read requests");

	ccif.dwait[1] = 1'b1;

	@(posedge CLK);
	@(posedge CLK);			
	@(posedge CLK);
	@(posedge CLK);

	nRST = 1'b0;
	#(PERIOD)
	nRST = 1'b1;

	//TEST 4 - D0 requests write permissions & D1 request read permissions
	cohif.cctrans_0 = 1'b1;
	cohif.cctrans_1 = 1'b1;
	cohif.ccwrite_0 = 1'b1;
	cohif.ccwrite_1 = 1'b0;
	cmif.dmemaddr_0 = 32'h2;
	cmif.dmemaddr_1 = 32'h1;
	cmif.cacheBlock0 = 32'h20;
	cmif.cacheBlock1 = 32'h40;
	
	@(posedge CLK);
	@(posedge CLK);

	$display("T4 = D0 requests read, D1 requests write");
	
	assert(cohif.ccwait_1 == 1)
	  $display("T4 - Correct! ccwait_1 should be asserted!");
        else
          $display("T4 - Failed! ccwait_1 should not be 0");

        assert(cohif.ccsnoopaddr == cmif.dmemaddr_1)
	  $display("T4 - Correct! ccsnoopaddr should be 32'h2");
	else
	  $display("T4 - Failed! ccsnoopaddr should be 32'h2");

	assert(cohif.ccinv_1 == 1)
	  $display("T4 -Correct! ccinv_1 should be 1 since D0 is requesting write permissions!");
        else
          $display("T4 - Failed! ccinv_1 should not be 0 for write requests");

	ccif.dwait[1] = 1'b1;

	@(posedge CLK);
	@(posedge CLK);			
	@(posedge CLK);
	@(posedge CLK);

	//TEST 5 - only D1 request read permissions
	cohif.cctrans_0 = 1'b0;
	cohif.cctrans_1 = 1'b1;
	cohif.ccwrite_0 = 1'b0;
	cohif.ccwrite_1 = 1'b0;
	cmif.dmemaddr_0 = 32'h0;
	cmif.dmemaddr_1 = 32'h34;
	cmif.cacheBlock0 = 32'h20;
	cmif.cacheBlock1 = 32'h40;
		
	@(posedge CLK);
	@(posedge CLK);

	$display("T5 = only D1 requests read");
	
	assert(cohif.ccwait_0 == 1)
	  $display("T5 - Correct! ccwait_0 should be asserted!");
        else
          $display("T5 - Failed! ccwait_0 should not be 0");

	assert(cohif.ccsnoopaddr == cmif.dmemaddr_0)
	  $display("T5 - Correct! ccsnoopaddr should be 32'h34");
	else
	  $display("T5 - Failed! ccsnoopaddr should be 32'h34");
	
	assert(cohif.ccinv_0 == 0)
	  $display("T5 -Correct! ccinv_0 should be 0 since D1 is requesting read permissions!");
        else
          $display("T5 - Failed! ccinv_0 should not be 1 for read requests");

	ccif.dwait[1] = 1'b1;

	@(posedge CLK);
	@(posedge CLK);			
	@(posedge CLK);
	@(posedge CLK);

	//TEST 6 - D1 requests write permissions
	cohif.cctrans_0 = 1'b0;
	cohif.cctrans_1 = 1'b1;
	cohif.ccwrite_0 = 1'b0;
	cohif.ccwrite_1 = 1'b1;
	cmif.dmemaddr_0 = 32'h10;
	cmif.dmemaddr_1 = 32'h11;
	cmif.cacheBlock0 = 32'h20;
	cmif.cacheBlock1 = 32'h40;
		
	@(posedge CLK);
	@(posedge CLK);

	$display("T6 = only D1 requests write");

	assert(cohif.ccwait_0 == 1)
	  $display("T6 - Correct! ccwait_0 should be asserted!");
        else
          $display("T6 - Failed! ccwait_0 should not be 0");

	assert(cohif.ccsnoopaddr == cmif.dmemaddr_0)
	  $display("T6 - Correct! ccsnoopaddr should be 32'h11");
	else
	  $display("T6 - Failed! ccsnoopaddr should be 32'h11");
	
	assert(cohif.ccinv_0 == 1)
	  $display("T6 -Correct! ccinv_0 should be 1 since D0 is requesting write permissions!");
        else
          $display("T6 - Failed! ccinv_0 should not be 0 for write requests");

	ccif.dwait[1] = 1'b1;

	@(posedge CLK);
	@(posedge CLK);			
	@(posedge CLK);
	@(posedge CLK);

     end // initial begin
endprogram // test
