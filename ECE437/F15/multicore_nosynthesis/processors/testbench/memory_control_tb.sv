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
   cache_control_if ccif();
   cpu_ram_if ramif();
   logic nRST;
   logic CLK = 0;

   always #(PERIOD / 2) CLK++;
   memory_control MEMARBITER(CLK, nRST, ccif);
   ram RAM(CLK, nRST, ramif);
   test PROG(CLK, nRST, ccif);
   /*
   always_comb
     begin
	ccif.ramload = ramif.ramload; // Input = Output
	ccif.ramstate = ramif.ramstate;
	ramif.ramstore = ccif.ramstore;
	ramif.ramaddr = ccif.ramaddr;
	ramif.ramWEN = ccif.ramWEN;
	ramif.ramREN = ccif.ramREN;
     end
    */
endmodule // memory_control_tb

program test (
	      input logic CLK,
	      output logic nRST,
	      cache_control_if.cc ccif
	      );
   parameter LAT = 50; //RAM latency
   parameter DELAY = 5; //Delay
   parameter PERIOD = 10;
   int 			   testnumber;
   
   initial begin
      //Test 1: Asserting reset signal
      nRST = 1'b0;
      ccif.iREN[0] = 1'b0;
      ccif.dREN[0] = 1'b0;
      ccif.dWEN[0] = 1'b0;
      ccif.dstore[0] = 32'habcdef32;
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
      ccif.iREN[0] = 1'b1;
      ccif.dREN[0] = 1'b0;
      ccif.dWEN[0] = 1'b0;
      ccif.iaddr[0] = 32'h00000000;
      #(DELAY);
      if (ccif.ramstate == BUSY) begin
	 assert((ccif.iwait[0] == 1'b1) && (ccif.dwait[0] == 1'b1) && (ccif.ramREN == 1'b1))
	   $display("Passed the iwait active case for load instruction (BUSY).");
	 else
	   $display("Failed the iwait active case for load instruction (BUSY).");
      end
      #(LAT);
      if (ccif.ramstate == ACCESS) begin
	 assert((ccif.iwait[0] == 1'b0) && (ccif.dwait[0] == 1'b1) && (ccif.ramREN == 1'b1))
	   $display("Passed the iwait inactive test case for load instruction (ACCESS).");
	 else
	   $display("Failed the iwait inactive test case for load instruction (ACCESS).");
      end

      ccif.dREN[0] = 1'b1;
      ccif.daddr[0] = 32'h3344000f;
      #(DELAY);
      if (ccif.ramstate == BUSY) begin
	 assert((ccif.iwait[0] == 1'b1) && (ccif.dwait[0] == 1'b1) && (ccif.ramREN == 1'b1))
	   $display("Passed the dwait active case for load instruction (BUSY).");
	 else
	   $display("Failed the dwait active case for load instruction (BUSY).");
      end
      #(LAT);
      if (ccif.ramstate == ACCESS) begin
	 assert((ccif.iwait[0] == 1'b1) && (ccif.dwait[0] == 1'b0) && (ccif.ramREN == 1'b1))
	   $display("Passed the dwait inactive test case for load instruction (ACCESS).");
	 else
	   $display("Failed the dwait inactive test case for load instruction (ACCESS).");
      end

      //Test3: STORE instruction execution with dREN = 0
      ccif.iREN[0] = 1'b0;
      ccif.dREN[0] = 1'b0;
      ccif.dWEN[0] = 1'b1;
      ccif.daddr[0] = 32'h0000;
      ccif.dstore[0] = 32'hFFFF;
      #(DELAY);
      if (ccif.ramstate == BUSY) begin
	 assert((ccif.iwait[0] == 1'b1) && (ccif.dwait[0] == 1'b1) && (ccif.ramREN == 1'b0))
	   $display("Passed the dwait active case for store instruction with dREN = 0 (BUSY).");
	 else
	   $display("Failed the dwait active case for store instruction with dREN = 0 (BUSY).");
      end
      #(LAT);
      if (ccif.ramstate == ACCESS) begin
	 assert((ccif.iwait[0] == 1'b1) && (ccif.dwait[0] == 1'b0) && (ccif.ramREN == 1'b0))
	   $display("Passed the dwait inactive test case for store instruction with dREN = 0 (ACCESS).");
	 else
	   $display("Failed the dwait inactive test case for store instruction with dREN = 0 (ACCESS).");
      end

      //Test4: STORE instruction execution with dREN = 1
      ccif.iREN[0] = 1'b0;
      ccif.dREN[0] = 1'b0;
      ccif.dWEN[0] = 1'b1;
      ccif.daddr[0] = 32'h0000;
      ccif.dstore[0] = 32'hFFFF;
      #(DELAY);
      if (ccif.ramstate == BUSY) begin
	 assert((ccif.iwait[0] == 1'b1) && (ccif.dwait[0] == 1'b1) && (ccif.ramREN == 1'b0))
	   $display("Passed the dwait active case for store instruction with dREN = 1 (BUSY).");
	 else
	   $display("Failed the dwait active case for store instruction with dREN = 1 (BUSY).");
      end
      #(LAT);
      if (ccif.ramstate == ACCESS) begin
	 assert((ccif.iwait[0] == 1'b1) && (ccif.dwait[0] == 1'b0) && (ccif.ramREN == 1'b0))
	   $display("Passed the dwait inactive test case for store instruction with dREN = 1 (ACCESS).");
	 else
	   $display("Failed the dwait inactive test case for store instruction with dREN = 1 (ACCESS).");
      end

      //Test5: STORE instruction execution with dREN = 1, iREN = 1
      ccif.iREN[0] = 1'b1;
      ccif.dREN[0] = 1'b1;
      ccif.dWEN[0] = 1'b1;
      ccif.daddr[0] = 32'h0000;
      ccif.dstore[0] = 32'hFFFF;
      #(DELAY);
      if (ccif.ramstate == BUSY) begin
	 assert((ccif.iwait[0] == 1'b1) && (ccif.dwait[0] == 1'b1) && (ccif.ramREN == 1'b0))
	   $display("Passed the dwait active case for store instruction with dREN = 1, iREN = 1 (BUSY).");
	 else
	   $display("Failed the dwait active case for store instruction with dREN = 1, iREN = 1 (BUSY).");
      end
      #(LAT);
      if (ccif.ramstate == ACCESS) begin
	 assert((ccif.iwait[0] == 1'b1) && (ccif.dwait[0] == 1'b0) && (ccif.ramREN == 1'b0))
	   $display("Passed the dwait inactive test case for store instruction with dREN = 1, iREN = 1 (ACCESS).");
	 else
	   $display("Failed the dwait inactive test case for store instruction with dREN = 1, iREN = 1 (ACCESS).");
      end


      
      #(DELAY)
      //Test Coherence Controller
      nRST = 1'b0;

      ccif.iREN[0] = 1'b0;
      ccif.dREN[0] = 1'b0;
      ccif.dWEN[0] = 1'b0;
      ccif.daddr[0] = 32'h0000;
      ccif.dstore[0] = 32'h0000;

      ccif.cctrans[0] = 0;
      ccif.ccwrite[0] = 0;
      ccif.dREN[0] = 0;
      ccif.dWEN[0] = 0;
      ccif.daddr[0] = 0;
      ccif.cctrans[1] = 0;
      ccif.ccwrite[1] = 0;
      ccif.dREN[1] = 0;
      ccif.dWEN[1] = 0;
      ccif.daddr[1] = 0;
      
      #(PERIOD)
      nRST = 1'b1;
      #(PERIOD)     

      //CC Test 1 : dWEN1
      testnumber = 1;
      
      #(DELAY)
      ccif.dWEN[1] = 1'b1;
      #(DELAY)

      if ( ccif.ccwait[0] == 1'b1 ) begin
	 $display("CC Test 1.1 Passed");
      end
      else begin
	 $display("CC Test 1.1 Failed");
      end

      ccif.dWEN[1] = 1'b0;
      #(PERIOD)

      if ( ccif.ccwait[0] == 1'b0 ) begin
	 $display("CC Test 1.2 Passed");
      end
      else begin
	 $display("CC Test 1.2 Failed");
      end

      #(PERIOD)

      //CC Test 2 : dWEN0
      testnumber = 2;
      
      ccif.dWEN[0] = 1'b1;
      #(PERIOD)
      
      if ( ccif.ccwait[1] == 1'b1 ) begin
	 $display("CC Test 2.1 Passed");
      end
      else begin
	 $display("CC Test 2.1 Failed");
      end

      #(PERIOD)
      ccif.dWEN[0] = 1'b0;
      #(PERIOD)

      if ( ccif.ccwait[1] == 1'b0 ) begin
	 $display("CC Test 2.2 Passed");
      end
      else begin
	 $display("CC Test 2.2 Failed");
      end

      #(PERIOD)      

      //CC Test 3 : dREN 0 without snoop match
      testnumber = 3;
      
      ccif.cctrans[0] = 1'b1;
      ccif.ccwrite[0] = 1'b1;
      ccif.dREN[0] = 1'b1;      
      ccif.daddr[0] = 32'hDEADBEEF;      
      #(PERIOD)
      if ( ccif.ccwait[0] == 1'b1 && ccif.ccwait[1] == 1'b1 &&
	   ccif.ccsnoopaddr[1] == 32'hDEADBEEF) begin
	 $display("CC Test 3.1 Passed");
      end
      else begin
	 $display("CC Test 3.1 Failed");
      end

      ccif.dWEN[1] = 1'b0;
      ccif.ramload = 32'hABAABABB;      
      #(PERIOD)

      if ( ccif.dload[0] == ccif.ramload ) begin
	 $display("CC Test 3.2 Passed");
      end
      else begin
	 $display("CC Test 3.2 Failed");
      end

      ccif.dREN[0] = 1'b0;      
      #(PERIOD)

      if ( ccif.ccinv[1] == 1'b1 && ccif.ccsnoopaddr[1] == 32'hDEADBEEF ) begin
	 $display("CC Test 3.3 Passed");
      end
      else begin
	 $display("CC Test 3.3 Failed");
      end
      #(PERIOD)
      
      //CC Test 4 : dREN 0 with snoop match and invalid cache1
      testnumber = 4;
      
      ccif.dREN[0] = 1'b1;
      ccif.cctrans[0] = 1'b1;
      ccif.ccwrite[0] = 1'b1;            
      ccif.daddr[0] = 32'hABABABAB;
      #(PERIOD)
      
      if ( ccif.ccwait[0] && ccif.ccwait[1] ) begin
	 $display("CC Test 4.1 Passed");
      end
      else begin
	 $display("CC Test 4.1 Failed");
      end

      ccif.dWEN[1] = 1'b0; 
      ccif.ramload = 32'hCCCCCCCC;      
      #(PERIOD)
      
      if ( ccif.dload[0] == ccif.ramload ) begin
	 $display("CC Test 4.2 Passed");
      end
      else begin
	 $display("CC Test 4.2 Failed");
      end

      ccif.dREN[0] = 1'b0;
      #(PERIOD)

      if ( ccif.ccinv[1] == 1'b1 && ccif.ccsnoopaddr[1] == ccif.daddr[0] ) begin
	 $display("CC Test 4.3 Passed");
      end
      else begin
	 $display("CC Test 4.3 Failed");
      end


      ccif.dREN[0] = 1'b0;
      ccif.cctrans[0] = 1'b0;
      ccif.ccwrite[0] = 1'b0;            
      ccif.daddr[0] = 32'h00000000;
      ccif.dWEN[1] = 1'b0; 
      #(PERIOD)
            
      //CC Test 5 : dREN 0 with snoop match and valid cache1
      testnumber = 5;
      
      ccif.dREN[0] = 1'b1;
      ccif.cctrans[0] = 1'b1;
      ccif.ccwrite[0] = 1'b0;            
      ccif.daddr[0] = 32'hFDFDFDFD;      
      #(PERIOD)

      if ( ccif.ccwait[0] && ccif.ccwait[1] ) begin
	 $display("CC Test 5.1 Passed");
      end
      else begin
	 $display("CC Test 5.1 Failed");
      end

      ccif.dWEN[1] = 1;
      ccif.dstore[1] = 32'hABCDABCD;      
      #(PERIOD)

      if ( ccif.dload[0] == 32'hABCDABCD ) begin
	 $display("CC Test 4.2 Passed");
      end
      else begin
	 $display("CC Test 4.2 Failed");
      end

      ccif.dREN[0] = 1'b0;
      #(PERIOD)

      if ( ccif.ccinv[1] == 1'b0 && ccif.ccsnoopaddr[1] == ccif.daddr[0] ) begin
	 $display("CC Test 4.3 Passed");
      end
      else begin
	 $display("CC Test 4.3 Failed");
      end

      ccif.dREN[0] = 1'b0;
      ccif.cctrans[0] = 1'b0;
      ccif.ccwrite[0] = 1'b0;            
      ccif.daddr[0] = 32'h00000000;
      ccif.dWEN[1] = 1'b0; 
      #(PERIOD)
      //CC Test 6 : modify cache0 w/o memory -- invalidate cache1
      testnumber = 6;
      
      ccif.dREN[0] = 1'b0;
      ccif.cctrans[0] = 1'b1;
      ccif.ccwrite[0] = 1'b1;
      ccif.daddr[0] = 32'hAABBCCDD;
      
      #(PERIOD)

      if ( ccif.ccwait[0] == 1'b1 && ccif.ccwait[1] == 1'b1 && 
	   ccif.ccsnoopaddr[1] == 32'hAABBCCDD ) begin
	 $display("CC Test 6.1 Passed");
      end
      else begin
	 $display("CC Test 6.1 Failed");
      end

      ccif.dWEN[1] = 1;
      ccif.dstore[1] = 32'hAAAAAAAA;      
      #(PERIOD)

      if ( ccif.dload[0] == 32'hAAAAAAAA ) begin
	 $display("CC Test 6.2 Passed");
      end
      else begin
	 $display("CC Test 6.2 Failed");
      end

      #(PERIOD)

      if (ccif.ccinv[1] == 1'b1 && ccif.ccsnoopaddr[1] == 32'hAABBCCDD ) begin
	 $display("CC Test 6.3 Passed");
      end
      else begin
	 $display("CC Test 6.3 Failed");
      end

      ccif.dREN[0] = 1'b0;
      ccif.cctrans[0] = 1'b0;
      ccif.ccwrite[0] = 1'b0;            
      ccif.daddr[0] = 32'h00000000;
      ccif.dWEN[1] = 1'b0;
      #(PERIOD)



      //CC Test 7 : dREN 1 without snoop match
      testnumber = 7;
      
      ccif.cctrans[1] = 1'b1;
      ccif.ccwrite[1] = 1'b1;
      ccif.dREN[1] = 1'b1;      
      ccif.daddr[1] = 32'hDEADBEEF;      
      #(PERIOD)
      if ( ccif.ccwait[0] == 1'b1 && ccif.ccwait[1] == 1'b1 &&
	   ccif.ccsnoopaddr[0] == 32'hDEADBEEF) begin
	 $display("CC Test 7.1 Passed");
      end
      else begin
	 $display("CC Test 7.1 Failed");
      end

      ccif.dWEN[0] = 1'b0;    
      ccif.ramload = 32'hDDDDDDDD;
      
      #(PERIOD)

      if ( ccif.dload[1] == ccif.ramload ) begin
	 $display("CC Test 7.2 Passed");
      end
      else begin
	 $display("CC Test 7.2 Failed");
      end

      ccif.dREN[1] = 1'b0;    
      #(PERIOD)

      if ( ccif.ccinv[0] == 1'b1 && ccif.ccsnoopaddr[0] == 32'hDEADBEEF ) begin
	 $display("CC Test 7.3 Passed");
      end
      else begin
	 $display("CC Test 7.4 Failed");
      end
      #(PERIOD)
      
      //CC Test 8 : dREN 0 with snoop match and invalid cache1
      testnumber = 8;
      
      ccif.dREN[1] = 1'b1;
      ccif.cctrans[1] = 1'b1;
      ccif.ccwrite[1] = 1'b1;            
      ccif.daddr[1] = 32'hABABABAB;
      #(PERIOD)
      
      if ( ccif.ccwait[0] && ccif.ccwait[1] ) begin
	 $display("CC Test 8.1 Passed");
      end
      else begin
	 $display("CC Test 8.1 Failed");
      end

      ccif.dWEN[0] = 1'b0;      
      ccif.ramload = 32'hEEEEFFFF;
      #(PERIOD)

      if ( ccif.dload[1] == ccif.ramload ) begin
	 $display("CC Test 8.2 Passed");
      end
      else begin
	 $display("CC Test 8.2 Failed");
      end

      ccif.dREN[1] = 1'b0;
      #(PERIOD)

      if ( ccif.ccinv[0] == 1'b1 && ccif.ccsnoopaddr[0] == ccif.daddr[1] ) begin
	 $display("CC Test 8.3 Passed");
      end
      else begin
	 $display("CC Test 8.3 Failed");
      end


      ccif.dREN[1] = 1'b0;
      ccif.cctrans[1] = 1'b0;
      ccif.ccwrite[1] = 1'b0;            
      ccif.daddr[1] = 32'h00000000;
      ccif.dWEN[0] = 1'b0; 
      #(PERIOD)
            
      //CC Test 9 : dREN 0 with snoop match and valid cache1
      testnumber = 9;
      
      ccif.dREN[1] = 1'b1;
      ccif.cctrans[1] = 1'b1;
      ccif.ccwrite[1] = 1'b0;            
      ccif.daddr[1] = 32'hFDFDFDFD;      
      #(PERIOD)

      if ( ccif.ccwait[0] && ccif.ccwait[1] ) begin
	 $display("CC Test 9.1 Passed");
      end
      else begin
	 $display("CC Test 9.1 Failed");
      end

      ccif.dWEN[0] = 1;
      ccif.dstore[0] = 32'hABCDABCD;      
      #(PERIOD)

      if ( ccif.dload[1] == 32'hABCDABCD ) begin
	 $display("CC Test 9.2 Passed");
      end
      else begin
	 $display("CC Test 9.2 Failed");
      end

      ccif.dREN[1] = 1'b0;
      #(PERIOD)

      if ( ccif.ccinv[0] == 1'b0 && ccif.ccsnoopaddr[0] == ccif.daddr[1] ) begin
	 $display("CC Test 9.3 Passed");
      end
      else begin
	 $display("CC Test 9.3 Failed");
      end

      ccif.dREN[1] = 1'b0;
      ccif.cctrans[1] = 1'b0;
      ccif.ccwrite[1] = 1'b0;            
      ccif.daddr[1] = 32'h00000000;
      ccif.dWEN[0] = 1'b0; 
      #(PERIOD)
      //CC Test 10 : modify cache0 w/o memory -- invalidate cache1
      testnumber = 10;
      
      ccif.dREN[1] = 1'b0;
      ccif.cctrans[1] = 1'b1;
      ccif.ccwrite[1] = 1'b1;
      ccif.daddr[1] = 32'hAABBCCDD;
      
      #(PERIOD)

      if ( ccif.ccwait[0] == 1'b1 && ccif.ccwait[1] == 1'b1 && 
	   ccif.ccsnoopaddr[0] == 32'hAABBCCDD ) begin
	 $display("CC Test 10.1 Passed");
      end
      else begin
	 $display("CC Test 10.1 Failed");
      end

      ccif.dWEN[0] = 1;
      ccif.dstore[0] = 32'hAAAAAAAA;      
      #(PERIOD)

      if ( ccif.dload[1] == 32'hAAAAAAAA ) begin
	 $display("CC Test 10.2 Passed");
      end
      else begin
	 $display("CC Test 10.2 Failed");
      end

      #(PERIOD)

      if (ccif.ccinv[0] == 1'b1 && ccif.ccsnoopaddr[0] == 32'hAABBCCDD ) begin
	 $display("CC Test 10.3 Passed");
      end
      else begin
	 $display("CC Test 10.3 Failed");
      end

      ccif.dREN[1] = 1'b0;
      ccif.cctrans[1] = 1'b0;
      ccif.ccwrite[1] = 1'b0;            
      ccif.daddr[1] = 32'h00000000;
      ccif.dWEN[0] = 1'b0;
      #(PERIOD)          
      
      dump_memory();
      $finish;
   end // initial begin
  
task automatic dump_memory();
    string filename = "memcpu.hex";
    int memfd;

    ccif.daddr[0] = 0;
    ccif.iREN[0] = 0;
    ccif.dWEN[0] = 0;
    ccif.dREN[0] = 0;

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

      ccif.daddr[0] = i << 2;
      ccif.dREN[0] = 1;
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
      ccif.dREN[0] = 0;
      $fdisplay(memfd,":00000001FF");
      $fclose(memfd);
      $display("Finished memory dump.");
    end
endtask // dump_memory

   
endprogram // test
   
