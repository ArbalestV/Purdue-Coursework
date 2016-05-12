
module scl_edge ( clk, n_rst, scl, rising_edge_found, falling_edge_found );
  input clk, n_rst, scl;
  output rising_edge_found, falling_edge_found;
  wire   nxt_state, nxt_state2, n3;

  DFFSR nxt_state_reg ( .D(scl), .CLK(clk), .R(1'b1), .S(n_rst), .Q(nxt_state)
         );
  DFFSR nxt_state2_reg ( .D(nxt_state), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        nxt_state2) );
  AND2X2 U5 ( .A(n3), .B(nxt_state), .Y(rising_edge_found) );
  NOR2X1 U7 ( .A(nxt_state), .B(n3), .Y(falling_edge_found) );
  INVX2 U6 ( .A(nxt_state2), .Y(n3) );
endmodule


module decode ( clk, n_rst, scl, sda_in, starting_byte, rw_mode, address_match, 
        stop_found, start_found );
  input [7:0] starting_byte;
  input clk, n_rst, scl, sda_in;
  output rw_mode, address_match, stop_found, start_found;
  wire   nxt_state, nxt_state2, b, d, n8, n9, n10, n11, n12, n13, n14, n5, n6,
         n7;
  assign rw_mode = starting_byte[0];

  DFFSR nxt_state_reg ( .D(sda_in), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        nxt_state) );
  DFFSR nxt_state2_reg ( .D(nxt_state), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        nxt_state2) );
  DFFSR b_reg ( .D(scl), .CLK(clk), .R(1'b1), .S(n_rst), .Q(b) );
  DFFSR d_reg ( .D(b), .CLK(clk), .R(1'b1), .S(n_rst), .Q(d) );
  NOR2X1 U10 ( .A(n8), .B(n9), .Y(stop_found) );
  NAND2X1 U11 ( .A(nxt_state), .B(d), .Y(n9) );
  NAND2X1 U12 ( .A(b), .B(n7), .Y(n8) );
  NOR2X1 U13 ( .A(n10), .B(n11), .Y(start_found) );
  NAND2X1 U14 ( .A(nxt_state2), .B(d), .Y(n11) );
  NAND2X1 U15 ( .A(b), .B(n6), .Y(n10) );
  NOR2X1 U16 ( .A(n12), .B(n13), .Y(address_match) );
  NAND3X1 U17 ( .A(starting_byte[6]), .B(starting_byte[5]), .C(
        starting_byte[7]), .Y(n13) );
  NAND3X1 U18 ( .A(starting_byte[4]), .B(n5), .C(n14), .Y(n12) );
  NOR2X1 U19 ( .A(starting_byte[3]), .B(starting_byte[2]), .Y(n14) );
  INVX2 U7 ( .A(starting_byte[1]), .Y(n5) );
  INVX2 U8 ( .A(nxt_state), .Y(n6) );
  INVX2 U9 ( .A(nxt_state2), .Y(n7) );
endmodule


module flex_stp_sr_NUM_BITS8_SHIFT_MSB1 ( clk, n_rst, shift_enable, serial_in, 
        parallel_out );
  output [7:0] parallel_out;
  input clk, n_rst, shift_enable, serial_in;
  wire   n3, n10, n12, n14, n16, n18, n20, n22, n24, n26, n1, n2, n4, n5, n6,
         n7, n8, n9;

  DFFSR \f_reg[0]  ( .D(n26), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[0]) );
  DFFSR \f_reg[1]  ( .D(n24), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[1]) );
  DFFSR \f_reg[2]  ( .D(n22), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[2]) );
  DFFSR \f_reg[3]  ( .D(n20), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[3]) );
  DFFSR \f_reg[4]  ( .D(n18), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[4]) );
  DFFSR \f_reg[5]  ( .D(n16), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[5]) );
  DFFSR \f_reg[6]  ( .D(n14), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[6]) );
  DFFSR \f_reg[7]  ( .D(n12), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[7]) );
  OAI21X1 U2 ( .A(n8), .B(n9), .C(n3), .Y(n12) );
  NAND2X1 U3 ( .A(parallel_out[7]), .B(n9), .Y(n3) );
  OAI22X1 U4 ( .A(shift_enable), .B(n8), .C(n9), .D(n7), .Y(n14) );
  OAI22X1 U6 ( .A(shift_enable), .B(n7), .C(n9), .D(n6), .Y(n16) );
  OAI22X1 U8 ( .A(shift_enable), .B(n6), .C(n9), .D(n5), .Y(n18) );
  OAI22X1 U10 ( .A(shift_enable), .B(n5), .C(n9), .D(n4), .Y(n20) );
  OAI22X1 U12 ( .A(shift_enable), .B(n4), .C(n9), .D(n2), .Y(n22) );
  OAI22X1 U14 ( .A(shift_enable), .B(n2), .C(n9), .D(n1), .Y(n24) );
  OAI21X1 U17 ( .A(shift_enable), .B(n1), .C(n10), .Y(n26) );
  NAND2X1 U18 ( .A(serial_in), .B(shift_enable), .Y(n10) );
  INVX2 U5 ( .A(parallel_out[0]), .Y(n1) );
  INVX2 U7 ( .A(parallel_out[1]), .Y(n2) );
  INVX2 U9 ( .A(parallel_out[2]), .Y(n4) );
  INVX2 U11 ( .A(parallel_out[3]), .Y(n5) );
  INVX2 U13 ( .A(parallel_out[4]), .Y(n6) );
  INVX2 U15 ( .A(parallel_out[5]), .Y(n7) );
  INVX2 U16 ( .A(parallel_out[6]), .Y(n8) );
  INVX2 U19 ( .A(shift_enable), .Y(n9) );
endmodule


module rx_sr ( clk, n_rst, sda_in, rx_enable, rising_edge_found, rx_data );
  output [7:0] rx_data;
  input clk, n_rst, sda_in, rx_enable, rising_edge_found;
  wire   se;

  AND2X2 U1 ( .A(rx_enable), .B(rising_edge_found), .Y(se) );
  flex_stp_sr_NUM_BITS8_SHIFT_MSB1 SHIFT_REGISTER ( .clk(clk), .n_rst(n_rst), 
        .shift_enable(se), .serial_in(sda_in), .parallel_out(rx_data) );
endmodule


module sda_sel ( tx_out, sda_mode, sda_out );
  input [1:0] sda_mode;
  input tx_out;
  output sda_out;
  wire   n1;

  NAND2X1 U3 ( .A(sda_mode[0]), .B(n1), .Y(sda_out) );
  NAND2X1 U4 ( .A(tx_out), .B(sda_mode[1]), .Y(n1) );
endmodule


