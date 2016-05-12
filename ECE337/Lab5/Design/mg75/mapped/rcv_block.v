
module start_bit_det ( clk, n_rst, serial_in, start_bit_detected );
  input clk, n_rst, serial_in;
  output start_bit_detected;
  wire   old_sample, new_sample, sync_phase, n4;

  DFFSR sync_phase_reg ( .D(serial_in), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        sync_phase) );
  DFFSR new_sample_reg ( .D(sync_phase), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        new_sample) );
  DFFSR old_sample_reg ( .D(new_sample), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        old_sample) );
  NOR2X1 U7 ( .A(new_sample), .B(n4), .Y(start_bit_detected) );
  INVX2 U6 ( .A(old_sample), .Y(n4) );
endmodule


module rcu ( clk, n_rst, start_bit_detected, packet_done, framing_error, 
        sbc_clear, sbc_enable, load_buffer, enable_timer );
  input clk, n_rst, start_bit_detected, packet_done, framing_error;
  output sbc_clear, sbc_enable, load_buffer, enable_timer;
  wire   n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18,
         enable_timer;
  wire   [2:0] state;
  wire   [2:0] nextstate;
  assign sbc_clear = enable_timer;

  DFFSR \state_reg[0]  ( .D(nextstate[0]), .CLK(clk), .R(n_rst), .S(1'b1), .Q(
        state[0]) );
  DFFSR \state_reg[1]  ( .D(nextstate[1]), .CLK(clk), .R(n_rst), .S(1'b1), .Q(
        state[1]) );
  DFFSR \state_reg[2]  ( .D(n18), .CLK(clk), .R(n_rst), .S(1'b1), .Q(state[2])
         );
  INVX1 U6 ( .A(enable_timer), .Y(n4) );
  INVX1 U7 ( .A(state[0]), .Y(n16) );
  INVX1 U8 ( .A(packet_done), .Y(n8) );
  INVX1 U9 ( .A(n11), .Y(n5) );
  INVX1 U10 ( .A(state[1]), .Y(n6) );
  INVX2 U11 ( .A(n6), .Y(n7) );
  INVX2 U12 ( .A(state[2]), .Y(n11) );
  NAND3X1 U13 ( .A(n11), .B(n6), .C(state[0]), .Y(n15) );
  NAND3X1 U14 ( .A(n7), .B(n11), .C(n16), .Y(n13) );
  OAI21X1 U15 ( .A(n4), .B(n8), .C(n13), .Y(nextstate[1]) );
  NOR2X1 U16 ( .A(framing_error), .B(n5), .Y(n9) );
  NAND3X1 U17 ( .A(n7), .B(state[0]), .C(n9), .Y(n10) );
  INVX2 U18 ( .A(n10), .Y(n18) );
  NAND3X1 U19 ( .A(start_bit_detected), .B(n11), .C(n16), .Y(n12) );
  OAI21X1 U20 ( .A(packet_done), .B(n4), .C(n12), .Y(n14) );
  INVX2 U21 ( .A(n13), .Y(sbc_enable) );
  OR2X2 U22 ( .A(n14), .B(sbc_enable), .Y(nextstate[0]) );
  INVX2 U23 ( .A(n15), .Y(enable_timer) );
  NAND2X1 U24 ( .A(n5), .B(n16), .Y(n17) );
  NOR2X1 U25 ( .A(n7), .B(n17), .Y(load_buffer) );
endmodule


module flex_counter_1 ( clk, n_rst, count_enable, clear, rollover_val, 
        count_out, rollover_flag );
  input [3:0] rollover_val;
  output [3:0] count_out;
  input clk, n_rst, count_enable, clear;
  output rollover_flag;
  wire   n77, n78, n79, n80, n41, n42, n43, n44, n45, n1, n2, n3, n4, n5, n6,
         n7, n9, n10, n18, n19, n20, n21, n23, n24, n25, n26, n27, n28, n29,
         n30, n31, n32, n33, n34, n35, n36, n37, n38, n39, n40, n46, n47, n48,
         n49, n50, n51, n52, n53, n54, n55, n56, n57, n58, n59, n60, n61, n62,
         n63, n64, n65, n66, n67, n68, n69, n70, n71, n72, n73, n74, n75, n76;

  DFFSR \f_reg[3]  ( .D(n45), .CLK(clk), .R(n_rst), .S(1'b1), .Q(n77) );
  DFFSR \f_reg[2]  ( .D(n44), .CLK(clk), .R(n_rst), .S(1'b1), .Q(n78) );
  DFFSR \f_reg[1]  ( .D(n43), .CLK(clk), .R(n_rst), .S(1'b1), .Q(n79) );
  DFFSR \f_reg[0]  ( .D(n42), .CLK(clk), .R(n_rst), .S(1'b1), .Q(n80) );
  DFFSR rollover_flag_reg ( .D(n41), .CLK(clk), .R(n_rst), .S(1'b1), .Q(
        rollover_flag) );
  INVX2 U6 ( .A(n79), .Y(n60) );
  AND2X2 U9 ( .A(n9), .B(n70), .Y(n1) );
  AND2X2 U10 ( .A(n25), .B(n24), .Y(n2) );
  XNOR2X1 U11 ( .A(n77), .B(rollover_val[3]), .Y(n26) );
  INVX1 U12 ( .A(n77), .Y(n46) );
  AND2X1 U13 ( .A(n9), .B(n70), .Y(n3) );
  INVX2 U14 ( .A(count_out[2]), .Y(n4) );
  BUFX4 U15 ( .A(n47), .Y(n5) );
  INVX1 U16 ( .A(n10), .Y(n6) );
  INVX2 U17 ( .A(n21), .Y(count_out[0]) );
  AND2X1 U18 ( .A(n70), .B(n34), .Y(n33) );
  INVX1 U19 ( .A(rollover_flag), .Y(n71) );
  INVX1 U20 ( .A(clear), .Y(n28) );
  OR2X2 U21 ( .A(count_enable), .B(clear), .Y(n72) );
  XNOR2X1 U22 ( .A(n79), .B(rollover_val[1]), .Y(n24) );
  NAND2X1 U23 ( .A(n19), .B(n2), .Y(n7) );
  OR2X1 U24 ( .A(n53), .B(n54), .Y(n45) );
  INVX1 U25 ( .A(n67), .Y(count_out[2]) );
  INVX2 U26 ( .A(n18), .Y(n49) );
  AND2X2 U27 ( .A(count_out[2]), .B(n7), .Y(n9) );
  INVX1 U28 ( .A(n9), .Y(n34) );
  INVX2 U29 ( .A(n55), .Y(n10) );
  INVX2 U30 ( .A(n55), .Y(n70) );
  INVX2 U31 ( .A(n46), .Y(count_out[3]) );
  INVX1 U32 ( .A(n60), .Y(count_out[1]) );
  AND2X2 U33 ( .A(count_out[3]), .B(n39), .Y(n18) );
  XNOR2X1 U34 ( .A(n80), .B(rollover_val[0]), .Y(n27) );
  AND2X2 U35 ( .A(n27), .B(n26), .Y(n19) );
  NAND2X1 U36 ( .A(n48), .B(count_out[0]), .Y(n20) );
  INVX2 U37 ( .A(n80), .Y(n21) );
  INVX2 U38 ( .A(n30), .Y(n23) );
  INVX1 U39 ( .A(n72), .Y(n30) );
  INVX2 U40 ( .A(n78), .Y(n67) );
  XOR2X1 U41 ( .A(n67), .B(rollover_val[2]), .Y(n25) );
  NAND2X1 U42 ( .A(n25), .B(n24), .Y(n32) );
  NAND2X1 U43 ( .A(n27), .B(n26), .Y(n31) );
  OAI21X1 U44 ( .A(n32), .B(n31), .C(count_out[1]), .Y(n47) );
  OAI21X1 U45 ( .A(n32), .B(n31), .C(count_out[0]), .Y(n35) );
  INVX2 U46 ( .A(n35), .Y(n56) );
  XOR2X1 U47 ( .A(n56), .B(n5), .Y(n29) );
  NAND2X1 U48 ( .A(n72), .B(n28), .Y(n55) );
  OAI22X1 U49 ( .A(n29), .B(n6), .C(n23), .D(n60), .Y(n43) );
  NAND2X1 U50 ( .A(count_out[2]), .B(n30), .Y(n38) );
  NAND2X1 U51 ( .A(n19), .B(n2), .Y(n39) );
  NAND3X1 U52 ( .A(n33), .B(count_out[1]), .C(n56), .Y(n37) );
  AOI22X1 U53 ( .A(n3), .B(n5), .C(n1), .D(n35), .Y(n36) );
  NAND3X1 U54 ( .A(n38), .B(n37), .C(n36), .Y(n44) );
  NAND3X1 U55 ( .A(n10), .B(n4), .C(n18), .Y(n40) );
  OAI21X1 U56 ( .A(n23), .B(n46), .C(n40), .Y(n54) );
  INVX2 U57 ( .A(n47), .Y(n48) );
  NAND2X1 U58 ( .A(n48), .B(count_out[0]), .Y(n52) );
  NAND3X1 U59 ( .A(count_out[2]), .B(n10), .C(n49), .Y(n51) );
  NAND3X1 U60 ( .A(n18), .B(n70), .C(n52), .Y(n50) );
  OAI21X1 U61 ( .A(n51), .B(n20), .C(n50), .Y(n53) );
  OAI22X1 U62 ( .A(n56), .B(n6), .C(n23), .D(n21), .Y(n42) );
  INVX2 U63 ( .A(rollover_val[2]), .Y(n65) );
  NAND2X1 U64 ( .A(n76), .B(n65), .Y(n64) );
  INVX2 U65 ( .A(n64), .Y(n58) );
  INVX2 U66 ( .A(rollover_val[3]), .Y(n57) );
  NOR2X1 U67 ( .A(n58), .B(n57), .Y(n59) );
  XOR2X1 U68 ( .A(count_out[3]), .B(n59), .Y(n62) );
  XOR2X1 U69 ( .A(n60), .B(n75), .Y(n61) );
  NOR2X1 U70 ( .A(n62), .B(n61), .Y(n63) );
  OAI21X1 U71 ( .A(rollover_val[3]), .B(n64), .C(n63), .Y(n74) );
  XOR2X1 U72 ( .A(rollover_val[0]), .B(count_out[0]), .Y(n69) );
  OAI21X1 U73 ( .A(n76), .B(n65), .C(n64), .Y(n66) );
  XOR2X1 U74 ( .A(n4), .B(n66), .Y(n68) );
  NAND3X1 U75 ( .A(n10), .B(n69), .C(n68), .Y(n73) );
  OAI22X1 U76 ( .A(n74), .B(n73), .C(n23), .D(n71), .Y(n41) );
  NOR2X1 U77 ( .A(rollover_val[1]), .B(rollover_val[0]), .Y(n76) );
  AOI21X1 U78 ( .A(rollover_val[0]), .B(rollover_val[1]), .C(n76), .Y(n75) );
endmodule


module flex_counter_0 ( clk, n_rst, count_enable, clear, rollover_val, 
        count_out, rollover_flag );
  input [3:0] rollover_val;
  output [3:0] count_out;
  input clk, n_rst, count_enable, clear;
  output rollover_flag;
  wire   n87, n88, n89, N3, N5, N7, n1, n2, n3, n4, n5, n6, n8, n10, n17, n18,
         n19, n20, n21, n25, n26, n27, n28, n29, n30, n31, n32, n33, n34, n35,
         n36, n37, n38, n39, n40, n46, n47, n48, n49, n50, n51, n52, n53, n54,
         n55, n56, n57, n58, n59, n60, n61, n62, n63, n64, n65, n66, n67, n68,
         n69, n70, n71, n72, n73, n74, n75, n76, n77, n78, n79, n80, n81;

  DFFSR \f_reg[3]  ( .D(n74), .CLK(clk), .R(n_rst), .S(1'b1), .Q(n87) );
  DFFSR \f_reg[2]  ( .D(n75), .CLK(clk), .R(n_rst), .S(1'b1), .Q(count_out[2])
         );
  DFFSR \f_reg[1]  ( .D(n76), .CLK(clk), .R(n_rst), .S(1'b1), .Q(n88) );
  DFFSR \f_reg[0]  ( .D(n77), .CLK(clk), .R(n_rst), .S(1'b1), .Q(n89) );
  DFFSR rollover_flag_reg ( .D(n78), .CLK(clk), .R(n_rst), .S(1'b1), .Q(
        rollover_flag) );
  OAI21X1 U15 ( .A(n80), .B(n81), .C(n79), .Y(n78) );
  NAND2X1 U16 ( .A(rollover_flag), .B(n68), .Y(n79) );
  BUFX2 U6 ( .A(n64), .Y(n3) );
  INVX2 U9 ( .A(n88), .Y(n6) );
  NAND2X1 U10 ( .A(n25), .B(n21), .Y(n1) );
  INVX2 U11 ( .A(count_out[1]), .Y(n2) );
  INVX1 U12 ( .A(n87), .Y(n63) );
  XNOR2X1 U13 ( .A(n4), .B(n56), .Y(n30) );
  AND2X2 U14 ( .A(count_out[1]), .B(n1), .Y(n4) );
  INVX2 U17 ( .A(n10), .Y(count_out[0]) );
  XNOR2X1 U18 ( .A(n5), .B(n49), .Y(n50) );
  INVX1 U19 ( .A(n52), .Y(n5) );
  XNOR2X1 U20 ( .A(n2), .B(n69), .Y(n65) );
  XNOR2X1 U21 ( .A(n63), .B(n72), .Y(n67) );
  INVX2 U22 ( .A(n6), .Y(count_out[1]) );
  INVX1 U23 ( .A(clear), .Y(n29) );
  INVX1 U24 ( .A(n87), .Y(n8) );
  INVX2 U25 ( .A(n63), .Y(count_out[3]) );
  AND2X2 U26 ( .A(n51), .B(count_out[2]), .Y(n49) );
  INVX2 U27 ( .A(n89), .Y(n10) );
  AND2X1 U28 ( .A(count_out[0]), .B(n3), .Y(n48) );
  XOR2X1 U29 ( .A(n8), .B(rollover_val[3]), .Y(n18) );
  INVX2 U30 ( .A(count_out[0]), .Y(n59) );
  XOR2X1 U31 ( .A(n10), .B(rollover_val[0]), .Y(n17) );
  NAND2X1 U32 ( .A(n18), .B(n17), .Y(n26) );
  INVX2 U33 ( .A(n26), .Y(n25) );
  XOR2X1 U34 ( .A(n6), .B(rollover_val[1]), .Y(n20) );
  INVX2 U35 ( .A(count_out[2]), .Y(n64) );
  XOR2X1 U36 ( .A(n64), .B(rollover_val[2]), .Y(n19) );
  NAND2X1 U37 ( .A(n20), .B(n19), .Y(n27) );
  INVX2 U38 ( .A(n27), .Y(n21) );
  NAND2X1 U39 ( .A(n25), .B(n21), .Y(n51) );
  OAI21X1 U40 ( .A(n27), .B(n26), .C(count_out[0]), .Y(n28) );
  INVX2 U41 ( .A(n28), .Y(n56) );
  OR2X2 U42 ( .A(count_enable), .B(clear), .Y(n57) );
  NAND2X1 U43 ( .A(n57), .B(n29), .Y(n58) );
  OAI22X1 U44 ( .A(n30), .B(n58), .C(n57), .D(n2), .Y(n76) );
  AND2X2 U45 ( .A(rollover_val[2]), .B(count_out[1]), .Y(n47) );
  INVX2 U46 ( .A(rollover_val[3]), .Y(n31) );
  NAND2X1 U47 ( .A(rollover_val[1]), .B(n31), .Y(n33) );
  NAND2X1 U48 ( .A(rollover_val[0]), .B(n63), .Y(n32) );
  OAI21X1 U49 ( .A(n33), .B(n32), .C(count_out[0]), .Y(n40) );
  NAND2X1 U50 ( .A(rollover_val[3]), .B(rollover_val[1]), .Y(n35) );
  NAND2X1 U51 ( .A(count_out[3]), .B(rollover_val[0]), .Y(n34) );
  OAI21X1 U52 ( .A(n35), .B(n34), .C(count_out[1]), .Y(n39) );
  NOR2X1 U53 ( .A(rollover_val[2]), .B(n6), .Y(n37) );
  NOR2X1 U54 ( .A(n10), .B(n64), .Y(n36) );
  NAND2X1 U55 ( .A(n37), .B(n36), .Y(n38) );
  OAI21X1 U56 ( .A(n40), .B(n39), .C(n38), .Y(n46) );
  AOI21X1 U57 ( .A(n48), .B(n47), .C(n46), .Y(n52) );
  OAI22X1 U58 ( .A(n50), .B(n58), .C(n57), .D(n3), .Y(n75) );
  NAND2X1 U59 ( .A(count_out[3]), .B(n1), .Y(n54) );
  NOR2X1 U60 ( .A(n52), .B(n3), .Y(n53) );
  XOR2X1 U61 ( .A(n53), .B(n54), .Y(n55) );
  OAI22X1 U62 ( .A(n55), .B(n58), .C(n57), .D(n63), .Y(n74) );
  OAI22X1 U63 ( .A(n56), .B(n58), .C(n59), .D(n57), .Y(n77) );
  INVX2 U64 ( .A(n57), .Y(n68) );
  INVX2 U65 ( .A(n58), .Y(n62) );
  XOR2X1 U66 ( .A(n59), .B(N3), .Y(n61) );
  INVX2 U67 ( .A(N7), .Y(n60) );
  NAND3X1 U68 ( .A(n60), .B(n61), .C(n62), .Y(n81) );
  XOR2X1 U69 ( .A(n3), .B(N5), .Y(n66) );
  NAND3X1 U70 ( .A(n67), .B(n66), .C(n65), .Y(n80) );
  NOR2X1 U71 ( .A(rollover_val[1]), .B(rollover_val[0]), .Y(n70) );
  AOI21X1 U72 ( .A(rollover_val[0]), .B(rollover_val[1]), .C(n70), .Y(n69) );
  NAND2X1 U73 ( .A(n70), .B(n73), .Y(n71) );
  OAI21X1 U74 ( .A(n70), .B(n73), .C(n71), .Y(N5) );
  NOR2X1 U75 ( .A(n71), .B(rollover_val[3]), .Y(N7) );
  AOI21X1 U76 ( .A(n71), .B(rollover_val[3]), .C(N7), .Y(n72) );
  INVX2 U77 ( .A(rollover_val[2]), .Y(n73) );
  INVX2 U78 ( .A(rollover_val[0]), .Y(N3) );
endmodule


module timer ( clk, n_rst, enable_timer, shift_strobe, packet_done );
  input clk, n_rst, enable_timer;
  output shift_strobe, packet_done;


  flex_counter_1 CTR1 ( .clk(clk), .n_rst(n_rst), .count_enable(enable_timer), 
        .clear(packet_done), .rollover_val({1'b1, 1'b0, 1'b1, 1'b0}), 
        .rollover_flag(shift_strobe) );
  flex_counter_0 CTR2 ( .clk(clk), .n_rst(n_rst), .count_enable(shift_strobe), 
        .clear(packet_done), .rollover_val({1'b1, 1'b0, 1'b0, 1'b1}), 
        .rollover_flag(packet_done) );
endmodule


module flex_stp_sr_NUM_BITS9_SHIFT_MSB0 ( clk, n_rst, shift_enable, serial_in, 
        parallel_out );
  output [8:0] parallel_out;
  input clk, n_rst, shift_enable, serial_in;
  wire   n3, n11, n13, n15, n17, n19, n21, n23, n25, n27, n29, n1, n2, n4, n5,
         n6, n7, n8, n9, n10, n30;

  DFFSR \f_reg[8]  ( .D(n29), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[8]) );
  DFFSR \f_reg[7]  ( .D(n27), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[7]) );
  DFFSR \f_reg[6]  ( .D(n25), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[6]) );
  DFFSR \f_reg[5]  ( .D(n23), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[5]) );
  DFFSR \f_reg[4]  ( .D(n21), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[4]) );
  DFFSR \f_reg[3]  ( .D(n19), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[3]) );
  DFFSR \f_reg[2]  ( .D(n17), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[2]) );
  DFFSR \f_reg[1]  ( .D(n15), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[1]) );
  DFFSR \f_reg[0]  ( .D(n13), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        parallel_out[0]) );
  OAI21X1 U2 ( .A(n30), .B(n1), .C(n3), .Y(n13) );
  NAND2X1 U3 ( .A(parallel_out[0]), .B(n1), .Y(n3) );
  OAI22X1 U4 ( .A(n1), .B(n10), .C(n2), .D(n30), .Y(n15) );
  OAI22X1 U6 ( .A(n1), .B(n9), .C(n2), .D(n10), .Y(n17) );
  OAI22X1 U8 ( .A(n1), .B(n8), .C(n2), .D(n9), .Y(n19) );
  OAI22X1 U10 ( .A(n1), .B(n7), .C(n2), .D(n8), .Y(n21) );
  OAI22X1 U12 ( .A(n1), .B(n6), .C(n2), .D(n7), .Y(n23) );
  OAI22X1 U14 ( .A(n1), .B(n5), .C(n2), .D(n6), .Y(n25) );
  OAI22X1 U16 ( .A(n1), .B(n4), .C(n2), .D(n5), .Y(n27) );
  OAI21X1 U19 ( .A(n2), .B(n4), .C(n11), .Y(n29) );
  NAND2X1 U20 ( .A(serial_in), .B(n2), .Y(n11) );
  INVX2 U5 ( .A(n1), .Y(n2) );
  INVX2 U7 ( .A(shift_enable), .Y(n1) );
  INVX2 U9 ( .A(parallel_out[8]), .Y(n4) );
  INVX2 U11 ( .A(parallel_out[7]), .Y(n5) );
  INVX2 U13 ( .A(parallel_out[6]), .Y(n6) );
  INVX2 U15 ( .A(parallel_out[5]), .Y(n7) );
  INVX2 U17 ( .A(parallel_out[4]), .Y(n8) );
  INVX2 U18 ( .A(parallel_out[3]), .Y(n9) );
  INVX2 U21 ( .A(parallel_out[2]), .Y(n10) );
  INVX2 U31 ( .A(parallel_out[1]), .Y(n30) );
endmodule


module sr_9bit ( clk, n_rst, shift_strobe, serial_in, packet_data, stop_bit );
  output [7:0] packet_data;
  input clk, n_rst, shift_strobe, serial_in;
  output stop_bit;


  flex_stp_sr_NUM_BITS9_SHIFT_MSB0 SHIFT_BLOCK ( .clk(clk), .n_rst(n_rst), 
        .shift_enable(shift_strobe), .serial_in(serial_in), .parallel_out({
        stop_bit, packet_data}) );
endmodule


module stop_bit_chk ( clk, n_rst, sbc_clear, sbc_enable, stop_bit, 
        framing_error );
  input clk, n_rst, sbc_clear, sbc_enable, stop_bit;
  output framing_error;
  wire   n4, n5, n2, n3;

  DFFSR framing_error_reg ( .D(n5), .CLK(clk), .R(n_rst), .S(1'b1), .Q(
        framing_error) );
  NOR2X1 U5 ( .A(sbc_clear), .B(n4), .Y(n5) );
  AOI22X1 U6 ( .A(framing_error), .B(n3), .C(sbc_enable), .D(n2), .Y(n4) );
  INVX2 U3 ( .A(stop_bit), .Y(n2) );
  INVX2 U4 ( .A(sbc_enable), .Y(n3) );
endmodule


module rx_data_buff ( clk, n_rst, load_buffer, packet_data, data_read, rx_data, 
        data_ready, overrun_error );
  input [7:0] packet_data;
  output [7:0] rx_data;
  input clk, n_rst, load_buffer, data_read;
  output data_ready, overrun_error;
  wire   n1, n4, n5, n6, n7, n8, n9, n10, n11, n30, n31, n2, n3, n15, n17, n19,
         n21, n23, n25, n27, n29, n32;

  DFFSR \rx_data_reg[7]  ( .D(n15), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        rx_data[7]) );
  DFFSR \rx_data_reg[6]  ( .D(n17), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        rx_data[6]) );
  DFFSR \rx_data_reg[5]  ( .D(n19), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        rx_data[5]) );
  DFFSR \rx_data_reg[4]  ( .D(n21), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        rx_data[4]) );
  DFFSR \rx_data_reg[3]  ( .D(n23), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        rx_data[3]) );
  DFFSR \rx_data_reg[2]  ( .D(n25), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        rx_data[2]) );
  DFFSR \rx_data_reg[1]  ( .D(n27), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        rx_data[1]) );
  DFFSR \rx_data_reg[0]  ( .D(n29), .CLK(clk), .R(1'b1), .S(n_rst), .Q(
        rx_data[0]) );
  DFFSR data_ready_reg ( .D(n31), .CLK(clk), .R(n_rst), .S(1'b1), .Q(
        data_ready) );
  DFFSR overrun_error_reg ( .D(n30), .CLK(clk), .R(n_rst), .S(1'b1), .Q(
        overrun_error) );
  NOR2X1 U3 ( .A(data_read), .B(n1), .Y(n30) );
  AOI21X1 U4 ( .A(n3), .B(data_ready), .C(overrun_error), .Y(n1) );
  OAI21X1 U5 ( .A(data_read), .B(n32), .C(n2), .Y(n31) );
  AOI22X1 U8 ( .A(rx_data[0]), .B(n2), .C(packet_data[0]), .D(n3), .Y(n4) );
  AOI22X1 U10 ( .A(rx_data[1]), .B(n2), .C(packet_data[1]), .D(n3), .Y(n5) );
  AOI22X1 U12 ( .A(rx_data[2]), .B(n2), .C(packet_data[2]), .D(n3), .Y(n6) );
  AOI22X1 U14 ( .A(rx_data[3]), .B(n2), .C(packet_data[3]), .D(n3), .Y(n7) );
  AOI22X1 U16 ( .A(rx_data[4]), .B(n2), .C(packet_data[4]), .D(n3), .Y(n8) );
  AOI22X1 U18 ( .A(rx_data[5]), .B(n2), .C(packet_data[5]), .D(n3), .Y(n9) );
  AOI22X1 U20 ( .A(rx_data[6]), .B(n2), .C(packet_data[6]), .D(n3), .Y(n10) );
  AOI22X1 U22 ( .A(rx_data[7]), .B(n2), .C(packet_data[7]), .D(n3), .Y(n11) );
  INVX4 U6 ( .A(n2), .Y(n3) );
  INVX4 U7 ( .A(load_buffer), .Y(n2) );
  INVX2 U9 ( .A(n11), .Y(n15) );
  INVX2 U11 ( .A(n10), .Y(n17) );
  INVX2 U13 ( .A(n9), .Y(n19) );
  INVX2 U15 ( .A(n8), .Y(n21) );
  INVX2 U17 ( .A(n7), .Y(n23) );
  INVX2 U19 ( .A(n6), .Y(n25) );
  INVX2 U21 ( .A(n5), .Y(n27) );
  INVX2 U23 ( .A(n4), .Y(n29) );
  INVX2 U34 ( .A(data_ready), .Y(n32) );
