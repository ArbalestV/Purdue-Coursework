
module sync ( clk, n_rst, async_in, sync_out );
  input clk, n_rst, async_in;
  output sync_out;
  wire   d;

  DFFSR d_reg ( .D(async_in), .CLK(clk), .R(n_rst), .S(1'b1), .Q(d) );
  DFFSR sync_out_reg ( .D(d), .CLK(clk), .R(n_rst), .S(1'b1), .Q(sync_out) );
endmodule


module controller ( clk, n_reset, dr, overflow, cnt_up, modwait, op, src1, 
        src2, dest, err );
  output [1:0] op;
  output [3:0] src1;
  output [3:0] src2;
  output [3:0] dest;
  input clk, n_reset, dr, overflow;
  output cnt_up, modwait, err;
  wire   N17, net4811, net4817, net6530, net20013, net20015, net20036,
         net20037, net20038, net20039, net20041, net20048, net20057, net20067,
         net20438, net20476, net20479, net20483, net21409, net21446, net21475,
         net21557, net21559, net21560, net21564, net21692, net21696, net21733,
         net21757, net21767, net21795, net21794, net21801, net21836, net21901,
         net21701, net20420, net20051, net20023, net20022, net21556, net20024,
         net21741, net21412, net26912, net21530, net21529, net20032, net20016,
         net21769, net21743, net21552, net21411, net21410, net20448, net20404,
         net20403, net21617, net20445, net20351, net20349, net21895, net21738,
         net21687, net21416, net21413, net20363, net20362, net20035, net20034,
         net62652, net62765, net62764, net21636, net20030, net20029, net21612,
         net20397, net20033, n5, n6, n8, n9, n10, n11, n12, n13, n14, n15, n16,
         n17, n18, n19, n20, n21;
  wire   [3:0] state;
  wire   [3:0] nextstate;
  assign dest[3] = 1'b0;
  assign src2[3] = 1'b0;
  assign src1[3] = 1'b0;
  assign err = N17;
  assign src2[0] = net4811;
  assign cnt_up = net4817;
  assign src2[2] = net6530;

  DFFSR \state_reg[0]  ( .D(nextstate[0]), .CLK(clk), .R(1'b1), .S(n_reset), 
        .Q(state[0]) );
  DFFSR \state_reg[1]  ( .D(nextstate[1]), .CLK(clk), .R(n_reset), .S(1'b1), 
        .Q(state[1]) );
  DFFSR \state_reg[3]  ( .D(nextstate[3]), .CLK(clk), .R(n_reset), .S(1'b1), 
        .Q(state[3]) );
  DFFSR \state_reg[2]  ( .D(net20483), .CLK(clk), .R(n_reset), .S(1'b1), .Q(
        state[2]) );
  AND2X2 U7 ( .A(net62765), .B(net21557), .Y(n5) );
  INVX2 U8 ( .A(net62764), .Y(net62765) );
  AND2X2 U9 ( .A(net21767), .B(net20033), .Y(net20397) );
  BUFX4 U10 ( .A(state[3]), .Y(net21767) );
  INVX2 U11 ( .A(net21612), .Y(net20033) );
  AOI22X1 U12 ( .A(net21416), .B(net20397), .C(net21412), .D(net21556), .Y(
        net20024) );
  NAND2X1 U13 ( .A(net20397), .B(net21559), .Y(net20037) );
  AOI22X1 U14 ( .A(net21416), .B(net20397), .C(net21413), .D(net21687), .Y(
        net20030) );
  INVX1 U15 ( .A(net20397), .Y(net21794) );
  BUFX2 U16 ( .A(state[0]), .Y(net21612) );
  AND2X2 U17 ( .A(net20363), .B(net20033), .Y(net62652) );
  INVX1 U18 ( .A(net21612), .Y(net21617) );
  NAND2X1 U19 ( .A(net21636), .B(net20030), .Y(src1[0]) );
  OR2X1 U20 ( .A(net20445), .B(net20029), .Y(net21636) );
  BUFX2 U21 ( .A(net21767), .Y(net20445) );
  NAND2X1 U22 ( .A(net20351), .B(net21617), .Y(net20029) );
  INVX2 U23 ( .A(net20349), .Y(net20351) );
  AND2X2 U24 ( .A(net20035), .B(net20034), .Y(net21416) );
  AND2X2 U25 ( .A(net20351), .B(net20363), .Y(net21413) );
  INVX1 U26 ( .A(net21767), .Y(net21687) );
  INVX1 U27 ( .A(net21412), .Y(net62764) );
  INVX1 U28 ( .A(overflow), .Y(n12) );
  NAND3X1 U29 ( .A(net21692), .B(net21687), .C(net62652), .Y(net20038) );
  NAND3X1 U30 ( .A(net21733), .B(net21687), .C(net21696), .Y(net20039) );
  INVX4 U31 ( .A(net20363), .Y(net20034) );
  AND2X2 U32 ( .A(net20035), .B(net20034), .Y(net21559) );
  AND2X2 U33 ( .A(net21769), .B(net20034), .Y(net20448) );
  AND2X2 U34 ( .A(net21738), .B(net20034), .Y(net21552) );
  INVX4 U35 ( .A(net20362), .Y(net20363) );
  INVX2 U36 ( .A(state[1]), .Y(net20362) );
  INVX1 U37 ( .A(net20362), .Y(net21741) );
  INVX2 U38 ( .A(net21895), .Y(net20035) );
  AND2X2 U39 ( .A(net21741), .B(net20035), .Y(net21412) );
  BUFX2 U40 ( .A(state[2]), .Y(net21895) );
  INVX1 U41 ( .A(net21895), .Y(net21692) );
  INVX1 U42 ( .A(net21895), .Y(net21738) );
  NAND2X1 U43 ( .A(net21413), .B(net21556), .Y(net20036) );
  INVX1 U44 ( .A(state[0]), .Y(net20403) );
  BUFX2 U45 ( .A(net21617), .Y(net21901) );
  NAND2X1 U46 ( .A(net20032), .B(net20351), .Y(net21529) );
  NAND3X1 U47 ( .A(net20351), .B(net20420), .C(net20051), .Y(net20022) );
  INVX1 U48 ( .A(state[2]), .Y(net20349) );
  INVX1 U49 ( .A(net20349), .Y(net21743) );
  INVX1 U50 ( .A(net20445), .Y(net21564) );
  OAI21X1 U51 ( .A(net20445), .B(net21409), .C(net20013), .Y(modwait) );
  AOI22X1 U52 ( .A(net21552), .B(net21410), .C(net21411), .D(net20448), .Y(n6)
         );
  NAND2X1 U53 ( .A(net20016), .B(n6), .Y(src1[2]) );
  AND2X2 U54 ( .A(net20404), .B(net21767), .Y(net21410) );
  NAND2X1 U55 ( .A(net21410), .B(net21559), .Y(net20023) );
  INVX2 U56 ( .A(net20403), .Y(net20404) );
  AND2X2 U57 ( .A(net20404), .B(net21743), .Y(net21411) );
  BUFX2 U58 ( .A(net20404), .Y(net21560) );
  INVX1 U59 ( .A(net20403), .Y(net21701) );
  NAND2X1 U60 ( .A(net21411), .B(net20448), .Y(net20041) );
  INVX1 U61 ( .A(net21767), .Y(net21769) );
  NAND2X1 U62 ( .A(net62652), .B(net21530), .Y(net20016) );
  INVX2 U63 ( .A(net21529), .Y(net21530) );
  NAND2X1 U64 ( .A(net62652), .B(net21530), .Y(net21757) );
  INVX2 U65 ( .A(net21767), .Y(net20032) );
  BUFX2 U66 ( .A(net20032), .Y(net26912) );
  AND2X2 U67 ( .A(net21701), .B(net20032), .Y(net21556) );
  NAND2X1 U68 ( .A(net62765), .B(net21557), .Y(net20048) );
  INVX2 U69 ( .A(net21741), .Y(net20420) );
  NAND3X1 U70 ( .A(net20023), .B(net20022), .C(net20024), .Y(src1[1]) );
  NAND2X1 U71 ( .A(net20037), .B(net20023), .Y(net20057) );
  INVX1 U72 ( .A(net20023), .Y(net4811) );
  NAND3X1 U73 ( .A(net20022), .B(net20048), .C(net21446), .Y(nextstate[2]) );
  NAND3X1 U74 ( .A(net21475), .B(net20476), .C(net20022), .Y(dest[1]) );
  NOR2X1 U75 ( .A(net21767), .B(net21701), .Y(net20051) );
  INVX1 U76 ( .A(net20420), .Y(net21733) );
  AND2X2 U77 ( .A(net21692), .B(net20420), .Y(net21409) );
  NAND3X1 U78 ( .A(net21836), .B(net20420), .C(net20438), .Y(net20013) );
  INVX2 U79 ( .A(net21564), .Y(net21836) );
  INVX1 U80 ( .A(net20067), .Y(net21801) );
  INVX1 U81 ( .A(net21794), .Y(net21795) );
  INVX1 U82 ( .A(net21692), .Y(net21696) );
  INVX1 U83 ( .A(op[1]), .Y(n11) );
  AND2X2 U84 ( .A(net21560), .B(net26912), .Y(net21557) );
  AND2X2 U85 ( .A(net21757), .B(net20041), .Y(net21446) );
  AND2X2 U86 ( .A(n9), .B(net20036), .Y(net21475) );
  NAND2X1 U87 ( .A(n8), .B(net20015), .Y(op[0]) );
  AND2X2 U88 ( .A(net20067), .B(net20036), .Y(n8) );
  INVX2 U89 ( .A(net20057), .Y(net20067) );
  INVX1 U90 ( .A(net20015), .Y(net20483) );
  INVX2 U91 ( .A(net4811), .Y(net20479) );
  NAND2X1 U92 ( .A(net21409), .B(net21795), .Y(n9) );
  BUFX2 U93 ( .A(net20041), .Y(net20476) );
  BUFX2 U94 ( .A(net21692), .Y(net20438) );
  INVX2 U95 ( .A(nextstate[2]), .Y(net20015) );
  NOR2X1 U96 ( .A(overflow), .B(net21475), .Y(nextstate[3]) );
  NAND2X1 U97 ( .A(n8), .B(net20038), .Y(op[1]) );
  NAND2X1 U98 ( .A(net21409), .B(net21557), .Y(n13) );
  NAND3X1 U99 ( .A(net21409), .B(net21901), .C(net21564), .Y(n20) );
  NAND2X1 U100 ( .A(n13), .B(n20), .Y(n18) );
  NOR2X1 U101 ( .A(n5), .B(n18), .Y(n10) );
  NAND3X1 U102 ( .A(net20476), .B(n11), .C(n10), .Y(n17) );
  NAND2X1 U103 ( .A(n12), .B(net21801), .Y(n16) );
  INVX2 U104 ( .A(n13), .Y(n14) );
  INVX2 U105 ( .A(net20038), .Y(net4817) );
  MUX2X1 U106 ( .B(n14), .A(net4817), .S(dr), .Y(n15) );
  NAND3X1 U107 ( .A(n17), .B(n15), .C(n16), .Y(nextstate[0]) );
  OAI21X1 U108 ( .A(net4817), .B(n18), .C(dr), .Y(n19) );
  NAND2X1 U109 ( .A(net21446), .B(n19), .Y(nextstate[1]) );
  INVX2 U110 ( .A(n20), .Y(N17) );
  NOR2X1 U111 ( .A(net4817), .B(n5), .Y(n21) );
  NAND3X1 U112 ( .A(net20476), .B(n9), .C(n21), .Y(dest[0]) );
  NAND3X1 U113 ( .A(n9), .B(net20038), .C(net20039), .Y(dest[2]) );
  NAND2X1 U114 ( .A(net20036), .B(net20479), .Y(src2[1]) );
  INVX2 U115 ( .A(net20013), .Y(net6530) );
endmodule


module flex_counter_NUM_CNT_BITS10_DW01_inc_1 ( A, SUM );
  input [9:0] A;
  output [9:0] SUM;
  wire   n2, n3, n4, n5, n6, n7, n9, n10, n11, n13, n14, n15, n17, n19, n21,
         n22, n23, n24, n25, n26, n28, n29, n31, n32, n33, n35, n60, n61;
  assign n7 = A[7];
  assign n11 = A[6];
  assign n17 = A[5];
  assign n21 = A[4];
  assign n26 = A[3];
  assign n29 = A[2];
  assign n33 = A[1];
  assign n35 = A[0];

  XOR2X1 U3 ( .A(n4), .B(n3), .Y(SUM[8]) );
  NOR2X1 U4 ( .A(n3), .B(n4), .Y(n2) );
  NAND2X1 U7 ( .A(n24), .B(n5), .Y(n4) );
  NOR2X1 U8 ( .A(n6), .B(n14), .Y(n5) );
  NAND2X1 U9 ( .A(n7), .B(n11), .Y(n6) );
  NOR2X1 U13 ( .A(n10), .B(n23), .Y(n9) );
  NAND2X1 U14 ( .A(n11), .B(n15), .Y(n10) );
  NOR2X1 U18 ( .A(n14), .B(n23), .Y(n13) );
  NAND2X1 U21 ( .A(n17), .B(n21), .Y(n14) );
  XOR2X1 U24 ( .A(n23), .B(n22), .Y(SUM[4]) );
  NOR2X1 U25 ( .A(n22), .B(n23), .Y(n19) );
  NOR2X1 U31 ( .A(n32), .B(n25), .Y(n24) );
  NAND2X1 U32 ( .A(n26), .B(n29), .Y(n25) );
  NAND2X1 U36 ( .A(n29), .B(n31), .Y(n28) );
  NAND2X1 U41 ( .A(n35), .B(n33), .Y(n32) );
  BUFX2 U48 ( .A(n33), .Y(n60) );
  INVX1 U49 ( .A(SUM[0]), .Y(n61) );
  INVX1 U50 ( .A(n35), .Y(SUM[0]) );
  XOR2X1 U51 ( .A(n13), .B(n11), .Y(SUM[6]) );
  XOR2X1 U52 ( .A(n19), .B(n17), .Y(SUM[5]) );
  XNOR2X1 U53 ( .A(n28), .B(n26), .Y(SUM[3]) );
  XOR2X1 U54 ( .A(n2), .B(A[9]), .Y(SUM[9]) );
  XOR2X1 U55 ( .A(n9), .B(n7), .Y(SUM[7]) );
  XOR2X1 U56 ( .A(n31), .B(n29), .Y(SUM[2]) );
  XOR2X1 U57 ( .A(n60), .B(n61), .Y(SUM[1]) );
  INVX2 U58 ( .A(n32), .Y(n31) );
  INVX2 U59 ( .A(A[8]), .Y(n3) );
  INVX2 U60 ( .A(n24), .Y(n23) );
  INVX2 U61 ( .A(n21), .Y(n22) );
  INVX2 U62 ( .A(n14), .Y(n15) );
endmodule


module flex_counter_NUM_CNT_BITS10 ( clk, n_rst, count_enable, clear, 
        rollover_val, count_out, rollover_flag );
  input [9:0] rollover_val;
  output [9:0] count_out;
  input clk, n_rst, count_enable, clear;
  output rollover_flag;
  wire   N3, N4, N5, N7, N8, N9, N17, N18, N19, N20, N21, N22, N23, N24, N25,
         N26, n80, n81, n82, n83, n84, n85, n86, n87, n88, n89, n90, N40, N39,
         N38, N37, N36, N35, N34, N33, N32, N31, n1, n2, n3, n4, n5, n6, n7,
         n8, n9, n10, n22, n23, n24, n25, n26, n27, n28, n29, n30, n31, n32,
         n33, n34, n35, n36, n37, n38, n39, n40, n41, n42, n43, n44, n45, n46,
         n47, n48, n49, n50, n51, n52, n53, n54, n55, n56, n57, n58, n59, n60,
         n61, n62, n63, n64, n65, n66, n67, n68, n69, n70, n71, n72, n73, n74,
         n75, n76, n77, n78, n79, n91, n92, n93, n94, n95, n96, n97, n98, n99,
         n100, n101, n102, n103, n104, n105;

  DFFSR \f_reg[9]  ( .D(n90), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[9])
         );
  DFFSR \f_reg[8]  ( .D(n89), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[8])
         );
  DFFSR \f_reg[7]  ( .D(n88), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[7])
         );
  DFFSR \f_reg[6]  ( .D(n87), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[6])
         );
  DFFSR \f_reg[5]  ( .D(n86), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[5])
         );
  DFFSR \f_reg[4]  ( .D(n85), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[4])
         );
  DFFSR \f_reg[3]  ( .D(n84), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[3])
         );
  DFFSR \f_reg[2]  ( .D(n83), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[2])
         );
  DFFSR \f_reg[1]  ( .D(n82), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[1])
         );
  DFFSR \f_reg[0]  ( .D(n81), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[0])
         );
  DFFSR rollover_flag_reg ( .D(n80), .CLK(clk), .R(n_rst), .S(1'b1), .Q(
        rollover_flag) );
  flex_counter_NUM_CNT_BITS10_DW01_inc_1 add_31_aco ( .A({N40, N39, N38, N37, 
        N36, N35, N34, N33, N32, N31}), .SUM({N26, N25, N24, N23, N22, N21, 
        N20, N19, N18, N17}) );
  AND2X2 U6 ( .A(n42), .B(n41), .Y(n1) );
  INVX4 U15 ( .A(n3), .Y(n5) );
  INVX2 U16 ( .A(n3), .Y(n4) );
  AND2X2 U17 ( .A(n5), .B(n6), .Y(n2) );
  NOR2X1 U18 ( .A(count_enable), .B(clear), .Y(n3) );
  INVX2 U19 ( .A(count_out[2]), .Y(n64) );
  INVX2 U20 ( .A(clear), .Y(n6) );
  NAND2X1 U21 ( .A(N19), .B(n2), .Y(n7) );
  OAI21X1 U22 ( .A(n4), .B(n64), .C(n7), .Y(n83) );
  INVX2 U23 ( .A(count_out[0]), .Y(n70) );
  NAND2X1 U24 ( .A(N17), .B(n2), .Y(n8) );
  OAI21X1 U25 ( .A(n5), .B(n70), .C(n8), .Y(n81) );
  INVX2 U26 ( .A(count_out[1]), .Y(n71) );
  NAND2X1 U27 ( .A(N18), .B(n2), .Y(n9) );
  OAI21X1 U28 ( .A(n4), .B(n71), .C(n9), .Y(n82) );
  INVX2 U29 ( .A(count_out[6]), .Y(n65) );
  NAND2X1 U30 ( .A(N23), .B(n2), .Y(n10) );
  OAI21X1 U31 ( .A(n5), .B(n65), .C(n10), .Y(n87) );
  INVX2 U32 ( .A(count_out[3]), .Y(n47) );
  NAND2X1 U33 ( .A(N20), .B(n2), .Y(n22) );
  OAI21X1 U34 ( .A(n4), .B(n47), .C(n22), .Y(n84) );
  INVX2 U35 ( .A(count_out[7]), .Y(n43) );
  NAND2X1 U36 ( .A(N24), .B(n2), .Y(n23) );
  OAI21X1 U37 ( .A(n5), .B(n43), .C(n23), .Y(n88) );
  INVX2 U38 ( .A(count_out[8]), .Y(n59) );
  NAND2X1 U39 ( .A(N25), .B(n2), .Y(n24) );
  OAI21X1 U40 ( .A(n4), .B(n59), .C(n24), .Y(n89) );
  INVX2 U41 ( .A(count_out[4]), .Y(n72) );
  NAND2X1 U42 ( .A(N21), .B(n2), .Y(n25) );
  OAI21X1 U43 ( .A(n5), .B(n72), .C(n25), .Y(n85) );
  INVX2 U44 ( .A(count_out[5]), .Y(n66) );
  NAND2X1 U45 ( .A(N22), .B(n2), .Y(n26) );
  OAI21X1 U46 ( .A(n4), .B(n66), .C(n26), .Y(n86) );
  XOR2X1 U47 ( .A(n65), .B(rollover_val[6]), .Y(n28) );
  INVX2 U48 ( .A(count_out[9]), .Y(n46) );
  XOR2X1 U49 ( .A(n46), .B(rollover_val[9]), .Y(n27) );
  NAND2X1 U50 ( .A(n28), .B(n27), .Y(n33) );
  XOR2X1 U51 ( .A(n64), .B(rollover_val[2]), .Y(n31) );
  XOR2X1 U52 ( .A(n71), .B(rollover_val[1]), .Y(n30) );
  XOR2X1 U53 ( .A(n70), .B(rollover_val[0]), .Y(n29) );
  NAND3X1 U54 ( .A(n31), .B(n30), .C(n29), .Y(n32) );
  NOR2X1 U55 ( .A(n33), .B(n32), .Y(n42) );
  XOR2X1 U56 ( .A(n66), .B(rollover_val[5]), .Y(n35) );
  XOR2X1 U57 ( .A(n72), .B(rollover_val[4]), .Y(n34) );
  NAND2X1 U58 ( .A(n35), .B(n34), .Y(n40) );
  XOR2X1 U59 ( .A(n47), .B(rollover_val[3]), .Y(n38) );
  XOR2X1 U60 ( .A(n59), .B(rollover_val[8]), .Y(n37) );
  XOR2X1 U61 ( .A(n43), .B(rollover_val[7]), .Y(n36) );
  NAND3X1 U62 ( .A(n38), .B(n37), .C(n36), .Y(n39) );
  NOR2X1 U63 ( .A(n40), .B(n39), .Y(n41) );
  AND2X2 U64 ( .A(n42), .B(n41), .Y(n44) );
  NOR2X1 U65 ( .A(n1), .B(n46), .Y(N40) );
  NOR2X1 U66 ( .A(n44), .B(n59), .Y(N39) );
  NOR2X1 U67 ( .A(n44), .B(n43), .Y(N38) );
  NOR2X1 U68 ( .A(n1), .B(n65), .Y(N37) );
  NOR2X1 U69 ( .A(n44), .B(n66), .Y(N36) );
  NOR2X1 U70 ( .A(n1), .B(n72), .Y(N35) );
  NOR2X1 U71 ( .A(n1), .B(n47), .Y(N34) );
  NOR2X1 U72 ( .A(n1), .B(n64), .Y(N33) );
  NOR2X1 U73 ( .A(n44), .B(n71), .Y(N32) );
  NOR2X1 U74 ( .A(n44), .B(n70), .Y(N31) );
  NAND2X1 U75 ( .A(N26), .B(n2), .Y(n45) );
  OAI21X1 U76 ( .A(n5), .B(n46), .C(n45), .Y(n90) );
  INVX2 U77 ( .A(rollover_flag), .Y(n92) );
  INVX2 U78 ( .A(rollover_val[8]), .Y(n57) );
  NAND2X1 U79 ( .A(n102), .B(n57), .Y(n56) );
  XOR2X1 U80 ( .A(n47), .B(n96), .Y(n53) );
  INVX2 U81 ( .A(rollover_val[7]), .Y(n50) );
  INVX2 U82 ( .A(n101), .Y(n49) );
  INVX2 U83 ( .A(n102), .Y(n48) );
  OAI21X1 U84 ( .A(n50), .B(n49), .C(n48), .Y(n51) );
  XOR2X1 U85 ( .A(n51), .B(count_out[7]), .Y(n52) );
  NOR2X1 U86 ( .A(n53), .B(n52), .Y(n54) );
  OAI21X1 U87 ( .A(rollover_val[9]), .B(n56), .C(n54), .Y(n63) );
  NAND2X1 U88 ( .A(rollover_val[9]), .B(n56), .Y(n55) );
  XOR2X1 U89 ( .A(n55), .B(count_out[9]), .Y(n61) );
  OAI21X1 U90 ( .A(n102), .B(n57), .C(n56), .Y(n58) );
  XOR2X1 U91 ( .A(n59), .B(n58), .Y(n60) );
  NAND3X1 U92 ( .A(n2), .B(n61), .C(n60), .Y(n62) );
  NOR2X1 U93 ( .A(n63), .B(n62), .Y(n79) );
  XOR2X1 U94 ( .A(n64), .B(N5), .Y(n69) );
  XOR2X1 U95 ( .A(n65), .B(N9), .Y(n68) );
  XOR2X1 U96 ( .A(n66), .B(N8), .Y(n67) );
  NAND3X1 U97 ( .A(n69), .B(n68), .C(n67), .Y(n77) );
  XOR2X1 U98 ( .A(n70), .B(N3), .Y(n75) );
  XOR2X1 U99 ( .A(n71), .B(N4), .Y(n74) );
  XOR2X1 U100 ( .A(n72), .B(N7), .Y(n73) );
  NAND3X1 U101 ( .A(n75), .B(n74), .C(n73), .Y(n76) );
  NOR2X1 U102 ( .A(n77), .B(n76), .Y(n78) );
  NAND2X1 U103 ( .A(n79), .B(n78), .Y(n91) );
  OAI21X1 U104 ( .A(n4), .B(n92), .C(n91), .Y(n80) );
  NOR2X1 U105 ( .A(rollover_val[1]), .B(rollover_val[0]), .Y(n94) );
  NAND2X1 U106 ( .A(n94), .B(n104), .Y(n95) );
  NOR2X1 U107 ( .A(n95), .B(rollover_val[3]), .Y(n97) );
  NAND2X1 U108 ( .A(n97), .B(n103), .Y(n98) );
  NOR2X1 U109 ( .A(n98), .B(rollover_val[5]), .Y(n100) );
  NAND2X1 U110 ( .A(n100), .B(n105), .Y(n101) );
  NOR2X1 U111 ( .A(n101), .B(rollover_val[7]), .Y(n102) );
  AOI21X1 U112 ( .A(rollover_val[0]), .B(rollover_val[1]), .C(n94), .Y(n93) );
  OAI21X1 U113 ( .A(n94), .B(n104), .C(n95), .Y(N5) );
  AOI21X1 U114 ( .A(n95), .B(rollover_val[3]), .C(n97), .Y(n96) );
  OAI21X1 U115 ( .A(n97), .B(n103), .C(n98), .Y(N7) );
  AOI21X1 U116 ( .A(n98), .B(rollover_val[5]), .C(n100), .Y(n99) );
  OAI21X1 U117 ( .A(n100), .B(n105), .C(n101), .Y(N9) );
  INVX2 U118 ( .A(rollover_val[4]), .Y(n103) );
  INVX2 U119 ( .A(rollover_val[2]), .Y(n104) );
  INVX2 U120 ( .A(rollover_val[0]), .Y(N3) );
  INVX2 U121 ( .A(n93), .Y(N4) );
  INVX2 U122 ( .A(rollover_val[6]), .Y(n105) );
  INVX2 U123 ( .A(n99), .Y(N8) );
endmodule


module counter ( clk, n_reset, cnt_up, one_k_samples );
  input clk, n_reset, cnt_up;
  output one_k_samples;


  flex_counter_NUM_CNT_BITS10 call_counter ( .clk(clk), .n_rst(n_reset), 
        .count_enable(cnt_up), .clear(1'b0), .rollover_val({1'b1, 1'b1, 1'b1, 
        1'b1, 1'b1, 1'b0, 1'b1, 1'b0, 1'b0, 1'b0}), .rollover_flag(
        one_k_samples) );
endmodule


module datapath_ctrl ( op, w_data_sel, w_en, alu_op );
  input [1:0] op;
  output w_data_sel, w_en, alu_op;
  wire   n2, n3, n4;

  INVX1 U1 ( .A(n4), .Y(w_data_sel) );
  INVX2 U2 ( .A(op[0]), .Y(n4) );
  OR2X2 U3 ( .A(n3), .B(n4), .Y(n2) );
  INVX4 U4 ( .A(n2), .Y(alu_op) );
  INVX2 U5 ( .A(op[1]), .Y(n3) );
  NAND2X1 U6 ( .A(n4), .B(n3), .Y(w_en) );
endmodule


