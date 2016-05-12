
module flex_pts_sr_NUM_BITS4_SHIFT_MSB0 ( clk, n_rst, shift_enable, 
        load_enable, parallel_in, serial_out );
  input [3:0] parallel_in;
  input clk, n_rst, shift_enable, load_enable;
  output serial_out;
  wire   n9, n11, n13, n15, n1, n2, n3, n4, n5;
  wire   [3:1] f;

  DFFSR \f_reg[3]  ( .D(n15), .CLK(clk), .R(1'b1), .S(n_rst), .Q(f[3]) );
  DFFSR \f_reg[2]  ( .D(n13), .CLK(clk), .R(1'b1), .S(n_rst), .Q(f[2]) );
  DFFSR \f_reg[1]  ( .D(n11), .CLK(clk), .R(1'b1), .S(n_rst), .Q(f[1]) );
  DFFSR \f_reg[0]  ( .D(n9), .CLK(clk), .R(1'b1), .S(n_rst), .Q(serial_out) );
  INVX1 U2 ( .A(n1), .Y(n9) );
  MUX2X1 U3 ( .B(serial_out), .A(f[1]), .S(load_enable), .Y(n1) );
  INVX1 U4 ( .A(n2), .Y(n15) );
  MUX2X1 U5 ( .B(f[3]), .A(parallel_in[3]), .S(n3), .Y(n2) );
  AND2X1 U6 ( .A(shift_enable), .B(load_enable), .Y(n3) );
  INVX1 U7 ( .A(n4), .Y(n13) );
  MUX2X1 U8 ( .B(f[2]), .A(f[3]), .S(load_enable), .Y(n4) );
  INVX1 U9 ( .A(n5), .Y(n11) );
  MUX2X1 U10 ( .B(f[1]), .A(f[2]), .S(load_enable), .Y(n5) );
endmodule


module flex_pts_sr_4_lsb ( clk, n_rst, shift_enable, load_enable, parallel_in, 
        serial_out );
  input [3:0] parallel_in;
  input clk, n_rst, shift_enable, load_enable;
  output serial_out;


  flex_pts_sr_NUM_BITS4_SHIFT_MSB0 CORE ( .clk(clk), .n_rst(n_rst), 
        .shift_enable(shift_enable), .load_enable(load_enable), .parallel_in(
        parallel_in), .serial_out(serial_out) );
endmodule

