module timer
  (
    input wire clk,
    input wire n_rst,
    input wire enable_timer,
    output reg shift_strobe,
    output reg packet_done
    );
  flex_counter CTR1(.clk(clk),.n_rst(n_rst),.count_enable(enable_timer),.clear(packet_done),.rollover_val(4'b1010),.rollover_flag(shift_strobe)); //wait until 10 clock cycles
	flex_counter CTR2(.clk(clk), .n_rst(n_rst), .count_enable(shift_strobe), .clear(packet_done), .rollover_val(4'b1001), .rollover_flag(packet_done));
	endmodule
	