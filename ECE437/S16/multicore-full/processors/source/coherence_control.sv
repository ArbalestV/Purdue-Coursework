`include "cpu_types_pkg.vh"
`include "coherence_control_if.vh"
`include "cache_control_if.vh"
`include "coherence_memory_if.vh"

import cpu_types_pkg::*;
module coherence_control (
			  input logic CLK, nRST, 
			  coherence_control_if.cc cohif,
			  coherence_memory_if.cc cmif,
			  cache_control_if.cc ccif
			  );


   typedef enum 	   logic [2:0] {IDLE, ARB, SNOOP, MEM_P0, MEM_P1, WB0, WB1, UPDATE} StateType;
   StateType current_state, next_state;
   logic [1:0] 		   MSI_serv, req_goto, serv_goto; //10 - M, 01 -S, 00 - I
   logic 		   tag_not_found; //dependent on the dcache
   word_t cacheBlock0; //dependent on the dcache
   word_t cacheBlock1; //dependent on the dcache  

   logic 		   req, serv;
   word_t dmemaddr; //the data address coming in from the requesting cache block
   word_t dataBus_cc; //this will be the bus to transfer data
   
   //next state logic
   always_comb
     begin
	next_state = current_state; //to avoid latch
	case (current_state)
	  IDLE:
	    if (cohif.cctrans_0 == 1 || cohif.cctrans_1 == 1)
	      begin
		 next_state = ARB;
	      end
	    else
	      begin
		 next_state = IDLE;
	      end

	  ARB:
	    next_state = SNOOP;

	  SNOOP:
	    if ((req == 1 && cohif.ccwrite_0 == 1) || (req == 0 && cohif.ccwrite_1 == 1))
	      begin
		 next_state = WB0;
	      end
	    else if ((req == 1 && cohif.ccwrite_0 == 0) || (req == 0 && cohif.ccwrite_1 == 0))
	      begin
		 next_state = MEM_P0;
	      end
	    else
	      begin
		 next_state = SNOOP;
	      end

	  WB0:
	    if ( (serv == 1 && cif1.dwait == 1) || (serv == 0 && cif0.dwait == 1) )
	      begin
		 next_state = WB1;
	      end
	    else
	      begin
		 next_state = WB0;
	      end

	  WB1:
	    if ( (serv == 1 && cif1.dwait == 1) || (serv == 0 && cif0.dwait == 1) )
	      begin
		 next_state = UPDATE;
	      end
	    else
	      begin
		 next_state = WB1;
	      end

	  MEM_P0:
	    if ( (req == 1 && cif1.dwait == 1) || (req == 0 && cif0.dwait == 1) )
	      begin
		 next_state = MEM_P1;
	      end
	    else
	      begin
		 next_state = MEM_P0;
	      end

	  MEM_P1:
	    if ( (req == 1 && cif1.dwait == 1) || (req == 0 && cif0.dwait == 1) )
	      begin
		 next_state = UPDATE;
	      end
	    else
	      begin
		 next_state = MEM_P1;
	      end

	  UPDATE:
	    next_state = IDLE;

	endcase // case (current_state)
	
     end // always_comb


   //output combinational logic
   always_comb
     begin
	//req = 0;
	//serv = 1;
	//dataBus_cc = 32'b0;
	//dmemaddr = 32'b0;
	req_goto = 2'b00;
	serv_goto = 2'b00;
	//the above statements written just to avoid latch
	case(current_state)
	  IDLE:
	    begin
	       cohif.ccwait_0 = 0;
	       cohif.ccwait_1 = 0;
	       cohif.ccinv_0 = 0;
	       cohif.ccinv_1 = 0;
	       cohif.ccsnoopaddr = 32'b0;
	    end
	  
	  ARB:
	    begin
	       if (cohif.cctrans_0 == 1)
		 begin
		    req = 0;
		    serv = 1;
		    dmemaddr = cmif.dmemaddr_1;
		    //dmemaddr = ccif.daddr[0];
		 end
	       else //only comes here if cctrans_0 = 0 and cctrans_1 =1
		 begin
		    req = 1;
		    serv = 0;
		    dmemaddr = cmif.dmemaddr_0;
		    //dmemaddr = ccif.daddr[1];
		 end
	    end // case: ARB
	  
	  SNOOP:
	    begin
	       if (req == 0)
		 begin
		    cohif.ccwait_1 = 1;
		    cohif.ccsnoopaddr = dmemaddr;
		    cohif.ccinv_1 = cohif.ccwrite_0;
		 end
	       else 
		 begin
		    cohif.ccwait_0 = 1;
		    cohif.ccsnoopaddr = dmemaddr;
		    cohif.ccinv_0 = cohif.ccwrite_1;
		 end
	    end // case: SNOOP
	  
	  WB0:
	    begin
	       dataBus_cc = cmif.cacheBlock0;
	    end
	  
	  WB1:
	    begin
	       dataBus_cc = cmif.cacheBlock1;
	    end
	  
	  MEM_P0:
	    begin
	       //since dcache is getting memory values
	    end

	  MEM_P1:
	    begin
	       //since dcache is getting memory values
	    end

	  UPDATE:
	    begin
	       //when $0 is the requestor
	       if (req == 0 && cohif.ccwrite_0 == 1)
		 begin
		    req_goto = 2'b10;
		    serv_goto = 2'b00;
		 end
	       else if (req == 0 && cohif.ccwrite_0 == 0)
		 begin
		    req_goto = 2'b01;
		    if (cohif.cctrans_0 == 1)
		      begin
			 serv_goto = 2'b01; //servicer goes to S when req is making read request
		      end
		 end

	       //when $1 is the requestor
	       else if (req == 1 && cohif.ccwrite_1 == 1)
		 begin
		    req_goto = 2'b10;
		    serv_goto = 2'b00;
		 end
	       else if (req == 1 && cohif.ccwrite_1 == 0)
		 begin
		    req_goto = 2'b01;
		    if (cohif.cctrans_1 == 1)
		      begin
			 serv_goto = 2'b01; //servicer goes to S when req is making read request
		      end
		 end
	    end // case: UPDATE
	endcase // case (current_state)
     end // always_comb


   always_ff @ (posedge CLK, negedge nRST)
     begin
	if (nRST == 0)
	  begin
	     current_state <= IDLE;
	  end
	else
	  begin
	     current_state <= next_state;
	  end
     end // always_ff @


endmodule // coherence_control

