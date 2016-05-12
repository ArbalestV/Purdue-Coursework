`timescale 1ns / 10ps
module tb_decode();
  reg tb_n_rst;
  reg tb_clk;
  reg tb_scl;
  reg tb_sda_in;
  reg [7:0] tb_starting_byte;
  reg tb_rw_mode;
  reg tb_address_match;
  reg tb_stop_found;
  reg tb_start_found;
  localparam CLK_PERIOD = 10;
  localparam SCL_PERIOD = 300;
  decode DUT
  (
    .clk(tb_clk),
    .n_rst(tb_n_rst),
    .scl(tb_scl),
    .sda_in(tb_sda_in),
    .starting_byte(tb_starting_byte),
    .rw_mode(tb_rw_mode),
    .address_match(tb_address_match),
    .stop_found(tb_stop_found),
    .start_found(tb_start_found)
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
	reg nxt_state, cur_state, cur_state2, nxt_state2, a, b, c, d;
	initial begin
	  tb_n_rst = 1'b1;
	  #(CLK_PERIOD/8.0);
	  tb_n_rst = 1'b0;
	  #(CLK_PERIOD/8.0);
	  tb_n_rst = 1'b1;
	  #(CLK_PERIOD/8.0);
	  
	  @(negedge tb_clk);
	  tb_scl = 1'b1;
	  tb_starting_byte = 8'b11110000;
	  tb_sda_in = 1'b0;
	  @(posedge tb_clk);
	  #(CLK_PERIOD/8.0);
	  tb_scl = 1'b1;
	  tb_sda_in = 1'b1;
	  if(tb_stop_found == 1'b1)
	    $info("Stop case passed.");
	  else
	    $error("Stop case failed.");
	  if(tb_start_found == 1'b0)
	    $info("Start case passed.");
	  else
	    $error("Start case failed."); 
	  #(0.1);
	  if(tb_address_match == 1'b1)
	    $info("Address match.");
	  else
	    $error("Address not match.");
	  if (tb_rw_mode == 1'b0)
	    $info("Read/Write passed.");
	  else
	    $error("Read/Write failed.");
	   #(0.1)
	   tb_starting_byte = 8'b10101011;
	   if(tb_address_match == 1'b1)
	    $info("Failed address.");
	  else
	    $error("Passed address.");
	  if (tb_rw_mode == 1'b1)
	    $info("Read/Write passed.");
	  else
	    $error("Read/Write failed.");
	  
	  @(negedge tb_clk);  
	  tb_sda_in = 1'b1; 
	  tb_starting_byte = 8'b11110000;
	  tb_scl = 1'b1; 
	  @(posedge tb_clk);
	  #(CLK_PERIOD/8.0);
	  tb_scl = 1'b1;
	  tb_sda_in = 1'b0;
	  if(tb_stop_found == 1'b0)
	    $info("Stop case passed.");
	  else
	    $error("Stop case failed.");
	  if(tb_start_found == 1'b1)
	    $info("Start case passed.");
	  else
	    $error("Start case failed."); 
	  #(0.1);
	  if(tb_address_match == 1'b1)
	    $info("Address match.");
	  else
	    $error("Address not match.");
	  if (tb_rw_mode == 1'b0)
	    $info("Read/Write passed.");
	  else
	    $error("Read/Write failed.");
	   #(0.1)
	   tb_starting_byte = 8'b01001010;
	   if(tb_address_match == 1'b1)
	    $info("Failed address.");
	  else
	    $error("Passed address.");
	  if (tb_rw_mode == 1'b1)
	    $info("Read/Write failed.");
	  else
	    $error("Read/Write passed.");
	    
	    @(negedge tb_clk);
	    tb_scl = 1'b0;
	    tb_sda_in = 1'b1; 
	    tb_starting_byte = 8'b11110000;
	    @(posedge tb_clk);
	  #(CLK_PERIOD/8.0);
	  tb_scl = 1'b1;
	  tb_sda_in = 1'b0;
	  if(tb_stop_found == 1'b0)
	    $info("Stop case passed.");
	  else
	    $error("Stop case failed.");
	  if(tb_start_found == 1'b0)
	    $info("Start case passed.");
	  else
	    $error("Start case failed."); 
	  #(0.1);
	  if(tb_address_match == 1'b1)
	    $info("Address match.");
	  else
	    $error("Address not match.");
	  if (tb_rw_mode == 1'b0)
	    $info("Read/Write passed.");
	  else
	    $error("Read/Write failed.");
	    
	    
	    @(negedge tb_clk);
	    tb_scl = 1'b1;
	    tb_sda_in = 1'b1; 
	    tb_starting_byte = 8'b11110000;
	    @(posedge tb_clk);
	  #(CLK_PERIOD/8.0);
	  tb_scl = 1'b0;
	  tb_sda_in = 1'b0;
	  if(tb_stop_found == 1'b0)
	    $info("Stop case passed.");
	  else
	    $error("Stop case failed.");
	  if(tb_start_found == 1'b0)
	    $info("Start case passed.");
	  else
	    $error("Start case failed."); 
	  #(0.1);
	  if(tb_address_match == 1'b1)
	    $info("Address match.");
	  else
	    $error("Address not match.");
	  if (tb_rw_mode == 1'b0)
	    $info("Read/Write passed.");
	  else
	    $error("Read/Write failed.");
	    
	    
	    end
	    endmodule
	  
	