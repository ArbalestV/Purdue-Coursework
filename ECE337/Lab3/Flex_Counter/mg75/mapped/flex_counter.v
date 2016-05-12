
module flex_counter ( clk, n_rst, count_enable, clear, rollover_val, count_out, 
        rollover_flag );
  input [3:0] rollover_val;
  output [3:0] count_out;
  input clk, n_rst, count_enable, clear;
  output rollover_flag;
  wire   n37, n38, n39, n40, n41, n42, n43, n44, n45, n46, n47, n48, n49, n50,
         n51, n52, n53, n54, n55, n56, n57, n58, n59, n60, n61, n62, n63, n64,
         n65, n66, n67, n68, n69, n70, n71;

  DFFSR \f_reg[0]  ( .D(n41), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[0])
         );
  DFFSR \f_reg[1]  ( .D(n40), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[1])
         );
  DFFSR \f_reg[2]  ( .D(n39), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[2])
         );
  DFFSR \f_reg[3]  ( .D(n38), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[3])
         );
  DFFSR rollover_flag_reg ( .D(n37), .CLK(clk), .R(n_rst), .S(1'b1), .Q(
        rollover_flag) );
  INVX1 U39 ( .A(n42), .Y(n41) );
  MUX2X1 U40 ( .B(n43), .A(n44), .S(count_out[0]), .Y(n42) );
  MUX2X1 U41 ( .B(n45), .A(n46), .S(n47), .Y(n40) );
  MUX2X1 U42 ( .B(n48), .A(n49), .S(count_out[2]), .Y(n39) );
  NAND2X1 U43 ( .A(n50), .B(count_out[1]), .Y(n48) );
  MUX2X1 U44 ( .B(n51), .A(n52), .S(count_out[3]), .Y(n38) );
  INVX1 U45 ( .A(n53), .Y(n52) );
  OAI21X1 U46 ( .A(clear), .B(count_out[2]), .C(n49), .Y(n53) );
  INVX1 U47 ( .A(n54), .Y(n49) );
  OAI21X1 U48 ( .A(count_out[1]), .B(clear), .C(n45), .Y(n54) );
  INVX1 U49 ( .A(n55), .Y(n45) );
  OAI21X1 U50 ( .A(count_out[0]), .B(clear), .C(n56), .Y(n55) );
  INVX1 U51 ( .A(n44), .Y(n56) );
  NAND3X1 U52 ( .A(n50), .B(count_out[1]), .C(count_out[2]), .Y(n51) );
  INVX1 U53 ( .A(n46), .Y(n50) );
  NAND2X1 U54 ( .A(n43), .B(count_out[0]), .Y(n46) );
  OAI21X1 U55 ( .A(n57), .B(n58), .C(n59), .Y(n37) );
  NAND2X1 U56 ( .A(rollover_flag), .B(n44), .Y(n59) );
  NAND3X1 U57 ( .A(n60), .B(n43), .C(n61), .Y(n58) );
  MUX2X1 U58 ( .B(n62), .A(n63), .S(n64), .Y(n61) );
  OAI21X1 U59 ( .A(n65), .B(n47), .C(n66), .Y(n63) );
  AND2X1 U60 ( .A(rollover_val[0]), .B(rollover_val[1]), .Y(n65) );
  NOR2X1 U61 ( .A(rollover_val[3]), .B(rollover_val[2]), .Y(n62) );
  NOR2X1 U62 ( .A(n44), .B(clear), .Y(n43) );
  NOR2X1 U63 ( .A(count_enable), .B(clear), .Y(n44) );
  XOR2X1 U64 ( .A(n67), .B(count_out[3]), .Y(n60) );
  OAI21X1 U65 ( .A(rollover_val[2]), .B(n64), .C(rollover_val[3]), .Y(n67) );
  INVX1 U66 ( .A(n68), .Y(n64) );
  NAND3X1 U67 ( .A(n69), .B(n70), .C(n71), .Y(n57) );
  XOR2X1 U68 ( .A(rollover_val[0]), .B(count_out[0]), .Y(n71) );
  NAND3X1 U69 ( .A(rollover_val[0]), .B(n47), .C(rollover_val[1]), .Y(n70) );
  OAI21X1 U70 ( .A(n66), .B(n47), .C(n68), .Y(n69) );
  NOR2X1 U71 ( .A(rollover_val[0]), .B(rollover_val[1]), .Y(n68) );
  INVX1 U72 ( .A(count_out[1]), .Y(n47) );
  XNOR2X1 U73 ( .A(count_out[2]), .B(rollover_val[2]), .Y(n66) );
endmodule