module fiforam ( wclk, wenable, waddr, raddr, wdata, rdata );
  input [2:0] waddr;
  input [2:0] raddr;
  input [7:0] wdata;
  output [7:0] rdata;
  input wclk, wenable;
  wire   \fiforeg[0][7] , \fiforeg[0][6] , \fiforeg[0][5] , \fiforeg[0][4] ,
         \fiforeg[0][3] , \fiforeg[0][2] , \fiforeg[0][1] , \fiforeg[0][0] ,
         \fiforeg[1][7] , \fiforeg[1][6] , \fiforeg[1][5] , \fiforeg[1][4] ,
         \fiforeg[1][3] , \fiforeg[1][2] , \fiforeg[1][1] , \fiforeg[1][0] ,
         \fiforeg[2][7] , \fiforeg[2][6] , \fiforeg[2][5] , \fiforeg[2][4] ,
         \fiforeg[2][3] , \fiforeg[2][2] , \fiforeg[2][1] , \fiforeg[2][0] ,
         \fiforeg[3][7] , \fiforeg[3][6] , \fiforeg[3][5] , \fiforeg[3][4] ,
         \fiforeg[3][3] , \fiforeg[3][2] , \fiforeg[3][1] , \fiforeg[3][0] ,
         \fiforeg[4][7] , \fiforeg[4][6] , \fiforeg[4][5] , \fiforeg[4][4] ,
         \fiforeg[4][3] , \fiforeg[4][2] , \fiforeg[4][1] , \fiforeg[4][0] ,
         \fiforeg[5][7] , \fiforeg[5][6] , \fiforeg[5][5] , \fiforeg[5][4] ,
         \fiforeg[5][3] , \fiforeg[5][2] , \fiforeg[5][1] , \fiforeg[5][0] ,
         \fiforeg[6][7] , \fiforeg[6][6] , \fiforeg[6][5] , \fiforeg[6][4] ,
         \fiforeg[6][3] , \fiforeg[6][2] , \fiforeg[6][1] , \fiforeg[6][0] ,
         \fiforeg[7][7] , \fiforeg[7][6] , \fiforeg[7][5] , \fiforeg[7][4] ,
         \fiforeg[7][3] , \fiforeg[7][2] , \fiforeg[7][1] , \fiforeg[7][0] ,
         n92, n93, n94, n95, n96, n97, n98, n99, n100, n101, n102, n103, n104,
         n105, n106, n107, n108, n109, n110, n111, n112, n113, n114, n115,
         n116, n117, n118, n119, n120, n121, n122, n123, n124, n125, n126,
         n127, n128, n129, n130, n131, n132, n133, n134, n135, n136, n137,
         n138, n139, n140, n141, n142, n143, n144, n145, n146, n147, n148,
         n149, n150, n151, n152, n153, n154, n155, n156, n157, n158, n159,
         n160, n161, n162, n163, n164, n165, n166, n167, n168, n169, n170,
         n171, n172, n173, n174, n175, n176, n177, n178, n179, n180, n181,
         n182, n183, n184, n185, n186, n187, n188, n189, n190, n191, n192,
         n193, n194, n195, n196, n197, n198, n199, n200, n201, n202, n203,
         n204, n205, n206, n207, n208, n209, n210, n211, n212, n213, n214,
         n215, n216, n217, n218, n219, n220, n221, n222, n223, n224, n225,
         n226, n227, n228, n229, n230, n231, n232, n233, n234, n235, n236,
         n237, n238, n239, n240, n241, n242, n243, n244, n245, n246, n247,
         n248, n249, n250, n251, n252, n253, n254, n255, n256, n257, n258,
         n259, n260, n261, n262, n263, n264, n265, n266, n267, n268, n269,
         n270, n271, n272, n273, n274, n275, n1, n2, n3, n4, n5, n6, n7, n8,
         n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20, n21, n22,
         n23, n24, n25, n26, n27, n28, n29, n30, n31, n32, n33, n34, n35, n36,
         n37, n38, n39, n40, n41, n42, n43, n44, n45, n46, n47, n48, n49, n50,
         n51, n52, n53, n54, n55, n56, n57, n58, n59, n60, n61, n62, n63, n64,
         n65, n66, n67, n68, n69, n70, n71, n72, n73, n74, n75, n76, n77, n78,
         n79, n80, n81, n82, n83, n84, n85, n86, n87, n88, n89, n90, n91;

  DFFPOSX1 \fiforeg_reg[7][7]  ( .D(n212), .CLK(wclk), .Q(\fiforeg[7][7] ) );
  DFFPOSX1 \fiforeg_reg[6][7]  ( .D(n213), .CLK(wclk), .Q(\fiforeg[6][7] ) );
  DFFPOSX1 \fiforeg_reg[5][7]  ( .D(n214), .CLK(wclk), .Q(\fiforeg[5][7] ) );
  DFFPOSX1 \fiforeg_reg[4][7]  ( .D(n215), .CLK(wclk), .Q(\fiforeg[4][7] ) );
  DFFPOSX1 \fiforeg_reg[3][7]  ( .D(n216), .CLK(wclk), .Q(\fiforeg[3][7] ) );
  DFFPOSX1 \fiforeg_reg[2][7]  ( .D(n217), .CLK(wclk), .Q(\fiforeg[2][7] ) );
  DFFPOSX1 \fiforeg_reg[1][7]  ( .D(n218), .CLK(wclk), .Q(\fiforeg[1][7] ) );
  DFFPOSX1 \fiforeg_reg[0][7]  ( .D(n219), .CLK(wclk), .Q(\fiforeg[0][7] ) );
  DFFPOSX1 \fiforeg_reg[7][6]  ( .D(n220), .CLK(wclk), .Q(\fiforeg[7][6] ) );
  DFFPOSX1 \fiforeg_reg[6][6]  ( .D(n221), .CLK(wclk), .Q(\fiforeg[6][6] ) );
  DFFPOSX1 \fiforeg_reg[5][6]  ( .D(n222), .CLK(wclk), .Q(\fiforeg[5][6] ) );
  DFFPOSX1 \fiforeg_reg[4][6]  ( .D(n223), .CLK(wclk), .Q(\fiforeg[4][6] ) );
  DFFPOSX1 \fiforeg_reg[3][6]  ( .D(n224), .CLK(wclk), .Q(\fiforeg[3][6] ) );
  DFFPOSX1 \fiforeg_reg[2][6]  ( .D(n225), .CLK(wclk), .Q(\fiforeg[2][6] ) );
  DFFPOSX1 \fiforeg_reg[1][6]  ( .D(n226), .CLK(wclk), .Q(\fiforeg[1][6] ) );
  DFFPOSX1 \fiforeg_reg[0][6]  ( .D(n227), .CLK(wclk), .Q(\fiforeg[0][6] ) );
  DFFPOSX1 \fiforeg_reg[7][5]  ( .D(n228), .CLK(wclk), .Q(\fiforeg[7][5] ) );
  DFFPOSX1 \fiforeg_reg[6][5]  ( .D(n229), .CLK(wclk), .Q(\fiforeg[6][5] ) );
  DFFPOSX1 \fiforeg_reg[5][5]  ( .D(n230), .CLK(wclk), .Q(\fiforeg[5][5] ) );
  DFFPOSX1 \fiforeg_reg[4][5]  ( .D(n231), .CLK(wclk), .Q(\fiforeg[4][5] ) );
  DFFPOSX1 \fiforeg_reg[3][5]  ( .D(n232), .CLK(wclk), .Q(\fiforeg[3][5] ) );
  DFFPOSX1 \fiforeg_reg[2][5]  ( .D(n233), .CLK(wclk), .Q(\fiforeg[2][5] ) );
  DFFPOSX1 \fiforeg_reg[1][5]  ( .D(n234), .CLK(wclk), .Q(\fiforeg[1][5] ) );
  DFFPOSX1 \fiforeg_reg[0][5]  ( .D(n235), .CLK(wclk), .Q(\fiforeg[0][5] ) );
  DFFPOSX1 \fiforeg_reg[7][4]  ( .D(n236), .CLK(wclk), .Q(\fiforeg[7][4] ) );
  DFFPOSX1 \fiforeg_reg[6][4]  ( .D(n237), .CLK(wclk), .Q(\fiforeg[6][4] ) );
  DFFPOSX1 \fiforeg_reg[5][4]  ( .D(n238), .CLK(wclk), .Q(\fiforeg[5][4] ) );
  DFFPOSX1 \fiforeg_reg[4][4]  ( .D(n239), .CLK(wclk), .Q(\fiforeg[4][4] ) );
  DFFPOSX1 \fiforeg_reg[3][4]  ( .D(n240), .CLK(wclk), .Q(\fiforeg[3][4] ) );
  DFFPOSX1 \fiforeg_reg[2][4]  ( .D(n241), .CLK(wclk), .Q(\fiforeg[2][4] ) );
  DFFPOSX1 \fiforeg_reg[1][4]  ( .D(n242), .CLK(wclk), .Q(\fiforeg[1][4] ) );
  DFFPOSX1 \fiforeg_reg[0][4]  ( .D(n243), .CLK(wclk), .Q(\fiforeg[0][4] ) );
  DFFPOSX1 \fiforeg_reg[7][3]  ( .D(n244), .CLK(wclk), .Q(\fiforeg[7][3] ) );
  DFFPOSX1 \fiforeg_reg[6][3]  ( .D(n245), .CLK(wclk), .Q(\fiforeg[6][3] ) );
  DFFPOSX1 \fiforeg_reg[5][3]  ( .D(n246), .CLK(wclk), .Q(\fiforeg[5][3] ) );
  DFFPOSX1 \fiforeg_reg[4][3]  ( .D(n247), .CLK(wclk), .Q(\fiforeg[4][3] ) );
  DFFPOSX1 \fiforeg_reg[3][3]  ( .D(n248), .CLK(wclk), .Q(\fiforeg[3][3] ) );
  DFFPOSX1 \fiforeg_reg[2][3]  ( .D(n249), .CLK(wclk), .Q(\fiforeg[2][3] ) );
  DFFPOSX1 \fiforeg_reg[1][3]  ( .D(n250), .CLK(wclk), .Q(\fiforeg[1][3] ) );
  DFFPOSX1 \fiforeg_reg[0][3]  ( .D(n251), .CLK(wclk), .Q(\fiforeg[0][3] ) );
  DFFPOSX1 \fiforeg_reg[7][2]  ( .D(n252), .CLK(wclk), .Q(\fiforeg[7][2] ) );
  DFFPOSX1 \fiforeg_reg[6][2]  ( .D(n253), .CLK(wclk), .Q(\fiforeg[6][2] ) );
  DFFPOSX1 \fiforeg_reg[5][2]  ( .D(n254), .CLK(wclk), .Q(\fiforeg[5][2] ) );
  DFFPOSX1 \fiforeg_reg[4][2]  ( .D(n255), .CLK(wclk), .Q(\fiforeg[4][2] ) );
  DFFPOSX1 \fiforeg_reg[3][2]  ( .D(n256), .CLK(wclk), .Q(\fiforeg[3][2] ) );
  DFFPOSX1 \fiforeg_reg[2][2]  ( .D(n257), .CLK(wclk), .Q(\fiforeg[2][2] ) );
  DFFPOSX1 \fiforeg_reg[1][2]  ( .D(n258), .CLK(wclk), .Q(\fiforeg[1][2] ) );
  DFFPOSX1 \fiforeg_reg[0][2]  ( .D(n259), .CLK(wclk), .Q(\fiforeg[0][2] ) );
  DFFPOSX1 \fiforeg_reg[7][1]  ( .D(n260), .CLK(wclk), .Q(\fiforeg[7][1] ) );
  DFFPOSX1 \fiforeg_reg[6][1]  ( .D(n261), .CLK(wclk), .Q(\fiforeg[6][1] ) );
  DFFPOSX1 \fiforeg_reg[5][1]  ( .D(n262), .CLK(wclk), .Q(\fiforeg[5][1] ) );
  DFFPOSX1 \fiforeg_reg[4][1]  ( .D(n263), .CLK(wclk), .Q(\fiforeg[4][1] ) );
  DFFPOSX1 \fiforeg_reg[3][1]  ( .D(n264), .CLK(wclk), .Q(\fiforeg[3][1] ) );
  DFFPOSX1 \fiforeg_reg[2][1]  ( .D(n265), .CLK(wclk), .Q(\fiforeg[2][1] ) );
  DFFPOSX1 \fiforeg_reg[1][1]  ( .D(n266), .CLK(wclk), .Q(\fiforeg[1][1] ) );
  DFFPOSX1 \fiforeg_reg[0][1]  ( .D(n267), .CLK(wclk), .Q(\fiforeg[0][1] ) );
  DFFPOSX1 \fiforeg_reg[7][0]  ( .D(n275), .CLK(wclk), .Q(\fiforeg[7][0] ) );
  DFFPOSX1 \fiforeg_reg[6][0]  ( .D(n268), .CLK(wclk), .Q(\fiforeg[6][0] ) );
  DFFPOSX1 \fiforeg_reg[5][0]  ( .D(n269), .CLK(wclk), .Q(\fiforeg[5][0] ) );
  DFFPOSX1 \fiforeg_reg[4][0]  ( .D(n270), .CLK(wclk), .Q(\fiforeg[4][0] ) );
  DFFPOSX1 \fiforeg_reg[3][0]  ( .D(n271), .CLK(wclk), .Q(\fiforeg[3][0] ) );
  DFFPOSX1 \fiforeg_reg[2][0]  ( .D(n272), .CLK(wclk), .Q(\fiforeg[2][0] ) );
  DFFPOSX1 \fiforeg_reg[1][0]  ( .D(n273), .CLK(wclk), .Q(\fiforeg[1][0] ) );
  DFFPOSX1 \fiforeg_reg[0][0]  ( .D(n274), .CLK(wclk), .Q(\fiforeg[0][0] ) );
  NAND3X1 U93 ( .A(n92), .B(n93), .C(n94), .Y(rdata[7]) );
  NOR2X1 U94 ( .A(n95), .B(n96), .Y(n94) );
  OAI22X1 U95 ( .A(n97), .B(n31), .C(n98), .D(n30), .Y(n96) );
  OAI22X1 U96 ( .A(n99), .B(n29), .C(n100), .D(n28), .Y(n95) );
  AOI22X1 U97 ( .A(\fiforeg[3][7] ), .B(n4), .C(\fiforeg[2][7] ), .D(n5), .Y(
        n93) );
  AOI22X1 U98 ( .A(\fiforeg[1][7] ), .B(n2), .C(\fiforeg[0][7] ), .D(n3), .Y(
        n92) );
  NAND3X1 U99 ( .A(n101), .B(n102), .C(n103), .Y(rdata[6]) );
  NOR2X1 U100 ( .A(n104), .B(n105), .Y(n103) );
  OAI22X1 U101 ( .A(n97), .B(n39), .C(n98), .D(n38), .Y(n105) );
  OAI22X1 U102 ( .A(n99), .B(n37), .C(n100), .D(n36), .Y(n104) );
  AOI22X1 U103 ( .A(\fiforeg[3][6] ), .B(n4), .C(\fiforeg[2][6] ), .D(n5), .Y(
        n102) );
  AOI22X1 U104 ( .A(\fiforeg[1][6] ), .B(n2), .C(\fiforeg[0][6] ), .D(n3), .Y(
        n101) );
  NAND3X1 U105 ( .A(n106), .B(n107), .C(n108), .Y(rdata[5]) );
  NOR2X1 U106 ( .A(n109), .B(n110), .Y(n108) );
  OAI22X1 U107 ( .A(n97), .B(n47), .C(n98), .D(n46), .Y(n110) );
  OAI22X1 U108 ( .A(n99), .B(n45), .C(n100), .D(n44), .Y(n109) );
  AOI22X1 U109 ( .A(\fiforeg[3][5] ), .B(n4), .C(\fiforeg[2][5] ), .D(n5), .Y(
        n107) );
  AOI22X1 U110 ( .A(\fiforeg[1][5] ), .B(n2), .C(\fiforeg[0][5] ), .D(n3), .Y(
        n106) );
  NAND3X1 U111 ( .A(n111), .B(n112), .C(n113), .Y(rdata[4]) );
  NOR2X1 U112 ( .A(n114), .B(n115), .Y(n113) );
  OAI22X1 U113 ( .A(n97), .B(n55), .C(n98), .D(n54), .Y(n115) );
  OAI22X1 U114 ( .A(n99), .B(n53), .C(n100), .D(n52), .Y(n114) );
  AOI22X1 U115 ( .A(\fiforeg[3][4] ), .B(n4), .C(\fiforeg[2][4] ), .D(n5), .Y(
        n112) );
  AOI22X1 U116 ( .A(\fiforeg[1][4] ), .B(n2), .C(\fiforeg[0][4] ), .D(n3), .Y(
        n111) );
  NAND3X1 U117 ( .A(n116), .B(n117), .C(n118), .Y(rdata[3]) );
  NOR2X1 U118 ( .A(n119), .B(n120), .Y(n118) );
  OAI22X1 U119 ( .A(n97), .B(n63), .C(n98), .D(n62), .Y(n120) );
  OAI22X1 U120 ( .A(n99), .B(n61), .C(n100), .D(n60), .Y(n119) );
  AOI22X1 U121 ( .A(\fiforeg[3][3] ), .B(n4), .C(\fiforeg[2][3] ), .D(n5), .Y(
        n117) );
  AOI22X1 U122 ( .A(\fiforeg[1][3] ), .B(n2), .C(\fiforeg[0][3] ), .D(n3), .Y(
        n116) );
  NAND3X1 U123 ( .A(n121), .B(n122), .C(n123), .Y(rdata[2]) );
  NOR2X1 U124 ( .A(n124), .B(n125), .Y(n123) );
  OAI22X1 U125 ( .A(n97), .B(n71), .C(n98), .D(n70), .Y(n125) );
  OAI22X1 U126 ( .A(n99), .B(n69), .C(n100), .D(n68), .Y(n124) );
  AOI22X1 U127 ( .A(\fiforeg[3][2] ), .B(n4), .C(\fiforeg[2][2] ), .D(n5), .Y(
        n122) );
  AOI22X1 U128 ( .A(\fiforeg[1][2] ), .B(n2), .C(\fiforeg[0][2] ), .D(n3), .Y(
        n121) );
  NAND3X1 U129 ( .A(n126), .B(n127), .C(n128), .Y(rdata[1]) );
  NOR2X1 U130 ( .A(n129), .B(n130), .Y(n128) );
  OAI22X1 U131 ( .A(n97), .B(n79), .C(n98), .D(n78), .Y(n130) );
  OAI22X1 U132 ( .A(n99), .B(n77), .C(n100), .D(n76), .Y(n129) );
  AOI22X1 U133 ( .A(\fiforeg[3][1] ), .B(n4), .C(\fiforeg[2][1] ), .D(n5), .Y(
        n127) );
  AOI22X1 U134 ( .A(\fiforeg[1][1] ), .B(n2), .C(\fiforeg[0][1] ), .D(n3), .Y(
        n126) );
  NAND3X1 U135 ( .A(n131), .B(n132), .C(n133), .Y(rdata[0]) );
  NOR2X1 U136 ( .A(n134), .B(n135), .Y(n133) );
  OAI22X1 U137 ( .A(n97), .B(n87), .C(n98), .D(n86), .Y(n135) );
  NAND3X1 U138 ( .A(raddr[0]), .B(n7), .C(raddr[2]), .Y(n98) );
  NAND3X1 U139 ( .A(n8), .B(n7), .C(raddr[2]), .Y(n97) );
  OAI22X1 U140 ( .A(n99), .B(n85), .C(n100), .D(n84), .Y(n134) );
  NAND3X1 U141 ( .A(raddr[1]), .B(raddr[0]), .C(raddr[2]), .Y(n100) );
  NAND3X1 U142 ( .A(raddr[1]), .B(n8), .C(raddr[2]), .Y(n99) );
  AOI22X1 U143 ( .A(\fiforeg[3][0] ), .B(n4), .C(\fiforeg[2][0] ), .D(n5), .Y(
        n132) );
  NAND3X1 U144 ( .A(n8), .B(n6), .C(raddr[1]), .Y(n136) );
  NAND3X1 U145 ( .A(raddr[0]), .B(n6), .C(raddr[1]), .Y(n137) );
  AOI22X1 U146 ( .A(\fiforeg[1][0] ), .B(n2), .C(\fiforeg[0][0] ), .D(n3), .Y(
        n131) );
  NAND3X1 U147 ( .A(n7), .B(n6), .C(n8), .Y(n138) );
  NAND3X1 U148 ( .A(n7), .B(n6), .C(raddr[0]), .Y(n139) );
  OAI22X1 U149 ( .A(n25), .B(n28), .C(n140), .D(n141), .Y(n212) );
  OAI22X1 U150 ( .A(n22), .B(n29), .C(n140), .D(n142), .Y(n213) );
  OAI22X1 U151 ( .A(n24), .B(n30), .C(n140), .D(n143), .Y(n214) );
  OAI22X1 U152 ( .A(n23), .B(n31), .C(n140), .D(n144), .Y(n215) );
  OAI22X1 U153 ( .A(n19), .B(n32), .C(n140), .D(n145), .Y(n216) );
  OAI22X1 U154 ( .A(n20), .B(n33), .C(n140), .D(n146), .Y(n217) );
  OAI22X1 U155 ( .A(n17), .B(n34), .C(n140), .D(n147), .Y(n218) );
  OAI22X1 U156 ( .A(n18), .B(n35), .C(n140), .D(n148), .Y(n219) );
  AOI21X1 U157 ( .A(wdata[7]), .B(wenable), .C(n16), .Y(n140) );
  OAI21X1 U158 ( .A(n150), .B(n151), .C(n1), .Y(n149) );
  NAND2X1 U159 ( .A(n152), .B(n153), .Y(n151) );
  AOI22X1 U160 ( .A(n19), .B(\fiforeg[3][7] ), .C(n20), .D(\fiforeg[2][7] ), 
        .Y(n153) );
  AOI22X1 U161 ( .A(n17), .B(\fiforeg[1][7] ), .C(n18), .D(\fiforeg[0][7] ), 
        .Y(n152) );
  NAND2X1 U162 ( .A(n154), .B(n155), .Y(n150) );
  AOI22X1 U163 ( .A(n25), .B(\fiforeg[7][7] ), .C(n22), .D(\fiforeg[6][7] ), 
        .Y(n155) );
  AOI22X1 U164 ( .A(n24), .B(\fiforeg[5][7] ), .C(n23), .D(\fiforeg[4][7] ), 
        .Y(n154) );
  OAI22X1 U165 ( .A(n25), .B(n36), .C(n156), .D(n141), .Y(n220) );
  OAI22X1 U166 ( .A(n22), .B(n37), .C(n156), .D(n142), .Y(n221) );
  OAI22X1 U167 ( .A(n24), .B(n38), .C(n156), .D(n143), .Y(n222) );
  OAI22X1 U168 ( .A(n23), .B(n39), .C(n156), .D(n144), .Y(n223) );
  OAI22X1 U169 ( .A(n19), .B(n40), .C(n156), .D(n145), .Y(n224) );
  OAI22X1 U170 ( .A(n20), .B(n41), .C(n156), .D(n146), .Y(n225) );
  OAI22X1 U171 ( .A(n17), .B(n42), .C(n156), .D(n147), .Y(n226) );
  OAI22X1 U172 ( .A(n18), .B(n43), .C(n156), .D(n148), .Y(n227) );
  AOI21X1 U173 ( .A(wenable), .B(wdata[6]), .C(n15), .Y(n156) );
  OAI21X1 U174 ( .A(n158), .B(n159), .C(n1), .Y(n157) );
  NAND2X1 U175 ( .A(n160), .B(n161), .Y(n159) );
  AOI22X1 U176 ( .A(n19), .B(\fiforeg[3][6] ), .C(n20), .D(\fiforeg[2][6] ), 
        .Y(n161) );
  AOI22X1 U177 ( .A(n17), .B(\fiforeg[1][6] ), .C(n18), .D(\fiforeg[0][6] ), 
        .Y(n160) );
  NAND2X1 U178 ( .A(n162), .B(n163), .Y(n158) );
  AOI22X1 U179 ( .A(n25), .B(\fiforeg[7][6] ), .C(n22), .D(\fiforeg[6][6] ), 
        .Y(n163) );
  AOI22X1 U180 ( .A(n24), .B(\fiforeg[5][6] ), .C(n23), .D(\fiforeg[4][6] ), 
        .Y(n162) );
  OAI22X1 U181 ( .A(n25), .B(n44), .C(n164), .D(n141), .Y(n228) );
  OAI22X1 U182 ( .A(n22), .B(n45), .C(n164), .D(n142), .Y(n229) );
  OAI22X1 U183 ( .A(n24), .B(n46), .C(n164), .D(n143), .Y(n230) );
  OAI22X1 U184 ( .A(n23), .B(n47), .C(n164), .D(n144), .Y(n231) );
  OAI22X1 U185 ( .A(n19), .B(n48), .C(n164), .D(n145), .Y(n232) );
  OAI22X1 U186 ( .A(n20), .B(n49), .C(n164), .D(n146), .Y(n233) );
  OAI22X1 U187 ( .A(n17), .B(n50), .C(n164), .D(n147), .Y(n234) );
  OAI22X1 U188 ( .A(n18), .B(n51), .C(n164), .D(n148), .Y(n235) );
  AOI21X1 U189 ( .A(wenable), .B(wdata[5]), .C(n14), .Y(n164) );
  OAI21X1 U190 ( .A(n166), .B(n167), .C(n1), .Y(n165) );
  NAND2X1 U191 ( .A(n168), .B(n169), .Y(n167) );
  AOI22X1 U192 ( .A(n19), .B(\fiforeg[3][5] ), .C(n20), .D(\fiforeg[2][5] ), 
        .Y(n169) );
  AOI22X1 U193 ( .A(n17), .B(\fiforeg[1][5] ), .C(n18), .D(\fiforeg[0][5] ), 
        .Y(n168) );
  NAND2X1 U194 ( .A(n170), .B(n171), .Y(n166) );
  AOI22X1 U195 ( .A(n25), .B(\fiforeg[7][5] ), .C(n22), .D(\fiforeg[6][5] ), 
        .Y(n171) );
  AOI22X1 U196 ( .A(n24), .B(\fiforeg[5][5] ), .C(n23), .D(\fiforeg[4][5] ), 
        .Y(n170) );
  OAI22X1 U197 ( .A(n25), .B(n52), .C(n172), .D(n141), .Y(n236) );
  OAI22X1 U198 ( .A(n22), .B(n53), .C(n172), .D(n142), .Y(n237) );
  OAI22X1 U199 ( .A(n24), .B(n54), .C(n172), .D(n143), .Y(n238) );
  OAI22X1 U200 ( .A(n23), .B(n55), .C(n172), .D(n144), .Y(n239) );
  OAI22X1 U201 ( .A(n19), .B(n56), .C(n172), .D(n145), .Y(n240) );
  OAI22X1 U202 ( .A(n20), .B(n57), .C(n172), .D(n146), .Y(n241) );
  OAI22X1 U203 ( .A(n17), .B(n58), .C(n172), .D(n147), .Y(n242) );
  OAI22X1 U204 ( .A(n18), .B(n59), .C(n172), .D(n148), .Y(n243) );
  AOI21X1 U205 ( .A(wenable), .B(wdata[4]), .C(n13), .Y(n172) );
  OAI21X1 U206 ( .A(n174), .B(n175), .C(n1), .Y(n173) );
  NAND2X1 U207 ( .A(n176), .B(n177), .Y(n175) );
  AOI22X1 U208 ( .A(n19), .B(\fiforeg[3][4] ), .C(n20), .D(\fiforeg[2][4] ), 
        .Y(n177) );
  AOI22X1 U209 ( .A(n17), .B(\fiforeg[1][4] ), .C(n18), .D(\fiforeg[0][4] ), 
        .Y(n176) );
  NAND2X1 U210 ( .A(n178), .B(n179), .Y(n174) );
  AOI22X1 U211 ( .A(n25), .B(\fiforeg[7][4] ), .C(n22), .D(\fiforeg[6][4] ), 
        .Y(n179) );
  AOI22X1 U212 ( .A(n24), .B(\fiforeg[5][4] ), .C(n23), .D(\fiforeg[4][4] ), 
        .Y(n178) );
  OAI22X1 U213 ( .A(n25), .B(n60), .C(n180), .D(n141), .Y(n244) );
  OAI22X1 U214 ( .A(n22), .B(n61), .C(n180), .D(n142), .Y(n245) );
  OAI22X1 U215 ( .A(n24), .B(n62), .C(n180), .D(n143), .Y(n246) );
  OAI22X1 U216 ( .A(n23), .B(n63), .C(n180), .D(n144), .Y(n247) );
  OAI22X1 U217 ( .A(n19), .B(n64), .C(n180), .D(n145), .Y(n248) );
  OAI22X1 U218 ( .A(n20), .B(n65), .C(n180), .D(n146), .Y(n249) );
  OAI22X1 U219 ( .A(n17), .B(n66), .C(n180), .D(n147), .Y(n250) );
  OAI22X1 U220 ( .A(n18), .B(n67), .C(n180), .D(n148), .Y(n251) );
  AOI21X1 U221 ( .A(wenable), .B(wdata[3]), .C(n12), .Y(n180) );
  OAI21X1 U222 ( .A(n182), .B(n183), .C(n1), .Y(n181) );
  NAND2X1 U223 ( .A(n184), .B(n185), .Y(n183) );
  AOI22X1 U224 ( .A(n19), .B(\fiforeg[3][3] ), .C(n20), .D(\fiforeg[2][3] ), 
        .Y(n185) );
  AOI22X1 U225 ( .A(n17), .B(\fiforeg[1][3] ), .C(n18), .D(\fiforeg[0][3] ), 
        .Y(n184) );
  NAND2X1 U226 ( .A(n186), .B(n187), .Y(n182) );
  AOI22X1 U227 ( .A(n25), .B(\fiforeg[7][3] ), .C(n22), .D(\fiforeg[6][3] ), 
        .Y(n187) );
  AOI22X1 U228 ( .A(n24), .B(\fiforeg[5][3] ), .C(n23), .D(\fiforeg[4][3] ), 
        .Y(n186) );
  OAI22X1 U229 ( .A(n25), .B(n68), .C(n188), .D(n141), .Y(n252) );
  OAI22X1 U230 ( .A(n22), .B(n69), .C(n188), .D(n142), .Y(n253) );
  OAI22X1 U231 ( .A(n24), .B(n70), .C(n188), .D(n143), .Y(n254) );
  OAI22X1 U232 ( .A(n23), .B(n71), .C(n188), .D(n144), .Y(n255) );
  OAI22X1 U233 ( .A(n19), .B(n72), .C(n188), .D(n145), .Y(n256) );
  OAI22X1 U234 ( .A(n20), .B(n73), .C(n188), .D(n146), .Y(n257) );
  OAI22X1 U235 ( .A(n17), .B(n74), .C(n188), .D(n147), .Y(n258) );
  OAI22X1 U236 ( .A(n18), .B(n75), .C(n188), .D(n148), .Y(n259) );
  AOI21X1 U237 ( .A(wenable), .B(wdata[2]), .C(n11), .Y(n188) );
  OAI21X1 U238 ( .A(n190), .B(n191), .C(n1), .Y(n189) );
  NAND2X1 U239 ( .A(n192), .B(n193), .Y(n191) );
  AOI22X1 U240 ( .A(n19), .B(\fiforeg[3][2] ), .C(n20), .D(\fiforeg[2][2] ), 
        .Y(n193) );
  AOI22X1 U241 ( .A(n17), .B(\fiforeg[1][2] ), .C(n18), .D(\fiforeg[0][2] ), 
        .Y(n192) );
  NAND2X1 U242 ( .A(n194), .B(n195), .Y(n190) );
  AOI22X1 U243 ( .A(n25), .B(\fiforeg[7][2] ), .C(n22), .D(\fiforeg[6][2] ), 
        .Y(n195) );
  AOI22X1 U244 ( .A(n24), .B(\fiforeg[5][2] ), .C(n23), .D(\fiforeg[4][2] ), 
        .Y(n194) );
  OAI22X1 U245 ( .A(n25), .B(n76), .C(n196), .D(n141), .Y(n260) );
  OAI22X1 U246 ( .A(n22), .B(n77), .C(n196), .D(n142), .Y(n261) );
  OAI22X1 U247 ( .A(n24), .B(n78), .C(n196), .D(n143), .Y(n262) );
  OAI22X1 U248 ( .A(n23), .B(n79), .C(n196), .D(n144), .Y(n263) );
  OAI22X1 U249 ( .A(n19), .B(n80), .C(n196), .D(n145), .Y(n264) );
  OAI22X1 U250 ( .A(n20), .B(n81), .C(n196), .D(n146), .Y(n265) );
  OAI22X1 U251 ( .A(n17), .B(n82), .C(n196), .D(n147), .Y(n266) );
  OAI22X1 U252 ( .A(n18), .B(n83), .C(n196), .D(n148), .Y(n267) );
  AOI21X1 U253 ( .A(wenable), .B(wdata[1]), .C(n10), .Y(n196) );
  OAI21X1 U254 ( .A(n198), .B(n199), .C(n1), .Y(n197) );
  NAND2X1 U255 ( .A(n200), .B(n201), .Y(n199) );
  AOI22X1 U256 ( .A(n19), .B(\fiforeg[3][1] ), .C(n20), .D(\fiforeg[2][1] ), 
        .Y(n201) );
  AOI22X1 U257 ( .A(n17), .B(\fiforeg[1][1] ), .C(n18), .D(\fiforeg[0][1] ), 
        .Y(n200) );
  NAND2X1 U258 ( .A(n202), .B(n203), .Y(n198) );
  AOI22X1 U259 ( .A(n25), .B(\fiforeg[7][1] ), .C(n22), .D(\fiforeg[6][1] ), 
        .Y(n203) );
  AOI22X1 U260 ( .A(n24), .B(\fiforeg[5][1] ), .C(n23), .D(\fiforeg[4][1] ), 
        .Y(n202) );
  OAI22X1 U261 ( .A(n22), .B(n85), .C(n204), .D(n142), .Y(n268) );
  OAI22X1 U262 ( .A(n24), .B(n86), .C(n204), .D(n143), .Y(n269) );
  OAI22X1 U263 ( .A(n23), .B(n87), .C(n204), .D(n144), .Y(n270) );
  OAI22X1 U264 ( .A(n19), .B(n88), .C(n204), .D(n145), .Y(n271) );
  OAI22X1 U265 ( .A(n20), .B(n89), .C(n204), .D(n146), .Y(n272) );
  OAI22X1 U266 ( .A(n17), .B(n90), .C(n204), .D(n147), .Y(n273) );
  OAI22X1 U267 ( .A(n18), .B(n91), .C(n204), .D(n148), .Y(n274) );
  OAI22X1 U268 ( .A(n25), .B(n84), .C(n204), .D(n141), .Y(n275) );
  AOI21X1 U269 ( .A(wenable), .B(wdata[0]), .C(n9), .Y(n204) );
  OAI21X1 U270 ( .A(n206), .B(n207), .C(n1), .Y(n205) );
  NAND2X1 U271 ( .A(n208), .B(n209), .Y(n207) );
  AOI22X1 U272 ( .A(n19), .B(\fiforeg[3][0] ), .C(n20), .D(\fiforeg[2][0] ), 
        .Y(n209) );
  NAND3X1 U273 ( .A(n27), .B(n21), .C(waddr[1]), .Y(n146) );
  NAND3X1 U274 ( .A(waddr[0]), .B(n21), .C(waddr[1]), .Y(n145) );
  AOI22X1 U275 ( .A(n17), .B(\fiforeg[1][0] ), .C(n18), .D(\fiforeg[0][0] ), 
        .Y(n208) );
  NAND3X1 U276 ( .A(n26), .B(n21), .C(n27), .Y(n148) );
  NAND3X1 U277 ( .A(n26), .B(n21), .C(waddr[0]), .Y(n147) );
  NAND2X1 U278 ( .A(n210), .B(n211), .Y(n206) );
  AOI22X1 U279 ( .A(n25), .B(\fiforeg[7][0] ), .C(n22), .D(\fiforeg[6][0] ), 
        .Y(n211) );
  NAND3X1 U280 ( .A(waddr[1]), .B(n27), .C(waddr[2]), .Y(n142) );
  AOI22X1 U281 ( .A(n24), .B(\fiforeg[5][0] ), .C(n23), .D(\fiforeg[4][0] ), 
        .Y(n210) );
  NAND3X1 U282 ( .A(n27), .B(n26), .C(waddr[2]), .Y(n144) );
  NAND3X1 U283 ( .A(waddr[0]), .B(n26), .C(waddr[2]), .Y(n143) );
  NAND3X1 U284 ( .A(waddr[1]), .B(waddr[0]), .C(waddr[2]), .Y(n141) );
  INVX2 U2 ( .A(n148), .Y(n18) );
  INVX2 U3 ( .A(n142), .Y(n22) );
  INVX2 U4 ( .A(n146), .Y(n20) );
  INVX2 U5 ( .A(n144), .Y(n23) );
  INVX2 U6 ( .A(n145), .Y(n19) );
  INVX2 U7 ( .A(n143), .Y(n24) );
  INVX2 U8 ( .A(n147), .Y(n17) );
  INVX2 U9 ( .A(n141), .Y(n25) );
  INVX2 U10 ( .A(wenable), .Y(n1) );
  INVX2 U11 ( .A(n139), .Y(n2) );
  INVX2 U12 ( .A(n138), .Y(n3) );
  INVX2 U13 ( .A(n137), .Y(n4) );
  INVX2 U14 ( .A(n136), .Y(n5) );
  INVX2 U15 ( .A(raddr[2]), .Y(n6) );
  INVX2 U16 ( .A(raddr[1]), .Y(n7) );
  INVX2 U17 ( .A(raddr[0]), .Y(n8) );
  INVX2 U18 ( .A(n205), .Y(n9) );
  INVX2 U19 ( .A(n197), .Y(n10) );
  INVX2 U20 ( .A(n189), .Y(n11) );
  INVX2 U21 ( .A(n181), .Y(n12) );
  INVX2 U22 ( .A(n173), .Y(n13) );
  INVX2 U23 ( .A(n165), .Y(n14) );
  INVX2 U24 ( .A(n157), .Y(n15) );
  INVX2 U25 ( .A(n149), .Y(n16) );
  INVX2 U26 ( .A(waddr[2]), .Y(n21) );
  INVX2 U27 ( .A(waddr[1]), .Y(n26) );
  INVX2 U28 ( .A(waddr[0]), .Y(n27) );
  INVX2 U29 ( .A(\fiforeg[7][7] ), .Y(n28) );
  INVX2 U30 ( .A(\fiforeg[6][7] ), .Y(n29) );
  INVX2 U31 ( .A(\fiforeg[5][7] ), .Y(n30) );
  INVX2 U32 ( .A(\fiforeg[4][7] ), .Y(n31) );
  INVX2 U33 ( .A(\fiforeg[3][7] ), .Y(n32) );
  INVX2 U34 ( .A(\fiforeg[2][7] ), .Y(n33) );
  INVX2 U35 ( .A(\fiforeg[1][7] ), .Y(n34) );
  INVX2 U36 ( .A(\fiforeg[0][7] ), .Y(n35) );
  INVX2 U37 ( .A(\fiforeg[7][6] ), .Y(n36) );
  INVX2 U38 ( .A(\fiforeg[6][6] ), .Y(n37) );
  INVX2 U39 ( .A(\fiforeg[5][6] ), .Y(n38) );
  INVX2 U40 ( .A(\fiforeg[4][6] ), .Y(n39) );
  INVX2 U41 ( .A(\fiforeg[3][6] ), .Y(n40) );
  INVX2 U42 ( .A(\fiforeg[2][6] ), .Y(n41) );
  INVX2 U43 ( .A(\fiforeg[1][6] ), .Y(n42) );
  INVX2 U44 ( .A(\fiforeg[0][6] ), .Y(n43) );
  INVX2 U45 ( .A(\fiforeg[7][5] ), .Y(n44) );
  INVX2 U46 ( .A(\fiforeg[6][5] ), .Y(n45) );
  INVX2 U47 ( .A(\fiforeg[5][5] ), .Y(n46) );
  INVX2 U48 ( .A(\fiforeg[4][5] ), .Y(n47) );
  INVX2 U49 ( .A(\fiforeg[3][5] ), .Y(n48) );
  INVX2 U50 ( .A(\fiforeg[2][5] ), .Y(n49) );
  INVX2 U51 ( .A(\fiforeg[1][5] ), .Y(n50) );
  INVX2 U52 ( .A(\fiforeg[0][5] ), .Y(n51) );
  INVX2 U53 ( .A(\fiforeg[7][4] ), .Y(n52) );
  INVX2 U54 ( .A(\fiforeg[6][4] ), .Y(n53) );
  INVX2 U55 ( .A(\fiforeg[5][4] ), .Y(n54) );
  INVX2 U56 ( .A(\fiforeg[4][4] ), .Y(n55) );
  INVX2 U57 ( .A(\fiforeg[3][4] ), .Y(n56) );
  INVX2 U58 ( .A(\fiforeg[2][4] ), .Y(n57) );
  INVX2 U59 ( .A(\fiforeg[1][4] ), .Y(n58) );
  INVX2 U60 ( .A(\fiforeg[0][4] ), .Y(n59) );
  INVX2 U61 ( .A(\fiforeg[7][3] ), .Y(n60) );
  INVX2 U62 ( .A(\fiforeg[6][3] ), .Y(n61) );
  INVX2 U63 ( .A(\fiforeg[5][3] ), .Y(n62) );
  INVX2 U64 ( .A(\fiforeg[4][3] ), .Y(n63) );
  INVX2 U65 ( .A(\fiforeg[3][3] ), .Y(n64) );
  INVX2 U66 ( .A(\fiforeg[2][3] ), .Y(n65) );
  INVX2 U67 ( .A(\fiforeg[1][3] ), .Y(n66) );
  INVX2 U68 ( .A(\fiforeg[0][3] ), .Y(n67) );
  INVX2 U69 ( .A(\fiforeg[7][2] ), .Y(n68) );
  INVX2 U70 ( .A(\fiforeg[6][2] ), .Y(n69) );
  INVX2 U71 ( .A(\fiforeg[5][2] ), .Y(n70) );
  INVX2 U72 ( .A(\fiforeg[4][2] ), .Y(n71) );
  INVX2 U73 ( .A(\fiforeg[3][2] ), .Y(n72) );
  INVX2 U74 ( .A(\fiforeg[2][2] ), .Y(n73) );
  INVX2 U75 ( .A(\fiforeg[1][2] ), .Y(n74) );
  INVX2 U76 ( .A(\fiforeg[0][2] ), .Y(n75) );
  INVX2 U77 ( .A(\fiforeg[7][1] ), .Y(n76) );
  INVX2 U78 ( .A(\fiforeg[6][1] ), .Y(n77) );
  INVX2 U79 ( .A(\fiforeg[5][1] ), .Y(n78) );
  INVX2 U80 ( .A(\fiforeg[4][1] ), .Y(n79) );
  INVX2 U81 ( .A(\fiforeg[3][1] ), .Y(n80) );
  INVX2 U82 ( .A(\fiforeg[2][1] ), .Y(n81) );
  INVX2 U83 ( .A(\fiforeg[1][1] ), .Y(n82) );
  INVX2 U84 ( .A(\fiforeg[0][1] ), .Y(n83) );
  INVX2 U85 ( .A(\fiforeg[7][0] ), .Y(n84) );
  INVX2 U86 ( .A(\fiforeg[6][0] ), .Y(n85) );
  INVX2 U87 ( .A(\fiforeg[5][0] ), .Y(n86) );
  INVX2 U88 ( .A(\fiforeg[4][0] ), .Y(n87) );
  INVX2 U89 ( .A(\fiforeg[3][0] ), .Y(n88) );
  INVX2 U90 ( .A(\fiforeg[2][0] ), .Y(n89) );
  INVX2 U91 ( .A(\fiforeg[1][0] ), .Y(n90) );
  INVX2 U92 ( .A(\fiforeg[0][0] ), .Y(n91) );