module regfile_NUM_REG_ADDR_BITS4_REG_SIZE_BITS16 ( clk, n_reset, w_sel, 
        r1_sel, r2_sel, w_data, w_en, r1_data, r2_data, outreg_data );
  input [3:0] w_sel;
  input [3:0] r1_sel;
  input [3:0] r2_sel;
  input [15:0] w_data;
  output [15:0] r1_data;
  output [15:0] r2_data;
  output [15:0] outreg_data;
  input clk, n_reset, w_en;
  wire   \regs[15][15] , \regs[15][14] , \regs[15][13] , \regs[15][12] ,
         \regs[15][11] , \regs[15][10] , \regs[15][9] , \regs[15][8] ,
         \regs[15][7] , \regs[15][6] , \regs[15][5] , \regs[15][4] ,
         \regs[15][3] , \regs[15][2] , \regs[15][1] , \regs[15][0] ,
         \regs[14][15] , \regs[14][14] , \regs[14][13] , \regs[14][12] ,
         \regs[14][11] , \regs[14][10] , \regs[14][9] , \regs[14][8] ,
         \regs[14][7] , \regs[14][6] , \regs[14][5] , \regs[14][4] ,
         \regs[14][3] , \regs[14][2] , \regs[14][1] , \regs[14][0] ,
         \regs[13][15] , \regs[13][14] , \regs[13][13] , \regs[13][12] ,
         \regs[13][11] , \regs[13][10] , \regs[13][9] , \regs[13][8] ,
         \regs[13][7] , \regs[13][6] , \regs[13][5] , \regs[13][4] ,
         \regs[13][3] , \regs[13][2] , \regs[13][1] , \regs[13][0] ,
         \regs[12][15] , \regs[12][14] , \regs[12][13] , \regs[12][12] ,
         \regs[12][11] , \regs[12][10] , \regs[12][9] , \regs[12][8] ,
         \regs[12][7] , \regs[12][6] , \regs[12][5] , \regs[12][4] ,
         \regs[12][3] , \regs[12][2] , \regs[12][1] , \regs[12][0] ,
         \regs[11][15] , \regs[11][14] , \regs[11][13] , \regs[11][12] ,
         \regs[11][11] , \regs[11][10] , \regs[11][9] , \regs[11][8] ,
         \regs[11][7] , \regs[11][6] , \regs[11][5] , \regs[11][4] ,
         \regs[11][3] , \regs[11][2] , \regs[11][1] , \regs[11][0] ,
         \regs[10][15] , \regs[10][14] , \regs[10][13] , \regs[10][12] ,
         \regs[10][11] , \regs[10][10] , \regs[10][9] , \regs[10][8] ,
         \regs[10][7] , \regs[10][6] , \regs[10][5] , \regs[10][4] ,
         \regs[10][3] , \regs[10][2] , \regs[10][1] , \regs[10][0] ,
         \regs[9][15] , \regs[9][14] , \regs[9][13] , \regs[9][12] ,
         \regs[9][11] , \regs[9][10] , \regs[9][9] , \regs[9][8] ,
         \regs[9][7] , \regs[9][6] , \regs[9][5] , \regs[9][4] , \regs[9][3] ,
         \regs[9][2] , \regs[9][1] , \regs[9][0] , \regs[8][15] ,
         \regs[8][14] , \regs[8][13] , \regs[8][12] , \regs[8][11] ,
         \regs[8][10] , \regs[8][9] , \regs[8][8] , \regs[8][7] , \regs[8][6] ,
         \regs[8][5] , \regs[8][4] , \regs[8][3] , \regs[8][2] , \regs[8][1] ,
         \regs[8][0] , \regs[7][15] , \regs[7][14] , \regs[7][13] ,
         \regs[7][12] , \regs[7][11] , \regs[7][10] , \regs[7][9] ,
         \regs[7][8] , \regs[7][7] , \regs[7][6] , \regs[7][5] , \regs[7][4] ,
         \regs[7][3] , \regs[7][2] , \regs[7][1] , \regs[7][0] , \regs[6][15] ,
         \regs[6][14] , \regs[6][13] , \regs[6][12] , \regs[6][11] ,
         \regs[6][10] , \regs[6][9] , \regs[6][8] , \regs[6][7] , \regs[6][6] ,
         \regs[6][5] , \regs[6][4] , \regs[6][3] , \regs[6][2] , \regs[6][1] ,
         \regs[6][0] , \regs[5][15] , \regs[5][14] , \regs[5][13] ,
         \regs[5][12] , \regs[5][11] , \regs[5][10] , \regs[5][9] ,
         \regs[5][8] , \regs[5][7] , \regs[5][6] , \regs[5][5] , \regs[5][4] ,
         \regs[5][3] , \regs[5][2] , \regs[5][1] , \regs[5][0] , \regs[4][15] ,
         \regs[4][14] , \regs[4][13] , \regs[4][12] , \regs[4][11] ,
         \regs[4][10] , \regs[4][9] , \regs[4][8] , \regs[4][7] , \regs[4][6] ,
         \regs[4][5] , \regs[4][4] , \regs[4][3] , \regs[4][2] , \regs[4][1] ,
         \regs[4][0] , \regs[3][15] , \regs[3][14] , \regs[3][13] ,
         \regs[3][12] , \regs[3][11] , \regs[3][10] , \regs[3][9] ,
         \regs[3][8] , \regs[3][7] , \regs[3][6] , \regs[3][5] , \regs[3][4] ,
         \regs[3][3] , \regs[3][2] , \regs[3][1] , \regs[3][0] , \regs[2][15] ,
         \regs[2][14] , \regs[2][13] , \regs[2][12] , \regs[2][11] ,
         \regs[2][10] , \regs[2][9] , \regs[2][8] , \regs[2][7] , \regs[2][6] ,
         \regs[2][5] , \regs[2][4] , \regs[2][3] , \regs[2][2] , \regs[2][1] ,
         \regs[2][0] , \regs[1][15] , \regs[1][14] , \regs[1][13] ,
         \regs[1][12] , \regs[1][11] , \regs[1][10] , \regs[1][9] ,
         \regs[1][8] , \regs[1][7] , \regs[1][6] , \regs[1][5] , \regs[1][4] ,
         \regs[1][3] , \regs[1][2] , \regs[1][1] , \regs[1][0] , n554, n555,
         n565, n566, n567, n568, n569, n570, n571, n572, n573, n582, n583,
         n589, n590, n591, n592, n593, n594, n595, n601, n602, n603, n604,
         n605, n606, n607, n613, n614, n615, n616, n617, n618, n619, n625,
         n626, n627, n628, n629, n630, n631, n637, n638, n639, n640, n641,
         n642, n643, n649, n650, n651, n652, n653, n654, n655, n661, n662,
         n663, n664, n665, n666, n667, n673, n674, n675, n676, n677, n678,
         n679, n685, n686, n687, n688, n689, n690, n691, n697, n698, n699,
         n700, n701, n702, n703, n709, n710, n711, n712, n713, n714, n715,
         n721, n722, n723, n724, n725, n726, n727, n733, n734, n735, n736,
         n737, n738, n739, n745, n746, n747, n748, n749, n750, n751, n757,
         n758, n759, n760, n761, n762, n763, n764, n765, n766, n767, n768,
         n769, n984, n1035, n1140, n1141, n1142, n1143, n1144, n1145, n1146,
         n1147, n1148, n1149, n1150, n1151, n1152, n1153, n1154, n1155, n1156,
         n1157, n1158, n1159, n1160, n1161, n1162, n1163, n1164, n1165, n1166,
         n1167, n1168, n1169, n1170, n1171, n1172, n1173, n1174, n1175, n1176,
         n1177, n1178, n1179, n1180, n1181, n1182, n1183, n1184, n1185, n1186,
         n1187, n1188, n1189, n1190, n1191, n1192, n1193, n1194, n1195, n1196,
         n1197, n1198, n1199, n1200, n1201, n1202, n1203, n1204, n1205, n1206,
         n1207, n1208, n1209, n1210, n1211, n1212, n1213, n1214, n1215, n1216,
         n1217, n1218, n1219, n1220, n1221, n1222, n1223, n1224, n1225, n1226,
         n1227, n1228, n1229, n1230, n1231, n1232, n1233, n1234, n1235, n1236,
         n1237, n1238, n1239, n1240, n1241, n1242, n1243, n1244, n1245, n1246,
         n1247, n1248, n1249, n1250, n1251, n1252, n1253, n1254, n1255, n1256,
         n1257, n1258, n1259, n1260, n1261, n1262, n1263, n1264, n1265, n1266,
         n1267, net4944, net4960, net4976, net4992, net5003, net5005, net5030,
         net5032, net5048, net5050, net5057, net5066, net5068, net5083,
         net5092, net5093, net5110, net5111, net5117, net5128, net5129,
         net5137, net19332, net19336, net19338, net19339, net19340, net19341,
         net19342, net19343, net19344, net19354, net19356, net19358, net19362,
         net19363, net19365, net19366, net19367, net19371, net19372, net19374,
         net19375, net19381, net19390, net19392, net19399, net19401, net19404,
         net19407, net19410, net19412, net19416, net19417, net19419, net19420,
         net19439, net19443, net19445, net19446, net19447, net19448, net19452,
         net19454, net19455, net19456, net19457, net19461, net19463, net19464,
         net19465, net19471, net19475, net19476, net19478, net19479, net19483,
         net19497, net19504, net19508, net19510, net19514, net19515, net19516,
         net19517, net19527, net19530, net19531, net19532, net19535, net19559,
         net19563, net19564, net19566, net19567, net19569, net19571, net19575,
         net19576, net19577, net19580, net19584, net19585, net19587, net19588,
         net19590, net19592, net19596, net19597, net19598, net19601, net19605,
         net19606, net19608, net19609, net19611, net19613, net19617, net19618,
         net19619, net19638, net19643, net19647, net19648, net19650, net19651,
         net19653, net19655, net19659, net19660, net19661, net19662, net19668,
         net19671, net19686, net19687, net19696, net19699, net19700, net19701,
         net19708, net19709, net19710, net19725, net19726, net19727, net19728,
         net19730, net19731, net19738, net19752, net19753, net19758, net19759,
         net19772, net19773, net19774, net19780, net19793, net19794, net19796,
         net19813, net19814, net19815, net19831, net19832, net19833, net19841,
         net19842, net19844, net19878, net19879, net19903, net19905, net19911,
         net19916, net19918, net20226, net20230, net20234, net20238, net20244,
         net20243, net20249, net20247, net20254, net20253, net20389, net20399,
         net20451, net20485, net21377, net21403, net21404, net21405, net21406,
         net21415, net21417, net21434, net21435, net21437, net21438, net21441,
         net21443, net21469, net21470, net21476, net21477, net21478, net21515,
         net21537, net21539, net21541, net21543, net21545, net21547, net21549,
         net21562, net21634, net21646, net21657, net21659, net21748, net21764,
         net21932, net20402, net19860, net19854, net19913, net25032, net25272,
         net25269, net25267, net25264, net25262, net25223, net25209, net20419,
         net19718, net19716, net19373, net19558, net32977, net33085, net19826,
         net21880, net21638, net21442, net19801, net19798, net19797, net19409,
         net21414, net36206, net36208, net19642, net19600, net42609, net21690,
         net21682, net20237, net19579, net19506, net44509, net19688, net21819,
         net20460, net19697, net19694, net19693, net19689, net46042, net19816,
         net21835, net21522, net20409, net19827, net19822, net19821, net19817,
         net21888, net21533, net19886, net19883, net25346, net21833, net21771,
         net19857, net19848, net19847, net19846, net19845, net19823, net19481,
         net21751, net21519, net19884, net19881, net19851, net19843, net44616,
         net19480, net62002, net62001, net62000, net62622, net62657, net62687,
         net62692, net62716, net62736, net62787, net62801, net62827, net21761,
         net19723, net19721, net19720, net19717, net19712, net19711, net20474,
         net19880, n257, n258, n259, n260, n261, n262, n263, n264, n265, n266,
         n267, n268, n269, n270, n271, n272, n273, n274, n275, n276, n277,
         n278, n279, n280, n281, n282, n283, n284, n285, n286, n287, n288,
         n289, n290, n291, n292, n293, n294, n295, n296, n297, n298, n299,
         n300, n301, n302, n303, n304, n305, n306, n307, n308, n309, n310,
         n311, n312, n313, n314, n315, n316, n317, n318, n319, n320, n321,
         n322, n323, n324, n325, n326, n327, n328, n329, n330, n331, n332,
         n333, n334, n335, n336, n337, n338, n339, n340, n341, n342, n343,
         n344, n345, n346, n347, n348, n349, n350, n351, n352, n353, n354,
         n355, n356, n357, n358, n359, n360, n361, n362, n363, n364, n365,
         n366, n367, n368, n369, n370, n371, n372, n373, n374, n375, n376,
         n377, n378, n379, n380, n381, n382, n383, n384, n385, n386, n387,
         n388, n389, n390, n391, n392, n393, n394, n395, n396, n397, n398,
         n399, n400, n401, n402, n403, n404, n405, n406, n407, n408, n409,
         n410, n411, n412, n413, n414, n415, n416, n417, n418, n419, n420,
         n421, n422, n423, n424, n425, n426, n427, n428, n429, n430, n431,
         n432, n433, n434, n435, n436, n437, n438, n439, n440, n441, n442,
         n443, n444, n445, n446, n447, n448, n449, n450, n451, n452, n453,
         n454, n455, n456, n457, n458, n459, n460, n461, n462, n463, n464,
         n465, n466, n467, n468, n469, n470, n471, n472, n473, n474, n475,
         n476, n477, n478, n479, n480, n481, n482, n483, n484, n485, n486,
         n487, n488, n489, n490, n491, n492, n493, n494, n495, n496, n497,
         n498, n499, n500, n501, n502, n503, n504, n505, n506, n507, n508,
         n509, n510, n511, n512, n513, n514, n515, n516, n517, n518, n519,
         n520, n521, n522, n523, n524, n525, n526, n527, n528, n529, n530,
         n531, n532, n533, n534, n535, n536, n537, n538, n539, n540, n541,
         n542, n543, n544, n545, n546, n547, n548, n549, n550, n551, n552,
         n553, n556, n557, n558, n559, n560, n561, n562, n563, n564, n574,
         n575, n576, n577, n578, n579, n580, n581, n584, n585, n586, n587,
         n588, n596, n597, n598, n599, n600, n608, n609, n610, n611, n612,
         n620, n621, n622, n623, n624, n632, n633, n634, n635, n636, n644,
         n645, n646, n647, n648, n656, n657, n658, n659, n660, n668, n669,
         n670, n671, n672, n680, n681, n682, n683, n684, n692, n693, n694,
         n695, n696, n704, n705, n706, n707, n708, n716, n717, n718, n719,
         n720, n728, n729, n730, n731, n732, n740, n741, n742, n743, n744,
         n752, n753, n754, n755, n756, n770, n771, n772, n773, n774, n775,
         n776, n777, n778, n779, n780, n781, n782, n783, n784, n785, n786,
         n787, n788, n789, n790, n791, n792, n793, n794, n795, n796, n797,
         n798, n799, n800, n801, n802, n803, n804, n805, n806, n807, n808,
         n809, n810, n811, n812, n813, n814, n815, n816, n817, n818, n819,
         n820, n821, n822, n823, n824, n825, n826, n827, n828, n829, n830,
         n831, n832, n833, n834, n835, n836, n837, n838, n839, n840, n841,
         n842, n843, n844, n845, n846, n847, n848, n849, n850, n851, n852,
         n853, n854, n855, n856, n857, n858, n859, n860, n861, n862, n863,
         n864, n865, n866, n867, n868, n869, n870, n871, n872, n873, n874,
         n875, n876, n877, n878, n879, n880, n881, n882, n883, n884, n885,
         n886, n887, n888, n889, n890, n891, n892, n893, n894, n895, n896,
         n897, n898, n899, n900, n901, n902, n903, n904, n905, n906, n907,
         n908, n909, n910, n911, n912, n913, n914, n915, n916, n917, n918,
         n919, n920, n921, n922, n923, n924, n925, n926, n927, n928, n929,
         n930, n931, n932, n933, n934, n935, n936, n937, n938, n939, n940,
         n941, n942, n943, n944, n945, n946, n947, n948, n949, n950, n951,
         n952, n953, n954, n955, n956, n957, n958, n959, n960, n961, n962,
         n963, n964, n965, n966, n967, n968;

  DFFSR \regs_reg[15][15]  ( .D(n898), .CLK(clk), .R(n412), .S(1'b1), .Q(
        \regs[15][15] ) );
  DFFSR \regs_reg[15][14]  ( .D(n889), .CLK(clk), .R(n412), .S(1'b1), .Q(
        \regs[15][14] ) );
  DFFSR \regs_reg[15][13]  ( .D(n882), .CLK(clk), .R(n412), .S(1'b1), .Q(
        \regs[15][13] ) );
  DFFSR \regs_reg[15][12]  ( .D(n904), .CLK(clk), .R(n412), .S(1'b1), .Q(
        \regs[15][12] ) );
  DFFSR \regs_reg[15][11]  ( .D(n868), .CLK(clk), .R(n411), .S(1'b1), .Q(
        \regs[15][11] ) );
  DFFSR \regs_reg[15][10]  ( .D(n862), .CLK(clk), .R(n411), .S(1'b1), .Q(
        \regs[15][10] ) );
  DFFSR \regs_reg[15][9]  ( .D(n855), .CLK(clk), .R(n411), .S(1'b1), .Q(
        \regs[15][9] ) );
  DFFSR \regs_reg[15][8]  ( .D(n875), .CLK(clk), .R(n411), .S(1'b1), .Q(
        \regs[15][8] ) );
  DFFSR \regs_reg[15][7]  ( .D(n841), .CLK(clk), .R(n411), .S(1'b1), .Q(
        \regs[15][7] ) );
  DFFSR \regs_reg[15][6]  ( .D(n835), .CLK(clk), .R(n411), .S(1'b1), .Q(
        \regs[15][6] ) );
  DFFSR \regs_reg[15][5]  ( .D(n827), .CLK(clk), .R(n411), .S(1'b1), .Q(
        \regs[15][5] ) );
  DFFSR \regs_reg[15][4]  ( .D(n848), .CLK(clk), .R(n411), .S(1'b1), .Q(
        \regs[15][4] ) );
  DFFSR \regs_reg[15][3]  ( .D(n814), .CLK(clk), .R(n411), .S(1'b1), .Q(
        \regs[15][3] ) );
  DFFSR \regs_reg[15][2]  ( .D(n808), .CLK(clk), .R(n411), .S(1'b1), .Q(
        \regs[15][2] ) );
  DFFSR \regs_reg[15][1]  ( .D(n801), .CLK(clk), .R(n411), .S(1'b1), .Q(
        \regs[15][1] ) );
  DFFSR \regs_reg[15][0]  ( .D(n821), .CLK(clk), .R(n411), .S(1'b1), .Q(
        \regs[15][0] ) );
  DFFSR \regs_reg[14][15]  ( .D(n897), .CLK(clk), .R(n410), .S(1'b1), .Q(
        \regs[14][15] ) );
  DFFSR \regs_reg[14][14]  ( .D(n888), .CLK(clk), .R(n410), .S(1'b1), .Q(
        \regs[14][14] ) );
  DFFSR \regs_reg[14][13]  ( .D(net5032), .CLK(clk), .R(n410), .S(1'b1), .Q(
        \regs[14][13] ) );
  DFFSR \regs_reg[14][12]  ( .D(net5005), .CLK(clk), .R(n410), .S(1'b1), .Q(
        \regs[14][12] ) );
  DFFSR \regs_reg[14][11]  ( .D(net5050), .CLK(clk), .R(n410), .S(1'b1), .Q(
        \regs[14][11] ) );
  DFFSR \regs_reg[14][10]  ( .D(n861), .CLK(clk), .R(n410), .S(1'b1), .Q(
        \regs[14][10] ) );
  DFFSR \regs_reg[14][9]  ( .D(net5068), .CLK(clk), .R(n410), .S(1'b1), .Q(
        \regs[14][9] ) );
  DFFSR \regs_reg[14][8]  ( .D(n874), .CLK(clk), .R(n410), .S(1'b1), .Q(
        \regs[14][8] ) );
  DFFSR \regs_reg[14][7]  ( .D(n840), .CLK(clk), .R(n410), .S(1'b1), .Q(
        \regs[14][7] ) );
  DFFSR \regs_reg[14][6]  ( .D(n834), .CLK(clk), .R(n410), .S(1'b1), .Q(
        \regs[14][6] ) );
  DFFSR \regs_reg[14][5]  ( .D(n826), .CLK(clk), .R(n410), .S(1'b1), .Q(
        \regs[14][5] ) );
  DFFSR \regs_reg[14][4]  ( .D(n847), .CLK(clk), .R(n410), .S(1'b1), .Q(
        \regs[14][4] ) );
  DFFSR \regs_reg[14][3]  ( .D(n813), .CLK(clk), .R(n409), .S(1'b1), .Q(
        \regs[14][3] ) );
  DFFSR \regs_reg[14][2]  ( .D(n807), .CLK(clk), .R(n409), .S(1'b1), .Q(
        \regs[14][2] ) );
  DFFSR \regs_reg[14][1]  ( .D(n800), .CLK(clk), .R(n409), .S(1'b1), .Q(
        \regs[14][1] ) );
  DFFSR \regs_reg[14][0]  ( .D(n820), .CLK(clk), .R(n409), .S(1'b1), .Q(
        \regs[14][0] ) );
  DFFSR \regs_reg[13][15]  ( .D(n896), .CLK(clk), .R(n409), .S(1'b1), .Q(
        \regs[13][15] ) );
  DFFSR \regs_reg[13][14]  ( .D(n887), .CLK(clk), .R(n409), .S(1'b1), .Q(
        \regs[13][14] ) );
  DFFSR \regs_reg[13][13]  ( .D(n881), .CLK(clk), .R(n409), .S(1'b1), .Q(
        \regs[13][13] ) );
  DFFSR \regs_reg[13][12]  ( .D(n903), .CLK(clk), .R(n409), .S(1'b1), .Q(
        \regs[13][12] ) );
  DFFSR \regs_reg[13][11]  ( .D(n867), .CLK(clk), .R(n409), .S(1'b1), .Q(
        \regs[13][11] ) );
  DFFSR \regs_reg[13][10]  ( .D(n860), .CLK(clk), .R(n409), .S(1'b1), .Q(
        \regs[13][10] ) );
  DFFSR \regs_reg[13][9]  ( .D(n854), .CLK(clk), .R(n409), .S(1'b1), .Q(
        \regs[13][9] ) );
  DFFSR \regs_reg[13][8]  ( .D(n873), .CLK(clk), .R(n409), .S(1'b1), .Q(
        \regs[13][8] ) );
  DFFSR \regs_reg[13][7]  ( .D(n839), .CLK(clk), .R(n408), .S(1'b1), .Q(
        \regs[13][7] ) );
  DFFSR \regs_reg[13][6]  ( .D(n833), .CLK(clk), .R(n408), .S(1'b1), .Q(
        \regs[13][6] ) );
  DFFSR \regs_reg[13][5]  ( .D(n825), .CLK(clk), .R(n408), .S(1'b1), .Q(
        \regs[13][5] ) );
  DFFSR \regs_reg[13][4]  ( .D(n846), .CLK(clk), .R(n408), .S(1'b1), .Q(
        \regs[13][4] ) );
  DFFSR \regs_reg[13][3]  ( .D(n812), .CLK(clk), .R(n408), .S(1'b1), .Q(
        \regs[13][3] ) );
  DFFSR \regs_reg[13][2]  ( .D(n806), .CLK(clk), .R(n408), .S(1'b1), .Q(
        \regs[13][2] ) );
  DFFSR \regs_reg[13][1]  ( .D(n799), .CLK(clk), .R(n408), .S(1'b1), .Q(
        \regs[13][1] ) );
  DFFSR \regs_reg[13][0]  ( .D(n819), .CLK(clk), .R(n408), .S(1'b1), .Q(
        \regs[13][0] ) );
  DFFSR \regs_reg[12][15]  ( .D(n895), .CLK(clk), .R(n408), .S(1'b1), .Q(
        \regs[12][15] ) );
  DFFSR \regs_reg[12][14]  ( .D(n886), .CLK(clk), .R(n408), .S(1'b1), .Q(
        \regs[12][14] ) );
  DFFSR \regs_reg[12][13]  ( .D(n880), .CLK(clk), .R(n408), .S(1'b1), .Q(
        \regs[12][13] ) );
  DFFSR \regs_reg[12][12]  ( .D(n902), .CLK(clk), .R(n408), .S(1'b1), .Q(
        \regs[12][12] ) );
  DFFSR \regs_reg[12][11]  ( .D(n866), .CLK(clk), .R(n407), .S(1'b1), .Q(
        \regs[12][11] ) );
  DFFSR \regs_reg[12][10]  ( .D(n859), .CLK(clk), .R(n407), .S(1'b1), .Q(
        \regs[12][10] ) );
  DFFSR \regs_reg[12][9]  ( .D(n853), .CLK(clk), .R(n407), .S(1'b1), .Q(
        \regs[12][9] ) );
  DFFSR \regs_reg[12][8]  ( .D(n872), .CLK(clk), .R(n407), .S(1'b1), .Q(
        \regs[12][8] ) );
  DFFSR \regs_reg[12][7]  ( .D(n838), .CLK(clk), .R(n407), .S(1'b1), .Q(
        \regs[12][7] ) );
  DFFSR \regs_reg[12][6]  ( .D(n832), .CLK(clk), .R(n407), .S(1'b1), .Q(
        \regs[12][6] ) );
  DFFSR \regs_reg[12][5]  ( .D(n824), .CLK(clk), .R(n407), .S(1'b1), .Q(
        \regs[12][5] ) );
  DFFSR \regs_reg[12][4]  ( .D(n845), .CLK(clk), .R(n407), .S(1'b1), .Q(
        \regs[12][4] ) );
  DFFSR \regs_reg[12][3]  ( .D(n811), .CLK(clk), .R(n407), .S(1'b1), .Q(
        \regs[12][3] ) );
  DFFSR \regs_reg[12][2]  ( .D(n805), .CLK(clk), .R(n407), .S(1'b1), .Q(
        \regs[12][2] ) );
  DFFSR \regs_reg[12][1]  ( .D(n798), .CLK(clk), .R(n407), .S(1'b1), .Q(
        \regs[12][1] ) );
  DFFSR \regs_reg[12][0]  ( .D(n818), .CLK(clk), .R(n407), .S(1'b1), .Q(
        \regs[12][0] ) );
  DFFSR \regs_reg[11][15]  ( .D(n1267), .CLK(clk), .R(n406), .S(1'b1), .Q(
        \regs[11][15] ) );
  DFFSR \regs_reg[11][14]  ( .D(n1266), .CLK(clk), .R(n406), .S(1'b1), .Q(
        \regs[11][14] ) );
  DFFSR \regs_reg[11][13]  ( .D(n1265), .CLK(clk), .R(n406), .S(1'b1), .Q(
        \regs[11][13] ) );
  DFFSR \regs_reg[11][12]  ( .D(n1264), .CLK(clk), .R(n406), .S(1'b1), .Q(
        \regs[11][12] ) );
  DFFSR \regs_reg[11][11]  ( .D(n1263), .CLK(clk), .R(n406), .S(1'b1), .Q(
        \regs[11][11] ) );
  DFFSR \regs_reg[11][10]  ( .D(n1262), .CLK(clk), .R(n406), .S(1'b1), .Q(
        \regs[11][10] ) );
  DFFSR \regs_reg[11][9]  ( .D(n1261), .CLK(clk), .R(n406), .S(1'b1), .Q(
        \regs[11][9] ) );
  DFFSR \regs_reg[11][8]  ( .D(n1260), .CLK(clk), .R(n406), .S(1'b1), .Q(
        \regs[11][8] ) );
  DFFSR \regs_reg[11][7]  ( .D(n1259), .CLK(clk), .R(n406), .S(1'b1), .Q(
        \regs[11][7] ) );
  DFFSR \regs_reg[11][6]  ( .D(n1258), .CLK(clk), .R(n406), .S(1'b1), .Q(
        \regs[11][6] ) );
  DFFSR \regs_reg[11][5]  ( .D(n1257), .CLK(clk), .R(n406), .S(1'b1), .Q(
        \regs[11][5] ) );
  DFFSR \regs_reg[11][4]  ( .D(n1256), .CLK(clk), .R(n406), .S(1'b1), .Q(
        \regs[11][4] ) );
  DFFSR \regs_reg[11][3]  ( .D(n1255), .CLK(clk), .R(n405), .S(1'b1), .Q(
        \regs[11][3] ) );
  DFFSR \regs_reg[11][2]  ( .D(n1254), .CLK(clk), .R(n405), .S(1'b1), .Q(
        \regs[11][2] ) );
  DFFSR \regs_reg[11][1]  ( .D(n1253), .CLK(clk), .R(n405), .S(1'b1), .Q(
        \regs[11][1] ) );
  DFFSR \regs_reg[11][0]  ( .D(n1252), .CLK(clk), .R(n405), .S(1'b1), .Q(
        \regs[11][0] ) );
  DFFSR \regs_reg[10][15]  ( .D(n1251), .CLK(clk), .R(n405), .S(1'b1), .Q(
        \regs[10][15] ) );
  DFFSR \regs_reg[10][14]  ( .D(n1250), .CLK(clk), .R(n405), .S(1'b1), .Q(
        \regs[10][14] ) );
  DFFSR \regs_reg[10][13]  ( .D(n1249), .CLK(clk), .R(n405), .S(1'b1), .Q(
        \regs[10][13] ) );
  DFFSR \regs_reg[10][12]  ( .D(n1248), .CLK(clk), .R(n405), .S(1'b1), .Q(
        \regs[10][12] ) );
  DFFSR \regs_reg[10][11]  ( .D(n1247), .CLK(clk), .R(n405), .S(1'b1), .Q(
        \regs[10][11] ) );
  DFFSR \regs_reg[10][10]  ( .D(n1246), .CLK(clk), .R(n405), .S(1'b1), .Q(
        \regs[10][10] ) );
  DFFSR \regs_reg[10][9]  ( .D(n1245), .CLK(clk), .R(n405), .S(1'b1), .Q(
        \regs[10][9] ) );
  DFFSR \regs_reg[10][8]  ( .D(n1244), .CLK(clk), .R(n405), .S(1'b1), .Q(
        \regs[10][8] ) );
  DFFSR \regs_reg[10][7]  ( .D(n1243), .CLK(clk), .R(n404), .S(1'b1), .Q(
        \regs[10][7] ) );
  DFFSR \regs_reg[10][6]  ( .D(n1242), .CLK(clk), .R(n404), .S(1'b1), .Q(
        \regs[10][6] ) );
  DFFSR \regs_reg[10][5]  ( .D(n1241), .CLK(clk), .R(n404), .S(1'b1), .Q(
        \regs[10][5] ) );
  DFFSR \regs_reg[10][4]  ( .D(n1240), .CLK(clk), .R(n404), .S(1'b1), .Q(
        \regs[10][4] ) );
  DFFSR \regs_reg[10][3]  ( .D(n1239), .CLK(clk), .R(n404), .S(1'b1), .Q(
        \regs[10][3] ) );
  DFFSR \regs_reg[10][2]  ( .D(n1238), .CLK(clk), .R(n404), .S(1'b1), .Q(
        \regs[10][2] ) );
  DFFSR \regs_reg[10][1]  ( .D(n1237), .CLK(clk), .R(n404), .S(1'b1), .Q(
        \regs[10][1] ) );
  DFFSR \regs_reg[10][0]  ( .D(n1236), .CLK(clk), .R(n404), .S(1'b1), .Q(
        \regs[10][0] ) );
  DFFSR \regs_reg[9][15]  ( .D(n1235), .CLK(clk), .R(n404), .S(1'b1), .Q(
        \regs[9][15] ) );
  DFFSR \regs_reg[9][14]  ( .D(n1234), .CLK(clk), .R(n404), .S(1'b1), .Q(
        \regs[9][14] ) );
  DFFSR \regs_reg[9][13]  ( .D(n1233), .CLK(clk), .R(n404), .S(1'b1), .Q(
        \regs[9][13] ) );
  DFFSR \regs_reg[9][12]  ( .D(n1232), .CLK(clk), .R(n404), .S(1'b1), .Q(
        \regs[9][12] ) );
  DFFSR \regs_reg[9][11]  ( .D(n1231), .CLK(clk), .R(n403), .S(1'b1), .Q(
        \regs[9][11] ) );
  DFFSR \regs_reg[9][10]  ( .D(n1230), .CLK(clk), .R(n403), .S(1'b1), .Q(
        \regs[9][10] ) );
  DFFSR \regs_reg[9][9]  ( .D(n1229), .CLK(clk), .R(n403), .S(1'b1), .Q(
        \regs[9][9] ) );
  DFFSR \regs_reg[9][8]  ( .D(n1228), .CLK(clk), .R(n403), .S(1'b1), .Q(
        \regs[9][8] ) );
  DFFSR \regs_reg[9][7]  ( .D(n1227), .CLK(clk), .R(n403), .S(1'b1), .Q(
        \regs[9][7] ) );
  DFFSR \regs_reg[9][6]  ( .D(n1226), .CLK(clk), .R(n403), .S(1'b1), .Q(
        \regs[9][6] ) );
  DFFSR \regs_reg[9][5]  ( .D(n1225), .CLK(clk), .R(n403), .S(1'b1), .Q(
        \regs[9][5] ) );
  DFFSR \regs_reg[9][4]  ( .D(n1224), .CLK(clk), .R(n403), .S(1'b1), .Q(
        \regs[9][4] ) );
  DFFSR \regs_reg[9][3]  ( .D(n1223), .CLK(clk), .R(n403), .S(1'b1), .Q(
        \regs[9][3] ) );
  DFFSR \regs_reg[9][2]  ( .D(n1222), .CLK(clk), .R(n403), .S(1'b1), .Q(
        \regs[9][2] ) );
  DFFSR \regs_reg[9][1]  ( .D(n1221), .CLK(clk), .R(n403), .S(1'b1), .Q(
        \regs[9][1] ) );
  DFFSR \regs_reg[9][0]  ( .D(n1220), .CLK(clk), .R(n403), .S(1'b1), .Q(
        \regs[9][0] ) );
  DFFSR \regs_reg[8][15]  ( .D(n1219), .CLK(clk), .R(n402), .S(1'b1), .Q(
        \regs[8][15] ) );
  DFFSR \regs_reg[8][14]  ( .D(n1218), .CLK(clk), .R(n402), .S(1'b1), .Q(
        \regs[8][14] ) );
  DFFSR \regs_reg[8][13]  ( .D(n1217), .CLK(clk), .R(n402), .S(1'b1), .Q(
        \regs[8][13] ) );
  DFFSR \regs_reg[8][12]  ( .D(n1216), .CLK(clk), .R(n402), .S(1'b1), .Q(
        \regs[8][12] ) );
  DFFSR \regs_reg[8][11]  ( .D(n1215), .CLK(clk), .R(n402), .S(1'b1), .Q(
        \regs[8][11] ) );
  DFFSR \regs_reg[8][10]  ( .D(n1214), .CLK(clk), .R(n402), .S(1'b1), .Q(
        \regs[8][10] ) );
  DFFSR \regs_reg[8][9]  ( .D(n1213), .CLK(clk), .R(n402), .S(1'b1), .Q(
        \regs[8][9] ) );
  DFFSR \regs_reg[8][8]  ( .D(n1212), .CLK(clk), .R(n402), .S(1'b1), .Q(
        \regs[8][8] ) );
  DFFSR \regs_reg[8][7]  ( .D(n1211), .CLK(clk), .R(n402), .S(1'b1), .Q(
        \regs[8][7] ) );
  DFFSR \regs_reg[8][6]  ( .D(n1210), .CLK(clk), .R(n402), .S(1'b1), .Q(
        \regs[8][6] ) );
  DFFSR \regs_reg[8][5]  ( .D(n1209), .CLK(clk), .R(n402), .S(1'b1), .Q(
        \regs[8][5] ) );
  DFFSR \regs_reg[8][4]  ( .D(n1208), .CLK(clk), .R(n402), .S(1'b1), .Q(
        \regs[8][4] ) );
  DFFSR \regs_reg[8][3]  ( .D(n1207), .CLK(clk), .R(n401), .S(1'b1), .Q(
        \regs[8][3] ) );
  DFFSR \regs_reg[8][2]  ( .D(n1206), .CLK(clk), .R(n401), .S(1'b1), .Q(
        \regs[8][2] ) );
  DFFSR \regs_reg[8][1]  ( .D(n1205), .CLK(clk), .R(n401), .S(1'b1), .Q(
        \regs[8][1] ) );
  DFFSR \regs_reg[8][0]  ( .D(n1204), .CLK(clk), .R(n401), .S(1'b1), .Q(
        \regs[8][0] ) );
  DFFSR \regs_reg[7][15]  ( .D(n1203), .CLK(clk), .R(n401), .S(1'b1), .Q(
        \regs[7][15] ) );
  DFFSR \regs_reg[7][14]  ( .D(n1202), .CLK(clk), .R(n401), .S(1'b1), .Q(
        \regs[7][14] ) );
  DFFSR \regs_reg[7][13]  ( .D(n1201), .CLK(clk), .R(n401), .S(1'b1), .Q(
        \regs[7][13] ) );
  DFFSR \regs_reg[7][12]  ( .D(n1200), .CLK(clk), .R(n401), .S(1'b1), .Q(
        \regs[7][12] ) );
  DFFSR \regs_reg[7][11]  ( .D(n1199), .CLK(clk), .R(n401), .S(1'b1), .Q(
        \regs[7][11] ) );
  DFFSR \regs_reg[7][10]  ( .D(n1198), .CLK(clk), .R(n401), .S(1'b1), .Q(
        \regs[7][10] ) );
  DFFSR \regs_reg[7][9]  ( .D(n1197), .CLK(clk), .R(n401), .S(1'b1), .Q(
        \regs[7][9] ) );
  DFFSR \regs_reg[7][8]  ( .D(n1196), .CLK(clk), .R(n401), .S(1'b1), .Q(
        \regs[7][8] ) );
  DFFSR \regs_reg[7][7]  ( .D(n1195), .CLK(clk), .R(n400), .S(1'b1), .Q(
        \regs[7][7] ) );
  DFFSR \regs_reg[7][6]  ( .D(n1194), .CLK(clk), .R(n400), .S(1'b1), .Q(
        \regs[7][6] ) );
  DFFSR \regs_reg[7][5]  ( .D(n1193), .CLK(clk), .R(n400), .S(1'b1), .Q(
        \regs[7][5] ) );
  DFFSR \regs_reg[7][4]  ( .D(n1192), .CLK(clk), .R(n400), .S(1'b1), .Q(
        \regs[7][4] ) );
  DFFSR \regs_reg[7][3]  ( .D(n1191), .CLK(clk), .R(n400), .S(1'b1), .Q(
        \regs[7][3] ) );
  DFFSR \regs_reg[7][2]  ( .D(n1190), .CLK(clk), .R(n400), .S(1'b1), .Q(
        \regs[7][2] ) );
  DFFSR \regs_reg[7][1]  ( .D(n1189), .CLK(clk), .R(n400), .S(1'b1), .Q(
        \regs[7][1] ) );
  DFFSR \regs_reg[7][0]  ( .D(n1188), .CLK(clk), .R(n400), .S(1'b1), .Q(
        \regs[7][0] ) );
  DFFSR \regs_reg[6][15]  ( .D(n1187), .CLK(clk), .R(n400), .S(1'b1), .Q(
        \regs[6][15] ) );
  DFFSR \regs_reg[6][14]  ( .D(n1186), .CLK(clk), .R(n400), .S(1'b1), .Q(
        \regs[6][14] ) );
  DFFSR \regs_reg[6][13]  ( .D(n1185), .CLK(clk), .R(n400), .S(1'b1), .Q(
        \regs[6][13] ) );
  DFFSR \regs_reg[6][12]  ( .D(n1184), .CLK(clk), .R(n400), .S(1'b1), .Q(
        \regs[6][12] ) );
  DFFSR \regs_reg[6][11]  ( .D(n1183), .CLK(clk), .R(n399), .S(1'b1), .Q(
        \regs[6][11] ) );
  DFFSR \regs_reg[6][10]  ( .D(n1182), .CLK(clk), .R(n399), .S(1'b1), .Q(
        \regs[6][10] ) );
  DFFSR \regs_reg[6][9]  ( .D(n1181), .CLK(clk), .R(n399), .S(1'b1), .Q(
        \regs[6][9] ) );
  DFFSR \regs_reg[6][8]  ( .D(n1180), .CLK(clk), .R(n399), .S(1'b1), .Q(
        \regs[6][8] ) );
  DFFSR \regs_reg[6][7]  ( .D(n1179), .CLK(clk), .R(n399), .S(1'b1), .Q(
        \regs[6][7] ) );
  DFFSR \regs_reg[6][6]  ( .D(n1178), .CLK(clk), .R(n399), .S(1'b1), .Q(
        \regs[6][6] ) );
  DFFSR \regs_reg[6][5]  ( .D(n1177), .CLK(clk), .R(n399), .S(1'b1), .Q(
        \regs[6][5] ) );
  DFFSR \regs_reg[6][4]  ( .D(n1176), .CLK(clk), .R(n399), .S(1'b1), .Q(
        \regs[6][4] ) );
  DFFSR \regs_reg[6][3]  ( .D(n1175), .CLK(clk), .R(n399), .S(1'b1), .Q(
        \regs[6][3] ) );
  DFFSR \regs_reg[6][2]  ( .D(n1174), .CLK(clk), .R(n399), .S(1'b1), .Q(
        \regs[6][2] ) );
  DFFSR \regs_reg[6][1]  ( .D(n1173), .CLK(clk), .R(n399), .S(1'b1), .Q(
        \regs[6][1] ) );
  DFFSR \regs_reg[6][0]  ( .D(n1172), .CLK(clk), .R(n399), .S(1'b1), .Q(
        \regs[6][0] ) );
  DFFSR \regs_reg[5][15]  ( .D(n1171), .CLK(clk), .R(n398), .S(1'b1), .Q(
        \regs[5][15] ) );
  DFFSR \regs_reg[5][14]  ( .D(n1170), .CLK(clk), .R(n398), .S(1'b1), .Q(
        \regs[5][14] ) );
  DFFSR \regs_reg[5][13]  ( .D(n1169), .CLK(clk), .R(n398), .S(1'b1), .Q(
        \regs[5][13] ) );
  DFFSR \regs_reg[5][12]  ( .D(n1168), .CLK(clk), .R(n398), .S(1'b1), .Q(
        \regs[5][12] ) );
  DFFSR \regs_reg[5][11]  ( .D(n1167), .CLK(clk), .R(n398), .S(1'b1), .Q(
        \regs[5][11] ) );
  DFFSR \regs_reg[5][10]  ( .D(n1166), .CLK(clk), .R(n398), .S(1'b1), .Q(
        \regs[5][10] ) );
  DFFSR \regs_reg[5][9]  ( .D(n1165), .CLK(clk), .R(n398), .S(1'b1), .Q(
        \regs[5][9] ) );
  DFFSR \regs_reg[5][8]  ( .D(n1164), .CLK(clk), .R(n398), .S(1'b1), .Q(
        \regs[5][8] ) );
  DFFSR \regs_reg[5][7]  ( .D(n1163), .CLK(clk), .R(n398), .S(1'b1), .Q(
        \regs[5][7] ) );
  DFFSR \regs_reg[5][6]  ( .D(n1162), .CLK(clk), .R(n398), .S(1'b1), .Q(
        \regs[5][6] ) );
  DFFSR \regs_reg[5][5]  ( .D(n1161), .CLK(clk), .R(n398), .S(1'b1), .Q(
        \regs[5][5] ) );
  DFFSR \regs_reg[5][4]  ( .D(n1160), .CLK(clk), .R(n398), .S(1'b1), .Q(
        \regs[5][4] ) );
  DFFSR \regs_reg[5][3]  ( .D(n1159), .CLK(clk), .R(n397), .S(1'b1), .Q(
        \regs[5][3] ) );
  DFFSR \regs_reg[5][2]  ( .D(n1158), .CLK(clk), .R(n397), .S(1'b1), .Q(
        \regs[5][2] ) );
  DFFSR \regs_reg[5][1]  ( .D(n1157), .CLK(clk), .R(n397), .S(1'b1), .Q(
        \regs[5][1] ) );
  DFFSR \regs_reg[5][0]  ( .D(n1156), .CLK(clk), .R(n397), .S(1'b1), .Q(
        \regs[5][0] ) );
  DFFSR \regs_reg[4][15]  ( .D(n1155), .CLK(clk), .R(n397), .S(1'b1), .Q(
        \regs[4][15] ) );
  DFFSR \regs_reg[4][14]  ( .D(n1154), .CLK(clk), .R(n397), .S(1'b1), .Q(
        \regs[4][14] ) );
  DFFSR \regs_reg[4][13]  ( .D(n1153), .CLK(clk), .R(n397), .S(1'b1), .Q(
        \regs[4][13] ) );
  DFFSR \regs_reg[4][12]  ( .D(n1152), .CLK(clk), .R(n397), .S(1'b1), .Q(
        \regs[4][12] ) );
  DFFSR \regs_reg[4][11]  ( .D(n1151), .CLK(clk), .R(n397), .S(1'b1), .Q(
        \regs[4][11] ) );
  DFFSR \regs_reg[4][10]  ( .D(n1150), .CLK(clk), .R(n397), .S(1'b1), .Q(
        \regs[4][10] ) );
  DFFSR \regs_reg[4][9]  ( .D(n1149), .CLK(clk), .R(n397), .S(1'b1), .Q(
        \regs[4][9] ) );
  DFFSR \regs_reg[4][8]  ( .D(n1148), .CLK(clk), .R(n397), .S(1'b1), .Q(
        \regs[4][8] ) );
  DFFSR \regs_reg[4][7]  ( .D(n1147), .CLK(clk), .R(n396), .S(1'b1), .Q(
        \regs[4][7] ) );
  DFFSR \regs_reg[4][6]  ( .D(n1146), .CLK(clk), .R(n396), .S(1'b1), .Q(
        \regs[4][6] ) );
  DFFSR \regs_reg[4][5]  ( .D(n1145), .CLK(clk), .R(n396), .S(1'b1), .Q(
        \regs[4][5] ) );
  DFFSR \regs_reg[4][4]  ( .D(n1144), .CLK(clk), .R(n396), .S(1'b1), .Q(
        \regs[4][4] ) );
  DFFSR \regs_reg[4][3]  ( .D(n1143), .CLK(clk), .R(n396), .S(1'b1), .Q(
        \regs[4][3] ) );
  DFFSR \regs_reg[4][2]  ( .D(n1142), .CLK(clk), .R(n396), .S(1'b1), .Q(
        \regs[4][2] ) );
  DFFSR \regs_reg[4][1]  ( .D(n1141), .CLK(clk), .R(n396), .S(1'b1), .Q(
        \regs[4][1] ) );
  DFFSR \regs_reg[4][0]  ( .D(n1140), .CLK(clk), .R(n396), .S(1'b1), .Q(
        \regs[4][0] ) );
  DFFSR \regs_reg[3][15]  ( .D(n894), .CLK(clk), .R(n396), .S(1'b1), .Q(
        \regs[3][15] ) );
  DFFSR \regs_reg[3][14]  ( .D(n885), .CLK(clk), .R(n396), .S(1'b1), .Q(
        \regs[3][14] ) );
  DFFSR \regs_reg[3][13]  ( .D(n879), .CLK(clk), .R(n396), .S(1'b1), .Q(
        \regs[3][13] ) );
  DFFSR \regs_reg[3][12]  ( .D(n901), .CLK(clk), .R(n396), .S(1'b1), .Q(
        \regs[3][12] ) );
  DFFSR \regs_reg[3][11]  ( .D(n865), .CLK(clk), .R(n395), .S(1'b1), .Q(
        \regs[3][11] ) );
  DFFSR \regs_reg[3][10]  ( .D(n858), .CLK(clk), .R(n395), .S(1'b1), .Q(
        \regs[3][10] ) );
  DFFSR \regs_reg[3][9]  ( .D(n852), .CLK(clk), .R(n395), .S(1'b1), .Q(
        \regs[3][9] ) );
  DFFSR \regs_reg[3][8]  ( .D(n871), .CLK(clk), .R(n395), .S(1'b1), .Q(
        \regs[3][8] ) );
  DFFSR \regs_reg[3][7]  ( .D(n837), .CLK(clk), .R(n395), .S(1'b1), .Q(
        \regs[3][7] ) );
  DFFSR \regs_reg[3][6]  ( .D(n831), .CLK(clk), .R(n395), .S(1'b1), .Q(
        \regs[3][6] ) );
  DFFSR \regs_reg[3][5]  ( .D(n823), .CLK(clk), .R(n395), .S(1'b1), .Q(
        \regs[3][5] ) );
  DFFSR \regs_reg[3][4]  ( .D(n844), .CLK(clk), .R(n395), .S(1'b1), .Q(
        \regs[3][4] ) );
  DFFSR \regs_reg[3][3]  ( .D(n810), .CLK(clk), .R(n395), .S(1'b1), .Q(
        \regs[3][3] ) );
  DFFSR \regs_reg[3][2]  ( .D(n804), .CLK(clk), .R(n395), .S(1'b1), .Q(
        \regs[3][2] ) );
  DFFSR \regs_reg[3][1]  ( .D(n797), .CLK(clk), .R(n395), .S(1'b1), .Q(
        \regs[3][1] ) );
  DFFSR \regs_reg[3][0]  ( .D(n817), .CLK(clk), .R(n395), .S(1'b1), .Q(
        \regs[3][0] ) );
  DFFSR \regs_reg[2][15]  ( .D(n893), .CLK(clk), .R(n394), .S(1'b1), .Q(
        \regs[2][15] ) );
  DFFSR \regs_reg[2][14]  ( .D(n884), .CLK(clk), .R(n394), .S(1'b1), .Q(
        \regs[2][14] ) );
  DFFSR \regs_reg[2][13]  ( .D(n878), .CLK(clk), .R(n394), .S(1'b1), .Q(
        \regs[2][13] ) );
  DFFSR \regs_reg[2][12]  ( .D(n900), .CLK(clk), .R(n394), .S(1'b1), .Q(
        \regs[2][12] ) );
  DFFSR \regs_reg[2][11]  ( .D(n864), .CLK(clk), .R(n394), .S(1'b1), .Q(
        \regs[2][11] ) );
  DFFSR \regs_reg[2][10]  ( .D(n857), .CLK(clk), .R(n394), .S(1'b1), .Q(
        \regs[2][10] ) );
  DFFSR \regs_reg[2][9]  ( .D(n851), .CLK(clk), .R(n394), .S(1'b1), .Q(
        \regs[2][9] ) );
  DFFSR \regs_reg[2][8]  ( .D(n870), .CLK(clk), .R(n394), .S(1'b1), .Q(
        \regs[2][8] ) );
  DFFSR \regs_reg[2][7]  ( .D(n836), .CLK(clk), .R(n394), .S(1'b1), .Q(
        \regs[2][7] ) );
  DFFSR \regs_reg[2][6]  ( .D(n830), .CLK(clk), .R(n394), .S(1'b1), .Q(
        \regs[2][6] ) );
  DFFSR \regs_reg[2][5]  ( .D(n822), .CLK(clk), .R(n394), .S(1'b1), .Q(
        \regs[2][5] ) );
  DFFSR \regs_reg[2][4]  ( .D(n843), .CLK(clk), .R(n394), .S(1'b1), .Q(
        \regs[2][4] ) );
  DFFSR \regs_reg[2][3]  ( .D(n809), .CLK(clk), .R(n393), .S(1'b1), .Q(
        \regs[2][3] ) );
  DFFSR \regs_reg[2][2]  ( .D(n803), .CLK(clk), .R(n393), .S(1'b1), .Q(
        \regs[2][2] ) );
  DFFSR \regs_reg[2][1]  ( .D(n796), .CLK(clk), .R(n393), .S(1'b1), .Q(
        \regs[2][1] ) );
  DFFSR \regs_reg[2][0]  ( .D(net5117), .CLK(clk), .R(n393), .S(1'b1), .Q(
        \regs[2][0] ) );
  DFFSR \regs_reg[1][15]  ( .D(n892), .CLK(clk), .R(n393), .S(1'b1), .Q(
        \regs[1][15] ) );
  DFFSR \regs_reg[1][14]  ( .D(n891), .CLK(clk), .R(n393), .S(1'b1), .Q(
        \regs[1][14] ) );
  DFFSR \regs_reg[1][13]  ( .D(n883), .CLK(clk), .R(n393), .S(1'b1), .Q(
        \regs[1][13] ) );
  DFFSR \regs_reg[1][12]  ( .D(n905), .CLK(clk), .R(n393), .S(1'b1), .Q(
        \regs[1][12] ) );
  DFFSR \regs_reg[1][11]  ( .D(n869), .CLK(clk), .R(n393), .S(1'b1), .Q(
        \regs[1][11] ) );
  DFFSR \regs_reg[1][10]  ( .D(n863), .CLK(clk), .R(n393), .S(1'b1), .Q(
        \regs[1][10] ) );
  DFFSR \regs_reg[1][9]  ( .D(n856), .CLK(clk), .R(n393), .S(1'b1), .Q(
        \regs[1][9] ) );
  DFFSR \regs_reg[1][8]  ( .D(n877), .CLK(clk), .R(n393), .S(1'b1), .Q(
        \regs[1][8] ) );
  DFFSR \regs_reg[1][7]  ( .D(net5083), .CLK(clk), .R(n392), .S(1'b1), .Q(
        \regs[1][7] ) );
  DFFSR \regs_reg[1][6]  ( .D(net5092), .CLK(clk), .R(n392), .S(1'b1), .Q(
        \regs[1][6] ) );
  DFFSR \regs_reg[1][5]  ( .D(n829), .CLK(clk), .R(n392), .S(1'b1), .Q(
        \regs[1][5] ) );
  DFFSR \regs_reg[1][4]  ( .D(n850), .CLK(clk), .R(n392), .S(1'b1), .Q(
        \regs[1][4] ) );
  DFFSR \regs_reg[1][3]  ( .D(n816), .CLK(clk), .R(n392), .S(1'b1), .Q(
        \regs[1][3] ) );
  DFFSR \regs_reg[1][2]  ( .D(net5128), .CLK(clk), .R(n392), .S(1'b1), .Q(
        \regs[1][2] ) );
  DFFSR \regs_reg[1][1]  ( .D(net5137), .CLK(clk), .R(n392), .S(1'b1), .Q(
        \regs[1][1] ) );
  DFFSR \regs_reg[1][0]  ( .D(net5110), .CLK(clk), .R(n392), .S(1'b1), .Q(
        \regs[1][0] ) );
  DFFSR \regs_reg[0][15]  ( .D(n899), .CLK(clk), .R(n392), .S(1'b1), .Q(
        outreg_data[15]) );
  DFFSR \regs_reg[0][14]  ( .D(n890), .CLK(clk), .R(n392), .S(1'b1), .Q(
        outreg_data[14]) );
  DFFSR \regs_reg[0][13]  ( .D(net5030), .CLK(clk), .R(n392), .S(1'b1), .Q(
        outreg_data[13]) );
  DFFSR \regs_reg[0][12]  ( .D(net5003), .CLK(clk), .R(n392), .S(1'b1), .Q(
        outreg_data[12]) );
  DFFSR \regs_reg[0][11]  ( .D(net5048), .CLK(clk), .R(n391), .S(1'b1), .Q(
        outreg_data[11]) );
  DFFSR \regs_reg[0][10]  ( .D(net5057), .CLK(clk), .R(n391), .S(1'b1), .Q(
        outreg_data[10]) );
  DFFSR \regs_reg[0][9]  ( .D(net5066), .CLK(clk), .R(n391), .S(1'b1), .Q(
        outreg_data[9]) );
  DFFSR \regs_reg[0][8]  ( .D(n876), .CLK(clk), .R(n391), .S(1'b1), .Q(
        outreg_data[8]) );
  DFFSR \regs_reg[0][7]  ( .D(n842), .CLK(clk), .R(n391), .S(1'b1), .Q(
        outreg_data[7]) );
  DFFSR \regs_reg[0][6]  ( .D(net5093), .CLK(clk), .R(n391), .S(1'b1), .Q(
        outreg_data[6]) );
  DFFSR \regs_reg[0][5]  ( .D(n828), .CLK(clk), .R(n391), .S(1'b1), .Q(
        outreg_data[5]) );
  DFFSR \regs_reg[0][4]  ( .D(n849), .CLK(clk), .R(n391), .S(1'b1), .Q(
        outreg_data[4]) );
  DFFSR \regs_reg[0][3]  ( .D(n815), .CLK(clk), .R(n391), .S(1'b1), .Q(
        outreg_data[3]) );
  DFFSR \regs_reg[0][2]  ( .D(net5129), .CLK(clk), .R(n391), .S(1'b1), .Q(
        outreg_data[2]) );
  DFFSR \regs_reg[0][1]  ( .D(n802), .CLK(clk), .R(n391), .S(1'b1), .Q(
        outreg_data[1]) );
  DFFSR \regs_reg[0][0]  ( .D(net5111), .CLK(clk), .R(n391), .S(1'b1), .Q(
        outreg_data[0]) );
  OR2X2 U258 ( .A(n554), .B(n555), .Y(r2_data[9]) );
  OR2X2 U259 ( .A(n582), .B(n583), .Y(r2_data[8]) );
  OR2X2 U260 ( .A(n594), .B(n595), .Y(r2_data[7]) );
  OR2X2 U261 ( .A(n606), .B(n607), .Y(r2_data[6]) );
  OR2X2 U262 ( .A(n618), .B(n619), .Y(r2_data[5]) );
  OR2X2 U263 ( .A(n630), .B(n631), .Y(r2_data[4]) );
  OR2X2 U264 ( .A(n642), .B(n643), .Y(r2_data[3]) );
  OR2X2 U265 ( .A(n654), .B(n655), .Y(r2_data[2]) );
  OR2X2 U266 ( .A(n666), .B(n667), .Y(r2_data[1]) );
  OR2X2 U267 ( .A(n678), .B(n679), .Y(r2_data[15]) );
  OR2X2 U268 ( .A(n690), .B(n691), .Y(r2_data[14]) );
  OR2X2 U269 ( .A(n702), .B(n703), .Y(r2_data[13]) );
  OR2X2 U270 ( .A(n714), .B(n715), .Y(r2_data[12]) );
  OR2X2 U271 ( .A(n726), .B(n727), .Y(r2_data[11]) );
  OR2X2 U272 ( .A(n738), .B(n739), .Y(r2_data[10]) );
  OR2X2 U273 ( .A(n750), .B(n751), .Y(r2_data[0]) );
  AND2X2 U274 ( .A(n762), .B(n761), .Y(n566) );
  AND2X2 U275 ( .A(n762), .B(n760), .Y(n565) );
  AND2X2 U276 ( .A(n762), .B(n759), .Y(n568) );
  AND2X2 U277 ( .A(n762), .B(n758), .Y(n567) );
  AND2X2 U279 ( .A(r2_sel[1]), .B(n967), .Y(n761) );
  AND2X2 U281 ( .A(r2_sel[1]), .B(r2_sel[0]), .Y(n760) );
  NAND3X1 U620 ( .A(n569), .B(n570), .C(n571), .Y(n554) );
  NOR2X1 U621 ( .A(n572), .B(n573), .Y(n571) );
  OAI22X1 U622 ( .A(n381), .B(n957), .C(n382), .D(n942), .Y(n573) );
  OAI22X1 U623 ( .A(n379), .B(n927), .C(n380), .D(n912), .Y(n572) );
  AOI22X1 U624 ( .A(\regs[15][9] ), .B(n287), .C(\regs[14][9] ), .D(n285), .Y(
        n570) );
  AOI22X1 U625 ( .A(\regs[13][9] ), .B(n286), .C(\regs[12][9] ), .D(n284), .Y(
        n569) );
  NAND3X1 U632 ( .A(n589), .B(n590), .C(n591), .Y(n582) );
  NOR2X1 U633 ( .A(n592), .B(n593), .Y(n591) );
  OAI22X1 U634 ( .A(n381), .B(n958), .C(n382), .D(n943), .Y(n593) );
  OAI22X1 U635 ( .A(n379), .B(n928), .C(n380), .D(n913), .Y(n592) );
  AOI22X1 U636 ( .A(\regs[15][8] ), .B(n287), .C(\regs[14][8] ), .D(n285), .Y(
        n590) );
  AOI22X1 U637 ( .A(\regs[13][8] ), .B(n286), .C(\regs[12][8] ), .D(n284), .Y(
        n589) );
  NAND3X1 U644 ( .A(n601), .B(n602), .C(n603), .Y(n594) );
  NOR2X1 U645 ( .A(n604), .B(n605), .Y(n603) );
  OAI22X1 U646 ( .A(n381), .B(n959), .C(n382), .D(n944), .Y(n605) );
  OAI22X1 U647 ( .A(n379), .B(n929), .C(n380), .D(n914), .Y(n604) );
  AOI22X1 U648 ( .A(\regs[15][7] ), .B(n287), .C(\regs[14][7] ), .D(n285), .Y(
        n602) );
  AOI22X1 U649 ( .A(\regs[13][7] ), .B(n286), .C(\regs[12][7] ), .D(n284), .Y(
        n601) );
  NAND3X1 U656 ( .A(n613), .B(n614), .C(n615), .Y(n606) );
  NOR2X1 U657 ( .A(n616), .B(n617), .Y(n615) );
  OAI22X1 U658 ( .A(n381), .B(net4944), .C(n382), .D(net4960), .Y(n617) );
  OAI22X1 U659 ( .A(n379), .B(net4976), .C(n380), .D(net4992), .Y(n616) );
  AOI22X1 U660 ( .A(\regs[15][6] ), .B(n287), .C(\regs[14][6] ), .D(n285), .Y(
        n614) );
  AOI22X1 U661 ( .A(\regs[13][6] ), .B(n286), .C(\regs[12][6] ), .D(n284), .Y(
        n613) );
  NAND3X1 U668 ( .A(n625), .B(n626), .C(n627), .Y(n618) );
  NOR2X1 U669 ( .A(n628), .B(n629), .Y(n627) );
  OAI22X1 U670 ( .A(n381), .B(n960), .C(n382), .D(n945), .Y(n629) );
  OAI22X1 U671 ( .A(n379), .B(n930), .C(n380), .D(n915), .Y(n628) );
  AOI22X1 U672 ( .A(\regs[15][5] ), .B(n287), .C(\regs[14][5] ), .D(n285), .Y(
        n626) );
  AOI22X1 U673 ( .A(\regs[13][5] ), .B(n286), .C(\regs[12][5] ), .D(n284), .Y(
        n625) );
  NAND3X1 U680 ( .A(n637), .B(n638), .C(n639), .Y(n630) );
  NOR2X1 U681 ( .A(n640), .B(n641), .Y(n639) );
  OAI22X1 U682 ( .A(n381), .B(n961), .C(n382), .D(n946), .Y(n641) );
  OAI22X1 U683 ( .A(n379), .B(n931), .C(n380), .D(n916), .Y(n640) );
  AOI22X1 U684 ( .A(\regs[15][4] ), .B(n287), .C(\regs[14][4] ), .D(n285), .Y(
        n638) );
  AOI22X1 U685 ( .A(\regs[13][4] ), .B(n286), .C(\regs[12][4] ), .D(n284), .Y(
        n637) );
  NAND3X1 U692 ( .A(n649), .B(n650), .C(n651), .Y(n642) );
  NOR2X1 U693 ( .A(n652), .B(n653), .Y(n651) );
  OAI22X1 U694 ( .A(n381), .B(n962), .C(n382), .D(n947), .Y(n653) );
  OAI22X1 U695 ( .A(n379), .B(n932), .C(n380), .D(n917), .Y(n652) );
  AOI22X1 U696 ( .A(\regs[15][3] ), .B(n287), .C(\regs[14][3] ), .D(n285), .Y(
        n650) );
  AOI22X1 U697 ( .A(\regs[13][3] ), .B(n286), .C(\regs[12][3] ), .D(n284), .Y(
        n649) );
  NAND3X1 U704 ( .A(n661), .B(n662), .C(n663), .Y(n654) );
  NOR2X1 U705 ( .A(n664), .B(n665), .Y(n663) );
  OAI22X1 U706 ( .A(n381), .B(n963), .C(n382), .D(n948), .Y(n665) );
  OAI22X1 U707 ( .A(n379), .B(n933), .C(n380), .D(n918), .Y(n664) );
  AOI22X1 U708 ( .A(\regs[15][2] ), .B(n287), .C(\regs[14][2] ), .D(n285), .Y(
        n662) );
  AOI22X1 U709 ( .A(\regs[13][2] ), .B(n286), .C(\regs[12][2] ), .D(n284), .Y(
        n661) );
  NAND3X1 U716 ( .A(n673), .B(n674), .C(n675), .Y(n666) );
  NOR2X1 U717 ( .A(n676), .B(n677), .Y(n675) );
  OAI22X1 U718 ( .A(n381), .B(n964), .C(n382), .D(n949), .Y(n677) );
  OAI22X1 U719 ( .A(n379), .B(n934), .C(n380), .D(n919), .Y(n676) );
  AOI22X1 U720 ( .A(\regs[15][1] ), .B(n287), .C(\regs[14][1] ), .D(n285), .Y(
        n674) );
  AOI22X1 U721 ( .A(\regs[13][1] ), .B(n286), .C(\regs[12][1] ), .D(n284), .Y(
        n673) );
  NAND3X1 U728 ( .A(n685), .B(n686), .C(n687), .Y(n678) );
  NOR2X1 U729 ( .A(n688), .B(n689), .Y(n687) );
  OAI22X1 U730 ( .A(n381), .B(n951), .C(n382), .D(n936), .Y(n689) );
  OAI22X1 U731 ( .A(n379), .B(n921), .C(n380), .D(n906), .Y(n688) );
  AOI22X1 U732 ( .A(\regs[15][15] ), .B(n287), .C(\regs[14][15] ), .D(n285), 
        .Y(n686) );
  AOI22X1 U733 ( .A(\regs[13][15] ), .B(n286), .C(\regs[12][15] ), .D(n284), 
        .Y(n685) );
  NAND3X1 U740 ( .A(n697), .B(n698), .C(n699), .Y(n690) );
  NOR2X1 U741 ( .A(n700), .B(n701), .Y(n699) );
  OAI22X1 U742 ( .A(n381), .B(n952), .C(n382), .D(n937), .Y(n701) );
  OAI22X1 U743 ( .A(n379), .B(n922), .C(n380), .D(n907), .Y(n700) );
  AOI22X1 U744 ( .A(\regs[15][14] ), .B(n287), .C(\regs[14][14] ), .D(n285), 
        .Y(n698) );
  AOI22X1 U745 ( .A(\regs[13][14] ), .B(n286), .C(\regs[12][14] ), .D(n284), 
        .Y(n697) );
  NAND3X1 U752 ( .A(n709), .B(n710), .C(n711), .Y(n702) );
  NOR2X1 U753 ( .A(n712), .B(n713), .Y(n711) );
  OAI22X1 U754 ( .A(n381), .B(n953), .C(n382), .D(n938), .Y(n713) );
  OAI22X1 U755 ( .A(n379), .B(n923), .C(n380), .D(n908), .Y(n712) );
  AOI22X1 U756 ( .A(\regs[15][13] ), .B(n287), .C(\regs[14][13] ), .D(n285), 
        .Y(n710) );
  AOI22X1 U757 ( .A(\regs[13][13] ), .B(n286), .C(\regs[12][13] ), .D(n284), 
        .Y(n709) );
  NAND3X1 U764 ( .A(n721), .B(n722), .C(n723), .Y(n714) );
  NOR2X1 U765 ( .A(n724), .B(n725), .Y(n723) );
  OAI22X1 U766 ( .A(n381), .B(n954), .C(n382), .D(n939), .Y(n725) );
  OAI22X1 U767 ( .A(n379), .B(n924), .C(n380), .D(n909), .Y(n724) );
  AOI22X1 U768 ( .A(\regs[15][12] ), .B(n287), .C(\regs[14][12] ), .D(n285), 
        .Y(n722) );
  AOI22X1 U769 ( .A(\regs[13][12] ), .B(n286), .C(\regs[12][12] ), .D(n284), 
        .Y(n721) );
  NAND3X1 U776 ( .A(n733), .B(n734), .C(n735), .Y(n726) );
  NOR2X1 U777 ( .A(n736), .B(n737), .Y(n735) );
  OAI22X1 U778 ( .A(n381), .B(n955), .C(n382), .D(n940), .Y(n737) );
  OAI22X1 U779 ( .A(n379), .B(n925), .C(n380), .D(n910), .Y(n736) );
  AOI22X1 U780 ( .A(\regs[15][11] ), .B(n287), .C(\regs[14][11] ), .D(n285), 
        .Y(n734) );
  AOI22X1 U781 ( .A(\regs[13][11] ), .B(n286), .C(\regs[12][11] ), .D(n284), 
        .Y(n733) );
  NAND3X1 U788 ( .A(n745), .B(n746), .C(n747), .Y(n738) );
  NOR2X1 U789 ( .A(n748), .B(n749), .Y(n747) );
  OAI22X1 U790 ( .A(n381), .B(n956), .C(n382), .D(n941), .Y(n749) );
  OAI22X1 U791 ( .A(n379), .B(n926), .C(n380), .D(n911), .Y(n748) );
  AOI22X1 U792 ( .A(\regs[15][10] ), .B(n287), .C(\regs[14][10] ), .D(n285), 
        .Y(n746) );
  AOI22X1 U793 ( .A(\regs[13][10] ), .B(n286), .C(\regs[12][10] ), .D(n284), 
        .Y(n745) );
  NOR2X1 U802 ( .A(n968), .B(r2_sel[3]), .Y(n757) );
  NOR2X1 U805 ( .A(r2_sel[2]), .B(r2_sel[3]), .Y(n762) );
  NAND3X1 U806 ( .A(n763), .B(n764), .C(n765), .Y(n750) );
  NOR2X1 U807 ( .A(n766), .B(n767), .Y(n765) );
  OAI22X1 U808 ( .A(n381), .B(n965), .C(n382), .D(n950), .Y(n767) );
  OAI22X1 U811 ( .A(n379), .B(n935), .C(n380), .D(n920), .Y(n766) );
  NOR2X1 U814 ( .A(n966), .B(r2_sel[2]), .Y(n768) );
  AOI22X1 U815 ( .A(\regs[15][0] ), .B(n287), .C(\regs[14][0] ), .D(n285), .Y(
        n764) );
  AOI22X1 U816 ( .A(\regs[13][0] ), .B(n286), .C(\regs[12][0] ), .D(n284), .Y(
        n763) );
  NOR2X1 U817 ( .A(r2_sel[0]), .B(r2_sel[1]), .Y(n759) );
  NOR2X1 U818 ( .A(n966), .B(n968), .Y(n769) );
  NOR2X1 U819 ( .A(n967), .B(r2_sel[1]), .Y(n758) );
  NOR2X1 U1020 ( .A(net19883), .B(net20485), .Y(n984) );
  AND2X2 U278 ( .A(net19817), .B(net19816), .Y(net21835) );
  INVX1 U280 ( .A(n258), .Y(n257) );
  AND2X2 U282 ( .A(n487), .B(n488), .Y(n344) );
  INVX8 U283 ( .A(w_data[5]), .Y(n300) );
  INVX8 U284 ( .A(w_data[1]), .Y(n258) );
  MUX2X1 U285 ( .B(n345), .A(net19793), .S(net21549), .Y(n1191) );
  MUX2X1 U286 ( .B(n357), .A(net19577), .S(net21543), .Y(n1153) );
  INVX4 U287 ( .A(net62000), .Y(net62001) );
  INVX1 U288 ( .A(w_data[5]), .Y(n262) );
  MUX2X1 U289 ( .B(n301), .A(n786), .S(n259), .Y(n871) );
  INVX8 U290 ( .A(net21659), .Y(n259) );
  INVX1 U291 ( .A(n345), .Y(n260) );
  INVX1 U292 ( .A(n257), .Y(n277) );
  INVX1 U293 ( .A(n301), .Y(n261) );
  INVX2 U294 ( .A(n377), .Y(n378) );
  AND2X2 U295 ( .A(n580), .B(n581), .Y(n291) );
  NOR2X1 U296 ( .A(net25262), .B(w_sel[1]), .Y(n263) );
  INVX1 U297 ( .A(net25223), .Y(net19530) );
  INVX2 U298 ( .A(net19530), .Y(n280) );
  INVX2 U299 ( .A(net44616), .Y(net42609) );
  INVX2 U300 ( .A(net42609), .Y(net62692) );
  INVX2 U301 ( .A(net42609), .Y(net62687) );
  AND2X2 U302 ( .A(n282), .B(net21441), .Y(n264) );
  AND2X2 U303 ( .A(n282), .B(n263), .Y(n265) );
  MUX2X1 U304 ( .B(net36206), .A(net19372), .S(net62687), .Y(net5093) );
  INVX8 U305 ( .A(w_data[6]), .Y(net36206) );
  INVX2 U306 ( .A(outreg_data[6]), .Y(net19372) );
  INVX4 U307 ( .A(net19880), .Y(net19497) );
  NAND3X1 U308 ( .A(net20474), .B(net21533), .C(r1_sel[1]), .Y(net19880) );
  BUFX2 U309 ( .A(r1_sel[0]), .Y(net20474) );
  AND2X2 U310 ( .A(net19886), .B(net19883), .Y(net21533) );
  INVX1 U311 ( .A(net19880), .Y(net62736) );
  INVX1 U312 ( .A(net19880), .Y(net21748) );
  NAND3X1 U313 ( .A(net20474), .B(r1_sel[1]), .C(net21519), .Y(net19881) );
  INVX1 U314 ( .A(net20474), .Y(net21515) );
  NAND2X1 U315 ( .A(net21761), .B(n266), .Y(r1_data[6]) );
  AND2X2 U316 ( .A(net19712), .B(net19711), .Y(net21761) );
  AOI22X1 U317 ( .A(net62001), .B(\regs[2][6] ), .C(net19517), .D(\regs[7][6] ), .Y(net19711) );
  INVX4 U318 ( .A(net19881), .Y(net19517) );
  AOI21X1 U319 ( .A(net19497), .B(\regs[3][6] ), .C(n269), .Y(net19712) );
  NAND3X1 U320 ( .A(net19720), .B(net19721), .C(n270), .Y(n269) );
  AOI22X1 U321 ( .A(net19514), .B(\regs[9][6] ), .C(net19515), .D(\regs[8][6] ), .Y(net19720) );
  INVX2 U322 ( .A(net19879), .Y(net19514) );
  INVX2 U323 ( .A(net19878), .Y(net19515) );
  AOI22X1 U324 ( .A(net21469), .B(\regs[11][6] ), .C(net21470), .D(
        \regs[10][6] ), .Y(net19721) );
  AND2X2 U325 ( .A(net21417), .B(net21764), .Y(net21469) );
  AND2X2 U326 ( .A(net21417), .B(net21515), .Y(net21470) );
  NOR2X1 U327 ( .A(net19723), .B(n271), .Y(n270) );
  OAI22X1 U328 ( .A(net20254), .B(net19727), .C(net19510), .D(net19728), .Y(
        net19723) );
  INVX2 U329 ( .A(net20253), .Y(net20254) );
  INVX2 U330 ( .A(\regs[13][6] ), .Y(net19727) );
  NAND3X1 U331 ( .A(net62657), .B(net21562), .C(net21515), .Y(net19510) );
  INVX2 U332 ( .A(\regs[12][6] ), .Y(net19728) );
  OAI22X1 U333 ( .A(net20244), .B(net19725), .C(net20238), .D(net19726), .Y(
        n271) );
  INVX2 U334 ( .A(net20243), .Y(net20244) );
  INVX2 U335 ( .A(\regs[15][6] ), .Y(net19725) );
  INVX2 U336 ( .A(net20237), .Y(net20238) );
  INVX2 U337 ( .A(\regs[14][6] ), .Y(net19726) );
  NOR2X1 U338 ( .A(n267), .B(n268), .Y(n266) );
  OAI22X1 U339 ( .A(n272), .B(net19718), .C(net20230), .D(net19373), .Y(n267)
         );
  INVX1 U340 ( .A(net20389), .Y(n272) );
  AND2X2 U341 ( .A(net20399), .B(r1_sel[1]), .Y(net20389) );
  INVX2 U342 ( .A(\regs[6][6] ), .Y(net19718) );
  INVX4 U343 ( .A(net21476), .Y(net20230) );
  INVX2 U344 ( .A(\regs[1][6] ), .Y(net19373) );
  OAI21X1 U345 ( .A(net19716), .B(net46042), .C(net19717), .Y(n268) );
  INVX2 U346 ( .A(\regs[5][6] ), .Y(net19716) );
  INVX8 U347 ( .A(net20419), .Y(net46042) );
  AOI22X1 U348 ( .A(net62801), .B(\regs[4][6] ), .C(outreg_data[6]), .D(
        net19696), .Y(net19717) );
  AND2X2 U349 ( .A(net20402), .B(net19671), .Y(net62801) );
  INVX4 U350 ( .A(net19823), .Y(net19696) );
  INVX2 U351 ( .A(n368), .Y(n369) );
  BUFX2 U352 ( .A(net19851), .Y(net62827) );
  INVX1 U353 ( .A(n261), .Y(n274) );
  MUX2X1 U354 ( .B(net19356), .A(n301), .S(net21657), .Y(n870) );
  INVX1 U355 ( .A(r1_sel[1]), .Y(net19671) );
  INVX4 U356 ( .A(r1_sel[1]), .Y(net25346) );
  AND2X2 U357 ( .A(net20402), .B(net19671), .Y(n273) );
  INVX1 U358 ( .A(n347), .Y(n275) );
  INVX4 U359 ( .A(net21476), .Y(net62787) );
  INVX1 U360 ( .A(n346), .Y(n276) );
  INVX1 U361 ( .A(n276), .Y(n278) );
  INVX1 U362 ( .A(n275), .Y(n279) );
  INVX1 U363 ( .A(net21638), .Y(net62716) );
  INVX1 U364 ( .A(n260), .Y(n281) );
  MUX2X1 U365 ( .B(n346), .A(n585), .S(net21549), .Y(n1203) );
  MUX2X1 U366 ( .B(n346), .A(n610), .S(net21547), .Y(n1187) );
  MUX2X1 U367 ( .B(n346), .A(n612), .S(net21545), .Y(n1171) );
  MUX2X1 U368 ( .B(n346), .A(n584), .S(net21543), .Y(n1155) );
  MUX2X1 U369 ( .B(n346), .A(n694), .S(net21541), .Y(n894) );
  MUX2X1 U370 ( .B(n346), .A(n695), .S(n280), .Y(n893) );
  MUX2X1 U371 ( .B(n346), .A(n696), .S(net21537), .Y(n892) );
  MUX2X1 U372 ( .B(n346), .A(n704), .S(net62692), .Y(n899) );
  MUX2X1 U373 ( .B(n347), .A(n552), .S(net21549), .Y(n1202) );
  MUX2X1 U374 ( .B(n347), .A(n574), .S(net21547), .Y(n1186) );
  MUX2X1 U375 ( .B(n347), .A(n576), .S(net21545), .Y(n1170) );
  MUX2X1 U376 ( .B(n347), .A(n551), .S(net21543), .Y(n1154) );
  MUX2X1 U377 ( .B(n347), .A(n671), .S(net21541), .Y(n885) );
  MUX2X1 U378 ( .B(n347), .A(n672), .S(n280), .Y(n884) );
  MUX2X1 U379 ( .B(n347), .A(n680), .S(net21537), .Y(n891) );
  MUX2X1 U380 ( .B(n347), .A(n681), .S(net62687), .Y(n890) );
  AND2X2 U381 ( .A(n304), .B(w_en), .Y(n282) );
  AND2X2 U382 ( .A(n364), .B(net21377), .Y(n283) );
  AND2X2 U383 ( .A(n759), .B(n769), .Y(n284) );
  AND2X2 U384 ( .A(n761), .B(n769), .Y(n285) );
  AND2X2 U385 ( .A(n758), .B(n769), .Y(n286) );
  AND2X2 U386 ( .A(n769), .B(n760), .Y(n287) );
  AND2X2 U387 ( .A(net20485), .B(r1_sel[3]), .Y(net62657) );
  OR2X2 U388 ( .A(net32977), .B(net25267), .Y(n288) );
  OR2X2 U389 ( .A(net32977), .B(net25269), .Y(n289) );
  AND2X2 U390 ( .A(n305), .B(w_en), .Y(n290) );
  AND2X1 U391 ( .A(net19579), .B(n324), .Y(n292) );
  AND2X1 U392 ( .A(net19600), .B(n331), .Y(n293) );
  AND2X1 U393 ( .A(net19642), .B(n339), .Y(n294) );
  AND2X1 U394 ( .A(net19796), .B(n350), .Y(n295) );
  AND2X1 U395 ( .A(net19558), .B(n358), .Y(n296) );
  AND2X1 U396 ( .A(n534), .B(n535), .Y(n297) );
  OR2X2 U397 ( .A(net32977), .B(net25264), .Y(n298) );
  MUX2X1 U398 ( .B(net36208), .A(net25209), .S(n280), .Y(net5117) );
  MUX2X1 U399 ( .B(n455), .A(net19772), .S(net21549), .Y(n1192) );
  MUX2X1 U400 ( .B(n455), .A(net19773), .S(net21543), .Y(n1144) );
  MUX2X1 U401 ( .B(n455), .A(n466), .S(net21547), .Y(n1176) );
  MUX2X1 U402 ( .B(n455), .A(net19392), .S(n280), .Y(n843) );
  MUX2X1 U403 ( .B(n455), .A(n752), .S(net21541), .Y(n844) );
  MUX2X1 U404 ( .B(n455), .A(net19390), .S(net62687), .Y(n849) );
  MUX2X1 U405 ( .B(n455), .A(net19758), .S(net21545), .Y(n1160) );
  INVX1 U406 ( .A(net62801), .Y(net62622) );
  AND2X2 U407 ( .A(\regs[1][0] ), .B(net62002), .Y(net19857) );
  INVX1 U408 ( .A(\regs[1][0] ), .Y(net19481) );
  MUX2X1 U409 ( .B(net19638), .A(n517), .S(net21549), .Y(n1198) );
  MUX2X1 U410 ( .B(net19638), .A(n516), .S(net21543), .Y(n1150) );
  MUX2X1 U411 ( .B(net19638), .A(n530), .S(net21545), .Y(n1166) );
  MUX2X1 U412 ( .B(net19638), .A(n528), .S(net21547), .Y(n1182) );
  MUX2X1 U413 ( .B(net19638), .A(n634), .S(n280), .Y(n857) );
  MUX2X1 U414 ( .B(net19638), .A(n633), .S(net21541), .Y(n858) );
  MUX2X1 U415 ( .B(net19813), .A(n348), .S(net62687), .Y(net5129) );
  MUX2X1 U416 ( .B(n330), .A(net19618), .S(net21549), .Y(n1199) );
  MUX2X1 U417 ( .B(n330), .A(net19619), .S(net21543), .Y(n1151) );
  MUX2X1 U418 ( .B(n323), .A(net19597), .S(net21549), .Y(n1200) );
  MUX2X1 U419 ( .B(n323), .A(net19598), .S(net21543), .Y(n1152) );
  MUX2X1 U420 ( .B(n337), .A(net19660), .S(net21549), .Y(n1197) );
  MUX2X1 U421 ( .B(n337), .A(net19661), .S(net21543), .Y(n1149) );
  MUX2X1 U422 ( .B(n337), .A(net19341), .S(n280), .Y(n851) );
  MUX2X1 U423 ( .B(n337), .A(net19343), .S(net21541), .Y(n852) );
  MUX2X1 U424 ( .B(n337), .A(n513), .S(net21545), .Y(n1165) );
  MUX2X1 U425 ( .B(n330), .A(n538), .S(net21545), .Y(n1167) );
  MUX2X1 U426 ( .B(n323), .A(n543), .S(net21545), .Y(n1168) );
  MUX2X1 U427 ( .B(n337), .A(net19648), .S(net21547), .Y(n1181) );
  MUX2X1 U428 ( .B(n330), .A(net19606), .S(net21547), .Y(n1183) );
  MUX2X1 U429 ( .B(n330), .A(net19464), .S(net21539), .Y(n864) );
  MUX2X1 U430 ( .B(n323), .A(net19585), .S(net21547), .Y(n1184) );
  MUX2X1 U431 ( .B(n323), .A(net19455), .S(net21539), .Y(n900) );
  MUX2X1 U432 ( .B(net19638), .A(n635), .S(net21537), .Y(n863) );
  MUX2X1 U433 ( .B(n357), .A(net19576), .S(net21549), .Y(n1201) );
  MUX2X1 U434 ( .B(n301), .A(net19686), .S(net21549), .Y(n1196) );
  MUX2X1 U435 ( .B(n301), .A(n505), .S(net21547), .Y(n1180) );
  MUX2X1 U436 ( .B(n301), .A(n506), .S(net21545), .Y(n1164) );
  MUX2X1 U437 ( .B(n301), .A(net19687), .S(net21543), .Y(n1148) );
  MUX2X1 U438 ( .B(n357), .A(n548), .S(net21545), .Y(n1169) );
  MUX2X1 U439 ( .B(n357), .A(net19564), .S(net21547), .Y(n1185) );
  MUX2X1 U440 ( .B(n357), .A(net19446), .S(n299), .Y(n878) );
  INVX4 U441 ( .A(net21539), .Y(net21657) );
  INVX4 U442 ( .A(net21657), .Y(n299) );
  MUX2X1 U443 ( .B(n357), .A(net19447), .S(net21541), .Y(n879) );
  AND2X2 U444 ( .A(net19689), .B(net19688), .Y(net21819) );
  MUX2X1 U445 ( .B(n301), .A(net19354), .S(net62687), .Y(n876) );
  MUX2X1 U446 ( .B(n301), .A(n787), .S(net21537), .Y(n877) );
  MUX2X1 U447 ( .B(n345), .A(net19794), .S(net21543), .Y(n1143) );
  MUX2X1 U448 ( .B(n345), .A(n450), .S(net21545), .Y(n1159) );
  MUX2X1 U449 ( .B(n345), .A(n449), .S(net21547), .Y(n1175) );
  MUX2X1 U450 ( .B(n345), .A(net19401), .S(n299), .Y(n809) );
  MUX2X1 U451 ( .B(n345), .A(n731), .S(net21541), .Y(n810) );
  INVX2 U452 ( .A(net21541), .Y(net21659) );
  MUX2X1 U453 ( .B(n345), .A(net19399), .S(net62692), .Y(n815) );
  MUX2X1 U454 ( .B(n345), .A(n732), .S(net21537), .Y(n816) );
  MUX2X1 U455 ( .B(n357), .A(net19445), .S(net21537), .Y(n883) );
  MUX2X1 U456 ( .B(n323), .A(net19456), .S(net21541), .Y(n901) );
  MUX2X1 U457 ( .B(n337), .A(net19339), .S(net21537), .Y(n856) );
  MUX2X1 U458 ( .B(n323), .A(net19454), .S(net21537), .Y(n905) );
  MUX2X1 U459 ( .B(n330), .A(net19463), .S(net21537), .Y(n869) );
  INVX8 U460 ( .A(w_data[8]), .Y(n301) );
  AND2X2 U461 ( .A(net20402), .B(r1_sel[1]), .Y(n302) );
  NAND3X1 U462 ( .A(net21533), .B(r1_sel[1]), .C(net62827), .Y(net62000) );
  INVX1 U463 ( .A(r1_sel[1]), .Y(net62002) );
  MUX2X1 U464 ( .B(net19480), .A(net36208), .S(net42609), .Y(net5111) );
  INVX8 U465 ( .A(w_data[0]), .Y(net36208) );
  INVX2 U466 ( .A(outreg_data[0]), .Y(net19480) );
  OAI22X1 U467 ( .A(net21771), .B(net19480), .C(net19848), .D(net62622), .Y(
        net19847) );
  OAI22X1 U468 ( .A(net19338), .B(net19480), .C(net19340), .D(net19481), .Y(
        net19479) );
  NAND2X1 U469 ( .A(n321), .B(n290), .Y(net44616) );
  INVX1 U470 ( .A(net44616), .Y(net44509) );
  NAND2X1 U471 ( .A(n290), .B(n263), .Y(net19918) );
  NAND2X1 U472 ( .A(n290), .B(net21441), .Y(net19916) );
  NAND2X1 U473 ( .A(n290), .B(n364), .Y(net25223) );
  NOR2X1 U474 ( .A(w_sel[0]), .B(w_sel[3]), .Y(n305) );
  NAND2X1 U475 ( .A(n303), .B(w_en), .Y(net25267) );
  NAND3X1 U476 ( .A(w_sel[0]), .B(w_sel[3]), .C(w_en), .Y(net25269) );
  NOR2X1 U477 ( .A(w_sel[0]), .B(n307), .Y(n303) );
  INVX2 U478 ( .A(w_sel[0]), .Y(n306) );
  NOR2X1 U479 ( .A(w_sel[3]), .B(n306), .Y(n304) );
  INVX2 U480 ( .A(w_sel[3]), .Y(n307) );
  AOI22X1 U481 ( .A(net19517), .B(\regs[7][0] ), .C(net62001), .D(\regs[2][0] ), .Y(net19843) );
  NAND3X1 U482 ( .A(net19844), .B(net19843), .C(net19845), .Y(r1_data[0]) );
  INVX4 U483 ( .A(net19884), .Y(net19516) );
  INVX1 U484 ( .A(net19881), .Y(net21751) );
  AOI22X1 U485 ( .A(net19516), .B(\regs[2][1] ), .C(net19517), .D(\regs[7][1] ), .Y(net19816) );
  AOI22X1 U486 ( .A(net19516), .B(\regs[2][8] ), .C(net21751), .D(\regs[7][8] ), .Y(net19662) );
  AOI22X1 U487 ( .A(\regs[6][0] ), .B(net21403), .C(\regs[7][0] ), .D(net21405), .Y(net19475) );
  INVX2 U488 ( .A(\regs[7][0] ), .Y(net19905) );
  INVX2 U489 ( .A(\regs[2][0] ), .Y(net25209) );
  NAND3X1 U490 ( .A(net21533), .B(r1_sel[1]), .C(net62827), .Y(net19884) );
  INVX1 U491 ( .A(r1_sel[0]), .Y(net19851) );
  AND2X2 U492 ( .A(net21414), .B(net19851), .Y(net20402) );
  BUFX2 U493 ( .A(net21414), .Y(net21519) );
  NAND2X1 U494 ( .A(net21414), .B(r1_sel[0]), .Y(net19826) );
  AND2X2 U495 ( .A(net21414), .B(net21880), .Y(net20399) );
  NOR2X1 U496 ( .A(net19846), .B(net19847), .Y(net19845) );
  AOI22X1 U497 ( .A(n273), .B(\regs[4][3] ), .C(net21478), .D(outreg_data[3]), 
        .Y(net19780) );
  AOI22X1 U498 ( .A(net62801), .B(\regs[4][7] ), .C(net21478), .D(
        outreg_data[7]), .Y(net19694) );
  AOI22X1 U499 ( .A(net62801), .B(\regs[4][1] ), .C(net21478), .D(
        outreg_data[1]), .Y(net19822) );
  INVX2 U500 ( .A(\regs[4][0] ), .Y(net19848) );
  MUX2X1 U501 ( .B(net36208), .A(net19848), .S(net21543), .Y(n1140) );
  INVX1 U502 ( .A(net19696), .Y(net21771) );
  NAND2X1 U503 ( .A(net21442), .B(net25346), .Y(net19823) );
  OAI21X1 U504 ( .A(net21646), .B(net19854), .C(n308), .Y(net19846) );
  AOI22X1 U505 ( .A(n309), .B(net21833), .C(net19857), .D(n310), .Y(n308) );
  BUFX2 U506 ( .A(net21443), .Y(n310) );
  MUX2X1 U507 ( .B(net36208), .A(net19481), .S(net21537), .Y(net5110) );
  BUFX2 U508 ( .A(net20402), .Y(net21833) );
  NOR2X1 U509 ( .A(net62002), .B(net19860), .Y(n309) );
  INVX2 U510 ( .A(\regs[6][0] ), .Y(net19860) );
  INVX1 U511 ( .A(r1_sel[2]), .Y(net19886) );
  INVX1 U512 ( .A(net19886), .Y(net20485) );
  INVX2 U513 ( .A(r1_sel[3]), .Y(net19883) );
  AND2X2 U514 ( .A(net19883), .B(r1_sel[2]), .Y(net21414) );
  AND2X2 U515 ( .A(net19883), .B(net21888), .Y(net21415) );
  INVX1 U516 ( .A(r1_sel[2]), .Y(net21888) );
  NAND2X1 U517 ( .A(net21835), .B(n312), .Y(r1_data[1]) );
  NOR2X1 U518 ( .A(n314), .B(n313), .Y(n312) );
  NAND2X1 U519 ( .A(net20409), .B(net19822), .Y(n314) );
  NAND2X1 U520 ( .A(net62716), .B(\regs[5][1] ), .Y(net20409) );
  INVX2 U521 ( .A(\regs[5][1] ), .Y(net19821) );
  MUX2X1 U522 ( .B(n258), .A(net19821), .S(net21545), .Y(n1157) );
  NAND2X1 U523 ( .A(\regs[5][7] ), .B(net62716), .Y(net20460) );
  NAND2X1 U524 ( .A(net62716), .B(\regs[5][4] ), .Y(net20451) );
  INVX4 U525 ( .A(net21522), .Y(net21478) );
  NAND2X1 U526 ( .A(net21442), .B(net25346), .Y(net21522) );
  OAI22X1 U527 ( .A(net20234), .B(net19827), .C(net20230), .D(n311), .Y(n313)
         );
  INVX2 U528 ( .A(\regs[1][1] ), .Y(n311) );
  MUX2X1 U529 ( .B(n258), .A(n311), .S(net21537), .Y(net5137) );
  OAI22X1 U530 ( .A(net19338), .B(net19417), .C(net19340), .D(n311), .Y(
        net19416) );
  INVX2 U531 ( .A(\regs[6][1] ), .Y(net19827) );
  MUX2X1 U532 ( .B(n258), .A(net19827), .S(net21547), .Y(n1173) );
  INVX4 U533 ( .A(n302), .Y(net20234) );
  AOI21X1 U534 ( .A(net19497), .B(\regs[3][1] ), .C(n315), .Y(net19817) );
  NAND3X1 U535 ( .A(net19831), .B(net19832), .C(net19833), .Y(n315) );
  INVX2 U536 ( .A(\regs[2][1] ), .Y(net19419) );
  INVX2 U537 ( .A(\regs[7][1] ), .Y(net19841) );
  AOI22X1 U538 ( .A(\regs[6][1] ), .B(net21403), .C(\regs[7][1] ), .D(net21405), .Y(net19412) );
  INVX4 U539 ( .A(net20419), .Y(net20226) );
  NAND2X1 U540 ( .A(net21819), .B(n317), .Y(r1_data[7]) );
  NOR2X1 U541 ( .A(n319), .B(n318), .Y(n317) );
  NAND2X1 U542 ( .A(net20460), .B(net19694), .Y(n319) );
  INVX2 U543 ( .A(\regs[5][7] ), .Y(net19693) );
  MUX2X1 U544 ( .B(net19708), .A(net19693), .S(net21545), .Y(n1163) );
  OAI22X1 U545 ( .A(net20234), .B(net19697), .C(net20230), .D(n316), .Y(n318)
         );
  INVX2 U546 ( .A(\regs[1][7] ), .Y(n316) );
  MUX2X1 U547 ( .B(net19708), .A(n316), .S(net21537), .Y(net5083) );
  OAI22X1 U548 ( .A(net19338), .B(net19363), .C(net19340), .D(n316), .Y(
        net19362) );
  INVX2 U549 ( .A(\regs[6][7] ), .Y(net19697) );
  MUX2X1 U550 ( .B(net19708), .A(net19697), .S(net21547), .Y(n1179) );
  AOI21X1 U551 ( .A(net19497), .B(\regs[3][7] ), .C(n320), .Y(net19689) );
  NAND3X1 U552 ( .A(net19699), .B(net19700), .C(net19701), .Y(n320) );
  AOI22X1 U553 ( .A(net19516), .B(\regs[2][7] ), .C(net19517), .D(\regs[7][7] ), .Y(net19688) );
  INVX2 U554 ( .A(\regs[2][7] ), .Y(net19365) );
  INVX2 U555 ( .A(\regs[7][7] ), .Y(net19709) );
  AOI22X1 U556 ( .A(\regs[6][7] ), .B(net21403), .C(\regs[7][7] ), .D(net21405), .Y(net19358) );
  MUX2X1 U557 ( .B(net19708), .A(net19709), .S(net21549), .Y(n1195) );
  MUX2X1 U558 ( .B(net19708), .A(net19710), .S(net21543), .Y(n1147) );
  MUX2X1 U559 ( .B(net19708), .A(net19366), .S(net21541), .Y(n837) );
  MUX2X1 U560 ( .B(net19708), .A(net19365), .S(net21539), .Y(n836) );
  MUX2X1 U561 ( .B(net19708), .A(net19363), .S(net62692), .Y(n842) );
  INVX2 U562 ( .A(w_sel[1]), .Y(net25264) );
  NAND2X1 U563 ( .A(w_sel[1]), .B(w_sel[2]), .Y(net25272) );
  AOI22X1 U564 ( .A(net21478), .B(outreg_data[12]), .C(net21477), .D(
        \regs[4][12] ), .Y(net19584) );
  NAND2X1 U565 ( .A(n321), .B(n282), .Y(net19913) );
  OAI22X1 U566 ( .A(net19338), .B(n322), .C(net19340), .D(net19454), .Y(
        net19452) );
  INVX2 U567 ( .A(outreg_data[12]), .Y(n322) );
  MUX2X1 U568 ( .B(n322), .A(n323), .S(net44509), .Y(net5003) );
  NOR2X1 U569 ( .A(w_sel[2]), .B(w_sel[1]), .Y(n321) );
  INVX8 U570 ( .A(w_data[12]), .Y(n323) );
  BUFX2 U571 ( .A(n323), .Y(net19596) );
  NAND2X1 U572 ( .A(n292), .B(net19580), .Y(r1_data[12]) );
  AOI22X1 U573 ( .A(net19516), .B(\regs[2][12] ), .C(net19517), .D(
        \regs[7][12] ), .Y(n324) );
  AOI21X1 U574 ( .A(net19497), .B(\regs[3][12] ), .C(n325), .Y(net19579) );
  NAND3X1 U575 ( .A(net19587), .B(net19588), .C(n326), .Y(n325) );
  NOR2X1 U576 ( .A(net19590), .B(n327), .Y(n326) );
  OAI22X1 U577 ( .A(net20244), .B(net19592), .C(net20238), .D(n328), .Y(n327)
         );
  INVX2 U578 ( .A(\regs[14][12] ), .Y(n328) );
  MUX2X1 U579 ( .B(n328), .A(net19596), .S(net21437), .Y(net5005) );
  INVX2 U580 ( .A(net19506), .Y(net20237) );
  NAND3X1 U581 ( .A(net62657), .B(net21690), .C(net21515), .Y(net19506) );
  INVX2 U582 ( .A(net21562), .Y(net21690) );
  NAND3X1 U583 ( .A(net21690), .B(net21764), .C(net62657), .Y(net19504) );
  AND2X2 U584 ( .A(n984), .B(net21690), .Y(net21417) );
  BUFX2 U585 ( .A(net21682), .Y(net21562) );
  BUFX2 U586 ( .A(net62002), .Y(net21682) );
  NAND2X1 U587 ( .A(\regs[5][0] ), .B(net21682), .Y(net19854) );
  NAND3X1 U588 ( .A(net62657), .B(net21764), .C(net21562), .Y(net19508) );
  INVX2 U589 ( .A(\regs[2][12] ), .Y(net19455) );
  AOI22X1 U590 ( .A(\regs[6][12] ), .B(net21403), .C(\regs[7][12] ), .D(
        net21405), .Y(net19448) );
  INVX2 U591 ( .A(\regs[7][12] ), .Y(net19597) );
  AOI22X1 U592 ( .A(net21478), .B(outreg_data[11]), .C(net21477), .D(
        \regs[4][11] ), .Y(net19605) );
  OAI22X1 U593 ( .A(net19338), .B(n329), .C(net19340), .D(net19463), .Y(
        net19461) );
  INVX2 U594 ( .A(outreg_data[11]), .Y(n329) );
  MUX2X1 U595 ( .B(n329), .A(n330), .S(net44509), .Y(net5048) );
  INVX8 U596 ( .A(w_data[11]), .Y(n330) );
  BUFX2 U597 ( .A(n330), .Y(net19617) );
  NAND2X1 U598 ( .A(n293), .B(net19601), .Y(r1_data[11]) );
  AOI22X1 U599 ( .A(net62001), .B(\regs[2][11] ), .C(net19517), .D(
        \regs[7][11] ), .Y(n331) );
  AOI21X1 U600 ( .A(net21748), .B(\regs[3][11] ), .C(n332), .Y(net19600) );
  NAND3X1 U601 ( .A(net19608), .B(net19609), .C(n333), .Y(n332) );
  NOR2X1 U602 ( .A(net19611), .B(n334), .Y(n333) );
  OAI22X1 U603 ( .A(net20244), .B(net19613), .C(net19506), .D(n335), .Y(n334)
         );
  INVX2 U604 ( .A(\regs[14][11] ), .Y(n335) );
  MUX2X1 U605 ( .B(n335), .A(net19617), .S(net21437), .Y(net5050) );
  INVX2 U606 ( .A(\regs[2][11] ), .Y(net19464) );
  INVX2 U607 ( .A(\regs[7][11] ), .Y(net19618) );
  AOI22X1 U608 ( .A(\regs[6][11] ), .B(net21403), .C(\regs[7][11] ), .D(
        net21405), .Y(net19457) );
  AOI22X1 U609 ( .A(net21478), .B(outreg_data[9]), .C(net21477), .D(
        \regs[4][9] ), .Y(net19647) );
  OAI22X1 U610 ( .A(net19338), .B(n336), .C(net19339), .D(net19340), .Y(
        net19336) );
  INVX2 U611 ( .A(outreg_data[9]), .Y(n336) );
  MUX2X1 U612 ( .B(n336), .A(n337), .S(net44509), .Y(net5066) );
  MUX2X1 U613 ( .B(net19471), .A(net19638), .S(net42609), .Y(net5057) );
  INVX8 U614 ( .A(w_data[9]), .Y(n337) );
  BUFX2 U615 ( .A(n337), .Y(net19659) );
  BUFX2 U616 ( .A(net19638), .Y(n338) );
  NAND2X1 U617 ( .A(n294), .B(net19643), .Y(r1_data[9]) );
  AOI22X1 U618 ( .A(net62001), .B(\regs[2][9] ), .C(net19517), .D(\regs[7][9] ), .Y(n339) );
  AOI21X1 U619 ( .A(net21748), .B(\regs[3][9] ), .C(n340), .Y(net19642) );
  NAND3X1 U626 ( .A(net19650), .B(net19651), .C(n341), .Y(n340) );
  NOR2X1 U627 ( .A(net19653), .B(n342), .Y(n341) );
  OAI22X1 U628 ( .A(net20244), .B(net19655), .C(net19506), .D(n343), .Y(n342)
         );
  INVX2 U629 ( .A(\regs[14][9] ), .Y(n343) );
  MUX2X1 U630 ( .B(n343), .A(net19659), .S(net21437), .Y(net5068) );
  INVX2 U631 ( .A(\regs[2][9] ), .Y(net19341) );
  INVX2 U638 ( .A(\regs[7][9] ), .Y(net19660) );
  AOI22X1 U639 ( .A(\regs[6][9] ), .B(net21403), .C(\regs[7][9] ), .D(net21405), .Y(net19332) );
  INVX8 U640 ( .A(w_data[3]), .Y(n345) );
  INVX8 U641 ( .A(w_data[15]), .Y(n346) );
  INVX8 U642 ( .A(w_data[14]), .Y(n347) );
  AND2X2 U643 ( .A(net19774), .B(n454), .Y(n366) );
  AOI22X1 U650 ( .A(net21478), .B(outreg_data[2]), .C(n273), .D(\regs[4][2] ), 
        .Y(net19801) );
  OAI22X1 U651 ( .A(net19338), .B(n348), .C(net19340), .D(net19409), .Y(
        net19407) );
  INVX2 U652 ( .A(outreg_data[2]), .Y(n348) );
  INVX8 U653 ( .A(w_data[2]), .Y(net19813) );
  BUFX2 U654 ( .A(net19813), .Y(n349) );
  NAND2X1 U655 ( .A(n295), .B(net19797), .Y(r1_data[2]) );
  NOR2X1 U662 ( .A(net19798), .B(n351), .Y(net19797) );
  OAI21X1 U663 ( .A(n352), .B(net46042), .C(net19801), .Y(n351) );
  AOI22X1 U664 ( .A(n273), .B(\regs[4][4] ), .C(net21478), .D(outreg_data[4]), 
        .Y(net19759) );
  AOI22X1 U665 ( .A(n273), .B(\regs[4][5] ), .C(outreg_data[5]), .D(net19696), 
        .Y(net19738) );
  INVX2 U666 ( .A(\regs[5][2] ), .Y(n352) );
  MUX2X1 U667 ( .B(net19813), .A(n352), .S(net21545), .Y(n1158) );
  OAI22X1 U674 ( .A(net21932), .B(n353), .C(net62787), .D(net19409), .Y(
        net19798) );
  INVX2 U675 ( .A(\regs[1][2] ), .Y(net19409) );
  MUX2X1 U676 ( .B(net19813), .A(net19409), .S(net21537), .Y(net5128) );
  INVX2 U677 ( .A(\regs[6][2] ), .Y(n353) );
  MUX2X1 U678 ( .B(net19813), .A(n353), .S(net21547), .Y(n1174) );
  AOI22X1 U679 ( .A(net62001), .B(\regs[2][2] ), .C(net19517), .D(\regs[7][2] ), .Y(n350) );
  AOI22X1 U686 ( .A(\regs[4][2] ), .B(net21404), .C(\regs[5][2] ), .D(net21406), .Y(net19404) );
  INVX2 U687 ( .A(\regs[4][2] ), .Y(net19815) );
  AND2X2 U688 ( .A(net21415), .B(net21880), .Y(net21442) );
  INVX1 U689 ( .A(r1_sel[0]), .Y(net21880) );
  OR2X2 U690 ( .A(net19826), .B(r1_sel[1]), .Y(net21638) );
  INVX4 U691 ( .A(net21638), .Y(net20419) );
  BUFX2 U698 ( .A(net19826), .Y(net21646) );
  AOI22X1 U699 ( .A(net19696), .B(outreg_data[13]), .C(net21634), .D(
        \regs[4][13] ), .Y(net19563) );
  OAI22X1 U700 ( .A(net19338), .B(n354), .C(net19340), .D(net19445), .Y(
        net19443) );
  INVX2 U701 ( .A(outreg_data[13]), .Y(n354) );
  MUX2X1 U702 ( .B(n354), .A(n357), .S(net44509), .Y(net5030) );
  OR2X2 U703 ( .A(net33085), .B(n288), .Y(n355) );
  INVX2 U710 ( .A(n355), .Y(net21435) );
  OR2X2 U711 ( .A(net33085), .B(n289), .Y(n356) );
  INVX2 U712 ( .A(n356), .Y(net21434) );
  INVX8 U713 ( .A(w_data[13]), .Y(n357) );
  BUFX2 U714 ( .A(n357), .Y(net19575) );
  BUFX2 U715 ( .A(w_sel[2]), .Y(net32977) );
  INVX1 U722 ( .A(net25264), .Y(net33085) );
  NAND2X1 U723 ( .A(n296), .B(net19559), .Y(r1_data[13]) );
  AOI22X1 U724 ( .A(net62001), .B(\regs[2][13] ), .C(net19517), .D(
        \regs[7][13] ), .Y(n358) );
  AOI21X1 U725 ( .A(net62736), .B(\regs[3][13] ), .C(n359), .Y(net19558) );
  NAND3X1 U726 ( .A(net19566), .B(net19567), .C(n360), .Y(n359) );
  NOR2X1 U727 ( .A(net19569), .B(n361), .Y(n360) );
  OAI22X1 U734 ( .A(net20244), .B(net19571), .C(net19506), .D(n362), .Y(n361)
         );
  INVX2 U735 ( .A(\regs[14][13] ), .Y(n362) );
  MUX2X1 U736 ( .B(n362), .A(net19575), .S(net21437), .Y(net5032) );
  INVX2 U737 ( .A(\regs[2][13] ), .Y(net19446) );
  INVX2 U738 ( .A(\regs[7][13] ), .Y(net19576) );
  AOI22X1 U739 ( .A(\regs[6][13] ), .B(net21403), .C(\regs[7][13] ), .D(
        net21405), .Y(net19439) );
  AOI22X1 U746 ( .A(net21634), .B(\regs[4][8] ), .C(net19696), .D(
        outreg_data[8]), .Y(net19668) );
  MUX2X1 U747 ( .B(net36206), .A(net19716), .S(net21545), .Y(n1162) );
  MUX2X1 U748 ( .B(net36206), .A(net19373), .S(net21537), .Y(net5092) );
  OAI22X1 U749 ( .A(net19338), .B(net19372), .C(net19340), .D(net19373), .Y(
        net19371) );
  MUX2X1 U750 ( .B(net36206), .A(net19718), .S(net21547), .Y(n1178) );
  AOI22X1 U751 ( .A(net19516), .B(\regs[2][3] ), .C(net19517), .D(\regs[7][3] ), .Y(net19774) );
  AOI22X1 U758 ( .A(net62001), .B(\regs[2][4] ), .C(net21751), .D(\regs[7][4] ), .Y(net19753) );
  INVX2 U759 ( .A(\regs[2][6] ), .Y(net19374) );
  INVX2 U760 ( .A(\regs[7][6] ), .Y(net19730) );
  AOI22X1 U761 ( .A(\regs[6][6] ), .B(net21403), .C(\regs[7][6] ), .D(net21405), .Y(net19367) );
  NAND2X1 U762 ( .A(n363), .B(n282), .Y(net19903) );
  OAI22X1 U763 ( .A(net19342), .B(net25209), .C(net19344), .D(net19483), .Y(
        net19478) );
  INVX2 U770 ( .A(w_sel[2]), .Y(net25262) );
  NOR2X1 U771 ( .A(net32977), .B(net25264), .Y(n364) );
  NOR2X1 U772 ( .A(net25264), .B(w_sel[2]), .Y(n363) );
  INVX2 U773 ( .A(net25272), .Y(net21441) );
  INVX2 U774 ( .A(net25269), .Y(n1035) );
  INVX2 U775 ( .A(net25267), .Y(net21377) );
  OR2X2 U782 ( .A(net25269), .B(n298), .Y(n365) );
  INVX2 U783 ( .A(n365), .Y(net21438) );
  BUFX2 U784 ( .A(net36208), .Y(net25032) );
  BUFX4 U785 ( .A(net25223), .Y(net21539) );
  INVX8 U786 ( .A(net19532), .Y(net21537) );
  INVX4 U787 ( .A(net19913), .Y(net19532) );
  MUX2X1 U794 ( .B(net36208), .A(net19860), .S(net21547), .Y(n1172) );
  AOI22X1 U795 ( .A(\regs[4][0] ), .B(net21404), .C(\regs[5][0] ), .D(net21406), .Y(net19476) );
  INVX4 U796 ( .A(net20389), .Y(net21932) );
  MUX2X1 U797 ( .B(net36208), .A(net19905), .S(net21549), .Y(n1188) );
  MUX2X1 U798 ( .B(net36208), .A(net19911), .S(net21545), .Y(n1156) );
  MUX2X1 U799 ( .B(net36208), .A(net19483), .S(net21541), .Y(n817) );
  MUX2X1 U800 ( .B(net19813), .A(net19814), .S(net21549), .Y(n1190) );
  INVX4 U801 ( .A(net19916), .Y(net19531) );
  MUX2X1 U803 ( .B(net19813), .A(net19815), .S(net21543), .Y(n1142) );
  INVX4 U804 ( .A(net19918), .Y(net19535) );
  MUX2X1 U809 ( .B(net19813), .A(n720), .S(net21541), .Y(n804) );
  INVX4 U810 ( .A(net19903), .Y(net19527) );
  MUX2X1 U812 ( .B(net19813), .A(net19410), .S(net21539), .Y(n803) );
  MUX2X1 U813 ( .B(n300), .A(n471), .S(net21549), .Y(n1193) );
  MUX2X1 U820 ( .B(n300), .A(n482), .S(net21547), .Y(n1177) );
  MUX2X1 U821 ( .B(n300), .A(n483), .S(net21545), .Y(n1161) );
  MUX2X1 U822 ( .B(n300), .A(net19752), .S(net21543), .Y(n1145) );
  MUX2X1 U823 ( .B(n300), .A(n772), .S(net21541), .Y(n823) );
  MUX2X1 U824 ( .B(n300), .A(n773), .S(net21539), .Y(n822) );
  MUX2X1 U825 ( .B(n300), .A(n774), .S(net21537), .Y(n829) );
  MUX2X1 U826 ( .B(n300), .A(net19381), .S(net62692), .Y(n828) );
  INVX2 U827 ( .A(net21515), .Y(net21764) );
  AND2X1 U828 ( .A(n510), .B(net19662), .Y(n367) );
  MUX2X1 U829 ( .B(net36206), .A(net19730), .S(net21549), .Y(n1194) );
  INVX8 U830 ( .A(n264), .Y(net21549) );
  INVX8 U831 ( .A(net19531), .Y(net21547) );
  INVX8 U832 ( .A(n265), .Y(net21545) );
  MUX2X1 U833 ( .B(net36206), .A(net19731), .S(net21543), .Y(n1146) );
  INVX8 U834 ( .A(net19535), .Y(net21543) );
  MUX2X1 U835 ( .B(net36206), .A(net19375), .S(net21541), .Y(n831) );
  INVX8 U836 ( .A(net19527), .Y(net21541) );
  MUX2X1 U837 ( .B(net36206), .A(net19374), .S(net21539), .Y(n830) );
  NAND2X1 U838 ( .A(n366), .B(n453), .Y(r1_data[3]) );
  NAND2X1 U839 ( .A(n367), .B(n509), .Y(r1_data[8]) );
  AND2X2 U840 ( .A(net25346), .B(net20399), .Y(net21634) );
  AND2X2 U841 ( .A(r1_sel[0]), .B(net21415), .Y(net21443) );
  NAND2X1 U842 ( .A(n624), .B(n623), .Y(n368) );
  NAND2X1 U843 ( .A(n369), .B(n622), .Y(r1_data[15]) );
  NAND2X1 U844 ( .A(n291), .B(n579), .Y(r1_data[14]) );
  NAND2X1 U845 ( .A(n297), .B(n533), .Y(r1_data[10]) );
  MUX2X1 U846 ( .B(n258), .A(net19841), .S(net21549), .Y(n1189) );
  MUX2X1 U847 ( .B(n258), .A(net19842), .S(net21543), .Y(n1141) );
  MUX2X1 U848 ( .B(n258), .A(net19420), .S(net21541), .Y(n797) );
  MUX2X1 U849 ( .B(n258), .A(net19419), .S(net21539), .Y(n796) );
  MUX2X1 U850 ( .B(n258), .A(net19417), .S(net62692), .Y(n802) );
  AND2X2 U851 ( .A(net20399), .B(net25346), .Y(net21477) );
  AND2X2 U852 ( .A(net21443), .B(net25346), .Y(net21476) );
  INVX2 U853 ( .A(net20247), .Y(net20249) );
  INVX2 U854 ( .A(n373), .Y(n382) );
  INVX2 U855 ( .A(n375), .Y(n380) );
  INVX2 U856 ( .A(n374), .Y(n381) );
  INVX2 U857 ( .A(n376), .Y(n379) );
  AND2X2 U858 ( .A(n1035), .B(n263), .Y(n370) );
  AND2X2 U859 ( .A(net21441), .B(net21377), .Y(net21437) );
  AND2X2 U860 ( .A(net21441), .B(n1035), .Y(n371) );
  AND2X2 U861 ( .A(net21377), .B(n263), .Y(n372) );
  INVX2 U862 ( .A(net19510), .Y(net20247) );
  INVX2 U863 ( .A(net19508), .Y(net20253) );
  INVX2 U864 ( .A(net19504), .Y(net20243) );
  AND2X2 U865 ( .A(n768), .B(n758), .Y(n373) );
  AND2X2 U866 ( .A(n768), .B(n759), .Y(n374) );
  AND2X2 U867 ( .A(n768), .B(n760), .Y(n375) );
  AND2X2 U868 ( .A(n768), .B(n761), .Y(n376) );
  AND2X2 U869 ( .A(n757), .B(n758), .Y(net21406) );
  AND2X2 U870 ( .A(n757), .B(n760), .Y(net21405) );
  AND2X2 U871 ( .A(n757), .B(n759), .Y(net21404) );
  AND2X2 U872 ( .A(n757), .B(n761), .Y(net21403) );
  BUFX2 U873 ( .A(n383), .Y(n391) );
  BUFX2 U874 ( .A(n383), .Y(n392) );
  BUFX2 U875 ( .A(n383), .Y(n393) );
  BUFX2 U876 ( .A(n384), .Y(n394) );
  BUFX2 U877 ( .A(n384), .Y(n395) );
  BUFX2 U878 ( .A(n384), .Y(n396) );
  BUFX2 U879 ( .A(n385), .Y(n397) );
  BUFX2 U880 ( .A(n385), .Y(n398) );
  BUFX2 U881 ( .A(n385), .Y(n399) );
  BUFX2 U882 ( .A(n386), .Y(n400) );
  BUFX2 U883 ( .A(n386), .Y(n401) );
  BUFX2 U884 ( .A(n386), .Y(n402) );
  BUFX2 U885 ( .A(n387), .Y(n403) );
  BUFX2 U886 ( .A(n387), .Y(n404) );
  BUFX2 U887 ( .A(n387), .Y(n405) );
  BUFX2 U888 ( .A(n388), .Y(n406) );
  BUFX2 U889 ( .A(n388), .Y(n407) );
  BUFX2 U890 ( .A(n388), .Y(n408) );
  BUFX2 U891 ( .A(n389), .Y(n409) );
  BUFX2 U892 ( .A(n389), .Y(n410) );
  BUFX2 U893 ( .A(n389), .Y(n411) );
  INVX2 U894 ( .A(n567), .Y(net19340) );
  INVX2 U895 ( .A(n565), .Y(net19344) );
  INVX2 U896 ( .A(n568), .Y(net19338) );
  INVX2 U897 ( .A(n566), .Y(net19342) );
  BUFX2 U898 ( .A(n390), .Y(n412) );
  BUFX2 U899 ( .A(n_reset), .Y(n390) );
  BUFX2 U900 ( .A(n_reset), .Y(n383) );
  BUFX2 U901 ( .A(n_reset), .Y(n384) );
  BUFX2 U902 ( .A(n_reset), .Y(n385) );
  BUFX2 U903 ( .A(n_reset), .Y(n386) );
  BUFX2 U904 ( .A(n_reset), .Y(n387) );
  BUFX2 U905 ( .A(n_reset), .Y(n388) );
  BUFX2 U906 ( .A(n_reset), .Y(n389) );
  NAND2X1 U907 ( .A(net20451), .B(net19759), .Y(n467) );
  NAND2X1 U908 ( .A(n344), .B(n486), .Y(r1_data[5]) );
  NAND2X1 U909 ( .A(net19753), .B(n470), .Y(n377) );
  NAND2X1 U910 ( .A(n378), .B(n469), .Y(r1_data[4]) );
  INVX8 U911 ( .A(w_data[4]), .Y(n455) );
  INVX8 U912 ( .A(w_data[7]), .Y(net19708) );
  INVX8 U913 ( .A(w_data[10]), .Y(net19638) );
  INVX2 U914 ( .A(outreg_data[1]), .Y(net19417) );
  INVX2 U915 ( .A(outreg_data[3]), .Y(net19399) );
  INVX2 U916 ( .A(outreg_data[4]), .Y(net19390) );
  INVX2 U917 ( .A(outreg_data[5]), .Y(net19381) );
  INVX2 U918 ( .A(outreg_data[7]), .Y(net19363) );
  INVX2 U919 ( .A(outreg_data[8]), .Y(net19354) );
  INVX2 U920 ( .A(outreg_data[10]), .Y(net19471) );
  INVX2 U921 ( .A(outreg_data[14]), .Y(n681) );
  INVX2 U922 ( .A(outreg_data[15]), .Y(n704) );
  INVX2 U923 ( .A(\regs[5][0] ), .Y(net19911) );
  INVX2 U924 ( .A(\regs[3][0] ), .Y(net19483) );
  INVX2 U925 ( .A(\regs[9][0] ), .Y(n950) );
  MUX2X1 U926 ( .B(n950), .A(net25032), .S(net21434), .Y(n1220) );
  INVX2 U927 ( .A(\regs[8][0] ), .Y(n965) );
  MUX2X1 U928 ( .B(n965), .A(net25032), .S(net21435), .Y(n1204) );
  INVX2 U929 ( .A(\regs[11][0] ), .Y(n920) );
  MUX2X1 U930 ( .B(n920), .A(net25032), .S(net21438), .Y(n1252) );
  INVX2 U931 ( .A(\regs[10][0] ), .Y(n935) );
  MUX2X1 U932 ( .B(n935), .A(net25032), .S(n283), .Y(n1236) );
  INVX2 U933 ( .A(\regs[14][0] ), .Y(n415) );
  MUX2X1 U934 ( .B(n415), .A(net25032), .S(net21437), .Y(n820) );
  INVX2 U935 ( .A(\regs[15][0] ), .Y(n416) );
  MUX2X1 U936 ( .B(n416), .A(net25032), .S(n371), .Y(n821) );
  INVX2 U937 ( .A(\regs[12][0] ), .Y(n413) );
  MUX2X1 U938 ( .B(n413), .A(net25032), .S(n372), .Y(n818) );
  INVX2 U939 ( .A(\regs[13][0] ), .Y(n414) );
  MUX2X1 U940 ( .B(n414), .A(net25032), .S(n370), .Y(n819) );
  NAND3X1 U941 ( .A(n984), .B(net21764), .C(net21562), .Y(net19879) );
  NAND3X1 U942 ( .A(n984), .B(net21562), .C(net21515), .Y(net19878) );
  AOI22X1 U943 ( .A(net19514), .B(\regs[9][0] ), .C(net19515), .D(\regs[8][0] ), .Y(n421) );
  AOI22X1 U944 ( .A(net21469), .B(\regs[11][0] ), .C(net21470), .D(
        \regs[10][0] ), .Y(n420) );
  OAI22X1 U945 ( .A(net20254), .B(n414), .C(net20249), .D(n413), .Y(n418) );
  OAI22X1 U946 ( .A(net20244), .B(n416), .C(net20238), .D(n415), .Y(n417) );
  NOR2X1 U947 ( .A(n418), .B(n417), .Y(n419) );
  NAND3X1 U948 ( .A(n421), .B(n420), .C(n419), .Y(n422) );
  AOI21X1 U949 ( .A(net21748), .B(\regs[3][0] ), .C(n422), .Y(net19844) );
  INVX2 U950 ( .A(\regs[4][1] ), .Y(net19842) );
  INVX2 U951 ( .A(\regs[3][1] ), .Y(net19420) );
  INVX2 U952 ( .A(\regs[9][1] ), .Y(n949) );
  MUX2X1 U953 ( .B(n949), .A(n277), .S(net21434), .Y(n1221) );
  INVX2 U954 ( .A(\regs[8][1] ), .Y(n964) );
  MUX2X1 U955 ( .B(n964), .A(n277), .S(net21435), .Y(n1205) );
  INVX2 U956 ( .A(\regs[11][1] ), .Y(n919) );
  MUX2X1 U957 ( .B(n919), .A(n277), .S(net21438), .Y(n1253) );
  INVX2 U958 ( .A(\regs[10][1] ), .Y(n934) );
  MUX2X1 U959 ( .B(n934), .A(n277), .S(n283), .Y(n1237) );
  INVX2 U960 ( .A(\regs[14][1] ), .Y(n425) );
  MUX2X1 U961 ( .B(n425), .A(n277), .S(net21437), .Y(n800) );
  INVX2 U962 ( .A(\regs[15][1] ), .Y(n426) );
  MUX2X1 U963 ( .B(n426), .A(n277), .S(n371), .Y(n801) );
  INVX2 U964 ( .A(\regs[12][1] ), .Y(n423) );
  MUX2X1 U965 ( .B(n423), .A(n277), .S(n372), .Y(n798) );
  INVX2 U966 ( .A(\regs[13][1] ), .Y(n424) );
  MUX2X1 U967 ( .B(n424), .A(n277), .S(n370), .Y(n799) );
  AOI22X1 U968 ( .A(net19514), .B(\regs[9][1] ), .C(net19515), .D(\regs[8][1] ), .Y(net19831) );
  AOI22X1 U969 ( .A(net21469), .B(\regs[11][1] ), .C(net21470), .D(
        \regs[10][1] ), .Y(net19832) );
  OAI22X1 U970 ( .A(net20254), .B(n424), .C(net20249), .D(n423), .Y(n428) );
  OAI22X1 U971 ( .A(net20244), .B(n426), .C(net20238), .D(n425), .Y(n427) );
  NOR2X1 U972 ( .A(n428), .B(n427), .Y(net19833) );
  INVX2 U973 ( .A(\regs[2][2] ), .Y(net19410) );
  INVX2 U974 ( .A(\regs[7][2] ), .Y(net19814) );
  INVX2 U975 ( .A(\regs[3][2] ), .Y(n720) );
  INVX2 U976 ( .A(\regs[9][2] ), .Y(n948) );
  MUX2X1 U977 ( .B(n948), .A(n349), .S(net21434), .Y(n1222) );
  INVX2 U978 ( .A(\regs[8][2] ), .Y(n963) );
  MUX2X1 U979 ( .B(n963), .A(n349), .S(net21435), .Y(n1206) );
  INVX2 U980 ( .A(\regs[11][2] ), .Y(n918) );
  MUX2X1 U981 ( .B(n918), .A(n349), .S(net21438), .Y(n1254) );
  INVX2 U982 ( .A(\regs[10][2] ), .Y(n933) );
  MUX2X1 U983 ( .B(n933), .A(n349), .S(n283), .Y(n1238) );
  INVX2 U984 ( .A(\regs[14][2] ), .Y(n431) );
  MUX2X1 U985 ( .B(n431), .A(n349), .S(net21437), .Y(n807) );
  INVX2 U986 ( .A(\regs[15][2] ), .Y(n432) );
  MUX2X1 U987 ( .B(n432), .A(n349), .S(n371), .Y(n808) );
  INVX2 U988 ( .A(\regs[12][2] ), .Y(n429) );
  MUX2X1 U989 ( .B(n429), .A(n349), .S(n372), .Y(n805) );
  INVX2 U990 ( .A(\regs[13][2] ), .Y(n430) );
  MUX2X1 U991 ( .B(n430), .A(n349), .S(n370), .Y(n806) );
  AOI22X1 U992 ( .A(net19514), .B(\regs[9][2] ), .C(net19515), .D(\regs[8][2] ), .Y(n437) );
  AOI22X1 U993 ( .A(net21469), .B(\regs[11][2] ), .C(net21470), .D(
        \regs[10][2] ), .Y(n436) );
  OAI22X1 U994 ( .A(net20254), .B(n430), .C(net19510), .D(n429), .Y(n434) );
  OAI22X1 U995 ( .A(net20244), .B(n432), .C(net20238), .D(n431), .Y(n433) );
  NOR2X1 U996 ( .A(n434), .B(n433), .Y(n435) );
  NAND3X1 U997 ( .A(n437), .B(n436), .C(n435), .Y(n438) );
  AOI21X1 U998 ( .A(net62736), .B(\regs[3][2] ), .C(n438), .Y(net19796) );
  INVX2 U999 ( .A(\regs[4][3] ), .Y(net19794) );
  INVX2 U1000 ( .A(\regs[5][3] ), .Y(n450) );
  INVX2 U1001 ( .A(\regs[1][3] ), .Y(n732) );
  INVX2 U1002 ( .A(\regs[6][3] ), .Y(n449) );
  INVX2 U1003 ( .A(\regs[2][3] ), .Y(net19401) );
  INVX2 U1004 ( .A(\regs[7][3] ), .Y(net19793) );
  INVX2 U1005 ( .A(\regs[3][3] ), .Y(n731) );
  INVX2 U1006 ( .A(\regs[9][3] ), .Y(n947) );
  MUX2X1 U1007 ( .B(n947), .A(n281), .S(net21434), .Y(n1223) );
  INVX2 U1008 ( .A(\regs[8][3] ), .Y(n962) );
  MUX2X1 U1009 ( .B(n962), .A(n281), .S(net21435), .Y(n1207) );
  INVX2 U1010 ( .A(\regs[11][3] ), .Y(n917) );
  MUX2X1 U1011 ( .B(n917), .A(n281), .S(net21438), .Y(n1255) );
  INVX2 U1012 ( .A(\regs[10][3] ), .Y(n932) );
  MUX2X1 U1013 ( .B(n932), .A(n281), .S(n283), .Y(n1239) );
  INVX2 U1014 ( .A(\regs[14][3] ), .Y(n441) );
  MUX2X1 U1015 ( .B(n441), .A(n345), .S(net21437), .Y(n813) );
  INVX2 U1016 ( .A(\regs[15][3] ), .Y(n442) );
  MUX2X1 U1017 ( .B(n442), .A(n281), .S(n371), .Y(n814) );
  INVX2 U1018 ( .A(\regs[12][3] ), .Y(n439) );
  MUX2X1 U1019 ( .B(n439), .A(n345), .S(n372), .Y(n811) );
  INVX2 U1021 ( .A(\regs[13][3] ), .Y(n440) );
  MUX2X1 U1022 ( .B(n440), .A(n281), .S(n370), .Y(n812) );
  AOI22X1 U1023 ( .A(net19514), .B(\regs[9][3] ), .C(net19515), .D(
        \regs[8][3] ), .Y(n447) );
  AOI22X1 U1024 ( .A(net21469), .B(\regs[11][3] ), .C(net21470), .D(
        \regs[10][3] ), .Y(n446) );
  OAI22X1 U1025 ( .A(net19508), .B(n440), .C(net20249), .D(n439), .Y(n444) );
  OAI22X1 U1026 ( .A(net20244), .B(n442), .C(net19506), .D(n441), .Y(n443) );
  NOR2X1 U1027 ( .A(n444), .B(n443), .Y(n445) );
  NAND3X1 U1028 ( .A(n447), .B(n446), .C(n445), .Y(n448) );
  AOI21X1 U1029 ( .A(net19497), .B(\regs[3][3] ), .C(n448), .Y(n454) );
  OAI22X1 U1030 ( .A(net20234), .B(n449), .C(net20230), .D(n732), .Y(n452) );
  OAI21X1 U1031 ( .A(n450), .B(net46042), .C(net19780), .Y(n451) );
  NOR2X1 U1032 ( .A(n452), .B(n451), .Y(n453) );
  INVX2 U1033 ( .A(\regs[4][4] ), .Y(net19773) );
  INVX2 U1034 ( .A(\regs[5][4] ), .Y(net19758) );
  INVX2 U1035 ( .A(\regs[1][4] ), .Y(n753) );
  MUX2X1 U1036 ( .B(n753), .A(n455), .S(net19532), .Y(n850) );
  INVX2 U1037 ( .A(\regs[6][4] ), .Y(n466) );
  INVX2 U1038 ( .A(\regs[2][4] ), .Y(net19392) );
  INVX2 U1039 ( .A(\regs[7][4] ), .Y(net19772) );
  INVX2 U1040 ( .A(\regs[3][4] ), .Y(n752) );
  INVX2 U1041 ( .A(\regs[9][4] ), .Y(n946) );
  MUX2X1 U1042 ( .B(n946), .A(n455), .S(net21434), .Y(n1224) );
  INVX2 U1043 ( .A(\regs[8][4] ), .Y(n961) );
  MUX2X1 U1044 ( .B(n961), .A(n455), .S(net21435), .Y(n1208) );
  INVX2 U1045 ( .A(\regs[11][4] ), .Y(n916) );
  MUX2X1 U1046 ( .B(n916), .A(n455), .S(net21438), .Y(n1256) );
  INVX2 U1047 ( .A(\regs[10][4] ), .Y(n931) );
  MUX2X1 U1048 ( .B(n931), .A(n455), .S(n283), .Y(n1240) );
  INVX2 U1049 ( .A(\regs[14][4] ), .Y(n458) );
  MUX2X1 U1050 ( .B(n458), .A(n455), .S(net21437), .Y(n847) );
  INVX2 U1051 ( .A(\regs[15][4] ), .Y(n459) );
  MUX2X1 U1052 ( .B(n459), .A(n455), .S(n371), .Y(n848) );
  INVX2 U1053 ( .A(\regs[12][4] ), .Y(n456) );
  MUX2X1 U1054 ( .B(n456), .A(n455), .S(n372), .Y(n845) );
  INVX2 U1055 ( .A(\regs[13][4] ), .Y(n457) );
  MUX2X1 U1056 ( .B(n457), .A(n455), .S(n370), .Y(n846) );
  AOI22X1 U1057 ( .A(net19514), .B(\regs[9][4] ), .C(net19515), .D(
        \regs[8][4] ), .Y(n464) );
  AOI22X1 U1058 ( .A(net21469), .B(\regs[11][4] ), .C(net21470), .D(
        \regs[10][4] ), .Y(n463) );
  OAI22X1 U1059 ( .A(net20254), .B(n457), .C(net19510), .D(n456), .Y(n461) );
  OAI22X1 U1060 ( .A(net20244), .B(n459), .C(net20238), .D(n458), .Y(n460) );
  NOR2X1 U1061 ( .A(n461), .B(n460), .Y(n462) );
  NAND3X1 U1062 ( .A(n464), .B(n463), .C(n462), .Y(n465) );
  AOI21X1 U1063 ( .A(net19497), .B(\regs[3][4] ), .C(n465), .Y(n470) );
  OAI22X1 U1064 ( .A(net20234), .B(n466), .C(net62787), .D(n753), .Y(n468) );
  NOR2X1 U1065 ( .A(n467), .B(n468), .Y(n469) );
  INVX2 U1066 ( .A(\regs[4][5] ), .Y(net19752) );
  INVX2 U1067 ( .A(\regs[5][5] ), .Y(n483) );
  INVX2 U1068 ( .A(\regs[1][5] ), .Y(n774) );
  INVX2 U1069 ( .A(\regs[6][5] ), .Y(n482) );
  INVX2 U1070 ( .A(\regs[2][5] ), .Y(n773) );
  INVX2 U1071 ( .A(\regs[7][5] ), .Y(n471) );
  INVX2 U1072 ( .A(\regs[3][5] ), .Y(n772) );
  INVX2 U1073 ( .A(\regs[9][5] ), .Y(n945) );
  MUX2X1 U1074 ( .B(n945), .A(n262), .S(net21434), .Y(n1225) );
  INVX2 U1075 ( .A(\regs[8][5] ), .Y(n960) );
  MUX2X1 U1076 ( .B(n960), .A(n262), .S(net21435), .Y(n1209) );
  INVX2 U1077 ( .A(\regs[11][5] ), .Y(n915) );
  MUX2X1 U1078 ( .B(n915), .A(n262), .S(net21438), .Y(n1257) );
  INVX2 U1079 ( .A(\regs[10][5] ), .Y(n930) );
  MUX2X1 U1080 ( .B(n930), .A(n262), .S(n283), .Y(n1241) );
  INVX2 U1081 ( .A(\regs[14][5] ), .Y(n474) );
  MUX2X1 U1082 ( .B(n474), .A(n262), .S(net21437), .Y(n826) );
  INVX2 U1083 ( .A(\regs[15][5] ), .Y(n475) );
  MUX2X1 U1084 ( .B(n475), .A(n262), .S(n371), .Y(n827) );
  INVX2 U1085 ( .A(\regs[12][5] ), .Y(n472) );
  MUX2X1 U1086 ( .B(n472), .A(n262), .S(n372), .Y(n824) );
  INVX2 U1087 ( .A(\regs[13][5] ), .Y(n473) );
  MUX2X1 U1088 ( .B(n473), .A(n262), .S(n370), .Y(n825) );
  AOI22X1 U1089 ( .A(net19516), .B(\regs[2][5] ), .C(net19517), .D(
        \regs[7][5] ), .Y(n488) );
  AOI22X1 U1090 ( .A(net19514), .B(\regs[9][5] ), .C(net19515), .D(
        \regs[8][5] ), .Y(n480) );
  AOI22X1 U1091 ( .A(net21469), .B(\regs[11][5] ), .C(net21470), .D(
        \regs[10][5] ), .Y(n479) );
  OAI22X1 U1092 ( .A(net19508), .B(n473), .C(net20249), .D(n472), .Y(n477) );
  OAI22X1 U1093 ( .A(net20244), .B(n475), .C(net19506), .D(n474), .Y(n476) );
  NOR2X1 U1094 ( .A(n477), .B(n476), .Y(n478) );
  NAND3X1 U1095 ( .A(n480), .B(n479), .C(n478), .Y(n481) );
  AOI21X1 U1096 ( .A(net19497), .B(\regs[3][5] ), .C(n481), .Y(n487) );
  OAI22X1 U1097 ( .A(net20234), .B(n482), .C(net20230), .D(n774), .Y(n485) );
  OAI21X1 U1098 ( .A(n483), .B(net46042), .C(net19738), .Y(n484) );
  NOR2X1 U1099 ( .A(n485), .B(n484), .Y(n486) );
  INVX2 U1100 ( .A(\regs[4][6] ), .Y(net19731) );
  INVX2 U1101 ( .A(\regs[3][6] ), .Y(net19375) );
  INVX2 U1102 ( .A(\regs[9][6] ), .Y(net4960) );
  MUX2X1 U1103 ( .B(net4960), .A(net36206), .S(net21434), .Y(n1226) );
  INVX2 U1104 ( .A(\regs[8][6] ), .Y(net4944) );
  MUX2X1 U1105 ( .B(net4944), .A(net36206), .S(net21435), .Y(n1210) );
  INVX2 U1106 ( .A(\regs[11][6] ), .Y(net4992) );
  MUX2X1 U1107 ( .B(net4992), .A(net36206), .S(net21438), .Y(n1258) );
  INVX2 U1108 ( .A(\regs[10][6] ), .Y(net4976) );
  MUX2X1 U1109 ( .B(net4976), .A(net36206), .S(n283), .Y(n1242) );
  MUX2X1 U1110 ( .B(net19726), .A(net36206), .S(net21437), .Y(n834) );
  MUX2X1 U1111 ( .B(net19725), .A(net36206), .S(n371), .Y(n835) );
  MUX2X1 U1112 ( .B(net19728), .A(net36206), .S(n372), .Y(n832) );
  MUX2X1 U1113 ( .B(net19727), .A(net36206), .S(n370), .Y(n833) );
  INVX2 U1114 ( .A(\regs[4][7] ), .Y(net19710) );
  INVX2 U1115 ( .A(\regs[3][7] ), .Y(net19366) );
  INVX2 U1116 ( .A(\regs[9][7] ), .Y(n944) );
  MUX2X1 U1117 ( .B(n944), .A(net19708), .S(net21434), .Y(n1227) );
  INVX2 U1118 ( .A(\regs[8][7] ), .Y(n959) );
  MUX2X1 U1119 ( .B(n959), .A(net19708), .S(net21435), .Y(n1211) );
  INVX2 U1120 ( .A(\regs[11][7] ), .Y(n914) );
  MUX2X1 U1121 ( .B(n914), .A(net19708), .S(net21438), .Y(n1259) );
  INVX2 U1122 ( .A(\regs[10][7] ), .Y(n929) );
  MUX2X1 U1123 ( .B(n929), .A(net19708), .S(n283), .Y(n1243) );
  INVX2 U1124 ( .A(\regs[14][7] ), .Y(n491) );
  MUX2X1 U1125 ( .B(n491), .A(net19708), .S(net21437), .Y(n840) );
  INVX2 U1126 ( .A(\regs[15][7] ), .Y(n492) );
  MUX2X1 U1127 ( .B(n492), .A(net19708), .S(n371), .Y(n841) );
  INVX2 U1128 ( .A(\regs[12][7] ), .Y(n489) );
  MUX2X1 U1129 ( .B(n489), .A(net19708), .S(n372), .Y(n838) );
  INVX2 U1130 ( .A(\regs[13][7] ), .Y(n490) );
  MUX2X1 U1131 ( .B(n490), .A(net19708), .S(n370), .Y(n839) );
  AOI22X1 U1132 ( .A(net19514), .B(\regs[9][7] ), .C(net19515), .D(
        \regs[8][7] ), .Y(net19699) );
  AOI22X1 U1133 ( .A(net21469), .B(\regs[11][7] ), .C(net21470), .D(
        \regs[10][7] ), .Y(net19700) );
  OAI22X1 U1134 ( .A(net19508), .B(n490), .C(net20249), .D(n489), .Y(n494) );
  OAI22X1 U1135 ( .A(net20244), .B(n492), .C(net19506), .D(n491), .Y(n493) );
  NOR2X1 U1136 ( .A(n494), .B(n493), .Y(net19701) );
  INVX2 U1137 ( .A(\regs[4][8] ), .Y(net19687) );
  INVX2 U1138 ( .A(\regs[5][8] ), .Y(n506) );
  INVX2 U1139 ( .A(\regs[1][8] ), .Y(n787) );
  INVX2 U1140 ( .A(\regs[6][8] ), .Y(n505) );
  INVX2 U1141 ( .A(\regs[2][8] ), .Y(net19356) );
  INVX2 U1142 ( .A(\regs[7][8] ), .Y(net19686) );
  INVX2 U1143 ( .A(\regs[3][8] ), .Y(n786) );
  INVX2 U1144 ( .A(\regs[9][8] ), .Y(n943) );
  MUX2X1 U1145 ( .B(n943), .A(n274), .S(net21434), .Y(n1228) );
  INVX2 U1146 ( .A(\regs[8][8] ), .Y(n958) );
  MUX2X1 U1147 ( .B(n958), .A(n301), .S(net21435), .Y(n1212) );
  INVX2 U1148 ( .A(\regs[11][8] ), .Y(n913) );
  MUX2X1 U1149 ( .B(n913), .A(n301), .S(net21438), .Y(n1260) );
  INVX2 U1150 ( .A(\regs[10][8] ), .Y(n928) );
  MUX2X1 U1151 ( .B(n928), .A(n301), .S(n283), .Y(n1244) );
  INVX2 U1152 ( .A(\regs[14][8] ), .Y(n497) );
  MUX2X1 U1153 ( .B(n497), .A(n301), .S(net21437), .Y(n874) );
  INVX2 U1154 ( .A(\regs[15][8] ), .Y(n498) );
  MUX2X1 U1155 ( .B(n498), .A(n274), .S(n371), .Y(n875) );
  INVX2 U1156 ( .A(\regs[12][8] ), .Y(n495) );
  MUX2X1 U1157 ( .B(n495), .A(n301), .S(n372), .Y(n872) );
  INVX2 U1158 ( .A(\regs[13][8] ), .Y(n496) );
  MUX2X1 U1159 ( .B(n496), .A(n274), .S(n370), .Y(n873) );
  AOI22X1 U1160 ( .A(net19514), .B(\regs[9][8] ), .C(net19515), .D(
        \regs[8][8] ), .Y(n503) );
  AOI22X1 U1161 ( .A(net21469), .B(\regs[11][8] ), .C(net21470), .D(
        \regs[10][8] ), .Y(n502) );
  OAI22X1 U1162 ( .A(net20254), .B(n496), .C(net19510), .D(n495), .Y(n500) );
  OAI22X1 U1163 ( .A(net20244), .B(n498), .C(net20238), .D(n497), .Y(n499) );
  NOR2X1 U1164 ( .A(n500), .B(n499), .Y(n501) );
  NAND3X1 U1165 ( .A(n503), .B(n502), .C(n501), .Y(n504) );
  AOI21X1 U1166 ( .A(net19497), .B(\regs[3][8] ), .C(n504), .Y(n510) );
  OAI22X1 U1167 ( .A(net20234), .B(n505), .C(net62787), .D(n787), .Y(n508) );
  OAI21X1 U1168 ( .A(n506), .B(net20226), .C(net19668), .Y(n507) );
  NOR2X1 U1169 ( .A(n507), .B(n508), .Y(n509) );
  INVX2 U1170 ( .A(\regs[4][9] ), .Y(net19661) );
  INVX2 U1171 ( .A(\regs[5][9] ), .Y(n513) );
  INVX2 U1172 ( .A(\regs[1][9] ), .Y(net19339) );
  INVX2 U1173 ( .A(\regs[6][9] ), .Y(net19648) );
  INVX2 U1174 ( .A(\regs[3][9] ), .Y(net19343) );
  INVX2 U1175 ( .A(\regs[9][9] ), .Y(n942) );
  MUX2X1 U1176 ( .B(n942), .A(net19659), .S(net21434), .Y(n1229) );
  INVX2 U1177 ( .A(\regs[8][9] ), .Y(n957) );
  MUX2X1 U1178 ( .B(n957), .A(net19659), .S(net21435), .Y(n1213) );
  INVX2 U1179 ( .A(\regs[11][9] ), .Y(n912) );
  MUX2X1 U1180 ( .B(n912), .A(net19659), .S(net21438), .Y(n1261) );
  INVX2 U1181 ( .A(\regs[10][9] ), .Y(n927) );
  MUX2X1 U1182 ( .B(n927), .A(net19659), .S(n283), .Y(n1245) );
  INVX2 U1183 ( .A(\regs[15][9] ), .Y(net19655) );
  MUX2X1 U1184 ( .B(net19655), .A(n337), .S(n371), .Y(n855) );
  INVX2 U1185 ( .A(\regs[12][9] ), .Y(n511) );
  MUX2X1 U1186 ( .B(n511), .A(net19659), .S(n372), .Y(n853) );
  INVX2 U1187 ( .A(\regs[13][9] ), .Y(n512) );
  MUX2X1 U1188 ( .B(n512), .A(n337), .S(n370), .Y(n854) );
  AOI22X1 U1189 ( .A(net19514), .B(\regs[9][9] ), .C(net19515), .D(
        \regs[8][9] ), .Y(net19650) );
  AOI22X1 U1190 ( .A(net21469), .B(\regs[11][9] ), .C(net21470), .D(
        \regs[10][9] ), .Y(net19651) );
  OAI22X1 U1191 ( .A(net19508), .B(n512), .C(net20249), .D(n511), .Y(net19653)
         );
  OAI22X1 U1192 ( .A(net21932), .B(net19648), .C(net62787), .D(net19339), .Y(
        n515) );
  OAI21X1 U1193 ( .A(n513), .B(net46042), .C(net19647), .Y(n514) );
  NOR2X1 U1194 ( .A(n515), .B(n514), .Y(net19643) );
  INVX2 U1195 ( .A(\regs[4][10] ), .Y(n516) );
  INVX2 U1196 ( .A(\regs[5][10] ), .Y(n530) );
  INVX2 U1197 ( .A(\regs[1][10] ), .Y(n635) );
  INVX2 U1198 ( .A(\regs[6][10] ), .Y(n528) );
  INVX2 U1199 ( .A(\regs[2][10] ), .Y(n634) );
  INVX2 U1200 ( .A(\regs[7][10] ), .Y(n517) );
  INVX2 U1201 ( .A(\regs[3][10] ), .Y(n633) );
  INVX2 U1202 ( .A(\regs[9][10] ), .Y(n941) );
  MUX2X1 U1203 ( .B(n941), .A(n338), .S(net21434), .Y(n1230) );
  INVX2 U1204 ( .A(\regs[8][10] ), .Y(n956) );
  MUX2X1 U1205 ( .B(n956), .A(n338), .S(net21435), .Y(n1214) );
  INVX2 U1206 ( .A(\regs[11][10] ), .Y(n911) );
  MUX2X1 U1207 ( .B(n911), .A(n338), .S(net21438), .Y(n1262) );
  INVX2 U1208 ( .A(\regs[10][10] ), .Y(n926) );
  MUX2X1 U1209 ( .B(n926), .A(n338), .S(n283), .Y(n1246) );
  INVX2 U1210 ( .A(\regs[14][10] ), .Y(n520) );
  MUX2X1 U1211 ( .B(n520), .A(n338), .S(net21437), .Y(n861) );
  INVX2 U1212 ( .A(\regs[15][10] ), .Y(n521) );
  MUX2X1 U1213 ( .B(n521), .A(net19638), .S(n371), .Y(n862) );
  INVX2 U1214 ( .A(\regs[12][10] ), .Y(n518) );
  MUX2X1 U1215 ( .B(n518), .A(n338), .S(n372), .Y(n859) );
  INVX2 U1216 ( .A(\regs[13][10] ), .Y(n519) );
  MUX2X1 U1217 ( .B(n519), .A(net19638), .S(n370), .Y(n860) );
  AOI22X1 U1218 ( .A(net62001), .B(\regs[2][10] ), .C(net19517), .D(
        \regs[7][10] ), .Y(n535) );
  AOI22X1 U1219 ( .A(net19514), .B(\regs[9][10] ), .C(net19515), .D(
        \regs[8][10] ), .Y(n526) );
  AOI22X1 U1220 ( .A(net21469), .B(\regs[11][10] ), .C(net21470), .D(
        \regs[10][10] ), .Y(n525) );
  OAI22X1 U1221 ( .A(net20254), .B(n519), .C(net19510), .D(n518), .Y(n523) );
  OAI22X1 U1222 ( .A(net20244), .B(n521), .C(net20238), .D(n520), .Y(n522) );
  NOR2X1 U1223 ( .A(n523), .B(n522), .Y(n524) );
  NAND3X1 U1224 ( .A(n526), .B(n525), .C(n524), .Y(n527) );
  AOI21X1 U1225 ( .A(net62736), .B(\regs[3][10] ), .C(n527), .Y(n534) );
  OAI22X1 U1226 ( .A(net21932), .B(n528), .C(net62787), .D(n635), .Y(n532) );
  AOI22X1 U1227 ( .A(net21634), .B(\regs[4][10] ), .C(net19696), .D(
        outreg_data[10]), .Y(n529) );
  OAI21X1 U1228 ( .A(n530), .B(net46042), .C(n529), .Y(n531) );
  NOR2X1 U1229 ( .A(n532), .B(n531), .Y(n533) );
  INVX2 U1230 ( .A(\regs[4][11] ), .Y(net19619) );
  INVX2 U1231 ( .A(\regs[5][11] ), .Y(n538) );
  INVX2 U1232 ( .A(\regs[1][11] ), .Y(net19463) );
  INVX2 U1233 ( .A(\regs[6][11] ), .Y(net19606) );
  INVX2 U1234 ( .A(\regs[3][11] ), .Y(net19465) );
  MUX2X1 U1235 ( .B(net19465), .A(n330), .S(net19527), .Y(n865) );
  INVX2 U1236 ( .A(\regs[9][11] ), .Y(n940) );
  MUX2X1 U1237 ( .B(n940), .A(net19617), .S(net21434), .Y(n1231) );
  INVX2 U1238 ( .A(\regs[8][11] ), .Y(n955) );
  MUX2X1 U1239 ( .B(n955), .A(net19617), .S(net21435), .Y(n1215) );
  INVX2 U1240 ( .A(\regs[11][11] ), .Y(n910) );
  MUX2X1 U1241 ( .B(n910), .A(net19617), .S(net21438), .Y(n1263) );
  INVX2 U1242 ( .A(\regs[10][11] ), .Y(n925) );
  MUX2X1 U1243 ( .B(n925), .A(net19617), .S(n283), .Y(n1247) );
  INVX2 U1244 ( .A(\regs[15][11] ), .Y(net19613) );
  MUX2X1 U1245 ( .B(net19613), .A(n330), .S(n371), .Y(n868) );
  INVX2 U1246 ( .A(\regs[12][11] ), .Y(n536) );
  MUX2X1 U1247 ( .B(n536), .A(net19617), .S(n372), .Y(n866) );
  INVX2 U1248 ( .A(\regs[13][11] ), .Y(n537) );
  MUX2X1 U1249 ( .B(n537), .A(n330), .S(n370), .Y(n867) );
  AOI22X1 U1250 ( .A(net19514), .B(\regs[9][11] ), .C(net19515), .D(
        \regs[8][11] ), .Y(net19608) );
  AOI22X1 U1251 ( .A(net21469), .B(\regs[11][11] ), .C(net21470), .D(
        \regs[10][11] ), .Y(net19609) );
  OAI22X1 U1252 ( .A(net19508), .B(n537), .C(net20249), .D(n536), .Y(net19611)
         );
  OAI22X1 U1253 ( .A(net21932), .B(net19606), .C(net62787), .D(net19463), .Y(
        n540) );
  OAI21X1 U1254 ( .A(n538), .B(net46042), .C(net19605), .Y(n539) );
  NOR2X1 U1255 ( .A(n540), .B(n539), .Y(net19601) );
  INVX2 U1256 ( .A(\regs[4][12] ), .Y(net19598) );
  INVX2 U1257 ( .A(\regs[5][12] ), .Y(n543) );
  INVX2 U1258 ( .A(\regs[1][12] ), .Y(net19454) );
  INVX2 U1259 ( .A(\regs[6][12] ), .Y(net19585) );
  INVX2 U1260 ( .A(\regs[3][12] ), .Y(net19456) );
  INVX2 U1261 ( .A(\regs[9][12] ), .Y(n939) );
  MUX2X1 U1262 ( .B(n939), .A(net19596), .S(net21434), .Y(n1232) );
  INVX2 U1263 ( .A(\regs[8][12] ), .Y(n954) );
  MUX2X1 U1264 ( .B(n954), .A(net19596), .S(net21435), .Y(n1216) );
  INVX2 U1265 ( .A(\regs[11][12] ), .Y(n909) );
  MUX2X1 U1266 ( .B(n909), .A(net19596), .S(net21438), .Y(n1264) );
  INVX2 U1267 ( .A(\regs[10][12] ), .Y(n924) );
  MUX2X1 U1268 ( .B(n924), .A(net19596), .S(n283), .Y(n1248) );
  INVX2 U1269 ( .A(\regs[15][12] ), .Y(net19592) );
  MUX2X1 U1270 ( .B(net19592), .A(n323), .S(n371), .Y(n904) );
  INVX2 U1271 ( .A(\regs[12][12] ), .Y(n541) );
  MUX2X1 U1272 ( .B(n541), .A(net19596), .S(n372), .Y(n902) );
  INVX2 U1273 ( .A(\regs[13][12] ), .Y(n542) );
  MUX2X1 U1274 ( .B(n542), .A(n323), .S(n370), .Y(n903) );
  AOI22X1 U1275 ( .A(net19514), .B(\regs[9][12] ), .C(net19515), .D(
        \regs[8][12] ), .Y(net19587) );
  AOI22X1 U1276 ( .A(net21469), .B(\regs[11][12] ), .C(net21470), .D(
        \regs[10][12] ), .Y(net19588) );
  OAI22X1 U1277 ( .A(net20254), .B(n542), .C(net19510), .D(n541), .Y(net19590)
         );
  OAI22X1 U1278 ( .A(net21932), .B(net19585), .C(net62787), .D(net19454), .Y(
        n545) );
  OAI21X1 U1279 ( .A(n543), .B(net46042), .C(net19584), .Y(n544) );
  NOR2X1 U1280 ( .A(n545), .B(n544), .Y(net19580) );
  INVX2 U1281 ( .A(\regs[4][13] ), .Y(net19577) );
  INVX2 U1282 ( .A(\regs[5][13] ), .Y(n548) );
  INVX2 U1283 ( .A(\regs[1][13] ), .Y(net19445) );
  INVX2 U1284 ( .A(\regs[6][13] ), .Y(net19564) );
  INVX2 U1285 ( .A(\regs[3][13] ), .Y(net19447) );
  INVX2 U1286 ( .A(\regs[9][13] ), .Y(n938) );
  MUX2X1 U1287 ( .B(n938), .A(net19575), .S(net21434), .Y(n1233) );
  INVX2 U1288 ( .A(\regs[8][13] ), .Y(n953) );
  MUX2X1 U1289 ( .B(n953), .A(net19575), .S(net21435), .Y(n1217) );
  INVX2 U1290 ( .A(\regs[11][13] ), .Y(n908) );
  MUX2X1 U1291 ( .B(n908), .A(net19575), .S(net21438), .Y(n1265) );
  INVX2 U1292 ( .A(\regs[10][13] ), .Y(n923) );
  MUX2X1 U1293 ( .B(n923), .A(net19575), .S(n283), .Y(n1249) );
  INVX2 U1294 ( .A(\regs[15][13] ), .Y(net19571) );
  MUX2X1 U1295 ( .B(net19571), .A(net19575), .S(n371), .Y(n882) );
  INVX2 U1296 ( .A(\regs[12][13] ), .Y(n546) );
  MUX2X1 U1297 ( .B(n546), .A(net19575), .S(n372), .Y(n880) );
  INVX2 U1298 ( .A(\regs[13][13] ), .Y(n547) );
  MUX2X1 U1299 ( .B(n547), .A(net19575), .S(n370), .Y(n881) );
  AOI22X1 U1300 ( .A(net19514), .B(\regs[9][13] ), .C(net19515), .D(
        \regs[8][13] ), .Y(net19566) );
  AOI22X1 U1301 ( .A(net21469), .B(\regs[11][13] ), .C(net21470), .D(
        \regs[10][13] ), .Y(net19567) );
  OAI22X1 U1302 ( .A(net19508), .B(n547), .C(net20249), .D(n546), .Y(net19569)
         );
  OAI22X1 U1303 ( .A(net21932), .B(net19564), .C(net62787), .D(net19445), .Y(
        n550) );
  OAI21X1 U1304 ( .A(n548), .B(net46042), .C(net19563), .Y(n549) );
  NOR2X1 U1305 ( .A(n550), .B(n549), .Y(net19559) );
  INVX2 U1306 ( .A(\regs[4][14] ), .Y(n551) );
  INVX2 U1307 ( .A(\regs[5][14] ), .Y(n576) );
  INVX2 U1308 ( .A(\regs[1][14] ), .Y(n680) );
  INVX2 U1309 ( .A(\regs[6][14] ), .Y(n574) );
  INVX2 U1310 ( .A(\regs[2][14] ), .Y(n672) );
  INVX2 U1311 ( .A(\regs[7][14] ), .Y(n552) );
  INVX2 U1312 ( .A(\regs[3][14] ), .Y(n671) );
  INVX2 U1313 ( .A(\regs[9][14] ), .Y(n937) );
  MUX2X1 U1314 ( .B(n937), .A(n347), .S(net21434), .Y(n1234) );
  INVX2 U1315 ( .A(\regs[8][14] ), .Y(n952) );
  MUX2X1 U1316 ( .B(n952), .A(n347), .S(net21435), .Y(n1218) );
  INVX2 U1317 ( .A(\regs[11][14] ), .Y(n907) );
  MUX2X1 U1318 ( .B(n907), .A(n347), .S(net21438), .Y(n1266) );
  INVX2 U1319 ( .A(\regs[10][14] ), .Y(n922) );
  MUX2X1 U1320 ( .B(n922), .A(n347), .S(n283), .Y(n1250) );
  INVX2 U1321 ( .A(\regs[14][14] ), .Y(n557) );
  MUX2X1 U1322 ( .B(n557), .A(n347), .S(net21437), .Y(n888) );
  INVX2 U1323 ( .A(\regs[15][14] ), .Y(n558) );
  MUX2X1 U1324 ( .B(n558), .A(n279), .S(n371), .Y(n889) );
  INVX2 U1325 ( .A(\regs[12][14] ), .Y(n553) );
  MUX2X1 U1326 ( .B(n553), .A(n347), .S(n372), .Y(n886) );
  INVX2 U1327 ( .A(\regs[13][14] ), .Y(n556) );
  MUX2X1 U1328 ( .B(n556), .A(n279), .S(n370), .Y(n887) );
  AOI22X1 U1329 ( .A(net19516), .B(\regs[2][14] ), .C(net19517), .D(
        \regs[7][14] ), .Y(n581) );
  AOI22X1 U1330 ( .A(net19514), .B(\regs[9][14] ), .C(net19515), .D(
        \regs[8][14] ), .Y(n563) );
  AOI22X1 U1331 ( .A(net21469), .B(\regs[11][14] ), .C(net21470), .D(
        \regs[10][14] ), .Y(n562) );
  OAI22X1 U1332 ( .A(net20254), .B(n556), .C(net19510), .D(n553), .Y(n560) );
  OAI22X1 U1333 ( .A(net20244), .B(n558), .C(net20238), .D(n557), .Y(n559) );
  NOR2X1 U1334 ( .A(n560), .B(n559), .Y(n561) );
  NAND3X1 U1335 ( .A(n563), .B(n562), .C(n561), .Y(n564) );
  AOI21X1 U1336 ( .A(net19497), .B(\regs[3][14] ), .C(n564), .Y(n580) );
  OAI22X1 U1337 ( .A(net21932), .B(n574), .C(net20230), .D(n680), .Y(n578) );
  AOI22X1 U1338 ( .A(net21477), .B(\regs[4][14] ), .C(net19696), .D(
        outreg_data[14]), .Y(n575) );
  OAI21X1 U1339 ( .A(n576), .B(net20226), .C(n575), .Y(n577) );
  NOR2X1 U1340 ( .A(n577), .B(n578), .Y(n579) );
  INVX2 U1341 ( .A(\regs[4][15] ), .Y(n584) );
  INVX2 U1342 ( .A(\regs[5][15] ), .Y(n612) );
  INVX2 U1343 ( .A(\regs[1][15] ), .Y(n696) );
  INVX2 U1344 ( .A(\regs[6][15] ), .Y(n610) );
  INVX2 U1345 ( .A(\regs[2][15] ), .Y(n695) );
  INVX2 U1346 ( .A(\regs[7][15] ), .Y(n585) );
  INVX2 U1347 ( .A(\regs[3][15] ), .Y(n694) );
  INVX2 U1348 ( .A(\regs[9][15] ), .Y(n936) );
  MUX2X1 U1349 ( .B(n936), .A(n346), .S(net21434), .Y(n1235) );
  INVX2 U1350 ( .A(\regs[8][15] ), .Y(n951) );
  MUX2X1 U1351 ( .B(n951), .A(n346), .S(net21435), .Y(n1219) );
  INVX2 U1352 ( .A(\regs[11][15] ), .Y(n906) );
  MUX2X1 U1353 ( .B(n906), .A(n346), .S(net21438), .Y(n1267) );
  INVX2 U1354 ( .A(\regs[10][15] ), .Y(n921) );
  MUX2X1 U1355 ( .B(n921), .A(n346), .S(n283), .Y(n1251) );
  INVX2 U1356 ( .A(\regs[14][15] ), .Y(n588) );
  MUX2X1 U1357 ( .B(n588), .A(n346), .S(net21437), .Y(n897) );
  INVX2 U1358 ( .A(\regs[15][15] ), .Y(n596) );
  MUX2X1 U1359 ( .B(n596), .A(n278), .S(n371), .Y(n898) );
  INVX2 U1360 ( .A(\regs[12][15] ), .Y(n586) );
  MUX2X1 U1361 ( .B(n586), .A(n346), .S(n372), .Y(n895) );
  INVX2 U1362 ( .A(\regs[13][15] ), .Y(n587) );
  MUX2X1 U1363 ( .B(n587), .A(n278), .S(n370), .Y(n896) );
  AOI22X1 U1364 ( .A(net19516), .B(\regs[2][15] ), .C(net21751), .D(
        \regs[7][15] ), .Y(n624) );
  AOI22X1 U1365 ( .A(net19514), .B(\regs[9][15] ), .C(net19515), .D(
        \regs[8][15] ), .Y(n608) );
  AOI22X1 U1366 ( .A(net21469), .B(\regs[11][15] ), .C(net21470), .D(
        \regs[10][15] ), .Y(n600) );
  OAI22X1 U1367 ( .A(net19508), .B(n587), .C(net20249), .D(n586), .Y(n598) );
  OAI22X1 U1368 ( .A(net20244), .B(n596), .C(net19506), .D(n588), .Y(n597) );
  NOR2X1 U1369 ( .A(n598), .B(n597), .Y(n599) );
  NAND3X1 U1370 ( .A(n608), .B(n600), .C(n599), .Y(n609) );
  AOI21X1 U1371 ( .A(net19497), .B(\regs[3][15] ), .C(n609), .Y(n623) );
  OAI22X1 U1372 ( .A(net21932), .B(n610), .C(net20230), .D(n696), .Y(n621) );
  AOI22X1 U1373 ( .A(net21634), .B(\regs[4][15] ), .C(net19696), .D(
        outreg_data[15]), .Y(n611) );
  OAI21X1 U1374 ( .A(net20226), .B(n612), .C(n611), .Y(n620) );
  NOR2X1 U1375 ( .A(n620), .B(n621), .Y(n622) );
  NOR2X1 U1376 ( .A(net19478), .B(net19479), .Y(n632) );
  NAND3X1 U1377 ( .A(net19475), .B(net19476), .C(n632), .Y(n751) );
  AOI22X1 U1378 ( .A(\regs[6][10] ), .B(net21403), .C(\regs[7][10] ), .D(
        net21405), .Y(n647) );
  AOI22X1 U1379 ( .A(\regs[4][10] ), .B(net21404), .C(\regs[5][10] ), .D(
        net21406), .Y(n646) );
  OAI22X1 U1380 ( .A(net19342), .B(n634), .C(net19344), .D(n633), .Y(n644) );
  OAI22X1 U1381 ( .A(net19338), .B(net19471), .C(net19340), .D(n635), .Y(n636)
         );
  NOR2X1 U1382 ( .A(n644), .B(n636), .Y(n645) );
  NAND3X1 U1383 ( .A(n647), .B(n646), .C(n645), .Y(n739) );
  AOI22X1 U1384 ( .A(\regs[4][11] ), .B(net21404), .C(\regs[5][11] ), .D(
        net21406), .Y(n657) );
  OAI22X1 U1385 ( .A(net19342), .B(net19464), .C(net19344), .D(net19465), .Y(
        n648) );
  NOR2X1 U1386 ( .A(n648), .B(net19461), .Y(n656) );
  NAND3X1 U1387 ( .A(net19457), .B(n657), .C(n656), .Y(n727) );
  AOI22X1 U1388 ( .A(\regs[4][12] ), .B(net21404), .C(\regs[5][12] ), .D(
        net21406), .Y(n660) );
  OAI22X1 U1389 ( .A(net19342), .B(net19455), .C(net19344), .D(net19456), .Y(
        n658) );
  NOR2X1 U1390 ( .A(n658), .B(net19452), .Y(n659) );
  NAND3X1 U1391 ( .A(net19448), .B(n660), .C(n659), .Y(n715) );
  AOI22X1 U1392 ( .A(\regs[4][13] ), .B(net21404), .C(\regs[5][13] ), .D(
        net21406), .Y(n670) );
  OAI22X1 U1393 ( .A(net19342), .B(net19446), .C(net19344), .D(net19447), .Y(
        n668) );
  NOR2X1 U1394 ( .A(n668), .B(net19443), .Y(n669) );
  NAND3X1 U1395 ( .A(net19439), .B(n670), .C(n669), .Y(n703) );
  AOI22X1 U1396 ( .A(\regs[6][14] ), .B(net21403), .C(\regs[7][14] ), .D(
        net21405), .Y(n693) );
  AOI22X1 U1397 ( .A(\regs[4][14] ), .B(net21404), .C(\regs[5][14] ), .D(
        net21406), .Y(n692) );
  OAI22X1 U1398 ( .A(net19342), .B(n672), .C(net19344), .D(n671), .Y(n683) );
  OAI22X1 U1399 ( .A(net19338), .B(n681), .C(net19340), .D(n680), .Y(n682) );
  NOR2X1 U1400 ( .A(n683), .B(n682), .Y(n684) );
  NAND3X1 U1401 ( .A(n693), .B(n692), .C(n684), .Y(n691) );
  AOI22X1 U1402 ( .A(\regs[6][15] ), .B(net21403), .C(\regs[7][15] ), .D(
        net21405), .Y(n716) );
  AOI22X1 U1403 ( .A(\regs[4][15] ), .B(net21404), .C(\regs[5][15] ), .D(
        net21406), .Y(n708) );
  OAI22X1 U1404 ( .A(net19342), .B(n695), .C(net19344), .D(n694), .Y(n706) );
  OAI22X1 U1405 ( .A(net19338), .B(n704), .C(net19340), .D(n696), .Y(n705) );
  NOR2X1 U1406 ( .A(n706), .B(n705), .Y(n707) );
  NAND3X1 U1407 ( .A(n716), .B(n708), .C(n707), .Y(n679) );
  AOI22X1 U1408 ( .A(\regs[4][1] ), .B(net21404), .C(\regs[5][1] ), .D(
        net21406), .Y(n719) );
  OAI22X1 U1409 ( .A(net19342), .B(net19419), .C(net19344), .D(net19420), .Y(
        n717) );
  NOR2X1 U1410 ( .A(n717), .B(net19416), .Y(n718) );
  NAND3X1 U1411 ( .A(net19412), .B(n719), .C(n718), .Y(n667) );
  AOI22X1 U1412 ( .A(\regs[6][2] ), .B(net21403), .C(\regs[7][2] ), .D(
        net21405), .Y(n730) );
  OAI22X1 U1413 ( .A(net19342), .B(net19410), .C(net19344), .D(n720), .Y(n728)
         );
  NOR2X1 U1414 ( .A(n728), .B(net19407), .Y(n729) );
  NAND3X1 U1415 ( .A(n730), .B(net19404), .C(n729), .Y(n655) );
  AOI22X1 U1416 ( .A(\regs[6][3] ), .B(net21403), .C(\regs[7][3] ), .D(
        net21405), .Y(n744) );
  AOI22X1 U1417 ( .A(\regs[4][3] ), .B(net21404), .C(\regs[5][3] ), .D(
        net21406), .Y(n743) );
  OAI22X1 U1418 ( .A(net19342), .B(net19401), .C(net19344), .D(n731), .Y(n741)
         );
  OAI22X1 U1419 ( .A(net19338), .B(net19399), .C(net19340), .D(n732), .Y(n740)
         );
  NOR2X1 U1420 ( .A(n741), .B(n740), .Y(n742) );
  NAND3X1 U1421 ( .A(n744), .B(n743), .C(n742), .Y(n643) );
  AOI22X1 U1422 ( .A(\regs[6][4] ), .B(net21403), .C(\regs[7][4] ), .D(
        net21405), .Y(n771) );
  AOI22X1 U1423 ( .A(\regs[4][4] ), .B(net21404), .C(\regs[5][4] ), .D(
        net21406), .Y(n770) );
  OAI22X1 U1424 ( .A(net19342), .B(net19392), .C(net19344), .D(n752), .Y(n755)
         );
  OAI22X1 U1425 ( .A(net19338), .B(net19390), .C(net19340), .D(n753), .Y(n754)
         );
  NOR2X1 U1426 ( .A(n755), .B(n754), .Y(n756) );
  NAND3X1 U1427 ( .A(n771), .B(n770), .C(n756), .Y(n631) );
  AOI22X1 U1428 ( .A(\regs[6][5] ), .B(net21403), .C(\regs[7][5] ), .D(
        net21405), .Y(n779) );
  AOI22X1 U1429 ( .A(\regs[4][5] ), .B(net21404), .C(\regs[5][5] ), .D(
        net21406), .Y(n778) );
  OAI22X1 U1430 ( .A(net19342), .B(n773), .C(net19344), .D(n772), .Y(n776) );
  OAI22X1 U1431 ( .A(net19338), .B(net19381), .C(net19340), .D(n774), .Y(n775)
         );
  NOR2X1 U1432 ( .A(n776), .B(n775), .Y(n777) );
  NAND3X1 U1433 ( .A(n779), .B(n778), .C(n777), .Y(n619) );
  AOI22X1 U1434 ( .A(\regs[4][6] ), .B(net21404), .C(\regs[5][6] ), .D(
        net21406), .Y(n782) );
  OAI22X1 U1435 ( .A(net19342), .B(net19374), .C(net19344), .D(net19375), .Y(
        n780) );
  NOR2X1 U1436 ( .A(n780), .B(net19371), .Y(n781) );
  NAND3X1 U1437 ( .A(net19367), .B(n782), .C(n781), .Y(n607) );
  AOI22X1 U1438 ( .A(\regs[4][7] ), .B(net21404), .C(\regs[5][7] ), .D(
        net21406), .Y(n785) );
  OAI22X1 U1439 ( .A(net19342), .B(net19365), .C(net19344), .D(net19366), .Y(
        n783) );
  NOR2X1 U1440 ( .A(n783), .B(net19362), .Y(n784) );
  NAND3X1 U1441 ( .A(net19358), .B(n785), .C(n784), .Y(n595) );
  AOI22X1 U1442 ( .A(\regs[6][8] ), .B(net21403), .C(\regs[7][8] ), .D(
        net21405), .Y(n792) );
  AOI22X1 U1443 ( .A(\regs[4][8] ), .B(net21404), .C(\regs[5][8] ), .D(
        net21406), .Y(n791) );
  OAI22X1 U1444 ( .A(net19342), .B(net19356), .C(net19344), .D(n786), .Y(n789)
         );
  OAI22X1 U1445 ( .A(net19338), .B(net19354), .C(net19340), .D(n787), .Y(n788)
         );
  NOR2X1 U1446 ( .A(n789), .B(n788), .Y(n790) );
  NAND3X1 U1447 ( .A(n792), .B(n791), .C(n790), .Y(n583) );
  AOI22X1 U1448 ( .A(\regs[4][9] ), .B(net21404), .C(\regs[5][9] ), .D(
        net21406), .Y(n795) );
  OAI22X1 U1449 ( .A(net19341), .B(net19342), .C(net19343), .D(net19344), .Y(
        n793) );
  NOR2X1 U1450 ( .A(n793), .B(net19336), .Y(n794) );
  NAND3X1 U1451 ( .A(net19332), .B(n795), .C(n794), .Y(n555) );
  INVX2 U1452 ( .A(r2_sel[3]), .Y(n966) );
  INVX2 U1453 ( .A(r2_sel[0]), .Y(n967) );
  INVX2 U1454 ( .A(r2_sel[2]), .Y(n968) );
