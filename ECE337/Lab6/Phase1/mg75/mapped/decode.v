
module decode ( clk, n_rst, scl, sda_in, starting_byte, rw_mode, address_match, 
        stop_found, start_found );
  input [7:0] starting_byte;
  input clk, n_rst, scl, sda_in;
  output rw_mode, address_match, stop_found, start_found;
  wire   nxt_state, nxt_state2, b, d, n16, n17, n18, n19, n20, n21, n22, n23,
         n24, n25;
  assign rw_mode = starting_byte[0];

  DFFSR nxt_state_reg ( .D(sda_in), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        nxt_state) );
  DFFSR nxt_state2_reg ( .D(nxt_state), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        nxt_state2) );
  DFFSR b_reg ( .D(scl), .CLK(clk), .R(1'b1), .S(n_rst), .Q(b) );
  DFFSR d_reg ( .D(b), .CLK(clk), .R(1'b1), .S(n_rst), .Q(d) );
  NOR2X1 U20 ( .A(n16), .B(n17), .Y(stop_found) );
  NAND2X1 U21 ( .A(nxt_state), .B(d), .Y(n17) );
  NAND2X1 U22 ( .A(b), .B(n18), .Y(n16) );
  INVX1 U23 ( .A(nxt_state2), .Y(n18) );
  NOR2X1 U24 ( .A(n19), .B(n20), .Y(start_found) );
  NAND2X1 U25 ( .A(nxt_state2), .B(d), .Y(n20) );
  NAND2X1 U26 ( .A(b), .B(n21), .Y(n19) );
  INVX1 U27 ( .A(nxt_state), .Y(n21) );
  NOR2X1 U28 ( .A(n22), .B(n23), .Y(address_match) );
  NAND3X1 U29 ( .A(starting_byte[6]), .B(starting_byte[5]), .C(
        starting_byte[7]), .Y(n23) );
  NAND3X1 U30 ( .A(starting_byte[4]), .B(n24), .C(n25), .Y(n22) );
  NOR2X1 U31 ( .A(starting_byte[3]), .B(starting_byte[2]), .Y(n25) );
  INVX1 U32 ( .A(starting_byte[1]), .Y(n24) );
endmodule

