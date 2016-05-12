`include "cpu_types_pkg.vh"

import cpu_types_pkg::*;

module btb (
	    input logic        CLK, nRST,
	    input logic [31:0] pc,
	    input btbset_t btbframes,
	    output logic       btbhit,
	    output 	       word_t jump_add,
	    output logic predicted
	    );
   // import types

   //convention
   //00 - ST
   //01 - WT
   //10 - WNT
   //11 - SNT
   
   //btbset_t btbframes; //the branch target bufer
   /*always_ff @(posedge CLK, negedge nRST) //to initialize the valid bit of the frame to 
     begin
	if (!nRST)
	  begin
	     btbframes.valid <= 0;
	     //the other fields wouldn't matter since valid bi is set to 0
	  end
	else
	  begin
	     btbframes.valid <= btbframes.valid;
	  end
     end*/

   //now we have to check based on the pc if here is a btb hit
   logic [27:0] tag_to_match;
   assign tag_to_match = pc[31:4];
   logic [1:0] 	get_index;
   assign get_index = pc[3:2];
   logic 	is_valid;
   assign is_valid = btbframes.frameblocks[get_index].valid;
   logic 	tag_match;
   assign tag_match = (tag_to_match == btbframes.frameblocks[get_index].tag);
   
   //now check if valid = 1 and thee is a tag hit
   logic 	found;
   assign found = (is_valid == 1'b1) && (tag_match == 1'b1);
/* && ( (btbframes.frameblocks[get_index].curr_state == 2'b00) || (btbframes.frameblocks[get_index].curr_state == 2'b01) );*/
   //found is btbhit
   assign btbhit = found; //this goes to the fetch state. If btbhit == 1 and with the corect sates, ie ST or WT, then pc_next for the fetch state will be the jump_addr at the particular matched frame. Else i will be pc+4 in the Fetch state.
   assign jump_add = btbframes.frameblocks[get_index].jump_add;
// ( (found == 1'b1) && ( (btbframes.frameblocks[get_index].curr_state == 2'b00) || (btbframes.frameblocks[get_index].curr_state == 2'b01) ) ) ? btbframes.frameblocks[get_index].jump_add : (pc + 4);
   assign predicted = ( (found == 1'b1) ) && ( (btbframes.frameblocks[get_index].curr_state == 2'b00) || (btbframes.frameblocks[get_index].curr_state == 2'b01) );
   

endmodule // btb

   

   
   

   
   