endmodule


module scalable_cla_block_CLA_BLK_SIZE_BITS4_3 ( A, B, Cin, S, PG, GG );
  input [3:0] A;
  input [3:0] B;
  output [3:0] S;
  input Cin;
  output PG, GG;
  wire   n10, n16, n17, net19260, net19262, net19264, net19267, net19268,
         net19269, net19273, net19274, n1, n3, n4, n5, n6, n7, n8, n9, n11,
         n12, n13, n14, n15, n18, n19, n20, n21, n22, n23, n24, n25, n26;

  AND2X2 U1 ( .A(A[3]), .B(B[3]), .Y(n1) );
  AND2X2 U2 ( .A(n3), .B(n4), .Y(PG) );
  INVX1 U3 ( .A(n5), .Y(n21) );
  INVX2 U4 ( .A(A[0]), .Y(net19274) );
  OAI21X1 U5 ( .A(A[0]), .B(B[0]), .C(Cin), .Y(n17) );
  INVX2 U6 ( .A(B[0]), .Y(net19273) );
  NAND2X1 U7 ( .A(n4), .B(n5), .Y(net19264) );
  INVX2 U8 ( .A(A[1]), .Y(net19269) );
  INVX2 U9 ( .A(B[1]), .Y(net19268) );
  NAND2X1 U10 ( .A(n5), .B(n6), .Y(net19260) );
  AOI21X1 U11 ( .A(n7), .B(n8), .C(n9), .Y(GG) );
  NOR2X1 U12 ( .A(B[3]), .B(A[3]), .Y(n11) );
  INVX2 U13 ( .A(net19267), .Y(n12) );
  INVX2 U14 ( .A(Cin), .Y(n13) );
  NOR2X1 U15 ( .A(n15), .B(n18), .Y(n14) );
  NOR2X1 U16 ( .A(B[3]), .B(A[3]), .Y(n9) );
  XOR2X1 U17 ( .A(A[1]), .B(B[1]), .Y(n16) );
  XOR2X1 U18 ( .A(B[3]), .B(A[3]), .Y(n10) );
  XNOR2X1 U19 ( .A(n19), .B(n13), .Y(S[0]) );
  NOR2X1 U20 ( .A(n12), .B(n11), .Y(n3) );
  XOR2X1 U21 ( .A(A[0]), .B(B[0]), .Y(n19) );
  NAND2X1 U22 ( .A(B[0]), .B(A[0]), .Y(n15) );
  OAI22X1 U23 ( .A(A[2]), .B(B[2]), .C(A[1]), .D(B[1]), .Y(n18) );
  AND2X2 U24 ( .A(B[1]), .B(A[1]), .Y(n20) );
  NOR2X1 U25 ( .A(n14), .B(n21), .Y(n8) );
  AOI21X1 U26 ( .A(n20), .B(n22), .C(n1), .Y(n7) );
  OR2X2 U27 ( .A(A[2]), .B(B[2]), .Y(n4) );
  INVX2 U28 ( .A(net19262), .Y(n23) );
  NAND2X1 U29 ( .A(A[2]), .B(B[2]), .Y(n5) );
  NAND2X1 U30 ( .A(n23), .B(n4), .Y(n6) );
  OR2X2 U31 ( .A(A[2]), .B(B[2]), .Y(n22) );
  NAND2X1 U32 ( .A(net19268), .B(net19269), .Y(net19267) );
  OAI21X1 U33 ( .A(net19273), .B(net19274), .C(n17), .Y(n24) );
  XOR2X1 U34 ( .A(n24), .B(n16), .Y(S[1]) );
  INVX2 U35 ( .A(n24), .Y(n25) );
  OAI21X1 U36 ( .A(net19268), .B(net19269), .C(n25), .Y(n26) );
  NAND2X1 U37 ( .A(n26), .B(net19267), .Y(net19262) );
  XNOR2X1 U38 ( .A(net19264), .B(n23), .Y(S[2]) );
  XOR2X1 U39 ( .A(net19260), .B(n10), .Y(S[3]) );
