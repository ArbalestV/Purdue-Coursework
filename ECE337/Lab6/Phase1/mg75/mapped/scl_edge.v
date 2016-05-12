
module scl_edge ( clk, n_rst, scl, rising_edge_found, falling_edge_found );
  input clk, n_rst, scl;
  output rising_edge_found, falling_edge_found;
  wire   nxt_state, nxt_state2, n4;

  DFFSR nxt_state_reg ( .D(scl), .CLK(clk), .R(1'b1), .S(n_rst), .Q(nxt_state)
         );
  DFFSR nxt_state2_reg ( .D(nxt_state), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        nxt_state2) );
  AND2X1 U8 ( .A(n4), .B(nxt_state), .Y(rising_edge_found) );
  NOR2X1 U9 ( .A(nxt_state), .B(n4), .Y(falling_edge_found) );
  INVX1 U10 ( .A(nxt_state2), .Y(n4) );
endmodule

