/*
  Eric Villasenor
  evillase@gmail.com

  datapath contains register file, control, hazard,
  muxes, and glue logic for processor
*/

// data path interface
`include "datapath_cache_if.vh"
`include "register_file_if.vh"
`include "control_unit_if.vh"
`include "alu_if.vh"
`include "cache_control_if.vh"

// alu op, mips op, and instruction type
`include "cpu_types_pkg.vh"

module datapath (
  input logic CLK, nRST,
  datapath_cache_if.dp dpif
);
   // import types
   import cpu_types_pkg::*;

   // pc init
   parameter PC_INIT = 0;

   //let us instantiate the interfaces to be used
   alu_if aluif();
   register_file_if rfif();
   control_unit_if cuif();

   //now, let us make the signals in the datapath.
   //these will be all the signals in the control unit and the individual blocks
   //control unit signals
   logic      j, jal, jr, beq, bne, cu_halt, RegWrite, dR_REQ, dW_REQ, RegDst, ExtOp, ShiftOp, ALUSrc, MemToReg, lui;
   word_t instruction;//the instruction loaded from the memory
   aluop_t ALUOp;
   //logic      halt; //this is from the request unit to the cache. control unit halt is cu_halt
   logic      negative, zero, overflow;
   logic [15:0] imm16;
   
   word_t pc; //the program counter
   word_t pc_next;//the next program counter
   word_t pc_plus_4;//pc + 4

   logic 	d_halt, d_dhit, d_ihit, d_imemREN, d_dmemREN, d_dmemWEN;//all dummy signals
   assign dpif.halt = d_halt;
   assign d_dhit = dpif.dhit;
   assign d_ihit = dpif.ihit;
   assign dpif.imemREN = d_imemREN;
   assign dpif.dmemREN = d_dmemREN;
   assign dpif.dmemWEN = d_dmemWEN;
   
   //define the interfaces and port connections to various blocks
   alu ALU (aluif);
   register_file REGISTER_FILE (CLK, nRST, rfif);
   control_unit CONTROL_UNIT (cuif);
   request_unit REQUEST_UNIT (.CLK(CLK), .nRST(nRST), .cu_halt(cu_halt), .dR_REQ(dR_REQ), .dW_REQ(dW_REQ), .ihit(d_ihit), .dhit(d_dhit), .halt(d_halt), .imemREN(d_imemREN), .dmemREN(d_dmemREN), .dmemWEN(d_dmemWEN));
   program_counter PROGRAM_COUNTER (.CLK(CLK), .nRST(nRST), .pc_EN(d_ihit), .pc_in(pc_next), .pc_out(pc));
   
   assign instruction = dpif.imemREN ? dpif.imemload : 0;
   assign cuif.imemload = instruction;
   assign imm16 = instruction[15:0];
   assign ALUSrc = cuif.ALUSrc;
   assign j = cuif.j;
   assign jal = cuif.jal;
   assign jr = cuif.jr;
   assign beq = cuif.beq;
   assign bne = cuif.bne;
   assign cu_halt = cuif.halt;
   assign RegWrite = cuif.RegWrite;
   assign dR_REQ = cuif.dR_REQ;
   assign dW_REQ = cuif.dW_REQ;
   assign RegDst = cuif.RegDst;
   assign ExtOp = cuif.ExtOp;
   assign ShiftOp = cuif.ShiftOp;
   assign MemToReg = cuif.MemToReg;
   assign lui = cuif.lui;
   assign ALUOp = cuif.ALUOp;


   word_t MemToReg_output_1, MemToReg_output_2, MemToReg_output;
   regbits_t RegDst_JAL_output_1, RegDst_JAL_output;

   //registers for the register file
   word_t rs_content, rt_content; //store the contents of rs, rt registers
   assign rs_content = rfif.rdat1;
   assign rt_content = rfif.rdat2;
   assign rfif.WEN = RegWrite;
   assign rfif.rsel1 = instruction[25:21];
   assign rfif.rsel2 = instruction[20:16];
   assign rfif.wsel = RegDst_JAL_output;
   assign rfif.wdat = MemToReg_output;

   word_t ALUSrc_output;
   word_t shifted_ALUSrc_output;
   word_t ALU_out;
   
   //alu
   assign aluif.aluOP = ALUOp;
   assign aluif.portA = rs_content;
   //assign aluif.portB = ALUSrc_output;
   assign aluif.portB = shifted_ALUSrc_output; //new statement - to fix sll and srl
   assign negative = aluif.nFlag;
   assign zero = aluif.zFlag;
   assign overflow = aluif.oFlag;
   assign ALU_out = aluif.portO;

   assign dpif.dmemaddr = ALU_out;
   assign dpif.dmemstore = rt_content;

   assign RegDst_JAL_output_1 = RegDst ? instruction[15:11] : instruction[20:16];
   assign RegDst_JAL_output = jal ? {5'b11111} : RegDst_JAL_output_1; //if jal, $31 is the write reg
   
   assign MemToReg_output_1 = MemToReg ? dpif.dmemload : ALU_out;
   assign MemToReg_output_2 = jal ? pc_plus_4 : MemToReg_output_1;
   assign MemToReg_output = lui ? {imm16, 16'b0} : MemToReg_output_2;

   word_t extended_imm16/*, extended_imm16_shifted*/;
   
   assign extended_imm16 = ExtOp ? {{16{imm16[15]}}, imm16} : {16'b0, imm16}; //extend the immediate 16 bits
   logic [31:0]	shamt;
   assign shamt = {27'b0, instruction[10:6]};
   //assign extended_imm16_shifted = ShiftOp ? shamt : extended_imm16;
   //assign ALUSrc_output = ALUSrc ? extended_imm16_shifted : rt_content;

   //new statements - to fix SLL and SRL
   assign ALUSrc_output = ALUSrc ? extended_imm16 : rt_content;
   assign shifted_ALUSrc_output = ShiftOp ? shamt : ALUSrc_output;

   //program counter logic
   assign pc_plus_4 = pc + 32'd4;
   word_t jump_address;
   logic [27:0] intermediate_jump_op;
   assign intermediate_jump_op = instruction[25:0] << 2;
   assign jump_address = {pc_plus_4[31:28], intermediate_jump_op}; //now this will be consecutively muxed with jr and then (jal or j) to decide the pc_next value

   //now, let us generate the branch control signals for its mux
   logic 	branch_mux_control;
   assign branch_mux_control = (zero & beq) | (~zero & bne);
   word_t imm16_sign_extended_1, imm16_sign_extended;
   assign imm16_sign_extended_1 = {{16{imm16[15]}}, imm16};
   //now shift left by 2
   assign imm16_sign_extended = imm16_sign_extended_1 << 2;
   //now add pc+4 with the sign extended and left shifted imm
   word_t branch_add;
   assign branch_add = imm16_sign_extended + pc_plus_4;
   //now the branch muxes
   word_t branch_mux_output;
   assign branch_mux_output = branch_mux_control ? branch_add : pc_plus_4;
   //now the jump muxes
   logic 	jal_or_j;
   assign jal_or_j = jal | j;
   word_t intermediate_jump_mux;
   assign intermediate_jump_mux = jr ? rs_content : branch_mux_output;
   assign pc_next = jal_or_j ? jump_address : intermediate_jump_mux; //this will be the next pc val, which will be clocked to the imemaddr in the next clock cycle
   
   

   assign dpif.imemaddr = pc;
   
	      

endmodule