endmodule


module scalable_cla_block_CLA_BLK_SIZE_BITS4_2 ( A, B, Cin, S, PG, GG );
  input [3:0] A;
  input [3:0] B;
  output [3:0] S;
  input Cin;
  output PG, GG;
  wire   net5198, net19216, net19218, net19220, net19221, net19223, net19224,
         net19225, net19226, net19228, net19232, net19235, net19238, net19239,
         net19241, net54898, net54897, net54894, net54917, net54915, net54907,
         net54913, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14
;
  assign PG = net5198;

  NOR2X1 U1 ( .A(n1), .B(net54913), .Y(n2) );
  NOR2X1 U2 ( .A(A[2]), .B(B[2]), .Y(n1) );
  NOR2X1 U3 ( .A(A[1]), .B(B[1]), .Y(net54913) );
  AOI21X1 U4 ( .A(net54915), .B(n2), .C(net54917), .Y(net54907) );
  NOR2X1 U5 ( .A(net54913), .B(net19223), .Y(net19221) );
  AOI21X1 U6 ( .A(n3), .B(net54907), .C(n4), .Y(GG) );
  AOI21X1 U7 ( .A(n5), .B(n6), .C(n7), .Y(n3) );
  AND2X2 U8 ( .A(B[1]), .B(A[1]), .Y(n5) );
  OR2X2 U9 ( .A(A[2]), .B(B[2]), .Y(n6) );
  AND2X2 U10 ( .A(B[3]), .B(A[3]), .Y(n7) );
  AND2X2 U11 ( .A(B[0]), .B(A[0]), .Y(net54915) );
  INVX2 U12 ( .A(net54894), .Y(net54917) );
  NAND2X1 U13 ( .A(B[2]), .B(A[2]), .Y(net54894) );
  INVX1 U14 ( .A(net19241), .Y(n4) );
  OR2X2 U15 ( .A(A[3]), .B(B[3]), .Y(net19241) );
  AND2X2 U16 ( .A(Cin), .B(net19224), .Y(n8) );
  OR2X2 U17 ( .A(A[1]), .B(B[1]), .Y(net19226) );
  OR2X2 U18 ( .A(A[2]), .B(B[2]), .Y(net19225) );
  NAND2X1 U19 ( .A(net19218), .B(net54894), .Y(net19216) );
  NAND2X1 U20 ( .A(net19225), .B(net54894), .Y(net19228) );
  OAI21X1 U21 ( .A(net54897), .B(net54898), .C(net19232), .Y(net19220) );
  INVX2 U22 ( .A(A[1]), .Y(net54897) );
  INVX2 U23 ( .A(B[1]), .Y(net54898) );
  NAND3X1 U24 ( .A(net19241), .B(n9), .C(net19225), .Y(net19239) );
  XOR2X1 U25 ( .A(A[1]), .B(B[1]), .Y(net19235) );
  OR2X2 U26 ( .A(B[1]), .B(A[1]), .Y(n9) );
  OR2X2 U27 ( .A(B[0]), .B(A[0]), .Y(net19224) );
  XOR2X1 U28 ( .A(A[0]), .B(B[0]), .Y(net19238) );
  BUFX2 U29 ( .A(Cin), .Y(n10) );
  INVX2 U30 ( .A(net19239), .Y(net5198) );
  XOR2X1 U31 ( .A(n10), .B(net19238), .Y(S[0]) );
  NAND2X1 U32 ( .A(Cin), .B(net19224), .Y(n12) );
  NAND2X1 U33 ( .A(A[0]), .B(B[0]), .Y(net19232) );
  NAND2X1 U34 ( .A(n12), .B(net19232), .Y(n11) );
  XOR2X1 U35 ( .A(n11), .B(net19235), .Y(S[1]) );
  OAI21X1 U36 ( .A(net19220), .B(n8), .C(net19226), .Y(n13) );
  XOR2X1 U37 ( .A(n13), .B(net19228), .Y(S[2]) );
  OAI21X1 U38 ( .A(net19220), .B(net19224), .C(net19225), .Y(net19223) );
  OAI21X1 U39 ( .A(Cin), .B(net19220), .C(net19221), .Y(net19218) );
  XOR2X1 U40 ( .A(A[3]), .B(B[3]), .Y(n14) );
  XOR2X1 U41 ( .A(net19216), .B(n14), .Y(S[3]) );
