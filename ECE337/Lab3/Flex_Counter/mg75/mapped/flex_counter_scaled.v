
module flex_counter_NUM_CNT_BITS9_DW01_inc_0 ( A, SUM );
  input [8:0] A;
  output [8:0] SUM;

  wire   [8:2] carry;

  HAX1 U1_1_7 ( .A(A[7]), .B(carry[7]), .YC(carry[8]), .YS(SUM[7]) );
  HAX1 U1_1_6 ( .A(A[6]), .B(carry[6]), .YC(carry[7]), .YS(SUM[6]) );
  HAX1 U1_1_5 ( .A(A[5]), .B(carry[5]), .YC(carry[6]), .YS(SUM[5]) );
  HAX1 U1_1_4 ( .A(A[4]), .B(carry[4]), .YC(carry[5]), .YS(SUM[4]) );
  HAX1 U1_1_3 ( .A(A[3]), .B(carry[3]), .YC(carry[4]), .YS(SUM[3]) );
  HAX1 U1_1_2 ( .A(A[2]), .B(carry[2]), .YC(carry[3]), .YS(SUM[2]) );
  HAX1 U1_1_1 ( .A(A[1]), .B(A[0]), .YC(carry[2]), .YS(SUM[1]) );
  INVX2 U1 ( .A(A[0]), .Y(SUM[0]) );
  XOR2X1 U2 ( .A(carry[8]), .B(A[8]), .Y(SUM[8]) );
endmodule