endmodule


module rcv_block ( clk, n_rst, serial_in, data_read, rx_data, data_ready, 
        overrun_error, framing_error );
  output [7:0] rx_data;
  input clk, n_rst, serial_in, data_read;
  output data_ready, overrun_error, framing_error;
  wire   start_bit_detected, packet_done, sbc_clear, sbc_enable, load_buffer,
         enable_timer, shift_strobe, stop_bit;
  wire   [7:0] packet_data;

  start_bit_det START ( .clk(clk), .n_rst(n_rst), .serial_in(serial_in), 
        .start_bit_detected(start_bit_detected) );
  rcu RCU ( .clk(clk), .n_rst(n_rst), .start_bit_detected(start_bit_detected), 
        .packet_done(packet_done), .framing_error(framing_error), .sbc_clear(
        sbc_clear), .sbc_enable(sbc_enable), .load_buffer(load_buffer), 
        .enable_timer(enable_timer) );
  timer TIME_CNT ( .clk(clk), .n_rst(n_rst), .enable_timer(enable_timer), 
        .shift_strobe(shift_strobe), .packet_done(packet_done) );
  sr_9bit SHIFT_REG ( .clk(clk), .n_rst(n_rst), .shift_strobe(shift_strobe), 
        .serial_in(serial_in), .packet_data(packet_data), .stop_bit(stop_bit)
         );
  stop_bit_chk STOP_BIT_CHCK ( .clk(clk), .n_rst(n_rst), .sbc_clear(sbc_clear), 
        .sbc_enable(sbc_enable), .stop_bit(stop_bit), .framing_error(
        framing_error) );
  rx_data_buff DATA_BUFFER ( .clk(clk), .n_rst(n_rst), .load_buffer(
        load_buffer), .packet_data(packet_data), .data_read(data_read), 
        .rx_data(rx_data), .data_ready(data_ready), .overrun_error(
        overrun_error) );
endmodule