endmodule


module scalable_cla_block_CLA_BLK_SIZE_BITS4_1 ( A, B, Cin, S, PG, GG );
  input [3:0] A;
  input [3:0] B;
  output [3:0] S;
  input Cin;
  output PG, GG;
  wire   net5190, net19170, net19171, net19174, net19176, net19177, net19178,
         net19180, net19182, net19190, net19191, net19193, net19206, net19208,
         net19209, net19215, net19179, net19210, net19207, net19200, n1, n2,
         n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17,
         n18, n19, n20, n21, n22, n23;
  assign PG = net5190;

  NAND2X1 U1 ( .A(n2), .B(n3), .Y(n1) );
  AND2X1 U2 ( .A(net19200), .B(net19179), .Y(n2) );
  AND2X2 U3 ( .A(net19215), .B(n9), .Y(n3) );
  NAND3X1 U4 ( .A(n9), .B(net19200), .C(net19210), .Y(n4) );
  INVX2 U5 ( .A(n4), .Y(net5190) );
  NAND2X1 U6 ( .A(n5), .B(n6), .Y(net19200) );
  INVX2 U7 ( .A(A[1]), .Y(n6) );
  NAND2X1 U8 ( .A(n5), .B(n6), .Y(net19180) );
  INVX2 U9 ( .A(B[1]), .Y(n5) );
  NAND2X1 U10 ( .A(n7), .B(n8), .Y(net19210) );
  AND2X2 U11 ( .A(net19209), .B(net19210), .Y(net19207) );
  INVX2 U12 ( .A(A[2]), .Y(n8) );
  NAND2X1 U13 ( .A(n7), .B(n8), .Y(net19179) );
  INVX2 U14 ( .A(B[2]), .Y(n7) );
  NAND2X1 U15 ( .A(n10), .B(n11), .Y(n9) );
  INVX2 U16 ( .A(A[3]), .Y(n11) );
  NAND2X1 U17 ( .A(n10), .B(n11), .Y(net19209) );
  INVX2 U18 ( .A(B[3]), .Y(n10) );
  XOR2X1 U19 ( .A(A[1]), .B(B[1]), .Y(net19193) );
  NAND2X1 U20 ( .A(A[1]), .B(B[1]), .Y(net19190) );
  NAND2X1 U21 ( .A(A[2]), .B(B[2]), .Y(net19177) );
  AOI22X1 U22 ( .A(A[3]), .B(B[3]), .C(net19207), .D(net19208), .Y(net19206)
         );
  XOR2X1 U23 ( .A(A[3]), .B(B[3]), .Y(net19170) );
  NAND2X1 U24 ( .A(net19179), .B(net19177), .Y(net19182) );
  NAND3X1 U25 ( .A(net19178), .B(net19179), .C(net19180), .Y(net19171) );
  AND2X2 U26 ( .A(net19180), .B(net19178), .Y(n18) );
  NOR2X1 U27 ( .A(B[0]), .B(A[0]), .Y(n12) );
  INVX1 U28 ( .A(n22), .Y(n13) );
  NAND2X1 U29 ( .A(A[0]), .B(B[0]), .Y(net19191) );
  INVX2 U30 ( .A(net19191), .Y(net19215) );
  NAND2X1 U31 ( .A(net19209), .B(net19176), .Y(n14) );
  INVX2 U32 ( .A(net19190), .Y(net19208) );
  NAND3X1 U33 ( .A(n1), .B(n14), .C(net19206), .Y(GG) );
  XOR2X1 U34 ( .A(A[0]), .B(B[0]), .Y(n15) );
  XOR2X1 U35 ( .A(n13), .B(n15), .Y(S[0]) );
  INVX2 U36 ( .A(Cin), .Y(n22) );
  OAI21X1 U37 ( .A(n22), .B(n12), .C(net19191), .Y(n16) );
  XOR2X1 U38 ( .A(n16), .B(net19193), .Y(S[1]) );
  NAND2X1 U39 ( .A(net19190), .B(net19191), .Y(n20) );
  INVX2 U40 ( .A(n20), .Y(n17) );
  NAND2X1 U41 ( .A(n17), .B(n12), .Y(net19178) );
  OAI21X1 U42 ( .A(Cin), .B(n20), .C(n18), .Y(n19) );
  XOR2X1 U43 ( .A(n19), .B(net19182), .Y(S[2]) );
  INVX2 U44 ( .A(net19171), .Y(net19174) );
  INVX2 U45 ( .A(net19177), .Y(net19176) );
  AOI21X1 U46 ( .A(net19174), .B(n20), .C(net19176), .Y(n21) );
  OAI21X1 U47 ( .A(n22), .B(net19171), .C(n21), .Y(n23) );
  XOR2X1 U48 ( .A(n23), .B(net19170), .Y(S[3]) );
