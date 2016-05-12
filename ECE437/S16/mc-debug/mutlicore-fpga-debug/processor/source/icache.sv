`include "cpu_types_pkg.vh"
`include "caches_if.vh"
`include "datapath_cache_if.vh"

import cpu_types_pkg::*;

module icache (
	       input logic CLK, nRST,
	       datapath_cache_if.icache dcif,
	       caches_if.icache cif
	       );
   
   logic [3:0] 		   index;
   logic 		   ihit;
   word_t imemload;

   logic 		   iREN;
   
   
   typedef enum logic {IDLE, UPDATE} StateType;
   StateType current_state, next_state;
   
   icacheframe_t [15:0] icacheset;
   assign index = dcif.imemaddr[5:2];

   assign dcif.ihit = ihit;
   assign dcif.imemload = imemload;

   assign cif.iREN = iREN;
   //assign cif.iaddr = dcif.imemaddr;

   always_ff @(posedge CLK, negedge nRST)
     begin
	if (nRST == 0)
	  begin
	     icacheset <= '{default:0};
	     current_state <= IDLE;
	  end
	else if (cif.iwait == 0 && dcif.imemREN == 1)
	  begin
	     icacheset[index].block <= cif.iload;
	     icacheset[index].tag <= dcif.imemaddr[31:6];
	     icacheset[index].valid <= 1;
	     current_state <= next_state;	     
	  end
	else
	  begin
	     icacheset <= icacheset;
	     current_state <= next_state;
	  end
     end // always_ff @

   //next state logic
   always_comb
     begin
	next_state = current_state; //to avoid latch
	case (current_state)
	  IDLE:
	    begin
	       if (dcif.imemREN == 1 && ihit == 0)
		 begin
		    next_state = UPDATE;
		 end
	       else
		 begin
		    next_state = IDLE;
		 end
	    end
	  UPDATE:
	    begin
	       if (cif.iwait == 0)
		 begin
		    next_state = IDLE;
		 end
	       else
		 begin
		    next_state = UPDATE;
		 end
	    end
	endcase // case (current_state)
     end // always_comb


   //output logic
   always_comb
     begin
	ihit = 0;
	iREN = 0;
	imemload = 32'b0;
	case (current_state)
	  IDLE:
	    begin
	       ihit = (icacheset[index].valid == 1) && (icacheset[index].tag == dcif.imemaddr[31:6]);
	       imemload = icacheset[index].block;
	       iREN = 0;
	       cif.iaddr = dcif.imemaddr;
	    end
	  UPDATE:
	    begin
	       ihit = 0;
	       imemload = 32'b0;
	       iREN = 1;
	       cif.iaddr = dcif.imemaddr;
	    end
	endcase // case (current_state)
     end // always_comb
endmodule // icache

	  
   
  
   
   
