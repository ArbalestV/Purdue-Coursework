// 337 TA Provided Lab 2 8-bit adder wrapper file template
// This code serves as a template for the 8-bit adder design wrapper file 
// STUDENT: Replace this message and the above header section with an
// appropriate header based on your other code files

module adder_1bit
(
	input a,
	input b,
	input wire carry_in,
	output wire sum,
	output wire carry_out
);

assign sum = carry_in ^ (a ^ b);
assign carry_out = ((~carry_in) & b & a) | (carry_in & (b | a));
	
endmodule
