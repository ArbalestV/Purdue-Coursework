// Copyright (C) 1991-2013 Altera Corporation
// Your use of Altera Corporation's design tools, logic functions 
// and other software and tools, and its AMPP partner logic 
// functions, and any output files from any of the foregoing 
// (including device programming or simulation files), and any 
// associated documentation or information are expressly subject 
// to the terms and conditions of the Altera Program License 
// Subscription Agreement, Altera MegaCore Function License 
// Agreement, or other applicable license agreement, including, 
// without limitation, that your use is for the sole purpose of 
// programming logic devices manufactured by Altera and sold by 
// Altera or its authorized distributors.  Please refer to the 
// applicable agreement for further details.

// VENDOR "Altera"
// PROGRAM "Quartus II 32-bit"
// VERSION "Version 13.0.1 Build 232 06/12/2013 Service Pack 1 SJ Full Version"

// DATE "01/18/2016 13:46:27"

// 
// Device: Altera EP4CE115F29C8 Package FBGA780
// 

// 
// This Verilog file should be used for ModelSim (Verilog) only
// 

`timescale 1 ps/ 1 ps

module test (
	CLK,
	nRST,
	down,
	value);
input 	CLK;
input 	nRST;
input 	down;
output 	[3:0] value;

// Design Ports Information
// value[0]	=>  Location: PIN_E27,	 I/O Standard: 2.5 V,	 Current Strength: Default
// value[1]	=>  Location: PIN_AE15,	 I/O Standard: 2.5 V,	 Current Strength: Default
// value[2]	=>  Location: PIN_AD15,	 I/O Standard: 2.5 V,	 Current Strength: Default
// value[3]	=>  Location: PIN_AH17,	 I/O Standard: 2.5 V,	 Current Strength: Default
// CLK	=>  Location: PIN_J1,	 I/O Standard: 2.5 V,	 Current Strength: Default
// nRST	=>  Location: PIN_Y2,	 I/O Standard: 2.5 V,	 Current Strength: Default
// down	=>  Location: PIN_AC15,	 I/O Standard: 2.5 V,	 Current Strength: Default


wire gnd;
wire vcc;
wire unknown;

assign gnd = 1'b0;
assign vcc = 1'b1;
assign unknown = 1'bx;

tri1 devclrn;
tri1 devpor;
tri1 devoe;
wire \CLK~input_o ;
wire \CLK~inputclkctrl_outclk ;
wire \value[1]~0_combout ;
wire \nRST~input_o ;
wire \nRST~inputclkctrl_outclk ;
wire \value[1]~reg0_Duplicate_1_q ;
wire \value[1]~reg0_q ;
wire \down~input_o ;
wire \value[2]~reg0_Duplicate_1_q ;
wire \Add1~0_combout ;
wire \value[2]~reg0_q ;
wire \value[3]~reg0_Duplicate_1_q ;
wire \Add1~1_combout ;
wire \value[3]~reg0_q ;


// Location: IOOBUF_X115_Y57_N16
cycloneive_io_obuf \value[0]~output (
	.i(gnd),
	.oe(vcc),
	.seriesterminationcontrol(16'b0000000000000000),
	.devoe(devoe),
	.o(value[0]),
	.obar());
// synopsys translate_off
defparam \value[0]~output .bus_hold = "false";
defparam \value[0]~output .open_drain_output = "false";
// synopsys translate_on

// Location: IOOBUF_X60_Y0_N9
cycloneive_io_obuf \value[1]~output (
	.i(\value[1]~reg0_q ),
	.oe(vcc),
	.seriesterminationcontrol(16'b0000000000000000),
	.devoe(devoe),
	.o(value[1]),
	.obar());
// synopsys translate_off
defparam \value[1]~output .bus_hold = "false";
defparam \value[1]~output .open_drain_output = "false";
// synopsys translate_on

// Location: IOOBUF_X60_Y0_N16
cycloneive_io_obuf \value[2]~output (
	.i(\value[2]~reg0_q ),
	.oe(vcc),
	.seriesterminationcontrol(16'b0000000000000000),
	.devoe(devoe),
	.o(value[2]),
	.obar());
// synopsys translate_off
defparam \value[2]~output .bus_hold = "false";
defparam \value[2]~output .open_drain_output = "false";
// synopsys translate_on

// Location: IOOBUF_X62_Y0_N16
cycloneive_io_obuf \value[3]~output (
	.i(\value[3]~reg0_q ),
	.oe(vcc),
	.seriesterminationcontrol(16'b0000000000000000),
	.devoe(devoe),
	.o(value[3]),
	.obar());
// synopsys translate_off
defparam \value[3]~output .bus_hold = "false";
defparam \value[3]~output .open_drain_output = "false";
// synopsys translate_on

// Location: IOIBUF_X0_Y36_N8
cycloneive_io_ibuf \CLK~input (
	.i(CLK),
	.ibar(gnd),
	.o(\CLK~input_o ));
// synopsys translate_off
defparam \CLK~input .bus_hold = "false";
defparam \CLK~input .simulate_z_as = "z";
// synopsys translate_on

// Location: CLKCTRL_G2
cycloneive_clkctrl \CLK~inputclkctrl (
	.ena(vcc),
	.inclk({vcc,vcc,vcc,\CLK~input_o }),
	.clkselect(2'b00),
	.devclrn(devclrn),
	.devpor(devpor),
	.outclk(\CLK~inputclkctrl_outclk ));
// synopsys translate_off
defparam \CLK~inputclkctrl .clock_type = "global clock";
defparam \CLK~inputclkctrl .ena_register_mode = "none";
// synopsys translate_on

// Location: LCCOMB_X61_Y1_N24
cycloneive_lcell_comb \value[1]~0 (
// Equation(s):
// \value[1]~0_combout  = !\value[1]~reg0_Duplicate_1_q 

	.dataa(gnd),
	.datab(gnd),
	.datac(\value[1]~reg0_Duplicate_1_q ),
	.datad(gnd),
	.cin(gnd),
	.combout(\value[1]~0_combout ),
	.cout());
// synopsys translate_off
defparam \value[1]~0 .lut_mask = 16'h0F0F;
defparam \value[1]~0 .sum_lutc_input = "datac";
// synopsys translate_on

// Location: IOIBUF_X0_Y36_N15
cycloneive_io_ibuf \nRST~input (
	.i(nRST),
	.ibar(gnd),
	.o(\nRST~input_o ));
// synopsys translate_off
defparam \nRST~input .bus_hold = "false";
defparam \nRST~input .simulate_z_as = "z";
// synopsys translate_on

// Location: CLKCTRL_G4
cycloneive_clkctrl \nRST~inputclkctrl (
	.ena(vcc),
	.inclk({vcc,vcc,vcc,\nRST~input_o }),
	.clkselect(2'b00),
	.devclrn(devclrn),
	.devpor(devpor),
	.outclk(\nRST~inputclkctrl_outclk ));
// synopsys translate_off
defparam \nRST~inputclkctrl .clock_type = "global clock";
defparam \nRST~inputclkctrl .ena_register_mode = "none";
// synopsys translate_on

// Location: FF_X61_Y1_N25
dffeas \value[1]~reg0_Duplicate_1 (
	.clk(\CLK~inputclkctrl_outclk ),
	.d(\value[1]~0_combout ),
	.asdata(vcc),
	.clrn(\nRST~inputclkctrl_outclk ),
	.aload(gnd),
	.sclr(gnd),
	.sload(gnd),
	.ena(vcc),
	.devclrn(devclrn),
	.devpor(devpor),
	.q(\value[1]~reg0_Duplicate_1_q ),
	.prn(vcc));
// synopsys translate_off
defparam \value[1]~reg0_Duplicate_1 .is_wysiwyg = "true";
defparam \value[1]~reg0_Duplicate_1 .power_up = "low";
// synopsys translate_on

// Location: DDIOOUTCELL_X60_Y0_N11
dffeas \value[1]~reg0 (
	.clk(\CLK~inputclkctrl_outclk ),
	.d(!\value[1]~reg0_Duplicate_1_q ),
	.asdata(vcc),
	.clrn(\nRST~inputclkctrl_outclk ),
	.aload(gnd),
	.sclr(gnd),
	.sload(gnd),
	.ena(vcc),
	.devclrn(devclrn),
	.devpor(devpor),
	.q(\value[1]~reg0_q ),
	.prn(vcc));
// synopsys translate_off
defparam \value[1]~reg0 .is_wysiwyg = "true";
defparam \value[1]~reg0 .power_up = "low";
// synopsys translate_on

// Location: IOIBUF_X60_Y0_N22
cycloneive_io_ibuf \down~input (
	.i(down),
	.ibar(gnd),
	.o(\down~input_o ));
// synopsys translate_off
defparam \down~input .bus_hold = "false";
defparam \down~input .simulate_z_as = "z";
// synopsys translate_on

// Location: FF_X61_Y1_N27
dffeas \value[2]~reg0_Duplicate_1 (
	.clk(\CLK~inputclkctrl_outclk ),
	.d(\Add1~0_combout ),
	.asdata(vcc),
	.clrn(\nRST~inputclkctrl_outclk ),
	.aload(gnd),
	.sclr(gnd),
	.sload(gnd),
	.ena(vcc),
	.devclrn(devclrn),
	.devpor(devpor),
	.q(\value[2]~reg0_Duplicate_1_q ),
	.prn(vcc));
// synopsys translate_off
defparam \value[2]~reg0_Duplicate_1 .is_wysiwyg = "true";
defparam \value[2]~reg0_Duplicate_1 .power_up = "low";
// synopsys translate_on

// Location: LCCOMB_X61_Y1_N26
cycloneive_lcell_comb \Add1~0 (
// Equation(s):
// \Add1~0_combout  = \down~input_o  $ (\value[2]~reg0_Duplicate_1_q  $ (\value[1]~reg0_Duplicate_1_q ))

	.dataa(gnd),
	.datab(\down~input_o ),
	.datac(\value[2]~reg0_Duplicate_1_q ),
	.datad(\value[1]~reg0_Duplicate_1_q ),
	.cin(gnd),
	.combout(\Add1~0_combout ),
	.cout());
// synopsys translate_off
defparam \Add1~0 .lut_mask = 16'hC33C;
defparam \Add1~0 .sum_lutc_input = "datac";
// synopsys translate_on

// Location: DDIOOUTCELL_X60_Y0_N18
dffeas \value[2]~reg0 (
	.clk(\CLK~inputclkctrl_outclk ),
	.d(\Add1~0_combout ),
	.asdata(vcc),
	.clrn(\nRST~inputclkctrl_outclk ),
	.aload(gnd),
	.sclr(gnd),
	.sload(gnd),
	.ena(vcc),
	.devclrn(devclrn),
	.devpor(devpor),
	.q(\value[2]~reg0_q ),
	.prn(vcc));
// synopsys translate_off
defparam \value[2]~reg0 .is_wysiwyg = "true";
defparam \value[2]~reg0 .power_up = "low";
// synopsys translate_on

// Location: FF_X61_Y1_N29
dffeas \value[3]~reg0_Duplicate_1 (
	.clk(\CLK~inputclkctrl_outclk ),
	.d(\Add1~1_combout ),
	.asdata(vcc),
	.clrn(\nRST~inputclkctrl_outclk ),
	.aload(gnd),
	.sclr(gnd),
	.sload(gnd),
	.ena(vcc),
	.devclrn(devclrn),
	.devpor(devpor),
	.q(\value[3]~reg0_Duplicate_1_q ),
	.prn(vcc));
// synopsys translate_off
defparam \value[3]~reg0_Duplicate_1 .is_wysiwyg = "true";
defparam \value[3]~reg0_Duplicate_1 .power_up = "low";
// synopsys translate_on

// Location: LCCOMB_X61_Y1_N28
cycloneive_lcell_comb \Add1~1 (
// Equation(s):
// \Add1~1_combout  = \value[3]~reg0_Duplicate_1_q  $ (((\value[2]~reg0_Duplicate_1_q  & (!\down~input_o  & \value[1]~reg0_Duplicate_1_q )) # (!\value[2]~reg0_Duplicate_1_q  & (\down~input_o  & !\value[1]~reg0_Duplicate_1_q ))))

	.dataa(\value[2]~reg0_Duplicate_1_q ),
	.datab(\down~input_o ),
	.datac(\value[3]~reg0_Duplicate_1_q ),
	.datad(\value[1]~reg0_Duplicate_1_q ),
	.cin(gnd),
	.combout(\Add1~1_combout ),
	.cout());
// synopsys translate_off
defparam \Add1~1 .lut_mask = 16'hD2B4;
defparam \Add1~1 .sum_lutc_input = "datac";
// synopsys translate_on

// Location: DDIOOUTCELL_X62_Y0_N18
dffeas \value[3]~reg0 (
	.clk(\CLK~inputclkctrl_outclk ),
	.d(\Add1~1_combout ),
	.asdata(vcc),
	.clrn(\nRST~inputclkctrl_outclk ),
	.aload(gnd),
	.sclr(gnd),
	.sload(gnd),
	.ena(vcc),
	.devclrn(devclrn),
	.devpor(devpor),
	.q(\value[3]~reg0_q ),
	.prn(vcc));
// synopsys translate_off
defparam \value[3]~reg0 .is_wysiwyg = "true";
defparam \value[3]~reg0 .power_up = "low";
// synopsys translate_on

endmodule
