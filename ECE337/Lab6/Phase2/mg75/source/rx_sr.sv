module rx_sr
  (
    input wire clk,
    input wire n_rst,
    input wire sda_in,
    input wire rx_enable,
    input wire rising_edge_found,
    output wire [7:0] rx_data
    );
    wire se;
    assign se = rx_enable & rising_edge_found;
    flex_stp_sr #(8,1) SHIFT_REGISTER(.clk(clk), .n_rst(n_rst), .shift_enable(se), .serial_in(sda_in), .parallel_out(rx_data));
  endmodule
  
  