module flex_counter_NUM_CNT_BITS9 ( clk, n_rst, count_enable, clear, 
        rollover_val, count_out, rollover_flag );
  input [8:0] rollover_val;
  output [8:0] count_out;
  input clk, n_rst, count_enable, clear;
  output rollover_flag;
  wire   N3, N4, N5, N6, N7, N8, N9, N10, N11, n56, n57, n58, n59, n60, n61,
         n62, n63, n64, n65, n1, n2, n3, n4, n5, n6, n17, n18, n19, n20, n21,
         n22, n23, n24, n25, n26, n27, n28, n29, n30, n31, n32, n33, n34, n35,
         n36, n37, n38, n39, n40, n41, n42, n43, n44, n45, n46, n47, n48, n49,
         n50, n51, n52, n53, n54, n55, n66, n67, n68, n69, n70, n71, n72, n73,
         n74, n75, n76, n77, n78, n79, n80, n81, n82, n83, n84, n85;

  DFFSR \f_reg[0]  ( .D(n65), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[0])
         );
  DFFSR \f_reg[1]  ( .D(n64), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[1])
         );
  DFFSR \f_reg[2]  ( .D(n63), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[2])
         );
  DFFSR \f_reg[3]  ( .D(n62), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[3])
         );
  DFFSR \f_reg[4]  ( .D(n61), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[4])
         );
  DFFSR \f_reg[5]  ( .D(n60), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[5])
         );
  DFFSR \f_reg[6]  ( .D(n59), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[6])
         );
  DFFSR \f_reg[7]  ( .D(n58), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[7])
         );
  DFFSR \f_reg[8]  ( .D(n57), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[8])
         );
  DFFSR rollover_flag_reg ( .D(n56), .CLK(clk), .R(n_rst), .S(1'b1), .Q(
        rollover_flag) );
  flex_counter_NUM_CNT_BITS9_DW01_inc_0 add_31 ( .A(count_out), .SUM({N11, N10, 
        N9, N8, N7, N6, N5, N4, N3}) );
  OAI21X1 U6 ( .A(n1), .B(n2), .C(n3), .Y(n65) );
  NAND2X1 U14 ( .A(N3), .B(n4), .Y(n3) );
  OAI21X1 U15 ( .A(n1), .B(n5), .C(n6), .Y(n64) );
  NAND2X1 U16 ( .A(N4), .B(n4), .Y(n6) );
  OAI21X1 U17 ( .A(n1), .B(n17), .C(n18), .Y(n63) );
  NAND2X1 U18 ( .A(N5), .B(n4), .Y(n18) );
  OAI21X1 U19 ( .A(n1), .B(n19), .C(n20), .Y(n62) );
  NAND2X1 U20 ( .A(N6), .B(n4), .Y(n20) );
  OAI21X1 U21 ( .A(n1), .B(n21), .C(n22), .Y(n61) );
  NAND2X1 U22 ( .A(N7), .B(n4), .Y(n22) );
  OAI21X1 U23 ( .A(n1), .B(n23), .C(n24), .Y(n60) );
  NAND2X1 U24 ( .A(N8), .B(n4), .Y(n24) );
  OAI21X1 U25 ( .A(n1), .B(n25), .C(n26), .Y(n59) );
  NAND2X1 U26 ( .A(N9), .B(n4), .Y(n26) );
  OAI21X1 U27 ( .A(n1), .B(n27), .C(n28), .Y(n58) );
  NAND2X1 U28 ( .A(N10), .B(n4), .Y(n28) );
  INVX1 U29 ( .A(count_out[7]), .Y(n27) );
  OAI21X1 U30 ( .A(n1), .B(n29), .C(n30), .Y(n57) );
  NAND2X1 U31 ( .A(N11), .B(n4), .Y(n30) );
  INVX1 U32 ( .A(count_out[8]), .Y(n29) );
  INVX1 U33 ( .A(n31), .Y(n1) );
  INVX1 U34 ( .A(n32), .Y(n56) );
  AOI22X1 U35 ( .A(n33), .B(n34), .C(rollover_flag), .D(n31), .Y(n32) );
  NOR2X1 U36 ( .A(n35), .B(n36), .Y(n34) );
  OAI21X1 U37 ( .A(n37), .B(n38), .C(n4), .Y(n36) );
  NOR2X1 U38 ( .A(n31), .B(clear), .Y(n4) );
  NOR2X1 U39 ( .A(count_enable), .B(clear), .Y(n31) );
  XOR2X1 U40 ( .A(n21), .B(n39), .Y(n38) );
  INVX1 U41 ( .A(count_out[4]), .Y(n21) );
  INVX1 U42 ( .A(rollover_val[4]), .Y(n37) );
  NAND3X1 U43 ( .A(n40), .B(n41), .C(n42), .Y(n35) );
  XOR2X1 U44 ( .A(n23), .B(n43), .Y(n42) );
  OAI21X1 U45 ( .A(n44), .B(n45), .C(n46), .Y(n43) );
  INVX1 U46 ( .A(count_out[5]), .Y(n23) );
  NAND3X1 U47 ( .A(n46), .B(n25), .C(rollover_val[6]), .Y(n41) );
  XOR2X1 U48 ( .A(n19), .B(n47), .Y(n40) );
  NAND2X1 U49 ( .A(n48), .B(n39), .Y(n47) );
  OAI21X1 U50 ( .A(rollover_val[2]), .B(n49), .C(rollover_val[3]), .Y(n48) );
  INVX1 U51 ( .A(count_out[3]), .Y(n19) );
  NOR2X1 U52 ( .A(n50), .B(n51), .Y(n33) );
  NAND2X1 U53 ( .A(n52), .B(n53), .Y(n51) );
  MUX2X1 U54 ( .B(n2), .A(n54), .S(rollover_val[0]), .Y(n53) );
  OAI21X1 U55 ( .A(count_out[1]), .B(n55), .C(n2), .Y(n54) );
  INVX1 U56 ( .A(rollover_val[1]), .Y(n55) );
  INVX1 U57 ( .A(count_out[0]), .Y(n2) );
  MUX2X1 U58 ( .B(n66), .A(n67), .S(n49), .Y(n52) );
  OAI21X1 U59 ( .A(n68), .B(n5), .C(n69), .Y(n67) );
  XOR2X1 U60 ( .A(n17), .B(rollover_val[2]), .Y(n69) );
  INVX1 U61 ( .A(count_out[2]), .Y(n17) );
  INVX1 U62 ( .A(count_out[1]), .Y(n5) );
  AND2X1 U63 ( .A(rollover_val[1]), .B(rollover_val[0]), .Y(n68) );
  NAND2X1 U64 ( .A(count_out[1]), .B(n70), .Y(n66) );
  XOR2X1 U65 ( .A(rollover_val[2]), .B(count_out[2]), .Y(n70) );
  NAND3X1 U66 ( .A(n71), .B(n72), .C(n73), .Y(n50) );
  MUX2X1 U67 ( .B(n74), .A(n75), .S(n76), .Y(n73) );
  NAND2X1 U68 ( .A(n77), .B(count_out[6]), .Y(n75) );
  MUX2X1 U69 ( .B(n78), .A(count_out[7]), .S(rollover_val[7]), .Y(n77) );
  NAND2X1 U70 ( .A(rollover_val[8]), .B(count_out[7]), .Y(n78) );
  OAI21X1 U71 ( .A(n79), .B(n25), .C(n80), .Y(n74) );
  XOR2X1 U72 ( .A(n81), .B(count_out[7]), .Y(n80) );
  INVX1 U73 ( .A(count_out[6]), .Y(n25) );
  AND2X1 U74 ( .A(n46), .B(rollover_val[6]), .Y(n79) );
  XOR2X1 U75 ( .A(n82), .B(n83), .Y(n72) );
  XOR2X1 U76 ( .A(rollover_val[8]), .B(count_out[8]), .Y(n83) );
  NAND2X1 U77 ( .A(n76), .B(n81), .Y(n82) );
  INVX1 U78 ( .A(rollover_val[7]), .Y(n81) );
  NOR2X1 U79 ( .A(n46), .B(rollover_val[6]), .Y(n76) );
  NAND2X1 U80 ( .A(n44), .B(n45), .Y(n46) );
  INVX1 U81 ( .A(rollover_val[5]), .Y(n45) );
  MUX2X1 U82 ( .B(n44), .A(n84), .S(count_out[4]), .Y(n71) );
  NOR2X1 U83 ( .A(rollover_val[4]), .B(n85), .Y(n84) );
  NOR2X1 U84 ( .A(n39), .B(rollover_val[4]), .Y(n44) );
  INVX1 U85 ( .A(n85), .Y(n39) );
  NOR3X1 U86 ( .A(rollover_val[2]), .B(rollover_val[3]), .C(n49), .Y(n85) );
  OR2X1 U87 ( .A(rollover_val[0]), .B(rollover_val[1]), .Y(n49) );
endmodule


module flex_counter_scaled ( clk, clear, n_rst, count_enable, rollover_val, 
        count_out, rollover_flag );
  input [8:0] rollover_val;
  output [8:0] count_out;
  input clk, clear, n_rst, count_enable;
  output rollover_flag;


  flex_counter_NUM_CNT_BITS9 CORE ( .clk(clk), .n_rst(n_rst), .count_enable(
        count_enable), .clear(clear), .rollover_val(rollover_val), .count_out(
        count_out), .rollover_flag(rollover_flag) );
endmodule

