
module mealy ( clk, n_rst, i, o );
  input clk, n_rst, i;
  output o;
  wire   n8, n9, n10;
  wire   [1:0] state;
  wire   [1:0] nextstate;

  DFFSR \state_reg[0]  ( .D(nextstate[0]), .CLK(clk), .R(n_rst), .S(1'b1), .Q(
        state[0]) );
  DFFSR \state_reg[1]  ( .D(nextstate[1]), .CLK(clk), .R(n_rst), .S(1'b1), .Q(
        state[1]) );
  INVX1 U12 ( .A(n8), .Y(o) );
  MUX2X1 U13 ( .B(n9), .A(state[0]), .S(state[1]), .Y(nextstate[1]) );
  NAND2X1 U14 ( .A(state[0]), .B(i), .Y(n9) );
  OAI21X1 U15 ( .A(state[0]), .B(n10), .C(n8), .Y(nextstate[0]) );
  NAND3X1 U16 ( .A(state[0]), .B(i), .C(state[1]), .Y(n8) );
  XNOR2X1 U17 ( .A(i), .B(state[1]), .Y(n10) );
endmodule

