
module flex_pts_sr_NUM_BITS9_SHIFT_MSB1 ( clk, n_rst, shift_enable, 
        load_enable, parallel_in, serial_out );
  input [8:0] parallel_in;
  input clk, n_rst, shift_enable, load_enable;
  output serial_out;
  wire   n14, n16, n18, n20, n22, n24, n26, n28, n30, n1, n2, n3, n4, n5, n6,
         n7, n8, n9, n10;
  wire   [7:0] f;

  DFFSR \f_reg[0]  ( .D(n30), .CLK(clk), .R(1'b1), .S(n_rst), .Q(f[0]) );
  DFFSR \f_reg[1]  ( .D(n28), .CLK(clk), .R(1'b1), .S(n_rst), .Q(f[1]) );
  DFFSR \f_reg[2]  ( .D(n26), .CLK(clk), .R(1'b1), .S(n_rst), .Q(f[2]) );
  DFFSR \f_reg[3]  ( .D(n24), .CLK(clk), .R(1'b1), .S(n_rst), .Q(f[3]) );
  DFFSR \f_reg[4]  ( .D(n22), .CLK(clk), .R(1'b1), .S(n_rst), .Q(f[4]) );
  DFFSR \f_reg[5]  ( .D(n20), .CLK(clk), .R(1'b1), .S(n_rst), .Q(f[5]) );
  DFFSR \f_reg[6]  ( .D(n18), .CLK(clk), .R(1'b1), .S(n_rst), .Q(f[6]) );
  DFFSR \f_reg[7]  ( .D(n16), .CLK(clk), .R(1'b1), .S(n_rst), .Q(f[7]) );
  DFFSR \f_reg[8]  ( .D(n14), .CLK(clk), .R(1'b1), .S(n_rst), .Q(serial_out)
         );
  INVX1 U2 ( .A(n1), .Y(n30) );
  MUX2X1 U3 ( .B(f[0]), .A(parallel_in[0]), .S(n2), .Y(n1) );
  AND2X1 U4 ( .A(shift_enable), .B(load_enable), .Y(n2) );
  INVX1 U5 ( .A(n3), .Y(n28) );
  MUX2X1 U6 ( .B(f[1]), .A(f[0]), .S(load_enable), .Y(n3) );
  INVX1 U7 ( .A(n4), .Y(n26) );
  MUX2X1 U8 ( .B(f[2]), .A(f[1]), .S(load_enable), .Y(n4) );
  INVX1 U9 ( .A(n5), .Y(n24) );
  MUX2X1 U10 ( .B(f[3]), .A(f[2]), .S(load_enable), .Y(n5) );
  INVX1 U11 ( .A(n6), .Y(n22) );
  MUX2X1 U12 ( .B(f[4]), .A(f[3]), .S(load_enable), .Y(n6) );
  INVX1 U13 ( .A(n7), .Y(n20) );
  MUX2X1 U14 ( .B(f[5]), .A(f[4]), .S(load_enable), .Y(n7) );
  INVX1 U15 ( .A(n8), .Y(n18) );
  MUX2X1 U16 ( .B(f[6]), .A(f[5]), .S(load_enable), .Y(n8) );
  INVX1 U17 ( .A(n9), .Y(n16) );
  MUX2X1 U18 ( .B(f[7]), .A(f[6]), .S(load_enable), .Y(n9) );
  INVX1 U19 ( .A(n10), .Y(n14) );
  MUX2X1 U20 ( .B(serial_out), .A(f[7]), .S(load_enable), .Y(n10) );
endmodule


module flex_pts_sr_9_msb ( clk, n_rst, shift_enable, load_enable, parallel_in, 
        serial_out );
  input [8:0] parallel_in;
  input clk, n_rst, shift_enable, load_enable;
  output serial_out;


  flex_pts_sr_NUM_BITS9_SHIFT_MSB1 CORE ( .clk(clk), .n_rst(n_rst), 
        .shift_enable(shift_enable), .load_enable(load_enable), .parallel_in(
        parallel_in), .serial_out(serial_out) );
endmodule