endmodule


module scalable_cla_block_CLA_BLK_SIZE_BITS4_0 ( A, B, Cin, S, PG, GG );
  input [3:0] A;
  input [3:0] B;
  output [3:0] S;
  input Cin;
  output PG, GG;
  wire   net5182, net19141, net19142, net19151, net19157, net19158, net19159,
         net19162, net19164, net50736, net50726, net50709, net19163, net19143,
         net19140, net19139, net19138, net19137, net19135, net19131, net62643,
         net62660, net62675, net19134, net19133, net19132, net19130, net19129,
         n1, n2, n3, n4;
  assign PG = net5182;

  XOR2X1 U1 ( .A(net19129), .B(net19130), .Y(S[3]) );
  NAND2X1 U2 ( .A(net19133), .B(n2), .Y(net19129) );
  NAND2X1 U3 ( .A(Cin), .B(net19134), .Y(net19133) );
  INVX2 U4 ( .A(net19135), .Y(net19134) );
  INVX2 U5 ( .A(n1), .Y(n2) );
  NAND2X1 U6 ( .A(net19132), .B(net19131), .Y(n1) );
  NAND2X1 U7 ( .A(net19134), .B(net19137), .Y(net19132) );
  OR2X2 U8 ( .A(net62660), .B(net62643), .Y(net19137) );
  NAND2X1 U9 ( .A(B[2]), .B(A[2]), .Y(net19131) );
  XOR2X1 U10 ( .A(A[3]), .B(B[3]), .Y(net19130) );
  XOR2X1 U11 ( .A(net62675), .B(n3), .Y(S[0]) );
  INVX1 U12 ( .A(Cin), .Y(net62675) );
  XNOR2X1 U13 ( .A(A[0]), .B(B[0]), .Y(n3) );
  AND2X2 U14 ( .A(A[0]), .B(B[0]), .Y(net62660) );
  AND2X2 U15 ( .A(A[1]), .B(B[1]), .Y(net62643) );
  INVX2 U16 ( .A(A[3]), .Y(net19158) );
  INVX2 U17 ( .A(B[3]), .Y(net19157) );
  OAI21X1 U18 ( .A(net19163), .B(net50709), .C(net19131), .Y(n4) );
  NAND2X1 U19 ( .A(net19131), .B(net19139), .Y(net19142) );
  OAI21X1 U20 ( .A(Cin), .B(net19137), .C(net19143), .Y(net19141) );
  AOI21X1 U21 ( .A(Cin), .B(net50726), .C(net62660), .Y(net50736) );
  NAND3X1 U22 ( .A(net19138), .B(net19139), .C(net19140), .Y(net19135) );
  OR2X2 U23 ( .A(net50726), .B(net19137), .Y(net19138) );
  INVX1 U24 ( .A(net62643), .Y(net50709) );
  AOI22X1 U25 ( .A(net62660), .B(net5182), .C(n4), .D(net19162), .Y(net19159)
         );
  OR2X2 U26 ( .A(A[2]), .B(B[2]), .Y(net19139) );
  AND2X2 U27 ( .A(net19140), .B(net19138), .Y(net19143) );
  INVX2 U28 ( .A(net19139), .Y(net19163) );
  NAND3X1 U29 ( .A(net19139), .B(net19140), .C(net19162), .Y(net19164) );
  XOR2X1 U30 ( .A(A[1]), .B(B[1]), .Y(net19151) );
  OR2X2 U31 ( .A(B[1]), .B(A[1]), .Y(net19140) );
  OR2X2 U32 ( .A(B[0]), .B(A[0]), .Y(net50726) );
  XNOR2X1 U33 ( .A(net50736), .B(net19151), .Y(S[1]) );
  NAND2X1 U34 ( .A(net19157), .B(net19158), .Y(net19162) );
  INVX2 U35 ( .A(net19164), .Y(net5182) );
  OAI21X1 U36 ( .A(net19157), .B(net19158), .C(net19159), .Y(GG) );
  XOR2X1 U37 ( .A(net19141), .B(net19142), .Y(S[2]) );
