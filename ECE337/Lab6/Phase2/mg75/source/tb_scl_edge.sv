`timescale 1ns / 10ps
module tb_scl_edge();
  reg tb_clk;
  reg tb_n_rst;
  reg tb_scl;
  reg tb_rising_edge_found;
  reg tb_falling_edge_found;
  localparam	CLK_PERIOD	= 10;
  localparam	SCL_PERIOD	= 300;
  scl_edge DUT
  (
    .clk(tb_clk),
    .n_rst(tb_n_rst),
    .scl(tb_scl),
    .rising_edge_found(tb_rising_edge_found),
    .falling_edge_found(tb_falling_edge_found)
    );
    // System Clock generation block
	always
	begin
		tb_clk = 1'b0;
		#(CLK_PERIOD/2.0);
		tb_clk = 1'b1;
		#(CLK_PERIOD/2.0);
	end
	// SCL Clock generation block
	always
	begin
		tb_scl = 1'b0;
		#(SCL_PERIOD/3.0);
		tb_scl = 1'b1;
		#(SCL_PERIOD/3.0);
		tb_scl = 1'b0;
		#(SCL_PERIOD/3.0);
	end
	initial begin
	 // @(negedge tb_clk);
	  tb_n_rst = 1'b1;
	  #(CLK_PERIOD/8.0);
	  tb_n_rst = 1'b0;//being reset
	  #(CLK_PERIOD/8.0);
	  tb_n_rst = 1'b1;//now reset if off
	end
	
	always@(negedge tb_scl)//basically now since we are in the negative edge of the scl input, that means its a falling condition
	begin
	  @(posedge tb_clk);
	  @(posedge tb_clk);
	  //@(posedge tb_clk);
	  //#(CLK_PERIOD/4.0);
	  #(0.1);
	  if ((tb_falling_edge_found==1'b1))
	    $info("Correct for fall edge.");
	  else
	    $error("Wrong for fall edge.");
	  end
	 always@(posedge tb_scl)//basically now since we are in the positive edge of the scl input, that means its a rising condition
	 begin
	  @(posedge tb_clk);
	  @(posedge tb_clk);
	  //@(posedge tb_clk);
	  //#(CLK_PERIOD/4.0);
	  #(0.1);
	  if ((tb_rising_edge_found == 1'b1))
	    $info("Correct for rise edge.");
	  else
	    $error("Wrong for rise edge.");
	  end
	  endmodule
	  
	  
	  
	  
	
	
  
    