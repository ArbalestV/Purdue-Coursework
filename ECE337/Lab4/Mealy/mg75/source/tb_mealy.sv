`timescale 1ns / 10ps
module tb_mealy();
  reg tb_clk;
  reg tb_n_rst;
  reg tb_i;
  reg tb_o;
  integer j;
  reg [7:0] tb_input;
  reg [7:0] tb_output;
  reg [11:0] tb_input_2;
  reg [11:0] tb_output_2;
  reg [11:0] tb_input_3;
  reg [11:0] tb_output_3;
  reg [11:0] tb_input_4;
  reg [11:0] tb_output_4;
  reg [6:0] tb_input_5;
  reg [6:0] tb_output_5;
  reg [3:0] tb_input_6;
  reg [3:0] tb_output_6;
  reg [3:0] tb_input_7;
  reg [3:0] tb_output_7;
  reg [5:0] tb_input_8;
  reg [5:0] tb_output_8;
  reg [9:0] tb_input_9;
  reg [9:0] tb_output_9;
  reg [9:0] tb_input_10;
  reg [9:0] tb_output_10;
  reg [8:0] tb_input_11;
  reg [8:0] tb_output_11;
  reg [8:0] tb_input_12;
  reg [8:0] tb_output_12;
	//DUI portmaps
	mealy DUT
	(
	 .clk(tb_clk),
	 .n_rst(tb_n_rst),
	 .i(tb_i),
	 .o(tb_o)
	 );
	 
	 // basic test bench parameters

	localparam	CLK_PERIOD	= 2.5; //clock period in ns
	localparam	CHECK_DELAY = 1; //delay in ns
	 
	 // Clock generation block
	always
	begin
		tb_clk = 1'b0;
		#(CLK_PERIOD/2.0);
		tb_clk = 1'b1;
		#(CLK_PERIOD/2.0);
	end
	initial begin
	  //test case 1: no. of inputs =8 and two matches
	tb_input = 8'b11011010;
	tb_output = 8'b00010010; 
	$info("Test Case 1");
  for (j=0;j<8;j++)
	 begin
	   @ (negedge tb_clk)
	       tb_i = tb_input[7-j];
	       #(CHECK_DELAY);
	   //@ (posedge tb_clk)
	     if (tb_o == tb_output[7-j])
	       begin
	         $info("Passed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output[7-j]);
	         end
	       else
	         begin
	           $error("Failed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output[7-j]);
	         end	 
	         end  
	         
	         //test case 2: no. of inputs =12 and two matches
	@(negedge tb_clk); 
	tb_n_rst = 1'b0;//resetting the outputs to 0
	tb_input_2 = 12'b011010110101;
	tb_output_2 = 12'b000010000100; 
	#(1);
	tb_n_rst = 1'b1; //enable outputs to change
	$info("Test case 2");
  for (j=0;j<12;j++)
	 begin
	   @ (negedge tb_clk)
	       tb_i = tb_input_2[11-j];
	       #(CHECK_DELAY);
	   //@ (posedge tb_clk)
	     if (tb_o == tb_output_2[11-j])
	       begin
	         $info("Passed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_2[11-j]);
	         end
	       else
	         begin
	           $error("Failed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_2[11-j]);
	         end	 
	    end
	         
	    //test case 3: no. of inputs =12 and three matches
	@(negedge tb_clk); 
	tb_n_rst = 1'b0;//resetting the outputs to 0
	tb_input_3 = 12'b110110110100;
	tb_output_3 = 12'b000100100100; 
	#(1);
	tb_n_rst = 1'b1; //enable outputs to change
	$info("Test case 3");
  for (j=0;j<12;j++)
	 begin
	   @ (negedge tb_clk)
	       tb_i = tb_input_3[11-j];
	       #(CHECK_DELAY);
	   //@ (posedge tb_clk)
	     if (tb_o == tb_output_3[11-j])
	       begin
	         $info("Passed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_3[11-j]);
	         end
	       else
	         begin
	           $error("Failed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_3[11-j]);
	         end	 
	         end
	         
	         //test case 4: reset being set so that the output is always 0
	@(negedge tb_clk); 
	tb_n_rst = 1'b0;//resetting the outputs to 0
	tb_input_4 = 12'b110110110100;
	tb_output_4 = 12'b000000000000; 
	#(1);
	//tb_n_rst = 1'b1; //enable outputs to change
	$info("Test case 4");
  for (j=0;j<12;j++)
	 begin
	   @ (negedge tb_clk)
	       tb_i = tb_input_4[11-j];
	       #(CHECK_DELAY);
	   //@ (posedge tb_clk)
	     if (tb_o == tb_output_4[11-j])
	       begin
	         $info("Passed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_4[11-j]);
	         end
	       else
	         begin
	           $error("Failed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_4[11-j]);
	         end	 
	         end
	         
	         //test case 5: just a random case with inputs = 7
	@(negedge tb_clk); 
	tb_n_rst = 1'b0;//resetting the outputs to 0
	tb_input_5 = 7'b0110110;
	tb_output_5 = 7'b0000100; 
	#(1);
	tb_n_rst = 1'b1; //enable outputs to change
	$info("Test case 5");
  for (j=0;j<7;j++)
	 begin
	   @ (negedge tb_clk)
	       tb_i = tb_input_5[6-j];
	       #(CHECK_DELAY);
	   //@ (posedge tb_clk)
	     if (tb_o == tb_output_5[6-j])
	       begin
	         $info("Passed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_5[6-j]);
	         end
	       else
	         begin
	           $error("Failed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_5[6-j]);
	         end	 
	         end
	         
	         //test case 6: just a random case with inputs = 4
	@(negedge tb_clk); 
	tb_n_rst = 1'b0;//resetting the outputs to 0
	tb_input_6 = 4'b0110;
	tb_output_6 = 4'b0000; 
	#(1);
	tb_n_rst = 1'b1; //enable outputs to change
	$info("Test case 6");
  for (j=0;j<4;j++)
	 begin
	   @ (negedge tb_clk)
	       tb_i = tb_input_6[3-j];
	       #(CHECK_DELAY);
	   //@ (posedge tb_clk)
	     if (tb_o == tb_output_6[3-j])
	       begin
	         $info("Passed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_6[3-j]);
	         end
	       else
	         begin
	           $error("Failed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_6[3-j]);
	         end	 
	         end
	         
	         //test case 7: just a random case with inputs = 4
	@(negedge tb_clk); 
	tb_n_rst = 1'b0;//resetting the outputs to 0
	tb_input_7 = 4'b1101;
	tb_output_7 = 4'b0001; 
	#(1);
	tb_n_rst = 1'b1; //enable outputs to change
	$info("Test case 7");
  for (j=0;j<4;j++)
	 begin
	   @ (negedge tb_clk)
	       tb_i = tb_input_7[3-j];
	       #(CHECK_DELAY);
	   //@ (posedge tb_clk)
	     if (tb_o == tb_output_7[3-j])
	       begin
	         $info("Passed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_7[3-j]);
	         end
	       else
	         begin
	           $error("Failed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_7[3-j]);
	         end	 
	         end
	         
	         //test case 8: just a random case with inputs = 6
	@(negedge tb_clk); 
	tb_n_rst = 1'b0;//resetting the outputs to 0
	tb_input_8 = 6'b011011;
	tb_output_8 = 6'b000010; 
	#(1);
	tb_n_rst = 1'b1; //enable outputs to change
	$info("Test case 8");
  for (j=0;j<6;j++)
	 begin
	   @ (negedge tb_clk)
	       tb_i = tb_input_8[5-j];
	       #(CHECK_DELAY);
	   //@ (posedge tb_clk)
	     if (tb_o == tb_output_8[5-j])
	       begin
	         $info("Passed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_8[5-j]);
	         end
	       else
	         begin
	           $error("Failed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_8[5-j]);
	         end	 
	         end
	         
	         //test case 9: just a random case with inputs = 10
	@(negedge tb_clk); 
	tb_n_rst = 1'b0;//resetting the outputs to 0
	tb_input_9 = 10'b1101101101;
	tb_output_9 = 10'b0001001001; 
	#(1);
	tb_n_rst = 1'b1; //enable outputs to change
	$info("Test case 9");
  for (j=0;j<10;j++)
	 begin
	   @ (negedge tb_clk)
	       tb_i = tb_input_9[9-j];
	       #(CHECK_DELAY);
	   //@ (posedge tb_clk)
	     if (tb_o == tb_output_9[9-j])
	       begin
	         $info("Passed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_9[9-j]);
	         end
	       else
	         begin
	           $error("Failed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_9[9-j]);
	         end	 
	         end
	         
	         //test case 10: just a random case with inputs = 10
	@(negedge tb_clk); 
	tb_n_rst = 1'b0;//resetting the outputs to 0
	tb_input_10 = 10'b0110100011;
	tb_output_10 = 10'b0000100000; 
	#(1);
	tb_n_rst = 1'b1; //enable outputs to change
	$info("Test case 10");
  for (j=0;j<10;j++)
	 begin
	   @ (negedge tb_clk)
	       tb_i = tb_input_10[9-j];
	       #(CHECK_DELAY);
	   //@ (posedge tb_clk)
	     if (tb_o == tb_output_10[9-j])
	       begin
	         $info("Passed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_10[9-j]);
	         end
	       else
	         begin
	           $error("Failed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_10[9-j]);
	         end	 
	         end
	         
	         //test case 11: just a random case with inputs = 9
	@(negedge tb_clk); 
	tb_n_rst = 1'b0;//resetting the outputs to 0
	tb_input_11 = 9'b000001101;
	tb_output_11 = 9'b000000001; 
	#(1);
	tb_n_rst = 1'b1; //enable outputs to change
	$info("Test case 11");
  for (j=0;j<9;j++)
	 begin
	   @ (negedge tb_clk)
	       tb_i = tb_input_11[8-j];
	       #(CHECK_DELAY);
	   //@ (posedge tb_clk)
	     if (tb_o == tb_output_11[8-j])
	       begin
	         $info("Passed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_11[8-j]);
	         end
	       else
	         begin
	           $error("Failed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_11[8-j]);
	         end	 
	         end
	         
	         //test case 12: just a random case with inputs = 9
	@(negedge tb_clk); 
	tb_n_rst = 1'b0;//resetting the outputs to 0
	tb_input_12 = 9'b011011011;
	tb_output_12 = 9'b000010010; 
	#(1);
	tb_n_rst = 1'b1; //enable outputs to change
	$info("Test case 12");
  for (j=0;j<9;j++)
	 begin
	   @ (negedge tb_clk)
	       tb_i = tb_input_12[8-j];
	       #(CHECK_DELAY);
	   //@ (posedge tb_clk)
	     if (tb_o == tb_output_12[8-j])
	       begin
	         $info("Passed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_12[8-j]);
	         end
	       else
	         begin
	           $error("Failed for input %d and output %d for expected output %d.", tb_i, tb_o, tb_output_12[8-j]);
	         end	 
	         end
	               
	      end
	  endmodule
	  