module sr_9bit
  (
    input wire clk,
    input wire n_rst,
    input wire shift_strobe,
    input wire serial_in,
    output wire [7:0] packet_data,
    output wire stop_bit
    );
    reg [8:0] tmp;
  flex_stp_sr #(9,0) SHIFT_BLOCK(.clk(clk), .n_rst(n_rst), .shift_enable(shift_strobe), .serial_in(serial_in), .parallel_out(tmp));
  assign packet_data = tmp[7:0];
  assign stop_bit = tmp[8];
endmodule