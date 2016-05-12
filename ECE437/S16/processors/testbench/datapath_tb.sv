/*`include "datapath_cache_if.vh"
`include "cache_control_if.vh"
`include "cpu_ram_if.vh"

module datapath_tb ();
  parameter PERIOD = 10;

  logic CLK = 0, nRST;

  always
    begin
      CLK = 0;
      #(PERIOD/2);
      CLK = 1;
      #(PERIOD/2);
    end

  datapath_cache_if dcif ();
  cache_control_if ccif ();
  cpu_ram_if ramif ();

  datapath DATAPATH ( CLK, nRST, dcif );

endmodule

program test (input logic CLK,
              output logic nRST,
              datapath_cache_if dcif);
parameter DELAY = 10;
initial
  begin
    //Reset System
    nRST = 1'b0;
    #(2*DELAY);
    nRST = 1'b1;

    //
  end
endprogram */
`include "cpu_types_pkg.vh"
`include "datapath_cache_if.vh"

`timescale 1 ns / 1 ns

import cpu_types_pkg::*;

module datapath_tb;

	//Instantiating required interfaces
	datapath_cache_if dpif();

	logic CLK = 0, nRst;
	parameter PERIOD = 10;

	always #(PERIOD / 2) CLK++;

	//Instantiating datapath 
	datapath DATAPATH_TEST(CLK, nRst, dpif);

	test PROG(CLK, nRst, dpif);

endmodule // datapath_tb

program test(
	input logic CLK,
	output logic nRst,
	datapath_cache_if.cache dpif
);
	parameter PERIOD = 10;
	parameter LAT = 0;
	parameter delay = 3;
	logic [OP_W - 1 : 0] opcode;
	logic [REG_W - 1 : 0] rs, rt, rd;
	logic [IMM_W - 1 : 0] imm;
	logic [ADDR_W - 1 : 0] jumpaddr;
	logic [SHAM_W - 1 : 0] shiftamt;
	logic [FUNC_W - 1 : 0] funct;
	logic [1 : 0] instrType;

	assign dpif.imemload = (instrType == 0)? {opcode, rs, rt, rd, shiftamt, funct} :
							(instrType == 1)? {opcode, rs, rt, imm} : {opcode, jumpaddr};
	typedef enum logic [3:0] {TEST1, TEST2, TEST3, TEST4, TEST5, TEST6, TEST7, TEST8, TEST9} test;
	test testno;

	initial begin
		shiftamt = 0;
		jumpaddr = 0;
		dpif.ihit = 1'b0;
		dpif.dhit = 1'b0;
		opcode = 0;

		//Test 1 : Resetting the Datapath subsystem
		testno = TEST1;
		nRst = 1'b0;
		#(delay);
		assert(~dpif.dmemREN && ~dpif.dmemWEN && dpif.imemREN)
			$display("PASSED the reset test for Memory Read and Write signals");
		else
			$display("FAILED the reset test for Memory Read and Write signals");	

		//Test 2 : I-type Instruction (LW $1, 4($0))
		@(posedge CLK);
		nRst = 1'b1;
		testno = TEST2;
		#(delay);
		instrType = 2'b01;
		opcode = LW;
		rs = 0;
		rt = 1;
		imm = 4;
		dpif.ihit = 1'b1;
		//Check for PC, Register value
		assert(~dpif.dmemREN && ~dpif.dmemWEN && dpif.imemREN && dpif.imemaddr == 0)
			$display("PASSED the Instruction Read test for I-Type LOAD");
		else
			$display("FAILED the Instruction Read test for I-Type LOAD");	
		@(posedge CLK);
		assert(dpif.dmemaddr == 4 && dpif.dmemREN && ~dpif.dmemWEN && dpif.imemREN)
			$display("PASSED the Data Read test for I-Type LOAD");
		else
			$display("FAILED the Data Read test for I-Type LOAD");	
		for(int i = 0; i < LAT; i++)
		begin
			if(i == 0)
				dpif.ihit = 0;
			@(posedge CLK);
		end
		dpif.ihit = 1'b0;
		dpif.dmemload = 32'ha;
		dpif.dhit = 1'b1;
		//Check for PC, Control Signals, Register File inputs
		@(posedge CLK);
		assert(~dpif.dmemREN && ~dpif.dmemWEN && dpif.imemREN && dpif.imemaddr == 4)
			$display("PASSED the Data Read dhit assertion test for I-Type LOAD");
		else
			$display("FAILED the Data Read dhit assertion test for I-Type LOAD");	
		dpif.dhit = 1'b0;

		//Test 3 : Testing R-Type Instruction (ADD $2, $1, $0)
		testno = TEST3;
		instrType = 0;
		#(delay);
		opcode = 0;
		funct = ADD;
		rs = 0;
		rd = 2;
		rt = 1;
		dpif.ihit = 1'b1;
		//Check for PC, Regsiter value
		assert(~dpif.dmemREN && ~dpif.dmemWEN && dpif.imemREN && dpif.imemaddr == 4 /*&& dpif.dmemstore == 32'ha*/)
			$display("PASSED the Instruction Read test for R-Type ADD");
		else
			$display("FAILED the Instruction Read test for R-Type ADD");	

		//Test 4 : Testing for J-Type (JAL 3)
		@(posedge CLK);
		testno = TEST4;
		instrType = 2'b10;
		#(delay);
		opcode = JAL;
		jumpaddr = 3;
		dpif.ihit = 1'b1;
		assert(~dpif.dmemREN && ~dpif.dmemWEN && dpif.imemREN && dpif.imemaddr == 8)
			$display("PASSED the Instruction Read test for J-Type JAL");
		else
			$display("FAILED the Instruction Read test for J-Type JAL");	
		//dpif.ihit = 1'b0;
		@(posedge CLK);
		assert(dpif.imemaddr == 32'hc)
			$display("PASSED the Address change test for J-Type Instruction");
		else
			$display("FAILED the Address change test for J Type JAL");

		//Test 5 : Testing for $31 value with I-Type (SW $31, a($0))
		testno = TEST5;
		instrType = 2'b01;
		#(delay);
		opcode = SW;
		rs = 0;
		rt = 31;
		imm = 13;
		dpif.ihit = 1'h1;
		assert(~dpif.dmemREN && ~dpif.dmemWEN && dpif.imemREN && dpif.imemaddr == 32'hc)
			$display("PASSED the Instruction Read test for I-Type SW");
		else
			$display("FAILED the Instruction Read test for I-Type SW");	
		@(posedge CLK);
		assert(~dpif.dmemREN && dpif.dmemWEN && dpif.imemREN && dpif.dmemaddr == 13 /*&& dpif.dmemstore == 32'hc*/)
			$display("PASSED the Data Write test for I-Type STORE");
		else
			$display("FAILED the Data Write test for I-Type STORE");	
		dpif.dhit = 1'b1;
		for(int i = 0; i < LAT; i++)
		begin
			if(i == 0)
				dpif.ihit = 1'b0;
			@(posedge CLK);
		end
		//dpif.ihit = 1'b0;
		//dpif.dhit = 1'b1;
		//Check for PC, Control Signals, Register File inputs
		@(posedge CLK);
		assert(~dpif.dmemREN && ~dpif.dmemWEN && dpif.imemREN && dpif.imemaddr == 32'h14)
			$display("PASSED the Data Write dhit assertion test for I-Type STORE");
		else
			$display("FAILED the Data Write dhit assertion test for I-Type STORE");	
		dpif.dhit = 1'b0;

		//Test 6 : Check with JR (JR $2)
		testno = TEST6;
		#(delay);
		instrType = 0;
		opcode = RTYPE;
		funct = 6'b001000;
		rs = 2;
		dpif.ihit = 1'b1;
		assert(~dpif.dmemREN && ~dpif.dmemWEN && dpif.imemREN && dpif.imemaddr == 32'h14)
			$display("PASSED the Instruction Read test for R-Type JR");
		else
			$display("FAILED the Instruction Read test for R-Type JR");	
		#(delay);
		dpif.ihit = 1'b0;
		@(posedge CLK);
		assert(~dpif.dmemREN && ~dpif.dmemWEN && dpif.imemREN /*&& dpif.imemaddr == 32'ha*/)
			$display("PASSED the PC address update test in R-Type JR");
		else
			$display("FAILED the PC address update test in R-Type JR");

		//Test 7 : Testing LUI Instruction (LUI $3, 128)
		testno = TEST7;
		instrType = 2'b01;
		#(delay);
		opcode = LUI; 	
		rs = 0;
		rt = 32'h3;
		imm = 16'h10;
		dpif.ihit = 1'b1;
		assert(~dpif.dmemREN && ~dpif.dmemWEN && dpif.imemREN && dpif.imemaddr == 32'ha)
			$display("PASSED the Instruction Read test for I-Type LUI");
		else
			$display("FAILED the Instruction Read test for I-Type LUI");	
		#(delay);
		dpif.ihit = 1'b0;
		assert(~dpif.dmemREN && ~dpif.dmemWEN && dpif.imemREN && dpif.dmemaddr == 32'h100000)
			$display("PASSED the Upper Half Word load test in I-Type LUI");
		else
			$display("FAILED the Upper Half Word load test in I-Type LUI");

		//Test 8 : Checking BNE instruction (BNE $1, $3, 0xff)
		@(posedge CLK);
		testno = TEST8;
		opcode  = BNE;
		rs = 3;
		rt = 1;
		imm = 32'hff;
		dpif.ihit = 1'b1;
		assert(~dpif.dmemREN && ~dpif.dmemWEN && dpif.imemREN && dpif.imemaddr == 32'he)
			$display("PASSED the Instruction Read test for I-Type BNE");
		else
			$display("FAILED the Instruction Read test for I-Type BNE");	
		@(posedge CLK);
		#(delay);
		assert(~dpif.dmemREN && ~dpif.dmemWEN && dpif.imemREN && dpif.imemaddr == 32'h40e)
			$display("PASSED the Branch address change test for I-Type BNE");
		else
			$display("FAILED the Branch address change test for I-Type BNE");

end
endprogram







