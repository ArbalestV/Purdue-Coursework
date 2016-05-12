/*
  Eric Villasenor
  evillase@gmail.com

  register file test bench
*/

// mapped needs this
`include "register_file_if.vh"

// mapped timing needs this. 1ns is too fast
`timescale 1 ns / 1 ns

module register_file_tb;

  parameter PERIOD = 10;

  logic CLK = 0, nRST;

  // test vars
  int v1 = 1;
  int v2 = 4721;
  int v3 = 25119;

  // clock
  always #(PERIOD/2) CLK++;

  // interface
  register_file_if rfif ();
  // test program
  test #(.PERIOD (PERIOD)) PROG (
				 .CLK,
				 .nRST,
				 .rfif
				 );
  // DUT
`ifndef MAPPED
  register_file DUT(CLK, nRST, rfif);
`else
  register_file DUT(
    .\rfif.rdat2 (rfif.rdat2),
    .\rfif.rdat1 (rfif.rdat1),
    .\rfif.wdat (rfif.wdat),
    .\rfif.rsel2 (rfif.rsel2),
    .\rfif.rsel1 (rfif.rsel1),
    .\rfif.wsel (rfif.wsel),
    .\rfif.WEN (rfif.WEN),
    .\nRST (nRST),
    .\CLK (CLK)
  );
`endif

endmodule

program test (
	      input logic CLK,
	      output logic nRST,
	      register_file_if.tb rfif
	      );
   parameter PERIOD = 10;
   int v1 = 1;
   int v2 = 4721;
   int v3 = 25119;
   initial begin
      nRST = 0;
      #(PERIOD * 4)
      
      nRST = 1;
      rfif.WEN = 0;
      rfif.wdat = 0;
      rfif.wsel = 0;
      rfif.rsel1 = 0;
      rfif.rsel2 = 0;
      #(PERIOD * 3)
      
      // writing data into register file;
      rfif.WEN = 1;
      rfif.wsel = 24;
      rfif.wdat = v2;
      rfif.rsel2 = 24;
      @(posedge CLK);
      rfif.wsel = 0;
      rfif.wdat = v3;
      rfif.rsel1 = 0;
      @(posedge CLK);
      rfif.wsel = 24;
      rfif.wdat = v1;
      rfif.rsel1 = 24;
      @(posedge CLK);
      rfif.wsel = 31;
      rfif.wdat = 8367;

      // stop writing data into register file;
      @(posedge CLK);
      rfif.WEN = 0;

      @(posedge CLK);
      //reading data from the register file;
      rfif.rsel1 = 24;
      rfif.rsel2 = 1;

      @(posedge CLK);
      rfif.rsel1 = 2;
      rfif.rsel2 = 31;
      
      @(posedge CLK);
      nRST = 0;
      @(posedge CLK);
      @(posedge CLK);
      #(PERIOD * 4);
      @(posedge CLK);
      
      
      
   end // initial begin
   
      
      
      
      
endprogram