endmodule


module write_ptr ( wclk, rst_n, wenable, wptr, wptr_nxt );
  output [3:0] wptr;
  output [3:0] wptr_nxt;
  input wclk, rst_n, wenable;
  wire   n10, n11, n12, n9;
  wire   [2:0] binary_nxt;
  wire   [3:0] binary_r;

  DFFSR \binary_r_reg[0]  ( .D(binary_nxt[0]), .CLK(wclk), .R(rst_n), .S(1'b1), 
        .Q(binary_r[0]) );
  DFFSR \binary_r_reg[1]  ( .D(binary_nxt[1]), .CLK(wclk), .R(rst_n), .S(1'b1), 
        .Q(binary_r[1]) );
  DFFSR \binary_r_reg[2]  ( .D(binary_nxt[2]), .CLK(wclk), .R(rst_n), .S(1'b1), 
        .Q(binary_r[2]) );
  DFFSR \binary_r_reg[3]  ( .D(wptr_nxt[3]), .CLK(wclk), .R(rst_n), .S(1'b1), 
        .Q(binary_r[3]) );
  DFFSR \gray_r_reg[3]  ( .D(wptr_nxt[3]), .CLK(wclk), .R(rst_n), .S(1'b1), 
        .Q(wptr[3]) );
  DFFSR \gray_r_reg[2]  ( .D(wptr_nxt[2]), .CLK(wclk), .R(rst_n), .S(1'b1), 
        .Q(wptr[2]) );
  DFFSR \gray_r_reg[1]  ( .D(wptr_nxt[1]), .CLK(wclk), .R(rst_n), .S(1'b1), 
        .Q(wptr[1]) );
  DFFSR \gray_r_reg[0]  ( .D(wptr_nxt[0]), .CLK(wclk), .R(rst_n), .S(1'b1), 
        .Q(wptr[0]) );
  XOR2X1 U12 ( .A(wptr_nxt[3]), .B(binary_nxt[2]), .Y(wptr_nxt[2]) );
  XNOR2X1 U13 ( .A(n10), .B(binary_r[3]), .Y(wptr_nxt[3]) );
  NAND2X1 U14 ( .A(binary_r[2]), .B(n11), .Y(n10) );
  XOR2X1 U15 ( .A(binary_nxt[2]), .B(binary_nxt[1]), .Y(wptr_nxt[1]) );
  XOR2X1 U16 ( .A(binary_nxt[1]), .B(binary_nxt[0]), .Y(wptr_nxt[0]) );
  XOR2X1 U17 ( .A(binary_r[2]), .B(n11), .Y(binary_nxt[2]) );
  NOR2X1 U18 ( .A(n9), .B(n12), .Y(n11) );
  XNOR2X1 U19 ( .A(n12), .B(binary_r[1]), .Y(binary_nxt[1]) );
  NAND2X1 U20 ( .A(wenable), .B(binary_r[0]), .Y(n12) );
  XOR2X1 U21 ( .A(binary_r[0]), .B(wenable), .Y(binary_nxt[0]) );
  INVX2 U11 ( .A(binary_r[1]), .Y(n9) );
endmodule


module write_fifo_ctrl ( wclk, rst_n, wenable, rptr, wenable_fifo, wptr, waddr, 
        full_flag );
  input [3:0] rptr;
  output [3:0] wptr;
  output [2:0] waddr;
  input wclk, rst_n, wenable;
  output wenable_fifo, full_flag;
  wire   \gray_wptr[2] , N5, n18, n19, n20, n21, n22, n23, n24, n1;
  wire   [3:0] wptr_nxt;
  wire   [3:0] wrptr_r2;
  wire   [3:0] wrptr_r1;

  DFFSR \wrptr_r1_reg[3]  ( .D(rptr[3]), .CLK(wclk), .R(rst_n), .S(1'b1), .Q(
        wrptr_r1[3]) );
  DFFSR \wrptr_r1_reg[2]  ( .D(rptr[2]), .CLK(wclk), .R(rst_n), .S(1'b1), .Q(
        wrptr_r1[2]) );
  DFFSR \wrptr_r1_reg[1]  ( .D(rptr[1]), .CLK(wclk), .R(rst_n), .S(1'b1), .Q(
        wrptr_r1[1]) );
  DFFSR \wrptr_r1_reg[0]  ( .D(rptr[0]), .CLK(wclk), .R(rst_n), .S(1'b1), .Q(
        wrptr_r1[0]) );
  DFFSR \wrptr_r2_reg[3]  ( .D(wrptr_r1[3]), .CLK(wclk), .R(rst_n), .S(1'b1), 
        .Q(wrptr_r2[3]) );
  DFFSR \wrptr_r2_reg[2]  ( .D(wrptr_r1[2]), .CLK(wclk), .R(rst_n), .S(1'b1), 
        .Q(wrptr_r2[2]) );
  DFFSR \wrptr_r2_reg[1]  ( .D(wrptr_r1[1]), .CLK(wclk), .R(rst_n), .S(1'b1), 
        .Q(wrptr_r2[1]) );
  DFFSR \wrptr_r2_reg[0]  ( .D(wrptr_r1[0]), .CLK(wclk), .R(rst_n), .S(1'b1), 
        .Q(wrptr_r2[0]) );
  DFFSR full_flag_r_reg ( .D(N5), .CLK(wclk), .R(rst_n), .S(1'b1), .Q(
        full_flag) );
  DFFSR \waddr_reg[2]  ( .D(\gray_wptr[2] ), .CLK(wclk), .R(rst_n), .S(1'b1), 
        .Q(waddr[2]) );
  DFFSR \waddr_reg[1]  ( .D(wptr_nxt[1]), .CLK(wclk), .R(rst_n), .S(1'b1), .Q(
        waddr[1]) );
  DFFSR \waddr_reg[0]  ( .D(wptr_nxt[0]), .CLK(wclk), .R(rst_n), .S(1'b1), .Q(
        waddr[0]) );
  NOR2X1 U16 ( .A(full_flag), .B(n1), .Y(wenable_fifo) );
  NOR2X1 U17 ( .A(n18), .B(n19), .Y(N5) );
  NAND2X1 U18 ( .A(n20), .B(n21), .Y(n19) );
  XOR2X1 U19 ( .A(n22), .B(\gray_wptr[2] ), .Y(n21) );
  XOR2X1 U20 ( .A(wptr_nxt[3]), .B(wptr_nxt[2]), .Y(\gray_wptr[2] ) );
  XNOR2X1 U21 ( .A(wrptr_r2[3]), .B(wrptr_r2[2]), .Y(n22) );
  XNOR2X1 U22 ( .A(wrptr_r2[1]), .B(wptr_nxt[1]), .Y(n20) );
  NAND2X1 U23 ( .A(n23), .B(n24), .Y(n18) );
  XOR2X1 U24 ( .A(wrptr_r2[3]), .B(wptr_nxt[3]), .Y(n24) );
  XNOR2X1 U25 ( .A(wrptr_r2[0]), .B(wptr_nxt[0]), .Y(n23) );
  write_ptr WPU1 ( .wclk(wclk), .rst_n(rst_n), .wenable(wenable_fifo), .wptr(
        wptr), .wptr_nxt(wptr_nxt) );
  INVX2 U15 ( .A(wenable), .Y(n1) );
endmodule


module read_ptr ( rclk, rst_n, renable, rptr, rptr_nxt );
  output [3:0] rptr;
  output [3:0] rptr_nxt;
  input rclk, rst_n, renable;
  wire   n10, n11, n12, n9;
  wire   [2:0] binary_nxt;
  wire   [3:0] binary_r;

  DFFSR \binary_r_reg[0]  ( .D(binary_nxt[0]), .CLK(rclk), .R(rst_n), .S(1'b1), 
        .Q(binary_r[0]) );
  DFFSR \binary_r_reg[1]  ( .D(binary_nxt[1]), .CLK(rclk), .R(rst_n), .S(1'b1), 
        .Q(binary_r[1]) );
  DFFSR \binary_r_reg[2]  ( .D(binary_nxt[2]), .CLK(rclk), .R(rst_n), .S(1'b1), 
        .Q(binary_r[2]) );
  DFFSR \binary_r_reg[3]  ( .D(rptr_nxt[3]), .CLK(rclk), .R(rst_n), .S(1'b1), 
        .Q(binary_r[3]) );
  DFFSR \gray_r_reg[3]  ( .D(rptr_nxt[3]), .CLK(rclk), .R(rst_n), .S(1'b1), 
        .Q(rptr[3]) );
  DFFSR \gray_r_reg[2]  ( .D(rptr_nxt[2]), .CLK(rclk), .R(rst_n), .S(1'b1), 
        .Q(rptr[2]) );
  DFFSR \gray_r_reg[1]  ( .D(rptr_nxt[1]), .CLK(rclk), .R(rst_n), .S(1'b1), 
        .Q(rptr[1]) );
  DFFSR \gray_r_reg[0]  ( .D(rptr_nxt[0]), .CLK(rclk), .R(rst_n), .S(1'b1), 
        .Q(rptr[0]) );
  XOR2X1 U12 ( .A(rptr_nxt[3]), .B(binary_nxt[2]), .Y(rptr_nxt[2]) );
  XNOR2X1 U13 ( .A(n10), .B(binary_r[3]), .Y(rptr_nxt[3]) );
  NAND2X1 U14 ( .A(binary_r[2]), .B(n11), .Y(n10) );
  XOR2X1 U15 ( .A(binary_nxt[2]), .B(binary_nxt[1]), .Y(rptr_nxt[1]) );
  XOR2X1 U16 ( .A(binary_nxt[1]), .B(binary_nxt[0]), .Y(rptr_nxt[0]) );
  XOR2X1 U17 ( .A(binary_r[2]), .B(n11), .Y(binary_nxt[2]) );
  NOR2X1 U18 ( .A(n9), .B(n12), .Y(n11) );
  XNOR2X1 U19 ( .A(n12), .B(binary_r[1]), .Y(binary_nxt[1]) );
  NAND2X1 U20 ( .A(renable), .B(binary_r[0]), .Y(n12) );
  XOR2X1 U21 ( .A(binary_r[0]), .B(renable), .Y(binary_nxt[0]) );
  INVX2 U11 ( .A(binary_r[1]), .Y(n9) );
endmodule


module read_fifo_ctrl ( rclk, rst_n, renable, wptr, rptr, raddr, empty_flag );
  input [3:0] wptr;
  output [3:0] rptr;
  output [2:0] raddr;
  input rclk, rst_n, renable;
  output empty_flag;
  wire   renable_p2, \gray_rptr[2] , N3, n18, n19, n20, n21, n22, n23, n24, n1
;
  wire   [3:0] rptr_nxt;
  wire   [3:0] rwptr_r2;
  wire   [3:0] rwptr_r1;

  DFFSR \rwptr_r1_reg[3]  ( .D(wptr[3]), .CLK(rclk), .R(rst_n), .S(1'b1), .Q(
        rwptr_r1[3]) );
  DFFSR \rwptr_r1_reg[2]  ( .D(wptr[2]), .CLK(rclk), .R(rst_n), .S(1'b1), .Q(
        rwptr_r1[2]) );
  DFFSR \rwptr_r1_reg[1]  ( .D(wptr[1]), .CLK(rclk), .R(rst_n), .S(1'b1), .Q(
        rwptr_r1[1]) );
  DFFSR \rwptr_r1_reg[0]  ( .D(wptr[0]), .CLK(rclk), .R(rst_n), .S(1'b1), .Q(
        rwptr_r1[0]) );
  DFFSR \rwptr_r2_reg[3]  ( .D(rwptr_r1[3]), .CLK(rclk), .R(rst_n), .S(1'b1), 
        .Q(rwptr_r2[3]) );
  DFFSR \rwptr_r2_reg[2]  ( .D(rwptr_r1[2]), .CLK(rclk), .R(rst_n), .S(1'b1), 
        .Q(rwptr_r2[2]) );
  DFFSR \rwptr_r2_reg[1]  ( .D(rwptr_r1[1]), .CLK(rclk), .R(rst_n), .S(1'b1), 
        .Q(rwptr_r2[1]) );
  DFFSR \rwptr_r2_reg[0]  ( .D(rwptr_r1[0]), .CLK(rclk), .R(rst_n), .S(1'b1), 
        .Q(rwptr_r2[0]) );
  DFFSR empty_flag_r_reg ( .D(N3), .CLK(rclk), .R(1'b1), .S(rst_n), .Q(
        empty_flag) );
  DFFSR \raddr_reg[2]  ( .D(\gray_rptr[2] ), .CLK(rclk), .R(rst_n), .S(1'b1), 
        .Q(raddr[2]) );
  DFFSR \raddr_reg[1]  ( .D(rptr_nxt[1]), .CLK(rclk), .R(rst_n), .S(1'b1), .Q(
        raddr[1]) );
  DFFSR \raddr_reg[0]  ( .D(rptr_nxt[0]), .CLK(rclk), .R(rst_n), .S(1'b1), .Q(
        raddr[0]) );
  NOR2X1 U16 ( .A(empty_flag), .B(n1), .Y(renable_p2) );
  NOR2X1 U17 ( .A(n18), .B(n19), .Y(N3) );
  NAND2X1 U18 ( .A(n20), .B(n21), .Y(n19) );
  XOR2X1 U19 ( .A(n22), .B(\gray_rptr[2] ), .Y(n21) );
  XOR2X1 U20 ( .A(rptr_nxt[3]), .B(rptr_nxt[2]), .Y(\gray_rptr[2] ) );
  XNOR2X1 U21 ( .A(rwptr_r2[3]), .B(rwptr_r2[2]), .Y(n22) );
  XNOR2X1 U22 ( .A(rwptr_r2[1]), .B(rptr_nxt[1]), .Y(n20) );
  NAND2X1 U23 ( .A(n23), .B(n24), .Y(n18) );
  XNOR2X1 U24 ( .A(rptr_nxt[3]), .B(rwptr_r2[3]), .Y(n24) );
  XNOR2X1 U25 ( .A(rwptr_r2[0]), .B(rptr_nxt[0]), .Y(n23) );
  read_ptr RPU1 ( .rclk(rclk), .rst_n(rst_n), .renable(renable_p2), .rptr(rptr), .rptr_nxt(rptr_nxt) );
  INVX2 U15 ( .A(renable), .Y(n1) );
endmodule


module fifo ( r_clk, w_clk, n_rst, r_enable, w_enable, w_data, r_data, empty, 
        full );
  input [7:0] w_data;
  output [7:0] r_data;
  input r_clk, w_clk, n_rst, r_enable, w_enable;
  output empty, full;
  wire   wenable_fifo;
  wire   [2:0] waddr;
  wire   [2:0] raddr;
  wire   [3:0] rptr;
  wire   [3:0] wptr;

  fiforam UFIFORAM ( .wclk(w_clk), .wenable(wenable_fifo), .waddr(waddr), 
        .raddr(raddr), .wdata(w_data), .rdata(r_data) );
  write_fifo_ctrl UWFC ( .wclk(w_clk), .rst_n(n_rst), .wenable(w_enable), 
        .rptr(rptr), .wenable_fifo(wenable_fifo), .wptr(wptr), .waddr(waddr), 
        .full_flag(full) );
  read_fifo_ctrl URFC ( .rclk(r_clk), .rst_n(n_rst), .renable(r_enable), 
        .wptr(wptr), .rptr(rptr), .raddr(raddr), .empty_flag(empty) );
endmodule


module tx_fifo ( clk, n_rst, read_enable, write_enable, write_data, read_data, 
        fifo_empty, fifo_full );
  input [7:0] write_data;
  output [7:0] read_data;
  input clk, n_rst, read_enable, write_enable;
  output fifo_empty, fifo_full;


  fifo WRAP ( .r_clk(clk), .w_clk(clk), .n_rst(n_rst), .r_enable(read_enable), 
        .w_enable(write_enable), .w_data(write_data), .r_data(read_data), 
        .empty(fifo_empty), .full(fifo_full) );
endmodule


module flex_pts_sr_NUM_BITS8_SHIFT_MSB1 ( clk, n_rst, shift_enable, 
        load_enable, parallel_in, serial_out );
  input [7:0] parallel_in;
  input clk, n_rst, shift_enable, load_enable;
  output serial_out;
  wire   n18, n19, n20, n21, n22, n23, n24, n25, n26, n27, n28, n29, n30, n31,
         n32, n33, n34, n35, n9, n10, n11, n12, n13, n14, n15, n16, n17;
  wire   [6:0] ip_nxt;

  DFFSR \ip_nxt_reg[0]  ( .D(n35), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        ip_nxt[0]) );
  DFFSR \ip_nxt_reg[1]  ( .D(n34), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        ip_nxt[1]) );
  DFFSR \ip_nxt_reg[2]  ( .D(n33), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        ip_nxt[2]) );
  DFFSR \ip_nxt_reg[3]  ( .D(n32), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        ip_nxt[3]) );
  DFFSR \ip_nxt_reg[4]  ( .D(n31), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        ip_nxt[4]) );
  DFFSR \ip_nxt_reg[5]  ( .D(n30), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        ip_nxt[5]) );
  DFFSR \ip_nxt_reg[6]  ( .D(n29), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        ip_nxt[6]) );
  DFFSR \ip_nxt_reg[7]  ( .D(n28), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        serial_out) );
  OAI21X1 U19 ( .A(n17), .B(n16), .C(n18), .Y(n28) );
  AOI22X1 U20 ( .A(ip_nxt[6]), .B(n19), .C(parallel_in[7]), .D(load_enable), 
        .Y(n18) );
  OAI21X1 U21 ( .A(n15), .B(n17), .C(n20), .Y(n29) );
  AOI22X1 U22 ( .A(ip_nxt[5]), .B(n19), .C(parallel_in[6]), .D(load_enable), 
        .Y(n20) );
  OAI21X1 U23 ( .A(n17), .B(n14), .C(n21), .Y(n30) );
  AOI22X1 U24 ( .A(ip_nxt[4]), .B(n19), .C(parallel_in[5]), .D(load_enable), 
        .Y(n21) );
  OAI21X1 U25 ( .A(n17), .B(n13), .C(n22), .Y(n31) );
  AOI22X1 U26 ( .A(ip_nxt[3]), .B(n19), .C(parallel_in[4]), .D(load_enable), 
        .Y(n22) );
  OAI21X1 U27 ( .A(n17), .B(n12), .C(n23), .Y(n32) );
  AOI22X1 U28 ( .A(ip_nxt[2]), .B(n19), .C(parallel_in[3]), .D(load_enable), 
        .Y(n23) );
  OAI21X1 U29 ( .A(n17), .B(n11), .C(n24), .Y(n33) );
  AOI22X1 U30 ( .A(ip_nxt[1]), .B(n19), .C(parallel_in[2]), .D(load_enable), 
        .Y(n24) );
  OAI21X1 U31 ( .A(n17), .B(n10), .C(n25), .Y(n34) );
  AOI22X1 U32 ( .A(ip_nxt[0]), .B(n19), .C(parallel_in[1]), .D(load_enable), 
        .Y(n25) );
  NOR2X1 U33 ( .A(n26), .B(load_enable), .Y(n19) );
  OAI21X1 U34 ( .A(n17), .B(n9), .C(n27), .Y(n35) );
  NAND2X1 U35 ( .A(parallel_in[0]), .B(load_enable), .Y(n27) );
  NOR2X1 U36 ( .A(load_enable), .B(shift_enable), .Y(n26) );
  INVX2 U10 ( .A(ip_nxt[0]), .Y(n9) );
  INVX2 U11 ( .A(ip_nxt[1]), .Y(n10) );
  INVX2 U12 ( .A(ip_nxt[2]), .Y(n11) );
  INVX2 U13 ( .A(ip_nxt[3]), .Y(n12) );
  INVX2 U14 ( .A(ip_nxt[4]), .Y(n13) );
  INVX2 U15 ( .A(ip_nxt[5]), .Y(n14) );
  INVX2 U16 ( .A(ip_nxt[6]), .Y(n15) );
  INVX2 U17 ( .A(serial_out), .Y(n16) );
  INVX2 U18 ( .A(n26), .Y(n17) );
endmodule


module tx_sr ( clk, n_rst, falling_edge_found, tx_enable, tx_data, load_data, 
        tx_out );
  input [7:0] tx_data;
  input clk, n_rst, falling_edge_found, tx_enable, load_data;
  output tx_out;
  wire   se;

  AND2X2 U1 ( .A(tx_enable), .B(falling_edge_found), .Y(se) );
  flex_pts_sr_NUM_BITS8_SHIFT_MSB1 SHIFT_REGISTER ( .clk(clk), .n_rst(n_rst), 
        .shift_enable(se), .load_enable(load_data), .parallel_in(tx_data), 
        .serial_out(tx_out) );
endmodule


module flex_counter_NUM_CNT_BITS4 ( clk, n_rst, count_enable, clear, 
        rollover_val, count_out, rollover_flag );
  input [3:0] rollover_val;
  output [3:0] count_out;
  input clk, n_rst, count_enable, clear;
  output rollover_flag;
  wire   N7, N8, N9, N10, N11, n20, n21, n22, n23, n24, n25, n26, n27, n28,
         n29, n30, n31, n32, n33, n34, n35, n36, n37, n38, n39, n40, n41, n1,
         n2, n3, n4, n5, n6, n12, n13, n14, n15, n16, n17, n18;

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
  OAI21X1 U17 ( .A(n20), .B(n21), .C(n22), .Y(n37) );
  NAND2X1 U18 ( .A(rollover_flag), .B(n23), .Y(n22) );
  NAND3X1 U19 ( .A(n24), .B(n25), .C(n26), .Y(n21) );
  XOR2X1 U20 ( .A(n14), .B(N8), .Y(n26) );
  XOR2X1 U21 ( .A(n16), .B(N10), .Y(n25) );
  XOR2X1 U22 ( .A(n15), .B(N9), .Y(n24) );
  NAND2X1 U23 ( .A(n27), .B(n28), .Y(n20) );
  XOR2X1 U24 ( .A(n13), .B(N7), .Y(n28) );
  NOR2X1 U25 ( .A(N11), .B(n29), .Y(n27) );
  OAI21X1 U26 ( .A(n30), .B(n16), .C(n31), .Y(n38) );
  NAND3X1 U27 ( .A(n32), .B(count_out[1]), .C(n33), .Y(n31) );
  NOR2X1 U28 ( .A(count_out[3]), .B(n15), .Y(n33) );
  AOI21X1 U29 ( .A(n17), .B(n15), .C(n34), .Y(n30) );
  OAI21X1 U30 ( .A(n6), .B(n15), .C(n35), .Y(n39) );
  NAND3X1 U31 ( .A(count_out[1]), .B(n15), .C(n32), .Y(n35) );
  OAI21X1 U32 ( .A(count_out[1]), .B(clear), .C(n36), .Y(n34) );
  OAI22X1 U33 ( .A(n36), .B(n14), .C(count_out[1]), .D(n12), .Y(n40) );
  NOR2X1 U34 ( .A(n29), .B(n13), .Y(n32) );
  AOI21X1 U35 ( .A(n13), .B(n17), .C(n23), .Y(n36) );
  OAI22X1 U36 ( .A(n13), .B(n18), .C(count_out[0]), .D(n29), .Y(n41) );
  NAND2X1 U37 ( .A(n18), .B(n17), .Y(n29) );
  NOR2X1 U38 ( .A(clear), .B(count_enable), .Y(n23) );
  NOR2X1 U6 ( .A(rollover_val[1]), .B(rollover_val[0]), .Y(n2) );
  AOI21X1 U9 ( .A(rollover_val[0]), .B(rollover_val[1]), .C(n2), .Y(n1) );
  NAND2X1 U10 ( .A(n2), .B(n5), .Y(n3) );
  OAI21X1 U11 ( .A(n2), .B(n5), .C(n3), .Y(N9) );
  NOR2X1 U12 ( .A(n3), .B(rollover_val[3]), .Y(N11) );
  AOI21X1 U13 ( .A(n3), .B(rollover_val[3]), .C(N11), .Y(n4) );
  INVX2 U14 ( .A(rollover_val[2]), .Y(n5) );
  INVX2 U15 ( .A(rollover_val[0]), .Y(N7) );
  INVX2 U16 ( .A(n4), .Y(N10) );
  INVX2 U39 ( .A(n1), .Y(N8) );
  INVX2 U40 ( .A(n34), .Y(n6) );
  INVX2 U41 ( .A(n32), .Y(n12) );
  INVX2 U42 ( .A(count_out[0]), .Y(n13) );
  INVX2 U43 ( .A(count_out[1]), .Y(n14) );
  INVX2 U44 ( .A(count_out[2]), .Y(n15) );
  INVX2 U45 ( .A(count_out[3]), .Y(n16) );
  INVX2 U46 ( .A(clear), .Y(n17) );
  INVX2 U47 ( .A(n23), .Y(n18) );
endmodule


module timer ( clk, n_rst, rising_edge_found, falling_edge_found, stop_found, 
        start_found, byte_received, ack_prep, check_ack, ack_done );
  input clk, n_rst, rising_edge_found, falling_edge_found, stop_found,
         start_found;
  output byte_received, ack_prep, check_ack, ack_done;
  wire   _0_net_, rollover_flag, N39, n1, n2, n3, n4, n5, n6, n20, n21, n22,
         n23, n24, n25, n26, n27, n28, n11, n12, n13, n15, n16, n17, n18, n19;
  wire   [3:0] count_out;
  wire   [2:0] state;
  wire   [2:0] nextstate;

  DFFSR \state_reg[0]  ( .D(n12), .CLK(clk), .R(n_rst), .S(1'b1), .Q(state[0])
         );
  DFFSR \state_reg[1]  ( .D(nextstate[1]), .CLK(clk), .R(n_rst), .S(1'b1), .Q(
        state[1]) );
  DFFSR \state_reg[2]  ( .D(nextstate[2]), .CLK(clk), .R(n_rst), .S(1'b1), .Q(
        state[2]) );
  MUX2X1 U3 ( .B(falling_edge_found), .A(n15), .S(state[0]), .Y(n1) );
  MUX2X1 U4 ( .B(n3), .A(n4), .S(state[2]), .Y(n2) );
  NOR2X1 U5 ( .A(state[2]), .B(n1), .Y(n5) );
  MUX2X1 U6 ( .B(start_found), .A(N39), .S(state[0]), .Y(n3) );
  NAND2X1 U7 ( .A(falling_edge_found), .B(n16), .Y(n4) );
  MUX2X1 U8 ( .B(n2), .A(n5), .S(state[1]), .Y(n6) );
  OR2X2 U14 ( .A(start_found), .B(ack_done), .Y(_0_net_) );
  OAI21X1 U24 ( .A(falling_edge_found), .B(n20), .C(n21), .Y(nextstate[2]) );
  OAI21X1 U25 ( .A(n17), .B(n22), .C(n23), .Y(nextstate[1]) );
  OAI21X1 U26 ( .A(n15), .B(n16), .C(n18), .Y(n22) );
  NAND3X1 U27 ( .A(state[0]), .B(state[1]), .C(n24), .Y(n21) );
  NOR2X1 U28 ( .A(state[2]), .B(n15), .Y(n24) );
  NAND3X1 U29 ( .A(state[0]), .B(n11), .C(n25), .Y(n23) );
  NOR2X1 U30 ( .A(state[2]), .B(state[1]), .Y(n25) );
  NOR2X1 U31 ( .A(n26), .B(n27), .Y(ack_prep) );
  NAND2X1 U32 ( .A(falling_edge_found), .B(state[1]), .Y(n27) );
  NAND2X1 U33 ( .A(n16), .B(n18), .Y(n26) );
  NOR2X1 U34 ( .A(n19), .B(n20), .Y(ack_done) );
  NAND3X1 U35 ( .A(n16), .B(n17), .C(state[2]), .Y(n20) );
  NAND3X1 U36 ( .A(count_out[3]), .B(n13), .C(n28), .Y(N39) );
  NOR2X1 U37 ( .A(count_out[2]), .B(count_out[1]), .Y(n28) );
  flex_counter_NUM_CNT_BITS4 CTR ( .clk(clk), .n_rst(n_rst), .count_enable(
        rising_edge_found), .clear(_0_net_), .rollover_val({1'b1, 1'b0, 1'b0, 
        1'b1}), .count_out(count_out), .rollover_flag(rollover_flag) );
  INVX2 U9 ( .A(n23), .Y(byte_received) );
  INVX2 U10 ( .A(N39), .Y(n11) );
  INVX2 U15 ( .A(n6), .Y(n12) );
  INVX2 U16 ( .A(count_out[0]), .Y(n13) );
  INVX2 U17 ( .A(n21), .Y(check_ack) );
  INVX2 U18 ( .A(rollover_flag), .Y(n15) );
  INVX2 U19 ( .A(state[0]), .Y(n16) );
  INVX2 U20 ( .A(state[1]), .Y(n17) );
  INVX2 U21 ( .A(state[2]), .Y(n18) );
  INVX2 U22 ( .A(falling_edge_found), .Y(n19) );
endmodule


module controller ( clk, n_rst, stop_found, start_found, byte_received, 
        ack_prep, check_ack, ack_done, rw_mode, address_match, sda_in, 
        rx_enable, tx_enable, read_enable, sda_mode, load_data );
  output [1:0] sda_mode;
  input clk, n_rst, stop_found, start_found, byte_received, ack_prep,
         check_ack, ack_done, rw_mode, address_match, sda_in;
  output rx_enable, tx_enable, read_enable, load_data;
  wire   n20, n21, n22, n23, n24, n25, n26, n27, n28, n29, n30, n31, n32, n33,
         n34, n35, n36, n37, n38, n39, n40, n41, n42, n43, n44, n45, n46, n47,
         n48, n49, n50, n51, n52, n53, n54, n55, n56, n5, n7, n8, n9, n10, n11,
         n13, n14, n15, n16, n17, n18, n19;
  wire   [3:0] state;
  wire   [3:0] nextstate;

  DFFSR \state_reg[0]  ( .D(nextstate[0]), .CLK(clk), .R(n_rst), .S(1'b1), .Q(
        state[0]) );
  DFFSR \state_reg[1]  ( .D(nextstate[1]), .CLK(clk), .R(n_rst), .S(1'b1), .Q(
        state[1]) );
  DFFSR \state_reg[2]  ( .D(nextstate[2]), .CLK(clk), .R(n_rst), .S(1'b1), .Q(
        state[2]) );
  DFFSR \state_reg[3]  ( .D(nextstate[3]), .CLK(clk), .R(n_rst), .S(1'b1), .Q(
        state[3]) );
  OR2X2 U7 ( .A(read_enable), .B(n7), .Y(n27) );
  OR2X2 U8 ( .A(n25), .B(read_enable), .Y(n38) );
  AND2X2 U9 ( .A(n51), .B(n29), .Y(n36) );
  AND2X2 U10 ( .A(n48), .B(n9), .Y(n31) );
  AND2X2 U11 ( .A(address_match), .B(rw_mode), .Y(n52) );
  OAI21X1 U27 ( .A(n20), .B(n14), .C(n21), .Y(sda_mode[1]) );
  NAND2X1 U28 ( .A(n21), .B(n22), .Y(sda_mode[0]) );
  NAND2X1 U29 ( .A(n23), .B(n24), .Y(nextstate[3]) );
  AOI22X1 U30 ( .A(tx_enable), .B(ack_prep), .C(n17), .D(n25), .Y(n24) );
  AOI21X1 U31 ( .A(n26), .B(n16), .C(n27), .Y(n23) );
  NAND3X1 U32 ( .A(n28), .B(n29), .C(n30), .Y(nextstate[2]) );
  AOI21X1 U33 ( .A(n31), .B(n32), .C(n33), .Y(n30) );
  OAI21X1 U34 ( .A(n14), .B(n34), .C(n22), .Y(n33) );
  NAND2X1 U35 ( .A(n8), .B(n17), .Y(n34) );
  NAND2X1 U36 ( .A(rw_mode), .B(address_match), .Y(n32) );
  AOI22X1 U37 ( .A(n10), .B(ack_prep), .C(n25), .D(ack_done), .Y(n28) );
  NAND3X1 U38 ( .A(n35), .B(n36), .C(n37), .Y(nextstate[1]) );
  NOR2X1 U39 ( .A(n38), .B(n39), .Y(n37) );
  OAI21X1 U40 ( .A(n40), .B(n5), .C(n41), .Y(n39) );
  NAND3X1 U41 ( .A(check_ack), .B(n7), .C(sda_in), .Y(n41) );
  NOR2X1 U42 ( .A(n42), .B(state[0]), .Y(n25) );
  AOI22X1 U43 ( .A(n10), .B(n18), .C(n11), .D(ack_done), .Y(n35) );
  NAND3X1 U44 ( .A(n44), .B(n36), .C(n45), .Y(nextstate[0]) );
  AOI21X1 U45 ( .A(n11), .B(n17), .C(n46), .Y(n45) );
  OAI21X1 U46 ( .A(n47), .B(n19), .C(n43), .Y(n46) );
  NAND3X1 U47 ( .A(n48), .B(n14), .C(state[0]), .Y(n43) );
  AOI22X1 U48 ( .A(n26), .B(n49), .C(n8), .D(n14), .Y(n47) );
  NAND3X1 U49 ( .A(n13), .B(n15), .C(n9), .Y(n20) );
  NAND3X1 U50 ( .A(state[0]), .B(state[2]), .C(n50), .Y(n22) );
  NOR2X1 U51 ( .A(state[3]), .B(state[1]), .Y(n50) );
  AOI21X1 U52 ( .A(n18), .B(tx_enable), .C(load_data), .Y(n29) );
  AOI22X1 U53 ( .A(n52), .B(n31), .C(n16), .D(n26), .Y(n51) );
  NOR2X1 U54 ( .A(n42), .B(n9), .Y(n26) );
  NAND3X1 U55 ( .A(state[1]), .B(n14), .C(state[3]), .Y(n42) );
  OAI21X1 U56 ( .A(n17), .B(n19), .C(n49), .Y(n53) );
  NAND2X1 U57 ( .A(stop_found), .B(ack_done), .Y(n49) );
  AOI22X1 U58 ( .A(check_ack), .B(n7), .C(rx_enable), .D(n5), .Y(n44) );
  NAND3X1 U59 ( .A(state[3]), .B(n9), .C(n55), .Y(n54) );
  NOR2X1 U60 ( .A(state[2]), .B(state[1]), .Y(n55) );
  NOR2X1 U61 ( .A(n15), .B(n40), .Y(read_enable) );
  NAND3X1 U62 ( .A(n48), .B(state[2]), .C(state[0]), .Y(n21) );
  NAND3X1 U63 ( .A(state[2]), .B(n9), .C(n48), .Y(n56) );
  NOR2X1 U64 ( .A(n13), .B(state[3]), .Y(n48) );
  NOR2X1 U65 ( .A(n40), .B(state[3]), .Y(rx_enable) );
  NAND3X1 U66 ( .A(n13), .B(n14), .C(state[0]), .Y(n40) );
  INVX2 U12 ( .A(byte_received), .Y(n5) );
  INVX2 U13 ( .A(n56), .Y(load_data) );
  INVX2 U14 ( .A(n54), .Y(n7) );
  INVX2 U15 ( .A(n20), .Y(n8) );
  INVX2 U16 ( .A(state[0]), .Y(n9) );
  INVX2 U17 ( .A(n43), .Y(n10) );
  INVX2 U18 ( .A(n22), .Y(n11) );
  INVX2 U19 ( .A(n21), .Y(tx_enable) );
  INVX2 U20 ( .A(state[1]), .Y(n13) );
  INVX2 U21 ( .A(state[2]), .Y(n14) );
  INVX2 U22 ( .A(state[3]), .Y(n15) );
  INVX2 U23 ( .A(n53), .Y(n16) );
  INVX2 U24 ( .A(ack_done), .Y(n17) );
  INVX2 U25 ( .A(ack_prep), .Y(n18) );
  INVX2 U26 ( .A(start_found), .Y(n19) );
endmodule


module i2c_slave ( clk, n_rst, scl, sda_in, sda_out, write_enable, write_data, 
        fifo_empty, fifo_full );
  input [7:0] write_data;
  input clk, n_rst, scl, sda_in, write_enable;
  output sda_out, fifo_empty, fifo_full;
  wire   rising_edge_found, falling_edge_found, rw_mode, address_match,
         stop_found, start_found, rx_enable, tx_out, read_enable, tx_enable,
         load_data, byte_received, ack_prep, check_ack, ack_done;
  wire   [7:0] rx_data;
  wire   [1:0] sda_mode;
  wire   [7:0] read_data;

  scl_edge edge_det ( .clk(clk), .n_rst(n_rst), .scl(scl), .rising_edge_found(
        rising_edge_found), .falling_edge_found(falling_edge_found) );
  decode decoder ( .clk(clk), .n_rst(n_rst), .scl(scl), .sda_in(sda_in), 
        .starting_byte(rx_data), .rw_mode(rw_mode), .address_match(
        address_match), .stop_found(stop_found), .start_found(start_found) );
  rx_sr rx_shift ( .clk(clk), .n_rst(n_rst), .sda_in(sda_in), .rx_enable(
        rx_enable), .rising_edge_found(rising_edge_found), .rx_data(rx_data)
         );
  sda_sel select_block ( .tx_out(tx_out), .sda_mode(sda_mode), .sda_out(
        sda_out) );
  tx_fifo fifo ( .clk(clk), .n_rst(n_rst), .read_enable(read_enable), 
        .write_enable(write_enable), .write_data(write_data), .read_data(
        read_data), .fifo_empty(fifo_empty), .fifo_full(fifo_full) );
  tx_sr tx_shift ( .clk(clk), .n_rst(n_rst), .falling_edge_found(
        falling_edge_found), .tx_enable(tx_enable), .tx_data(read_data), 
        .load_data(load_data), .tx_out(tx_out) );
  timer timer_block ( .clk(clk), .n_rst(n_rst), .rising_edge_found(
        rising_edge_found), .falling_edge_found(falling_edge_found), 
        .stop_found(1'b0), .start_found(start_found), .byte_received(
        byte_received), .ack_prep(ack_prep), .check_ack(check_ack), .ack_done(
        ack_done) );
  controller slv_controller ( .clk(clk), .n_rst(n_rst), .stop_found(stop_found), .start_found(start_found), .byte_received(byte_received), .ack_prep(ack_prep), .check_ack(check_ack), .ack_done(ack_done), .rw_mode(rw_mode), 
        .address_match(address_match), .sda_in(sda_in), .rx_enable(rx_enable), 
        .tx_enable(tx_enable), .read_enable(read_enable), .sda_mode(sda_mode), 
        .load_data(load_data) );
endmodule

