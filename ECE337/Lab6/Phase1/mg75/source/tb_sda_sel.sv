`timescale 1ns / 10ps
module tb_sda_sel();
  reg tb_tx_out;
  reg tb_clk;
  reg [1:0] tb_sda_mode;
  reg tb_sda_out;
  localparam CLK_PERIOD = 10;
  sda_sel DUT
  (
    .tx_out(tb_tx_out),
    .sda_mode(tb_sda_mode),
    .sda_out(tb_sda_out)
    );
    // System Clock generation block
	always
	begin
		tb_clk = 1'b0;
		#(CLK_PERIOD/2.0);
		tb_clk = 1'b1;
		#(CLK_PERIOD/2.0);
	end
	initial begin
	  //test case 1
	@(negedge tb_clk);
	tb_tx_out = 1'b1;
  tb_sda_mode = 2'b00;
	$info("Test Case 1");
	@ (posedge tb_clk)
	 #(CLK_PERIOD/8);
	    if (tb_sda_out == 1'b1)
	     begin
	       $info("Passed");
	     end
	    else
	     begin
	       $error("Failed");
	     end	    
	//test case 2
	@(negedge tb_clk);
	tb_tx_out = 1'b1;
  tb_sda_mode = 2'b01;
	$info("Test Case 2");
	@ (posedge tb_clk)
	 #(CLK_PERIOD/8);
	    if (tb_sda_out == 1'b0)
	     begin
	       $info("Passed");
	     end
	    else
	     begin
	       $error("Failed");
	     end	    
	//test case 3
	@(negedge tb_clk);
	tb_tx_out = 1'b1;
  tb_sda_mode = 2'b10;
	$info("Test Case 3");
	@ (posedge tb_clk)
	 #(CLK_PERIOD/8);
	    if (tb_sda_out == 1'b1)
	     begin
	       $info("Passed");
	     end
	    else
	     begin
	       $error("Failed");
	     end   
	 //test case 4
	@(negedge tb_clk);
	tb_tx_out = 1'b1;
  tb_sda_mode = 2'b11;
	$info("Test Case 4");
	@ (posedge tb_clk)
	 #(CLK_PERIOD/8);
	    if (tb_sda_out == 1'b1)
	     begin
	       $info("Passed");
	     end
	    else
	     begin
	       $error("Failed");
	     end
	  //test case 5
	@(negedge tb_clk);
	tb_tx_out = 1'b0;
  tb_sda_mode = 2'b00;
	$info("Test Case 5");
	@ (posedge tb_clk)
	 #(CLK_PERIOD/8);
	    if (tb_sda_out == 1'b1)
	     begin
	       $info("Passed");
	     end
	    else
	     begin
	       $error("Failed");
	     end	    
	//test case 6
	@(negedge tb_clk);
	tb_tx_out = 1'b0;
  tb_sda_mode = 2'b01;
	$info("Test Case 6");
	@ (posedge tb_clk)
	 #(CLK_PERIOD/8);
	    if (tb_sda_out == 1'b0)
	     begin
	       $info("Passed");
	     end
	    else
	     begin
	       $error("Failed");
	     end	    
	//test case 7
	@(negedge tb_clk);
	tb_tx_out = 1'b0;
  tb_sda_mode = 2'b10;
	$info("Test Case 7");
	@ (posedge tb_clk)
	 #(CLK_PERIOD/8);
	    if (tb_sda_out == 1'b1)
	     begin
	       $info("Passed");
	     end
	    else
	     begin
	       $error("Failed");
	     end   
	 //test case 8
	@(negedge tb_clk);
	tb_tx_out = 1'b0;
  tb_sda_mode = 2'b11;
	$info("Test Case 8");
	@ (posedge tb_clk)
	 #(CLK_PERIOD/8);
	    if (tb_sda_out == 1'b0)
	     begin
	       $info("Passed");
	     end
	    else
	     begin
	       $error("Failed");
	     end	 
	  end
	  endmodule
	         