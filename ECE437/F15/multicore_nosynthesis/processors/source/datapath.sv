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
//`include "hazard_unit_if.vh"
//`include "branch_unit_if.vh"

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

   /***************************** INTERFACES *****************************************/
   alu_if aluif();
   register_file_if rfif();
   control_unit_if cuif();
   hazard_unit_if huif();
   branch_unit_if buif();  
   forwarding_unit_if fuif();
   hazard_detection_unit_if hduif();

   //define the interfaces and port connections to various blocks
   alu ALU (aluif);
   register_file REGISTER_FILE (CLK, nRST, rfif);
   control_unit CONTROL_UNIT (cuif);
   hazard_unit HAZARD_UNIT (huif);
   branch_unit BRANCH_UNIT (buif);
   forwarding_unit FORWARDING_UNIT (fuif);
   hazard_detection_unit HAZARD_DETECTION_UNIT (hduif);

   /**************************** DECLARATIONS *****************************************/
   //WB Latch
   logic 	halt_M, halt_EX, halt_WB;
   logic 	datomic_EX, datomic_M;	
   logic      MemToReg_EX, MemToReg_M, MemToReg_WB;
   logic      RegWrite_EX, RegWrite_M, RegWrite_WB;
   logic [15:0] imm16_EX, imm16_M, imm16_WB;
   logic 	jal_EX, jal_M, jal_WB;
   word_t pc_plus_4_EX, pc_plus_4_M, pc_plus_4_WB;
   logic 	lui_EX, lui_M, lui_WB;
   word_t	dmemload_WB; 	

   //M Latch
   logic 	dR_REQ_EX, dR_REQ_M;
   logic 	dW_REQ_EX, dW_REQ_M;
   logic        flushed_M;
   logic 	portA_M, j_M, jr_M;
   logic [31:0] instruction_M, pc_plus_M;

   logic 	is_branch_EX; //if there is a branch and is met with a hazard
   
   

   //EX Latch
   logic 	j_EX;
   logic 	jr_EX;
   aluop_t ALUOp_EX;
   logic 	ShiftOp_EX;
   logic 	ALUSrc_EX;
   logic 	RegDst_EX;
   logic 	ExtOp_EX;
   word_t ALUSrc_output;
   word_t shifted_ALUSrc_output;
   word_t extended_imm16;
   word_t extended_shamt;
   word_t portO_EX;   

   logic 	noop_EX;
   logic 	flushed_de;
   logic 	flushed_EX;
   logic 	pc_plus_EX;


   logic 	stall_LDST;
   
   r_t instr_M, instr_WB;
   
   
   word_t instruction;//the instruction loaded from the memory
   logic      negative, zero, overflow;
   
   word_t pc; //the program counter
   word_t pc_next;//the next program counter
   word_t pc_plus_4;//pc + 4
   word_t      npc;
   

   

   /************************ DATAPATH PIPELINE ******************************************/

   //
   //PIPELINE ENABLER
   //
   logic 	pipe_en, pipe_en_others; //will be our ihit
   assign pipe_en = dpif.ihit /*| ~dpif.dhit*/;
   
   assign pipe_en_others = dpif.dhit | dpif.ihit;

   assign instruction = dpif.imemREN ? dpif.imemload : 0;//the instruction from RAM via cache. This is the previous state of IF/ID latch

   //
   //FETCH
   //
   
   //program counter logic
   
   assign pc_plus_4 = pc + 32'd4;
   assign npc = flushed_de ? pc_next : pc_plus_4;   
   program_counter #(.PC_INIT(PC_INIT))PROGRAM_COUNTER (.CLK(CLK), .nRST(nRST), .pc_EN( (dpif.ihit & ~dpif.dhit & ~noop_EX) || flushed_de), .pc_in(npc), .pc_out(pc)); //program counter has been updated with pc_next as the next value calculated from the EX latch

   regbits_t dummyRt, dummyRs;
   assign dummyRt = instruction[20:16];   
   assign dummyRs = instruction[25:21];
   
   //****************
   //DECODE LATCH
   //****************
   logic [31:0] instruction_D, instruction_EX, pc_plus_4_D; //instruction_EX added newly for lab 6 for use in program counter jump in EX
   word_t MemToReg_output_1, MemToReg_output_2, MemToReg_output;
   regbits_t RegDst_JAL_output_1, RegDst_JAL_output;
   regbits_t RegDst_JAL_output_WB;
   regbits_t dummyRt_DE, dummyRs_DE;
   assign dummyRt_DE = instruction_D[20:16];   
   assign dummyRs_DE = instruction_D[25:21];
   
   word_t ra_content_EX, ra_content_EX1, rb_content_EX, rb_content_EX1;
   logic [4:0] shamt_EX, rt_EX, rd_EX; //rs_EX might be a new addition to check the hazard unit in lab 6
   //logic       RegWrite_EX;
   
   always_ff @ (posedge CLK, negedge nRST) //only at the positive edge of each clock cycle
     begin
	if ( ~nRST ) begin
	   instruction_D <= 0;
	   pc_plus_4_D  <= 0;	   
	end       
	else if (stall_LDST || (noop_EX & ~flushed_de))
	  begin
	     instruction_D <= instruction_D;
	     pc_plus_4_D <= pc_plus_4_D;	     
	  end	  
	else if ( (pipe_en && ~noop_EX & ~flushed_de)  /*| ~dpif.dhit*/) begin //only if the enabler is on
	   instruction_D <= instruction;
	   pc_plus_4_D <= pc_plus_4;	   
	end
	else if (flushed_de)
	  begin
	     instruction_D <= 0;
	     pc_plus_4_D <= 0;	     
	  end
	else if (dpif.dhit & ~dpif.ihit)
	  begin
	     instruction_D <= 0;
	     pc_plus_4_D <= 0;
	  end
     end

   assign cuif.imemload = instruction_D; //control unit input
   
   //Register File Read
   assign rfif.rsel1 = instruction_D[25:21]; //this is the previous state of ID/EX latch
   assign rfif.rsel2 = instruction_D[20:16]; //this is the previous state of ID/EX latch
   
   //Register File Write
   assign rfif.wdat = MemToReg_output; //this will have already incorporated the jal and lui 
   assign rfif.wsel = RegDst_JAL_output_WB;
   assign rfif.WEN = RegWrite_WB;

   //Hazard Detection Unit interace
   assign hduif.ex_dR_REQ = dR_REQ_EX;
   assign hduif.ex_regRt = rt_EX;
   assign hduif.de_regRs = instruction_D[25:21];
   assign hduif.de_regRt = instruction_D[20:16];

   //new line to be added to the datapath of pipeline for remediation
   /* MULTICORE : adding condition for SC to bubble */
   assign noop_EX = ( hduif.stall || (instruction_M[31:26] == 6'b111000 ) || (instruction_EX[31:26] == 6'b111000) ||
		     ((instruction_EX[31:26] == 6'b001101 /*ori*/ || instruction_EX[31:26] == 6'b001100 /*andi*/ || instruction_EX[31:26] == 6'b001000 /*addi*/ || instruction_EX[31:26] == 6'b001001 /*addiu*/
		       || instruction_EX[31:26] == 6'b001010 /*slti*/ || instruction_EX[31:26] == 6'b001011 /*sltiu*/ || instruction_EX[31:26] == 6'b001110 /*xori*/) 
		      && (instruction_D[31:26] == 6'b101011)) )  && pipe_en_others; //noop_EX was becoming high due to the ram accessing, which was causing instructions to be overwritten. Make it dependent on EX pipe enabler /*((instruction_EX[31:26] == 6'b001101) && (instruction_D[31:26] == 6'b101011)) added for multi-core fixing forwarding issue */
   /*    
    //end of new line to be added to the datapath of pipeline for remediation
    
    
   assign hduif.ex_dW_REQ = dW_REQ_EX;
   assign hduif.de_dR_REQ = cuif.dR_REQ;
   assign hduif.de_dW_REQ = cuif.dW_REQ;
   */
   
   //*************  
   // EX LATCH
   //*************
   always_ff @ (posedge CLK, negedge nRST)
     begin
	if ( ~nRST ) begin
	   ra_content_EX1 <= 0;
	   rb_content_EX1 <= 0;
	   shamt_EX <= 0;
	   imm16_EX <= 0;
	   rt_EX <= 0;
	   rd_EX <= 0;
	   MemToReg_EX <= 0;
	   RegWrite_EX <= 0;
	   jal_EX <= 0;
	   lui_EX <= 0;
	   pc_plus_4_EX <= 0;
	   dR_REQ_EX <= 0;
	   dW_REQ_EX <= 0;
	   halt_EX <= 0;
	   j_EX <= 0;
	   jr_EX <= 0;
	   ALUOp_EX <= ALU_SLL;
	   ALUSrc_EX <= 0;
	   ShiftOp_EX <= 0;
	   RegDst_EX <= 0;
	   ExtOp_EX <= 0;
	   instruction_EX <= 0;
	   datomic_EX <= 0;	   
	   is_branch_EX <= 0;
	   
	end
	else begin	
	   /*
	   if (stall_LDST) 
	     begin
		ra_content_EX1 <= ra_content_EX;
		rb_content_EX1 <= rb_content_EX1;
		shamt_EX <= shamt_EX;
		imm16_EX <= imm16_EX;
		rt_EX <= rt_EX;
		rd_EX <= rd_EX;
		MemToReg_EX <= MemToReg_EX;
		RegWrite_EX <= RegWrite_EX;
		jal_EX <= jal_EX;
		lui_EX <= lui_EX;
		pc_plus_4_EX <= pc_plus_4_EX;
		dR_REQ_EX <= dR_REQ_EX;
		dW_REQ_EX <= dW_REQ_EX;
		halt_EX <= halt_EX;
		j_EX <= j_EX;
		jr_EX <= jr_EX;
		ALUOp_EX <= ALUOp_EX;
		ALUSrc_EX <= ALUSrc_EX;
		ShiftOp_EX <= ShiftOp_EX;
		RegDst_EX <= RegDst_EX;	 
  		ExtOp_EX <= ExtOp_EX;
		instruction_EX <= instruction_EX;		
	     end // if (pipe_en_others)	 */ 
	   if ( (pipe_en_others & ~noop_EX & ~flushed_EX) /*| ~dpif.dhit*/)//|| stall_LDST) //dml
	   //if ( (pipe_en_others & ~flushed_EX) /*| ~dpif.dhit*/)//|| stall_LDST)
	     begin
		ra_content_EX1 <= rfif.rdat1;
		rb_content_EX1 <= rfif.rdat2;
		shamt_EX <= instruction_D[10:6];
		imm16_EX <= instruction_D[15:0];
		rt_EX <= instruction_D[20:16];
		rd_EX <= instruction_D[15:11];
		MemToReg_EX <= cuif.MemToReg;
		RegWrite_EX <= cuif.RegWrite & (dpif.dhit | dpif.ihit);
		jal_EX <= cuif.jal;
		lui_EX <= cuif.lui;
		pc_plus_4_EX <= pc_plus_4_D;
		dR_REQ_EX <= cuif.dR_REQ;
		dW_REQ_EX <= cuif.dW_REQ;
		halt_EX <= cuif.halt;
		j_EX <= cuif.j;
		jr_EX <= cuif.jr;
		ALUOp_EX <= cuif.ALUOp;
		ALUSrc_EX <= cuif.ALUSrc;
		ShiftOp_EX <= cuif.ShiftOp;
		RegDst_EX <= cuif.RegDst;	 
  		ExtOp_EX <= cuif.ExtOp;
		datomic_EX <= cuif.datomic;		
		instruction_EX <= instruction_D;

		is_branch_EX <= cuif.beq || cuif.bne;
		
	     end // if (pipe_en_others)
	   if (noop_EX || flushed_EX) 
	     begin
		ra_content_EX1 <= 0;
		rb_content_EX1 <= 0;
		shamt_EX <= 0;
		imm16_EX <= 0;
		rt_EX <= 0;
		rd_EX <= 0;
		MemToReg_EX <= 0;
		RegWrite_EX <= 0;
		jal_EX <= 0;
		lui_EX <= 0;
		pc_plus_4_EX <= 0;
		dR_REQ_EX <= 0;
		dW_REQ_EX <= 0;
		halt_EX <= 0;
		j_EX <= 0;
		jr_EX <= 0;
		ALUOp_EX <= ALU_SLL;
		ALUSrc_EX <= 0;
		ShiftOp_EX <= 0;
		RegDst_EX <= 0;
		ExtOp_EX <= 0;
		instruction_EX <= 0;
		datomic_EX <= 0;		

		is_branch_EX <= 0;
		
	     end // if (noop_EX || flushed_EX)	   
	   if (stall_LDST) 
	     begin
		ra_content_EX1 <= ra_content_EX1;
		rb_content_EX1 <= rb_content_EX1;
		shamt_EX <= shamt_EX;
		imm16_EX <= imm16_EX;
		rt_EX <= rt_EX;
		rd_EX <= rd_EX;
		MemToReg_EX <= MemToReg_EX;
		RegWrite_EX <= RegWrite_EX;
		jal_EX <= jal_EX;
		lui_EX <= lui_EX;
		pc_plus_4_EX <= pc_plus_4_EX;
		dR_REQ_EX <= dR_REQ_EX;
		dW_REQ_EX <= dW_REQ_EX;
		halt_EX <= halt_EX;
		j_EX <= j_EX;
		jr_EX <= jr_EX;
		ALUOp_EX <= ALUOp_EX;
		ALUSrc_EX <= ALUSrc_EX;
		ShiftOp_EX <= ShiftOp_EX;
		RegDst_EX <= RegDst_EX;	 
  		ExtOp_EX <= ExtOp_EX;
		instruction_EX <= instruction_EX;
		datomic_EX <= datomic_EX;		

		is_branch_EX <= is_branch_EX;
		
	     end // if (pipe_en_others)	  
	end
     end //include rt_EX, rd_EX

   assign extended_shamt = {27'b0, shamt_EX};
   assign extended_imm16 = ExtOp_EX ? {{16{imm16_EX[15]}}, imm16_EX} : {16'b0, imm16_EX};
   
   //MUX 1
   assign RegDst_JAL_output_1 = RegDst_EX ? rd_EX : rt_EX;
   assign RegDst_JAL_output = jal_EX ? {5'b11111} : RegDst_JAL_output_1; //if jal, $31 is the write reg
   
   //MUX 2
   assign ALUSrc_output = ALUSrc_EX ? extended_imm16 : rb_content_EX1;
   assign shifted_ALUSrc_output = ShiftOp_EX ? extended_shamt : ALUSrc_output; 
   
   //alu
   assign aluif.aluOP = ALUOp_EX;
   //assign aluif.portA = ra_content_EX;
   //assign aluif.portB = shifted_ALUSrc_output; //TODO - to fix sll and srl
   assign negative = aluif.nFlag;
   
   assign overflow = aluif.oFlag;

   //only for LUI overwrite it
   assign portO_EX = lui_EX ? {imm16_EX, 16'b0} : aluif.portO;

   //for SW hazard controlling

   word_t porto_M, porto_WB;
   //word_t dmemload_Mem; //this is for initiating the stall during the LW memory read phase
   word_t rb_content_M;
   regbits_t RegDst_JAL_output_M;
   regbits_t Dummy_rs_EX;
   assign Dummy_rs_EX = instruction_EX[25:21];

   //FORWARDING UNIT CODE
   assign fuif.de_regRt = instruction_D[20:16];   
   assign fuif.ex_regRt = rt_EX;
   assign fuif.ex_regRs = instruction_EX[25:21];
   assign fuif.mem_regRd = RegDst_JAL_output_M;
   assign fuif.wb_regRd = RegDst_JAL_output_WB;
   assign fuif.mem_RegWrite = RegWrite_M;
   assign fuif.wb_RegWrite = RegWrite_WB;
   assign fuif.dWEN = dW_REQ_EX;
   assign fuif.dREN = dR_REQ_EX;   
   assign fuif.isLUI_EX = lui_EX;
   assign fuif.isIType = ((instruction_EX[31:26] != 6'b000000 ) &&  
			  (instruction_EX[31:26] != 6'b000011 ) &&
			  (instruction_EX[31:26] != 6'b000010 )) ?  1 : 0;

   assign fuif.is_branch = is_branch_EX; //the new controller signal signifying branches, separating from itype in general. Otherwise could have included two other BEQ and BNE opcodes to the above conditional assignment
   
  
   //MUX portA - forwarding
   always_comb begin
      if (fuif.ForwardA == 3'b100) begin
	 aluif.portA = pc_plus_4_M;	 
      end
      else if (fuif.ForwardA == 3'b011) begin
	 aluif.portA = pc_plus_4_WB;	 
      end
      else if ( fuif.ForwardA == 3'b010 ) begin
	 aluif.portA = porto_M;	 
      end
      else if (fuif.ForwardA == 3'b001) begin
	 aluif.portA = MemToReg_output;	 
      end
      else begin
	 aluif.portA = ra_content_EX;
      end	       
   end
   //MUX portB - forwarding
   always_comb begin
      if (fuif.ForwardB == 3'b100) begin
	 aluif.portB = pc_plus_4_M;	 
      end
      else if (fuif.ForwardB == 3'b011) begin
	 aluif.portB = pc_plus_4_WB;	 
      end
      else if ( fuif.ForwardB == 3'b010 ) begin
	 aluif.portB = porto_M;	 
      end
      else if (fuif.ForwardB == 3'b001) begin
	 aluif.portB = MemToReg_output;	 
      end
      else begin
	 aluif.portB = shifted_ALUSrc_output;
      end	       
   end
  //MUX rb_content_M - forwarding
   //assign rb_content_EX = fuif.stCntl ? porto_M : rb_content_EX1;
   always_comb begin
      if(fuif.stCntl == 2'b01) begin
	 rb_content_EX = porto_M;	 
      end
      else if (fuif.stCntl == 2'b10) begin
	 rb_content_EX = porto_WB;	 
      end
      else begin
	 rb_content_EX = rb_content_EX1;	 
      end
   end // always_comb

   /*
    always_comb begin
      if(fuif.stCntl2 == 2'b01) begin
	 ra_content_EX = porto_M;	 
      end
      else if (fuif.stCntl2 == 2'b10) begin
	 ra_content_EX = porto_WB;	 
      end
      else begin
	 ra_content_EX = rb_content_EX1;	 
      end
   end*/
   assign ra_content_EX = fuif.stCntl2 ? porto_M : ra_content_EX1;
   
   //*************************
   //M LATCH
   //*************************

   always_ff @ (posedge CLK, negedge nRST)
     begin
	if ( ~nRST ) begin
	   porto_M <= 0;
	   RegWrite_M <= 0;
	   imm16_M <= 0;
	   rb_content_M <= 0;
	   MemToReg_M <= 0;
	   jal_M <= 0;
	   lui_M <= 0;
	   pc_plus_4_M <= 0;
	   dR_REQ_M <= 0;
	   dW_REQ_M <= 0;
	   halt_M <= 0;
	   datomic_M <= 0;	   
	   RegDst_JAL_output_M <= 0;
	   portA_M <= 0; //port A -> to do branch in the Mem stage
	   instruction_M <= 0;
	   pc_plus_M <= 0;
	   imm16_M <= 0;
	   jal_M <= 0;
	   j_M <= 0;
	   jr_M <= 0;
	   zero <= 0;
	end // if ( ~nRST )
	else 
	  begin
	   if ( (~dpif.halt & pipe_en_others & ~flushed_M) /*| ~dpif.dhit*/) 
	     begin
		porto_M <= portO_EX;
		imm16_M <= imm16_EX;
		rb_content_M <= rb_content_EX;
		MemToReg_M <= MemToReg_EX;
		RegWrite_M <= RegWrite_EX;
		jal_M <= jal_EX;
		lui_M <= lui_EX;
		pc_plus_4_M <= pc_plus_4_EX;
		dR_REQ_M <= dR_REQ_EX;
		dW_REQ_M <= dW_REQ_EX;
		halt_M <= halt_EX;
		datomic_M <= datomic_EX;		
		RegDst_JAL_output_M <= RegDst_JAL_output;
		portA_M <= aluif.portA; //port A -> to do branch in the Mem stage
		instruction_M <= instruction_EX;
		pc_plus_M <= pc_plus_EX;
		imm16_M <= imm16_EX;
		jal_M <= jal_EX;
		j_M <= j_EX;
		jr_M <= jr_EX;	
		zero <= aluif.zFlag;
	     end // if (pipe_en_others)
	   if ( ~dpif.halt & flushed_M /*|| stall_LDST*/ ) 
	     begin
		porto_M <= 0;
		RegWrite_M <= 0;
		imm16_M <= 0;
		rb_content_M <= 0;
		MemToReg_M <= 0;
		jal_M <= 0;
		lui_M <= 0;
		pc_plus_4_M <= 0;
		dR_REQ_M <= 0;
		dW_REQ_M <= 0;
		halt_M <= 0;
		datomic_M <= 0;		
		RegDst_JAL_output_M <= 0;
		portA_M <= 0; //port A -> to do branch in the Mem stage
		instruction_M <= 0;
		pc_plus_M <= 0;
		imm16_M <= 0;
		jal_M <= 0;
		j_M <= 0;
		jr_M <= 0;
		zero <= 0;
	     end
	  end // else: !if( ~nRST )
     end // always_ff @ 
   
   //cache
   assign dpif.dmemREN = dR_REQ_M;
   assign dpif.dmemWEN = dW_REQ_M;
   assign dpif.dmemaddr = porto_M;
   assign dpif.dmemstore = rb_content_M;
   assign dpif.imemaddr = pc;
   assign dpif.imemREN = 1'b1;
   assign dpif.datomic = datomic_M;   

   ////***********************************************************************************
   //now, we will execute the branch and jal/jr/j program counter combinational logic
   
   word_t jump_address;
   logic [27:0] intermediate_jump_op;
   assign intermediate_jump_op = instruction_M[25:0] << 2; //instruction_EX is a new flip-flop that takes in instruction_D
   assign jump_address = {pc_plus_4_M[31:28], intermediate_jump_op}; //now this will be consecutively muxed with jr and then (jal or j) to decide the pc_next value
   
   //now we have the buif.brTgt as storing the 32-bit address to be added to the pc + 4
   word_t imm16_sign_extended_1, imm16_sign_extended;
   assign imm16_sign_extended_1 = {{16{imm16_M[15]}}, imm16_M};
   //now shift left by 2
   assign imm16_sign_extended = imm16_sign_extended_1 << 2;
   word_t branch_add; //this is where the pc goes in case of branch
   assign branch_add = imm16_sign_extended + pc_plus_4_M; //this is where the program counter should go in a branch
   //now the branch muxes
   word_t branch_mux_output;
   logic 	branch_mux_control;
   assign branch_mux_control = (( zero && (instruction_M[31:26] == 6'b000100 )) ||
				(~zero && (instruction_M[31:26] == 6'b000101 )) );
   assign branch_mux_output = branch_mux_control ? branch_add : pc_plus_4_M;
   //now the jump muxes
   logic 	jal_or_j;
   assign jal_or_j = jal_M | j_M;
   word_t intermediate_jump_mux;
   assign intermediate_jump_mux = jr_M ? porto_M : branch_mux_output; //before portA_M
   assign pc_next = jal_or_j ? jump_address : intermediate_jump_mux; //this will be the next pc val, which will be clocked to the imemaddr in the next clock cycle

   assign flushed_de = ( ( ( zero && (instruction_M[31:26] == 6'b000100 )) || 
			 (~zero && (instruction_M[31:26] == 6'b000101 )) ||
		         (jal_or_j) ||
                         ( jr_M  ) ) ? 1 : 0) && pipe_en; //flush decode when jump or branch
   
   assign flushed_EX = ( ( ( zero && (instruction_M[31:26] == 6'b000100 )) || 
			 (~zero && (instruction_M[31:26] == 6'b000101 )) ||
		         (jal_or_j) ||
                         ( jr_M  ) ) ? 1 : 0) && pipe_en_others; //flush execute when jump or branch

   assign flushed_M = ( ( ( zero && (instruction_M[31:26] == 6'b000100 )) || 
			 (~zero && (instruction_M[31:26] == 6'b000101 )) ||
		         (jal_or_j) ||
                         ( jr_M  ) ) ? 1 : 0) && pipe_en_others; //flush execute when jump or branch
    
   ////////////********************************************************************************
   
   assign stall_LDST = dR_REQ_M;
   
   /*
    assign stall_LDST = ( (dR_REQ_M && dR_REQ_EX) ||
			 (dR_REQ_M && dW_REQ_EX) ||
			 (dW_REQ_M && dR_REQ_EX) ||
			 (dW_REQ_M && dW_REQ_EX) );
    */
   
   
   //***********************
   //WB Latch
   //***********************

   always_ff @ (posedge CLK, negedge nRST)
     begin
	if (~nRST)
	  begin
	     halt_WB <= 0;
	     MemToReg_WB <= 0;
	     RegWrite_WB <= 0;
	     imm16_WB <= 0;
	     jal_WB <= 0;
	     pc_plus_4_WB <= 0;
	     lui_WB <= 0;
	     dmemload_WB <= 0;
	     porto_WB <= 0;
	     RegDst_JAL_output_WB <= 0;
	     instr_WB <= 0;
	  end
	else begin 
	   if ((pipe_en_others && ~dpif.halt)  /*|| ~dpif.dhit*/)
	     begin
		halt_WB <= halt_M;
		MemToReg_WB <= MemToReg_M;
		RegWrite_WB <= RegWrite_M;
		imm16_WB <= imm16_M;
		jal_WB <= jal_M;
		pc_plus_4_WB <= pc_plus_4_M;
		lui_WB <= lui_M;
		dmemload_WB <= dpif.dmemload;
		porto_WB <= porto_M;	  
		RegDst_JAL_output_WB <= RegDst_JAL_output_M; 
		instr_WB <= instr_M;
	     end // if (pipe_en_others)
	end // else: !if(~nRST)
     end // always_ff @

   //assign dpif.halt = halt_WB; ///->new code added to fix synthesis
   logic tmp_flush;
   //assign tmp_flush = halt_WB;
   
   /*to fix synthesis*/
   always_ff @ (posedge CLK, negedge nRST)
     begin
	if (~nRST)
	  begin
	     tmp_flush <= 0;
	  end
	else if(halt_WB)
	  begin
	     tmp_flush <= 1;
	  end
     end

   assign dpif.halt = tmp_flush;
   
   
   assign MemToReg_output_1 = MemToReg_WB ? dmemload_WB : porto_WB;
   assign MemToReg_output_2 = jal_WB ? pc_plus_4_WB : MemToReg_output_1;
   assign MemToReg_output = lui_WB ? {imm16_WB, 16'b0} : MemToReg_output_2; 	      

   opcode_t     d_instr_DE, d_instr_EX, d_instr_M;   
   assign d_instr_DE = opcode_t'(instruction_D[31:26]);
   assign d_instr_EX = opcode_t'(instruction_EX[31:26]);
   assign d_instr_M  = opcode_t'(instruction_M[31:26]);
   assign instr_M = r_t'(instruction_M);
  
   
endmodule
