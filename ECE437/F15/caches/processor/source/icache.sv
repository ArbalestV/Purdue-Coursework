`include "cache_control_if.vh"
`include "datapath_cache_if.vh"
`include "cpu_types_pkg.vh"

module icache (
	       input logic CLK, nRST,
	       datapath_cache_if dcif,
	       cache_control_if ccif
	       );
   //import types
   import cpu_types_pkg::*;
   
   typedef enum logic {IDLE, UPDATE} StateType;
   icacheframe_t [15:0] frames;
   icachef_t iaddr;
   assign iaddr = dcif.imemaddr;
   logic [3:0] 	index;
   assign index = iaddr.idx;

   StateType current_state, next_state;
   

   //next state logic
   always_comb 
     begin
	next_state = current_state; //to avoid latch
	case (current_state)
	  IDLE: 
	    begin
	       if (dcif.imemREN == 1'b1 && dcif.ihit == 1'b0)
		 begin
		    next_state = UPDATE;
		 end
	       else
		 begin
		    next_state = next_state;
		 end
	    end // case: IDLE
	  UPDATE:
	    begin
	       if (ccif.iwait == 1'b0) //no more wait
		 begin
		    next_state = IDLE;
		 end
	       else //instruction not quite fetched yet
		 begin
		    next_state = UPDATE;
		 end
	    end // case: UPDATE
	endcase // case (current_state)
     end // always_comb

   always_ff @ (posedge CLK, negedge nRST)
     begin
	if (nRST == 0)
	  begin
	     frames <= '{default:0}/*0*/; //initialize all frames to zero
	     current_state <= IDLE;
	  end
	else
	  begin
	     if (dcif.imemREN == 1'b1 && ccif.iwait == 1'b0) //when to load from the ram
	       begin
		  frames[index].valid <= 1'b1;
		  frames[index].tag <= iaddr.tag;
		  frames[index].block.Data <= ccif.iload[0];
		  current_state <= next_state;
	       end
	     else
	       begin
		  frames <= frames;
		  current_state <= next_state;
	       end // else: !if(icif.imemREN == 1'b1 && icif.iwait == 1'b0)
	  end // else: !if(nRST == 0)
     end // always_ff @

   //output logic combinational
   always_comb
     begin
	case(current_state)
	  IDLE:
	    begin
	       dcif.ihit = ((frames[index].valid == 1'b1)  && (frames[index].tag == iaddr.tag)) && ~dcif.dmemREN && ~dcif.dmemWEN; //adding new stuff
	       dcif.imemload = frames[index].block.Data;
	       ccif.iREN = 1'b0;
	       ccif.iaddr[0] = dcif.imemaddr;//does not matter
	    end
	  UPDATE:
	    begin
	       dcif.ihit = 1'b0;
	       dcif.imemload = 32'b0;
	       ccif.iREN = 1'b1;
	       ccif.iaddr[0] = dcif.imemaddr;
	    end
	endcase // case (current_state)
     end // always_comb
endmodule // icache

   
	       
	  
	  
	      
	      
	     
		  
		  
		  
   
