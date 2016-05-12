
module flex_stp_sr ( clk, n_rst, shift_enable, serial_in, parallel_out );
  output [3:0] parallel_out;
  input clk, n_rst, shift_enable, serial_in;
  wire   n7, n9, n11, n13, n14, n15, n16, n17;

  DFFSR \f_reg[0]  ( .D(n13), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[0]) );
  DFFSR \f_reg[1]  ( .D(n11), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[1]) );
  DFFSR \f_reg[2]  ( .D(n9), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[2]) );
  DFFSR \f_reg[3]  ( .D(n7), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[3]) );
  MUX2X1 U15 ( .B(n14), .A(n15), .S(shift_enable), .Y(n9) );
  MUX2X1 U16 ( .B(n16), .A(n14), .S(shift_enable), .Y(n7) );
  INVX1 U17 ( .A(parallel_out[2]), .Y(n14) );
  MUX2X1 U18 ( .B(n17), .A(n16), .S(shift_enable), .Y(n13) );
  INVX1 U19 ( .A(parallel_out[3]), .Y(n16) );
  MUX2X1 U20 ( .B(n15), .A(n17), .S(shift_enable), .Y(n11) );
  INVX1 U21 ( .A(parallel_out[0]), .Y(n17) );
  INVX1 U22 ( .A(parallel_out[1]), .Y(n15) );
endmodule

