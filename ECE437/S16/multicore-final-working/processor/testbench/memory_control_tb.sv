//mapped needs this
`include "cache_control_if.vh"
`include "cpu_ram_if.vh"
`include "cpu_types_pkg.vh"

//mapped timing needs this. 1 ns is too fast
`timescale 1 ns / 1 ns

import cpu_types_pkg::*;

module memory_control_tb;
   parameter PERIOD = 10;

   //interface
   caches_if cif0();
   caches_if cif1();
   cache_control_if #(.CPUS(1)) ccif(cif0, cif1);
   cpu_ram_if ramif();
   logic nRST;
   logic CLK = 0;

   always #(PERIOD / 2) CLK++;
   memory_control MEMARBITER(CLK, nRST, ccif);
   ram RAM(CLK, nRST, ramif);
   test PROG(CLK, nRST, cif0, ccif);

   always_comb
     begin
	ccif.ramload = ramif.ramload; // Input = Output
	ccif.ramstate = ramif.ramstate;
	ramif.ramstore = ccif.ramstore;
	ramif.ramaddr = ccif.ramaddr;
	ramif.ramWEN = ccif.ramWEN;
	ramif.ramREN = ccif.ramREN;
     end
endmodule // memory_control_tb

program test (
	      input logic CLK,
	      output logic nRST,
	      caches_if cif0,
	      cache_control_if.cc ccif
	      );
   parameter LAT = 50; //RAM latency
   parameter DELAY = 5; //Delay
   initial begin
      
      
      
      //Test 1: Asserting reset signal
      nRST = 1'b0;
      cif0.iREN = 1'b0;
      cif0.dREN = 1'b0;
      cif0.dWEN = 1'b0;
      cif0.dstore = 32'habcdef32;
      #(DELAY);
      /*
      //Test2: Reading instruction from the memory
      nRST = 1'b1;
      ccif.iREN[0] = 1'b1;
      ccif.dREN[0] = 1'b0;
      ccif.dWEN[0] = 1'b0;
      ccif.iaddr[0] = 32'h000010af;
      #(DELAY);
      if (ccif.ramstate == BUSY) begin
	 assert(ccif.iwait[0] == 1'b1 && ccif.ramREN == 1'b1)
	   $display("Passed the iwait active test case for memory instruction read");
	 else
	   $display("Failed the iwait active test case for memory instruction read.");
      end
      #(LAT);//wait for the ram to read from itself
      if (ccif.ramstate == ACCESS) begin
	 assert(ccif.iwait[0] == 1'b0)
	   $display("Passed the iwait inactive test case for memory instruction read");
	 else
	   $display("Failed the iwait inactive test case for memory instruction read.");
      end
       */

      nRST = 1'b1; //make the RAM come out of reset
      
      //Test2: LOAD instruction execution
      cif0.iREN = 1'b1;
      cif0.dREN = 1'b0;
      cif0.dWEN = 1'b0;
      cif0.iaddr = 32'h00000000;
      #(DELAY);
      if (ccif.ramstate == BUSY) begin
	 assert((ccif.iwait == 1'b1) && (ccif.dwait == 1'b1) && (ccif.ramREN == 1'b1))
	   $display("Passed the iwait active case for load instruction (BUSY).");
	 else
	   $display("Failed the iwait active case for load instruction (BUSY).");
      end
      #(LAT);
      if (ccif.ramstate == ACCESS) begin
	 assert((ccif.iwait == 1'b0) && (ccif.dwait == 1'b1) && (ccif.ramREN == 1'b1))
	   $display("Passed the iwait inactive test case for load instruction (ACCESS).");
	 else
	   $display("Failed the iwait inactive test case for load instruction (ACCESS).");
      end

      cif0.dREN = 1'b1;
      cif0.daddr = 32'h3344000f;
      #(DELAY);
      if (ccif.ramstate == BUSY) begin
	 assert((ccif.iwait == 1'b1) && (ccif.dwait == 1'b1) && (ccif.ramREN == 1'b1))
	   $display("Passed the dwait active case for load instruction (BUSY).");
	 else
	   $display("Failed the dwait active case for load instruction (BUSY).");
      end
      #(LAT);
      if (ccif.ramstate == ACCESS) begin
	 assert((ccif.iwait == 1'b1) && (ccif.dwait == 1'b0) && (ccif.ramREN == 1'b1))
	   $display("Passed the dwait inactive test case for load instruction (ACCESS).");
	 else
	   $display("Failed the dwait inactive test case for load instruction (ACCESS).");
      end

      //Test3: STORE instruction execution with dREN = 0
      cif0.iREN = 1'b0;
      cif0.dREN = 1'b0;
      cif0.dWEN = 1'b1;
      cif0.daddr = 32'h0000;
      cif0.dstore = 32'hFFFF;
      #(DELAY);
      if (ccif.ramstate == BUSY) begin
	 assert((ccif.iwait == 1'b1) && (ccif.dwait == 1'b1) && (ccif.ramREN == 1'b0))
	   $display("Passed the dwait active case for store instruction with dREN = 0 (BUSY).");
	 else
	   $display("Failed the dwait active case for store instruction with dREN = 0 (BUSY).");
      end
      #(LAT);
      if (ccif.ramstate == ACCESS) begin
	 assert((ccif.iwait == 1'b1) && (ccif.dwait == 1'b0) && (ccif.ramREN == 1'b0))
	   $display("Passed the dwait inactive test case for store instruction with dREN = 0 (ACCESS).");
	 else
	   $display("Failed the dwait inactive test case for store instruction with dREN = 0 (ACCESS).");
      end

      //Test4: STORE instruction execution with dREN = 1
      cif0.iREN = 1'b0;
      cif0.dREN = 1'b0;
      cif0.dWEN = 1'b1;
      cif0.daddr = 32'h0000;
      cif0.dstore = 32'hFFFF;
      #(DELAY);
      if (ccif.ramstate == BUSY) begin
	 assert((ccif.iwait == 1'b1) && (ccif.dwait == 1'b1) && (ccif.ramREN == 1'b0))
	   $display("Passed the dwait active case for store instruction with dREN = 1 (BUSY).");
	 else
	   $display("Failed the dwait active case for store instruction with dREN = 1 (BUSY).");
      end
      #(LAT);
      if (ccif.ramstate == ACCESS) begin
	 assert((ccif.iwait == 1'b1) && (ccif.dwait == 1'b0) && (ccif.ramREN == 1'b0))
	   $display("Passed the dwait inactive test case for store instruction with dREN = 1 (ACCESS).");
	 else
	   $display("Failed the dwait inactive test case for store instruction with dREN = 1 (ACCESS).");
      end

      //Test5: STORE instruction execution with dREN = 1, iREN = 1
      cif0.iREN = 1'b1;
      cif0.dREN = 1'b1;
      cif0.dWEN = 1'b1;
      cif0.daddr = 32'h0000;
      cif0.dstore = 32'hFFFF;
      #(DELAY);
      if (ccif.ramstate == BUSY) begin
	 assert((ccif.iwait == 1'b1) && (ccif.dwait == 1'b1) && (ccif.ramREN == 1'b0))
	   $display("Passed the dwait active case for store instruction with dREN = 1, iREN = 1 (BUSY).");
	 else
	   $display("Failed the dwait active case for store instruction with dREN = 1, iREN = 1 (BUSY).");
      end
      #(LAT);
      if (ccif.ramstate == ACCESS) begin
	 assert((ccif.iwait == 1'b1) && (ccif.dwait == 1'b0) && (ccif.ramREN == 1'b0))
	   $display("Passed the dwait inactive test case for store instruction with dREN = 1, iREN = 1 (ACCESS).");
	 else
	   $display("Failed the dwait inactive test case for store instruction with dREN = 1, iREN = 1 (ACCESS).");
      end

      dump_memory();
      $finish;
   end // initial begin
  
task automatic dump_memory();
    string filename = "memcpu.hex";
    int memfd;

    cif0.daddr = 0;
    cif0.iREN = 0;
    cif0.dWEN = 0;
    cif0.dREN = 0;

    memfd = $fopen(filename,"w");
    if (memfd)
      $display("Starting memory dump.");
    else
      begin $display("Failed to open %s.",filename); $finish; end

    for (int unsigned i = 0; memfd && i < 16384; i++)
    begin
      int chksum = 0;
      bit [7:0][7:0] values;
      string ihex;

      cif0.daddr = i << 2;
      cif0.dREN = 1;
      repeat (4) @(posedge CLK);
      if (ccif.ramload === 0)
        continue;
      values = {8'h04,16'(i),8'h00,ccif.ramload};
      foreach (values[j])
        chksum += values[j];
      chksum = 16'h100 - chksum;
      ihex = $sformatf(":04%h00%h%h",16'(i),ccif.ramload,8'(chksum));
      $fdisplay(memfd,"%s",ihex.toupper());
    end //for
    if (memfd)
    begin
      //syif.tbCTRL = 0;
      cif0.dREN = 0;
      $fdisplay(memfd,":00000001FF");
      $fclose(memfd);
      $display("Finished memory dump.");
    end
endtask // dump_memory

   
endprogram // test
   
