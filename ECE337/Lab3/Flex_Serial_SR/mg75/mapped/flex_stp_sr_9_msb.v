
module flex_stp_sr_NUM_BITS9_SHIFT_MSB1 ( clk, n_rst, shift_enable, serial_in, 
        parallel_out );
  output [8:0] parallel_out;
  input clk, n_rst, shift_enable, serial_in;
  wire   n12, n14, n16, n18, n20, n22, n24, n26, n28, n1, n2, n3, n4, n5, n6,
         n7, n8, n9;

  DFFSR \f_reg[0]  ( .D(n28), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[0]) );
  DFFSR \f_reg[1]  ( .D(n26), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[1]) );
  DFFSR \f_reg[2]  ( .D(n24), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[2]) );
  DFFSR \f_reg[3]  ( .D(n22), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[3]) );
  DFFSR \f_reg[4]  ( .D(n20), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[4]) );
  DFFSR \f_reg[5]  ( .D(n18), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[5]) );
  DFFSR \f_reg[6]  ( .D(n16), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[6]) );
  DFFSR \f_reg[7]  ( .D(n14), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[7]) );
  DFFSR \f_reg[8]  ( .D(n12), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[8]) );
  NOR2X1 U2 ( .A(shift_enable), .B(n1), .Y(n28) );
  MUX2X1 U3 ( .B(n2), .A(n1), .S(shift_enable), .Y(n26) );
  INVX1 U4 ( .A(parallel_out[0]), .Y(n1) );
  MUX2X1 U5 ( .B(n3), .A(n2), .S(shift_enable), .Y(n24) );
  INVX1 U6 ( .A(parallel_out[1]), .Y(n2) );
  MUX2X1 U7 ( .B(n4), .A(n3), .S(shift_enable), .Y(n22) );
  INVX1 U8 ( .A(parallel_out[2]), .Y(n3) );
  MUX2X1 U9 ( .B(n5), .A(n4), .S(shift_enable), .Y(n20) );
  INVX1 U10 ( .A(parallel_out[3]), .Y(n4) );
  MUX2X1 U11 ( .B(n6), .A(n5), .S(shift_enable), .Y(n18) );
  INVX1 U12 ( .A(parallel_out[4]), .Y(n5) );
  INVX1 U13 ( .A(parallel_out[5]), .Y(n6) );
  INVX1 U14 ( .A(n7), .Y(n16) );
  MUX2X1 U15 ( .B(parallel_out[6]), .A(parallel_out[5]), .S(shift_enable), .Y(
        n7) );
  INVX1 U16 ( .A(n8), .Y(n14) );
  MUX2X1 U17 ( .B(parallel_out[7]), .A(parallel_out[6]), .S(shift_enable), .Y(
        n8) );
  INVX1 U18 ( .A(n9), .Y(n12) );
  MUX2X1 U19 ( .B(parallel_out[8]), .A(parallel_out[7]), .S(shift_enable), .Y(
        n9) );
endmodule


module flex_stp_sr_9_msb ( clk, n_rst, serial_in, shift_enable, parallel_out
 );
  output [8:0] parallel_out;
  input clk, n_rst, serial_in, shift_enable;


  flex_stp_sr_NUM_BITS9_SHIFT_MSB1 CORE ( .clk(clk), .n_rst(n_rst), 
        .shift_enable(shift_enable), .serial_in(serial_in), .parallel_out(
        parallel_out) );
endmodule