endmodule


module scalable_cla_addr_NUM_CLA_BLKS4_CLA_BLK_SIZE_BITS4 ( A, B, Cin, S, V );
  input [15:0] A;
  input [15:0] B;
  output [15:0] S;
  input Cin;
  output V;
  wire   net5163, net5165, net19293, net19294, net19295, net19292, net19291,
         net62105, net62672, net19298, n1, n2, n3, n5;
  wire   [3:0] gg_vector;
  wire   [3:0] pg_vector;

  scalable_cla_block_CLA_BLK_SIZE_BITS4_3 CLA_BLK_0 ( .A(A[3:0]), .B(B[3:0]), 
        .Cin(Cin), .S(S[3:0]), .PG(pg_vector[0]), .GG(gg_vector[0]) );
  scalable_cla_block_CLA_BLK_SIZE_BITS4_2 CLA_BLK_1 ( .A(A[7:4]), .B(B[7:4]), 
        .Cin(net5163), .S(S[7:4]), .PG(pg_vector[1]), .GG(gg_vector[1]) );
  scalable_cla_block_CLA_BLK_SIZE_BITS4_1 CLA_BLK_2 ( .A(A[11:8]), .B(B[11:8]), 
        .Cin(n5), .S(S[11:8]), .PG(pg_vector[2]), .GG(gg_vector[2]) );
  scalable_cla_block_CLA_BLK_SIZE_BITS4_0 CLA_BLK_3 ( .A(A[15:12]), .B(
        B[15:12]), .Cin(net62672), .S(S[15:12]), .PG(pg_vector[3]), .GG(
        gg_vector[3]) );
  NAND2X1 U1 ( .A(n1), .B(n2), .Y(net62672) );
  AOI22X1 U2 ( .A(gg_vector[1]), .B(pg_vector[2]), .C(gg_vector[0]), .D(
        net19298), .Y(n1) );
  AOI21X1 U3 ( .A(net19295), .B(net62105), .C(gg_vector[2]), .Y(n2) );
  AND2X2 U4 ( .A(pg_vector[2]), .B(pg_vector[1]), .Y(net19298) );
  NAND2X1 U5 ( .A(n1), .B(n2), .Y(net5165) );
  INVX1 U6 ( .A(gg_vector[0]), .Y(net19291) );
  AND2X2 U7 ( .A(pg_vector[2]), .B(pg_vector[1]), .Y(net62105) );
  AOI21X1 U8 ( .A(net19295), .B(pg_vector[1]), .C(gg_vector[1]), .Y(net19293)
         );
  NAND2X1 U9 ( .A(gg_vector[0]), .B(pg_vector[1]), .Y(net19294) );
  INVX2 U10 ( .A(net19292), .Y(net19295) );
  NAND2X1 U11 ( .A(pg_vector[0]), .B(Cin), .Y(net19292) );
  NAND2X1 U12 ( .A(net19291), .B(net19292), .Y(net5163) );
  NAND2X1 U13 ( .A(net19294), .B(net19293), .Y(n5) );
  AOI21X1 U14 ( .A(pg_vector[3]), .B(net5165), .C(gg_vector[3]), .Y(n3) );
  INVX2 U15 ( .A(n3), .Y(V) );
