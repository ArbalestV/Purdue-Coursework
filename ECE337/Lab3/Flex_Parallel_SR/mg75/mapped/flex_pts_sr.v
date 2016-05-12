
module flex_pts_sr ( clk, n_rst, shift_enable, load_enable, parallel_in, 
        serial_out );
  input [3:0] parallel_in;
  input clk, n_rst, shift_enable, load_enable;
  output serial_out;
  wire   n9, n11, n13, n15, n16, n17, n18, n19, n20;
  wire   [2:0] f;

  DFFSR \f_reg[0]  ( .D(n15), .CLK(clk), .R(1'b1), .S(n_rst), .Q(f[0]) );
  DFFSR \f_reg[1]  ( .D(n13), .CLK(clk), .R(1'b1), .S(n_rst), .Q(f[1]) );
  DFFSR \f_reg[2]  ( .D(n11), .CLK(clk), .R(1'b1), .S(n_rst), .Q(f[2]) );
  DFFSR \f_reg[3]  ( .D(n9), .CLK(clk), .R(1'b1), .S(n_rst), .Q(serial_out) );
  INVX1 U17 ( .A(n16), .Y(n9) );
  MUX2X1 U18 ( .B(serial_out), .A(f[2]), .S(load_enable), .Y(n16) );
  INVX1 U19 ( .A(n17), .Y(n15) );
  MUX2X1 U20 ( .B(f[0]), .A(parallel_in[0]), .S(n18), .Y(n17) );
  AND2X1 U21 ( .A(shift_enable), .B(load_enable), .Y(n18) );
  INVX1 U22 ( .A(n19), .Y(n13) );
  MUX2X1 U23 ( .B(f[1]), .A(f[0]), .S(load_enable), .Y(n19) );
  INVX1 U24 ( .A(n20), .Y(n11) );
  MUX2X1 U25 ( .B(f[2]), .A(f[1]), .S(load_enable), .Y(n20) );
endmodule

