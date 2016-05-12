module i2c_slave
  (
    input wire clk,
    input wire n_rst,
    input wire scl,
    input wire sda_in,
    output reg sda_out,
    input wire write_enable,
    input wire [7:0] write_data,
    output reg fifo_empty,
    output reg fifo_full
    );
    reg rising_edge_found;
    reg falling_edge_found;
    scl_edge edge_det(.clk(clk),.n_rst(n_rst),.scl(scl),.rising_edge_found(rising_edge_found),.falling_edge_found(falling_edge_found));
    reg rw_mode;
    reg address_match;
    reg stop_found;
    reg start_found;
    reg [7:0] rx_data;
    decode decoder(.clk(clk),.n_rst(n_rst),.scl(scl),.sda_in(sda_in),.starting_byte(rx_data),.rw_mode(rw_mode),.address_match(address_match),.stop_found(stop_found),.start_found(start_found));
    reg rx_enable;
    rx_sr rx_shift(.clk(clk),.n_rst(n_rst),.sda_in(sda_in),.rising_edge_found(rising_edge_found),.rx_enable(rx_enable),.rx_data(rx_data));
    reg [1:0] sda_mode;
    reg tx_out;
    sda_sel select_block(.tx_out(tx_out),.sda_mode(sda_mode),.sda_out(sda_out));
    reg tx_enable;
    reg load_data;
    reg [7:0] read_data;
    reg read_enable;
    tx_fifo fifo(.clk(clk),.n_rst(n_rst),.read_enable(read_enable),.read_data(read_data),.fifo_empty(fifo_empty),.fifo_full(fifo_full),.write_enable(write_enable),.write_data(write_data));
    tx_sr tx_shift(.clk(clk),.n_rst(n_rst),.tx_out(tx_out),.falling_edge_found(falling_edge_found),.tx_enable(tx_enable),.tx_data(read_data),.load_data(load_data));
    reg byte_received;
    reg ack_prep;
    reg check_ack;
    reg ack_done;
    timer timer_block(.clk(clk),.n_rst(n_rst),.rising_edge_found(rising_edge_found),.falling_edge_found(falling_edge_found),.stop_found(stoop_found),.start_found(start_found),.byte_received(byte_received),.ack_prep(ack_prep),.check_ack(check_ack),.ack_done(ack_done));
    controller slv_controller(.clk(clk),.n_rst(n_rst),.stop_found(stop_found),.start_found(start_found),.byte_received(byte_received),.ack_prep(ack_prep),.check_ack(check_ack),.ack_done(ack_done),
    .rw_mode(rw_mode),.address_match(address_match),.sda_in(sda_in),.rx_enable(rx_enable),.tx_enable(tx_enable),.read_enable(read_enable),.sda_mode(sda_mode),.load_data(load_data));
  endmodule
  
    
    
    