endmodule


module alu_DATA_SIZE_BITS16 ( A, B, alu_op, result, overflow );
  input [15:0] A;
  input [15:0] B;
  output [15:0] result;
  input alu_op;
  output overflow;
  wire   int_V, net19300, net19301, net19316, net19317, net19318, net19324,
         net19325, net19326, net19327, net19330, net20148, net20455, net20454,
         net21787, net21813, net21812, net21816, net21820, net21852, net26830,
         net36183, net36187, net36189, net36201, net37380, net38301, net39314,
         net31088, net19319, net45993, net48779, net62027, net62591, n1, n2,
         n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18,
         n20, n21, n22, n23, n24, n25, n26;
  wire   [15:0] int_A;
  wire   [15:0] int_B;
  wire   [15:0] int_S;
  assign result[5] = net20454;
  assign result[2] = net21787;
  assign result[4] = net21812;
  assign net37380 = alu_op;

  AND2X2 U3 ( .A(B[9]), .B(net36201), .Y(int_B[9]) );
  AND2X2 U4 ( .A(B[8]), .B(net36201), .Y(int_B[8]) );
  AND2X2 U5 ( .A(B[7]), .B(net38301), .Y(int_B[7]) );
  AND2X2 U6 ( .A(B[6]), .B(net36201), .Y(int_B[6]) );
  AND2X2 U7 ( .A(B[5]), .B(net36201), .Y(int_B[5]) );
  AND2X2 U8 ( .A(B[4]), .B(net36201), .Y(int_B[4]) );
  AND2X2 U9 ( .A(B[3]), .B(net36201), .Y(int_B[3]) );
  AND2X2 U10 ( .A(B[2]), .B(net36201), .Y(int_B[2]) );
  AND2X2 U11 ( .A(B[1]), .B(net36201), .Y(int_B[1]) );
  AND2X2 U12 ( .A(B[15]), .B(net36201), .Y(int_B[15]) );
  AND2X2 U13 ( .A(B[14]), .B(net36201), .Y(int_B[14]) );
  AND2X2 U14 ( .A(B[13]), .B(net36201), .Y(int_B[13]) );
  AND2X2 U15 ( .A(B[12]), .B(net36201), .Y(int_B[12]) );
  AND2X2 U16 ( .A(B[11]), .B(net36201), .Y(int_B[11]) );
  AND2X2 U17 ( .A(B[10]), .B(net36201), .Y(int_B[10]) );
  AND2X2 U18 ( .A(B[0]), .B(net36201), .Y(int_B[0]) );
  scalable_cla_addr_NUM_CLA_BLKS4_CLA_BLK_SIZE_BITS4 CLA_ADDR ( .A(int_A), .B(
        int_B), .Cin(1'b0), .S(int_S), .V(int_V) );
  INVX2 U2 ( .A(n18), .Y(result[13]) );
  MUX2X1 U19 ( .B(n1), .A(n2), .S(net38301), .Y(result[6]) );
  INVX2 U20 ( .A(A[6]), .Y(n1) );
  INVX2 U21 ( .A(int_S[6]), .Y(n2) );
  INVX8 U22 ( .A(net48779), .Y(net38301) );
  BUFX2 U23 ( .A(n1), .Y(net19325) );
  INVX2 U24 ( .A(net19301), .Y(result[14]) );
  INVX2 U25 ( .A(net19300), .Y(result[15]) );
  INVX4 U26 ( .A(net48779), .Y(net62591) );
  INVX8 U27 ( .A(net38301), .Y(net20148) );
  MUX2X1 U28 ( .B(int_S[14]), .A(A[14]), .S(net48779), .Y(net19301) );
  INVX2 U29 ( .A(int_S[10]), .Y(n20) );
  INVX1 U30 ( .A(net38301), .Y(net62027) );
  NAND2X1 U31 ( .A(n4), .B(n5), .Y(result[0]) );
  NAND2X1 U32 ( .A(net62027), .B(A[0]), .Y(n5) );
  NAND2X1 U33 ( .A(int_S[0]), .B(net38301), .Y(n4) );
  INVX8 U34 ( .A(net37380), .Y(net48779) );
  BUFX2 U35 ( .A(net37380), .Y(net39314) );
  INVX2 U36 ( .A(net37380), .Y(net26830) );
  INVX1 U37 ( .A(A[0]), .Y(n6) );
  INVX2 U38 ( .A(int_S[4]), .Y(net21813) );
  INVX2 U39 ( .A(A[1]), .Y(n7) );
  MUX2X1 U40 ( .B(n7), .A(n8), .S(net62591), .Y(result[1]) );
  INVX2 U41 ( .A(int_S[1]), .Y(n8) );
  INVX2 U42 ( .A(net26830), .Y(net45993) );
  BUFX2 U43 ( .A(n7), .Y(net19330) );
  INVX2 U44 ( .A(A[7]), .Y(n9) );
  MUX2X1 U45 ( .B(n9), .A(n10), .S(net62591), .Y(result[7]) );
  INVX2 U46 ( .A(int_S[7]), .Y(n10) );
  BUFX2 U47 ( .A(n9), .Y(net19324) );
  MUX2X1 U48 ( .B(net19319), .A(net31088), .S(net38301), .Y(result[12]) );
  INVX2 U49 ( .A(int_S[12]), .Y(net31088) );
  INVX2 U50 ( .A(A[12]), .Y(net19319) );
  BUFX2 U51 ( .A(net19319), .Y(net36189) );
  MUX2X1 U52 ( .B(n11), .A(n12), .S(net38301), .Y(result[11]) );
  INVX2 U53 ( .A(int_S[11]), .Y(n12) );
  INVX2 U54 ( .A(A[11]), .Y(n11) );
  BUFX2 U55 ( .A(n11), .Y(net36187) );
  MUX2X1 U56 ( .B(n13), .A(n14), .S(net45993), .Y(result[9]) );
  INVX2 U57 ( .A(int_S[9]), .Y(n14) );
  INVX2 U58 ( .A(A[9]), .Y(n13) );
  BUFX2 U59 ( .A(n13), .Y(net36183) );
  MUX2X1 U60 ( .B(net19327), .A(net21813), .S(net39314), .Y(net21812) );
  MUX2X1 U61 ( .B(net19326), .A(net20455), .S(net39314), .Y(net20454) );
  BUFX2 U62 ( .A(net38301), .Y(net36201) );
  BUFX2 U63 ( .A(n24), .Y(n15) );
  MUX2X1 U64 ( .B(n16), .A(n17), .S(net38301), .Y(net21787) );
  INVX2 U65 ( .A(int_S[2]), .Y(n17) );
  INVX2 U66 ( .A(A[2]), .Y(n16) );
  BUFX2 U67 ( .A(n16), .Y(net21852) );
  MUX2X1 U68 ( .B(A[13]), .A(int_S[13]), .S(net62591), .Y(n18) );
  MUX2X1 U69 ( .B(A[15]), .A(int_S[15]), .S(net62591), .Y(net19300) );
  INVX1 U70 ( .A(A[13]), .Y(net19318) );
  MUX2X1 U71 ( .B(n24), .A(n20), .S(net45993), .Y(result[10]) );
  INVX2 U72 ( .A(A[10]), .Y(n24) );
  BUFX2 U73 ( .A(net19326), .Y(net21820) );
  BUFX2 U74 ( .A(net19327), .Y(net21816) );
  INVX2 U75 ( .A(A[4]), .Y(net19327) );
  INVX2 U76 ( .A(n25), .Y(result[3]) );
  MUX2X1 U77 ( .B(int_S[3]), .A(A[3]), .S(net26830), .Y(n25) );
  INVX2 U78 ( .A(n26), .Y(result[8]) );
  MUX2X1 U79 ( .B(int_S[8]), .A(A[8]), .S(net26830), .Y(n26) );
  INVX2 U80 ( .A(int_V), .Y(n21) );
  NOR2X1 U81 ( .A(n21), .B(net20148), .Y(overflow) );
  INVX2 U82 ( .A(int_S[5]), .Y(net20455) );
  INVX2 U83 ( .A(A[5]), .Y(net19326) );
  INVX1 U84 ( .A(A[15]), .Y(net19316) );
  INVX1 U85 ( .A(A[14]), .Y(net19317) );
  INVX1 U86 ( .A(A[3]), .Y(n22) );
  INVX1 U87 ( .A(A[8]), .Y(n23) );
  NOR2X1 U88 ( .A(net20148), .B(n6), .Y(int_A[0]) );
  NOR2X1 U89 ( .A(net20148), .B(net19330), .Y(int_A[1]) );
  NOR2X1 U90 ( .A(net20148), .B(net21852), .Y(int_A[2]) );
  NOR2X1 U91 ( .A(net20148), .B(n22), .Y(int_A[3]) );
  NOR2X1 U92 ( .A(net20148), .B(net21816), .Y(int_A[4]) );
  NOR2X1 U93 ( .A(net20148), .B(net21820), .Y(int_A[5]) );
  NOR2X1 U94 ( .A(net20148), .B(net19325), .Y(int_A[6]) );
  NOR2X1 U95 ( .A(net20148), .B(net19324), .Y(int_A[7]) );
  NOR2X1 U96 ( .A(net20148), .B(n23), .Y(int_A[8]) );
  NOR2X1 U97 ( .A(net20148), .B(net36183), .Y(int_A[9]) );
  NOR2X1 U98 ( .A(net20148), .B(n15), .Y(int_A[10]) );
  NOR2X1 U99 ( .A(net20148), .B(net36187), .Y(int_A[11]) );
  NOR2X1 U100 ( .A(net20148), .B(net36189), .Y(int_A[12]) );
  NOR2X1 U101 ( .A(net20148), .B(net19318), .Y(int_A[13]) );
  NOR2X1 U102 ( .A(net20148), .B(net19317), .Y(int_A[14]) );
  NOR2X1 U103 ( .A(net20148), .B(net19316), .Y(int_A[15]) );
endmodule


module datapath ( clk, n_reset, op, src1, src2, dest, ext_data, outreg_data, 
        overflow );
  input [1:0] op;
  input [3:0] src1;
  input [3:0] src2;
  input [3:0] dest;
  input [15:0] ext_data;
  output [15:0] outreg_data;
  input clk, n_reset;
  output overflow;
  wire   int_w_data_sel, int_w_en, int_alu_op, net4819, net4822, net4824,
         net4826, net4828, net4829, net4831, net4833, net4834, net19928,
         net20165, net20164, net20163, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10,
         n11, n12, n13, n14, n15, n16, n17, n18, n19, n20, n21, n22, n23;
  wire   [15:0] int_src1_data;
  wire   [15:0] int_src2_data;
  wire   [15:0] int_result;

  datapath_ctrl DP_CTRL ( .op(op), .w_data_sel(int_w_data_sel), .w_en(int_w_en), .alu_op(int_alu_op) );
  regfile_NUM_REG_ADDR_BITS4_REG_SIZE_BITS16 REG_FILE ( .clk(clk), .n_reset(
        n_reset), .w_sel(dest), .r1_sel(src1), .r2_sel(src2), .w_data({n23, 
        n22, net4822, net4819, net4824, n20, net4826, n21, net4828, net4829, 
        n18, n19, n17, net4833, net4834, net4831}), .w_en(int_w_en), .r1_data(
        int_src1_data), .r2_data(int_src2_data), .outreg_data(outreg_data) );
  alu_DATA_SIZE_BITS16 ALU_MAP ( .A(int_src1_data), .B(int_src2_data), 
        .alu_op(int_alu_op), .result(int_result), .overflow(overflow) );
  INVX4 U1 ( .A(n1), .Y(net4829) );
  AOI22X1 U2 ( .A(ext_data[6]), .B(net19928), .C(int_result[6]), .D(net20165), 
        .Y(n1) );
  INVX8 U3 ( .A(net20164), .Y(net19928) );
  INVX2 U4 ( .A(net20163), .Y(net20165) );
  INVX4 U5 ( .A(n8), .Y(net4833) );
  AOI22X1 U6 ( .A(ext_data[0]), .B(net19928), .C(int_result[0]), .D(net20164), 
        .Y(n2) );
  INVX4 U7 ( .A(n2), .Y(net4831) );
  INVX4 U8 ( .A(net20163), .Y(net20164) );
  INVX1 U9 ( .A(int_w_data_sel), .Y(net20163) );
  AOI22X1 U10 ( .A(ext_data[1]), .B(net19928), .C(int_result[1]), .D(net20164), 
        .Y(n3) );
  INVX4 U11 ( .A(n3), .Y(net4834) );
  AOI22X1 U12 ( .A(ext_data[7]), .B(net19928), .C(int_result[7]), .D(net20165), 
        .Y(n4) );
  INVX4 U13 ( .A(n4), .Y(net4828) );
  AOI22X1 U14 ( .A(ext_data[12]), .B(net19928), .C(int_result[12]), .D(
        net20165), .Y(n5) );
  INVX4 U15 ( .A(n5), .Y(net4819) );
  AOI22X1 U16 ( .A(ext_data[11]), .B(net19928), .C(int_result[11]), .D(
        net20165), .Y(n6) );
  INVX4 U17 ( .A(n6), .Y(net4824) );
  AOI22X1 U18 ( .A(ext_data[9]), .B(net19928), .C(int_result[9]), .D(net20165), 
        .Y(n7) );
  INVX4 U19 ( .A(n7), .Y(net4826) );
  AOI22X1 U20 ( .A(ext_data[2]), .B(net19928), .C(int_result[2]), .D(net20164), 
        .Y(n8) );
  AOI22X1 U21 ( .A(ext_data[13]), .B(net19928), .C(int_result[13]), .D(
        net20165), .Y(n9) );
  INVX4 U22 ( .A(n9), .Y(net4822) );
  INVX4 U23 ( .A(n12), .Y(n18) );
  INVX4 U24 ( .A(n16), .Y(n23) );
  INVX4 U25 ( .A(n15), .Y(n22) );
  INVX4 U26 ( .A(n14), .Y(n20) );
  INVX4 U27 ( .A(n13), .Y(n21) );
  INVX4 U28 ( .A(n11), .Y(n19) );
  INVX4 U29 ( .A(n10), .Y(n17) );
  AOI22X1 U30 ( .A(ext_data[3]), .B(net19928), .C(net20164), .D(int_result[3]), 
        .Y(n10) );
  AOI22X1 U31 ( .A(ext_data[4]), .B(net19928), .C(int_result[4]), .D(net20164), 
        .Y(n11) );
  AOI22X1 U32 ( .A(ext_data[5]), .B(net19928), .C(int_result[5]), .D(net20164), 
        .Y(n12) );
  AOI22X1 U33 ( .A(ext_data[8]), .B(net19928), .C(net20165), .D(int_result[8]), 
        .Y(n13) );
  AOI22X1 U34 ( .A(ext_data[10]), .B(net19928), .C(int_result[10]), .D(
        net20165), .Y(n14) );
  AOI22X1 U35 ( .A(ext_data[14]), .B(net19928), .C(int_result[14]), .D(
        net20165), .Y(n15) );
  AOI22X1 U36 ( .A(ext_data[15]), .B(net19928), .C(int_result[15]), .D(
        net20165), .Y(n16) );
endmodule


module avg_four ( clk, n_reset, sample_data, data_ready, one_k_samples, 
        modwait, avg_out, err );
  input [15:0] sample_data;
  output [15:0] avg_out;
  input clk, n_reset, data_ready;
  output one_k_samples, modwait, err;
  wire   dr, overflow, cnt_up, n1, n2;
  wire   [1:0] op;
  wire   [3:0] src1;
  wire   [3:0] src2;
  wire   [3:0] dest;
  wire   SYNOPSYS_UNCONNECTED__0, SYNOPSYS_UNCONNECTED__1, 
        SYNOPSYS_UNCONNECTED__2, SYNOPSYS_UNCONNECTED__3, 
        SYNOPSYS_UNCONNECTED__4;
  assign avg_out[14] = 1'b0;
  assign avg_out[15] = 1'b0;

  sync sync_main ( .clk(clk), .n_rst(n_reset), .async_in(data_ready), 
        .sync_out(dr) );
  controller control ( .clk(clk), .n_reset(n_reset), .dr(dr), .overflow(
        overflow), .cnt_up(cnt_up), .modwait(modwait), .op(op), .src1({
        SYNOPSYS_UNCONNECTED__0, src1[2:0]}), .src2({SYNOPSYS_UNCONNECTED__1, 
        src2[2:0]}), .dest({SYNOPSYS_UNCONNECTED__2, dest[2:0]}), .err(err) );
  counter ctr_main ( .clk(clk), .n_reset(n_reset), .cnt_up(cnt_up), 
        .one_k_samples(one_k_samples) );
  datapath dp ( .clk(clk), .n_reset(n_reset), .op(op), .src1({1'b0, src1[2], 
        n2, src1[0]}), .src2({1'b0, src2[2:0]}), .dest({1'b0, dest[2:0]}), 
        .ext_data(sample_data), .outreg_data({avg_out[13:0], 
        SYNOPSYS_UNCONNECTED__3, SYNOPSYS_UNCONNECTED__4}), .overflow(overflow) );
  INVX4 U2 ( .A(src1[1]), .Y(n1) );
  INVX8 U3 ( .A(n1), .Y(n2) );
endmodule

