
`include "caches_if.vh"
`include "datapath_cache_if.vh"
`include "cpu_types_pkg.vh"

module dcache (
	       input logic CLK, nRST,
	       datapath_cache_if.dcache dcif,
	       caches_if.dcache cif
	       );
   //import types
   import cpu_types_pkg::*;

   typedef enum 	   logic [3:0] {IDLE, WB0, WB1, FETCH0, FETCH1, SNOOP_SERVICER, WB0_SERVICER, WB1_SERVICER, FLUSH, ITERATE, FLUSH_WB0, FLUSH_WB1, FLUSH_DONE} StateType;
   StateType curr_state, next_state;

   dcacheset_t [7:0] dcacheset;

   //adding in the ll-sc hw
   word_t link_reg; //the link register for ll-sc
   logic 		   valid_lr; //the valid bit for the ll operation and to be checked by the sc operation
   

   //address bits
   logic [1:0] 		   byte_offset;
   assign byte_offset = dcif.dmemaddr[1:0];

   logic 		   block_offset;
   assign block_offset = dcif.dmemaddr[2];

   logic [2:0] 		   index;
   assign index = dcif.dmemaddr[5:3];

   logic [25:0] 	   dmemaddr;
   //assign dmemaddr = dcif.dmemaddr[31:6];

   //dhit calculation signals
   logic 		   tag_match1, tag_match2;
   logic 		   valid1, valid2;
   logic 		   dirty1, dirty2;
   logic 		   hit1, hit2;
   logic 		   LRU;

   //flushing logic signals
   logic [7:0] 		   curr_frame;
   logic 		   curr_block;
   

   //snooping signals
   logic 		   M_access, S_access;

   logic 		   snoop_tag_hit;
   logic 		   snoop_block_invalid;

   logic 		   which_snoop;



   //new signal added to go to the WB0 state from IDLE as soon as the core finds a replacement instead of the memory controller going to SNOOP - basically to signal the memory controller to go to WB instead of SNOOP
   logic 		   to_replace, to_replace2;
   logic 		   permission_miss_w, permission_miss_r; //ADDED SPECIFICALLY FOR FIXING PERMISSION MISS/LRU WRITEBACK PROBLEM
   //end of new signal added to go to the WB0 state from IDLE as soon as the core finds a replacement instead of the memory controller going to SNOOP - basically to signal the memory controller to go to WB instead of SNOOP
   
   
   //cctrans, ccwrite
   logic 		   ReadHit1, ReadHit2, WriteHit1, WriteHit2;
   
   //for an ll operation, we just have to update the link register and the valid bit corresponding to it
   //assign link_reg = (dcif.ll == 1'b1) ? dcif.dmemaddr : 32'b0;
   //assign valid_lr = (dcif.ll == 1'b1) ? 1'b1 : 1'b0;
   

   always_comb
     begin
	dmemaddr = dcif.dmemaddr[31:6];
	tag_match1 = (dmemaddr == dcacheset[index].frameblocks[0].tag) ? 1'b1 : 1'b0;
	tag_match2 = (dmemaddr == dcacheset[index].frameblocks[1].tag) ? 1'b1 : 1'b0;
	
	valid1 = dcacheset[index].frameblocks[0].valid;
	valid2 = dcacheset[index].frameblocks[1].valid;
	
	dirty1 = dcacheset[index].frameblocks[0].dirty;
	dirty2 = dcacheset[index].frameblocks[1].dirty;
	
	hit1 = (tag_match1 == 1'b1) && (valid1 == 1'b1);
	hit2 = (tag_match2 == 1'b1) && (valid2 == 1'b1);

	ReadHit1 = (dcif.dmemREN && tag_match1 && valid1 /*&& ~dirty1*/); //when in M state, by default we have read permissions, so don't care for dirty
	ReadHit2 = (dcif.dmemREN && tag_match2 && valid2 /*&& ~dirty2*/); //when in M state, by default we have read permissions, so don't care for dirty
	
	WriteHit1 = (dcif.dmemWEN && tag_match1 && valid1 && dirty1);
	WriteHit2 = (dcif.dmemWEN && tag_match2 && valid2 && dirty2);
	
	LRU = dcacheset[index].lru;
     end // always_comb

   //the logic for to_replace - NEW
   assign permission_miss_w = (dcif.dmemWEN && ( (~WriteHit1 && tag_match1) || (~WriteHit2 && tag_match2) )); //mergesort debugging
   assign permission_miss_r = (dcif.dmemREN && ( (~ReadHit1 && tag_match1) || (~ReadHit2 && tag_match2) )); //mergesort debugging
   assign to_replace = /*((~tag_match1 || ~valid1) && dirty1 && ~LRU) || ((~tag_match2 || ~valid2) && dirty2 && LRU)*/( cif.ccwait == 1'b0 && ( ((~tag_match1 || ~valid1) && dirty1 && ~LRU) || ((~tag_match2 || ~valid2) && dirty2 && LRU)) && (dcif.dmemREN || dcif.dmemWEN) && cif.dwait == 1'b0);
   assign to_replace2 = /*((~tag_match1 || ~valid1) && dirty1 && ~LRU) || ((~tag_match2 || ~valid2) && dirty2 && LRU)*/( cif.ccwait == 1'b0 && ( ((~tag_match1 || ~valid1) && dirty1 && ~LRU /*&& ~tag_match2 && ~valid2*/) || ((~tag_match2 || ~valid2) && dirty2 && LRU /*&& ~tag_match1 && ~valid1*/)) && (dcif.dmemREN || dcif.dmemWEN)) && ~dcif.dhit && ~permission_miss_w && ~permission_miss_r; ///////// -------------------------------- MERGESORT 36 onwards new logic added && ~tag_match2 && ~valid2 - nevermind!! - ---- added  && ~permission_miss_w && ~permission_miss_r
   //end of the logic for to_replace - NEW
		      
	
   //next state logic
   always_comb
     begin
	next_state = curr_state;
	case(curr_state)
	  IDLE:
	    begin
	       /*if ( (tag_match1 && valid1 && ~dirty1 && dcif.dmemWEN) || (tag_match2 && valid2 && ~dirty2 && dcif.dmemWEN) ) //S->M transition need not require Mem pull
		 begin
		    next_state = IDLE;
		 end

	        
	       else */if (cif.ccwait == 1'b1 /*&& cif.dwait == 1'b1*/) //added dwait -> adding dwait does not make logical sense
		 begin
		    next_state = SNOOP_SERVICER; //flipped the order of this and the previous one since it was interfering
		 end
	       

	       else if ( (dcif.sc == 1'b1 && dcif.datomic == 1'b1 && dcif.dhit && (link_reg == dcif.dmemaddr) && ~valid_lr) || (dcif.sc == 1'b1 && dcif.datomic == 1'b1 && (link_reg == dcif.dmemaddr) && ~valid_lr) )  //new code exclusively for sc
		 begin
		    next_state = IDLE;
		 end
			      
	       
	      
	       else if(dcif.halt == 1'b1)
		 begin
		    next_state = FLUSH;
		 end
	       
	       else if( cif.ccwait == 1'b0 && ( ((~tag_match1 || ~valid1) && dirty1) && ((~tag_match2 || ~valid2) && dirty2)) && (dcif.dmemREN) && cif.dwait == 1'b0) //added dwait -> i see what you wanted to do, but adding dwait does not solve the problem. it is also not logically too much sensible. -> works for requestor, need to find something for servicer ---- added ~valid1 and ~valid2 parts with an or condition
		 begin
		    next_state = WB0;
		 end ////// --- WILL EXTEND IT FOR MERGESORT DEBUGGING!!!!!!!!!

	       else if( cif.ccwait == 1'b0 && ( ((~tag_match1 || ~valid1) && dirty1 && ~LRU) || ((~tag_match2 || ~valid2) && dirty2 && LRU)) && (dcif.dmemREN || dcif.dmemWEN) && ~dcif.dhit/*&& cif.dwait == 1'b0*/ && ~permission_miss_w && ~permission_miss_r) // ---- playing around while debugging mergesort - only the above was present before -REMOVED DWAIT DEPENDENCY -  ------------------------------------------------- REMEMBER THIS CHANGE FOR MERGESORT --added &&~dcif.dhit --- added  && ~permission_miss_w && ~permission_miss_r ------MERGESORT 36
		 begin
		    next_state = WB0; ///new condition added in mergesort
		 end
	       
	       else if ((cif.ccwait == 1'b0) && (( (~tag_match1 || ~valid1) /*&& ~dirty1*/) && ( (~tag_match2 || ~valid2) /*&& ~dirty2*/)) && (dcif.dmemWEN || dcif.dmemREN) && cif.dwait == 1'b0) //added dwait -> i see what you wanted to do, but adding dwait does not solve the problem. it is also not logically too much sensible. -> works for requestor, need to find something for servicer ------------ removed the dependency on ~dirty1 and ~dirty2
		 begin
		    next_state = FETCH0; ///one of the fixes while debugging mergesort
		 end

	       
	       else if ( (cif.ccwait == 1'b0 && cif.dwait == 1'b0) && ((tag_match1 && valid1 & ~dirty1) || (tag_match2 && valid2 && ~dirty2)) && (dcif.dmemWEN)) // -> added cif.dwait == 0
		 begin
		    next_state = FETCH0;
		 end	   
	       /*else if (~cif.ccwait && (~tag_match1 || ~valid1) && (~tag_match2 || ~valid2) && (dcif.dmemWEN || dcif.dmemREN) )
		 begin
		    next_state = FETCH0;
		 end*/
	       else
		 begin
		    next_state = IDLE;
		 end
	    end // case: IDLE

	  SNOOP_SERVICER:
	    begin
	       if( (snoop_tag_hit == 1'b0) || (snoop_block_invalid == 1'b1) /*|| (cif.ccinv == 1'b0) */) //inv == 0 because the requesting $ will want to only read -> this may need to be changed 
		 begin
		    next_state = IDLE;
		 end
	       else if ( (cif.ccinv == 1'b1) && (snoop_tag_hit && ~snoop_block_invalid) && dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[which_snoop].dirty) //basically if you are asked to invalidate yourself and you had previously written to it, then do not write back to memory; instead you just go to idle and let the other $ pull from memory while you will be made invalid and be removed of the dirty block
		 begin
		    next_state = WB0_SERVICER; // -> newly added 
		 end
	       else if( (cif.ccinv == 1'b0) && (snoop_tag_hit && ~snoop_block_invalid && dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[which_snoop].dirty) )
		 begin
		    next_state = WB0_SERVICER;
		 end
	       else //might need a few more next state logic ---------------- REMEMBER
		 begin
		    next_state = SNOOP_SERVICER;
		 end	       
	    end
	  
	  
	  WB0:
	    begin
	       if (cif.ccwait == 1'b1)
		 begin
		    next_state = SNOOP_SERVICER;
		 end
	       else if(cif.dwait == 1'b0)
		 begin
		    next_state = WB1;
		 end
	       else
		 begin
		    next_state = WB0;
		 end
	    end // case: WB0

	  WB0_SERVICER:
	    begin
	       if (cif.dwait == 1'b0)
		 begin
		    next_state = WB1_SERVICER;
		 end
	       else
		 begin
		    next_state = WB0_SERVICER;
		 end
	    end
	       
	  WB1:
	    begin
	       if (cif.ccwait == 1'b1)
		 begin
		    next_state = SNOOP_SERVICER;
		 end
	       else if(cif.dwait == 1'b0)
		 begin
		    next_state = FETCH0;
		 end
	       else
		 begin
		    next_state = WB1;
		 end
	    end // case: WB1

	  WB1_SERVICER:
	    begin
	       if (cif.dwait == 1'b0)
		 begin
		    next_state = IDLE;
		 end
	       else
		 begin
		    next_state = WB1_SERVICER;
		 end
	    end
	  

	  FETCH0:
	    begin
	       if (cif.ccwait == 1'b1)
		 begin
		    next_state = SNOOP_SERVICER;
		 end
	       else if(cif.dwait == 1'b0)
		 begin
		    next_state = FETCH1;
		 end
	       else
		 begin
		    next_state = FETCH0;
		 end
	    end // case: FETCH0

	  FETCH1:
	    begin
	       if (cif.ccwait == 1'b1)
		 begin
		    next_state = SNOOP_SERVICER;
		 end
	       else if(cif.dwait == 1'b0)
		 begin
		    next_state = IDLE;
		 end
	       else
		 begin
		    next_state = FETCH1;
		 end
	    end // case: FETCH1

	  FLUSH:
	    begin
	       if (cif.ccwait == 1'b1)
		 begin
		    next_state = SNOOP_SERVICER;
		 end
	       else
		 begin
		    next_state = ITERATE;
		 end
	    end

	  ITERATE:
	    begin
	       if (cif.ccwait == 1'b1)
		 begin
		    next_state = SNOOP_SERVICER;
		 end
	       else if(curr_frame == 8)
		 begin
		    next_state = FLUSH_DONE;
		 end
	       else if(dcacheset[curr_frame].frameblocks[curr_block].dirty == 1'b1)
		 begin
		    next_state = FLUSH_WB0;
		 end
	       else
		 begin
		    next_state = ITERATE;
		 end
	    end // case: ITERATE
	  
	  FLUSH_WB0:
	    begin
	       if (cif.ccwait == 1'b1)
		 begin
		    next_state = SNOOP_SERVICER;
		 end
	       else if(cif.dwait == 1'b0)
		 begin
		    next_state = FLUSH_WB1;
		 end
	       else
		 begin
		    next_state = FLUSH_WB0;
		 end
	    end // case: FLUSH_WB0

	  FLUSH_WB1:
	    begin
	       if (cif.ccwait == 1'b1)
		 begin
		    next_state = SNOOP_SERVICER;
		 end
	       else if(cif.dwait == 1'b0)
		 begin
		    next_state = ITERATE;
		 end
	       else
		 begin
		    next_state = FLUSH_WB1;
		 end
	    end // case: FLUSH_WB1
	  
	  FLUSH_DONE:
	    begin
	       next_state = FLUSH_DONE;
	    end

	endcase // case (curr_state)
     end // always_comb
   
   //output logic
   always_comb
     begin
	snoop_tag_hit = 1'b0;
	snoop_block_invalid = 1'b0;
	which_snoop = 1'b0;

	dcif.dhit = 1'b0; 
	dcif.dmemload = 32'b0;
	dcif.flushed = 1'b0;
	cif.dREN = 1'b0;
	cif.dWEN = 1'b0;
	cif.daddr = 32'b0;
	cif.dstore = 32'b0;
	cif.ccwrite = 1'b0; //let this remain
	cif.cctrans = 1'b0; //let this remain
	
	case(curr_state)
	  IDLE:
	    begin
	       snoop_tag_hit = 1'b0;
	       snoop_block_invalid = 1'b0;
	       which_snoop = 1'b0;
	       
	       dcif.dhit = WriteHit1 || WriteHit2 || ReadHit1 || ReadHit2 || (dcif.sc == 1'b1 && dcif.datomic == 1'b1 && (link_reg == dcif.dmemaddr) && ~valid_lr); //basically if on SC it had already been invalidated, then i want the dhit to be asserted and carry on like usual --- new code
	       dcif.dmemload = (dcif.sc && dcif.datomic && (valid_lr == 1'b1 && link_reg == dcif.dmemaddr)) ? 32'h00000001 : ( (dcif.dmemREN == 1 && (ReadHit1 || ReadHit2)) ? ((dcif.dmemREN == 1 && ReadHit1) ? dcacheset[index].frameblocks[0].block.words[block_offset] : dcacheset[index].frameblocks[1].block.words[block_offset] ) : 32'b0); //chanhed for sc op
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b0;
	       cif.dWEN = to_replace2 || 1'b0; // - NEW CODE ADDED FOR TO_REPLACE
	       cif.daddr = /*32'b0;*/dcif.dmemaddr;
	       cif.dstore = /*32'b0;*/dcif.dmemstore;
	       cif.ccwrite = /*~to_replace && */( (dcif.sc && dcif.datomic && (valid_lr != 1'b1 || link_reg != dcif.dmemaddr)) ? 1'b0 : (~cif.ccwait && dcif.dmemWEN && ~(WriteHit1 || WriteHit2)) ); //let this remain -> new code added for sc - NEW CODE ADDED FOR TO_REPLACE
	       cif.cctrans = /*~to_replace && */( (dcif.sc && dcif.datomic && (valid_lr != 1'b1 || link_reg != dcif.dmemaddr)) ? 1'b0 : (~cif.ccwait && ((dcif.dmemREN && ~(ReadHit1 || ReadHit2)) || (dcif.dmemWEN && ~(WriteHit1 || WriteHit2)))) ); //let this remain -> new code added for sc - NEW CODE ADDED FOR TO_REPLACE
	    end

	  WB0:
	    begin
	       snoop_tag_hit = 1'b0;
	       snoop_block_invalid = 1'b0;
	       which_snoop = 1'b0;
	       
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b0;
	       cif.dWEN = 1'b1;
	       cif.daddr = {dcacheset[index].frameblocks[LRU].tag, index, block_offset, byte_offset};
	       cif.dstore = dcacheset[index].frameblocks[LRU].block.words[block_offset];
	       cif.ccwrite = 0;
	       cif.cctrans = 0;
	    end

	  WB0_SERVICER:
	    begin
	       snoop_tag_hit = 1'b0;
	       snoop_block_invalid = 1'b0;
	       which_snoop = 1'b0;
	       
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b0;
	       cif.dWEN = 1'b1;
	       cif.daddr = (dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[0].tag == cif.ccsnoopaddr[31:6]) ?
			   {dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[0].tag, cif.ccsnoopaddr[5:3], cif.ccsnoopaddr[2], cif.ccsnoopaddr[1:0]} : 
			   {dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[1].tag, cif.ccsnoopaddr[5:3], cif.ccsnoopaddr[2], cif.ccsnoopaddr[1:0]};
	       cif.dstore = (dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[0].tag == cif.ccsnoopaddr[31:6]) ? 
			    dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[0].block.words[cif.ccsnoopaddr[2]] : 
			    dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[1].block.words[cif.ccsnoopaddr[2]];
	       cif.cctrans = 1'b0;
	       cif.ccwrite = 1'b0;
	    end
	  
	  WB1:
	    begin
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b0;
	       cif.dWEN = 1'b1;
	       cif.daddr = {dcacheset[index].frameblocks[LRU].tag, index, ~block_offset, byte_offset};
	       cif.dstore = dcacheset[index].frameblocks[LRU].block.words[~block_offset];
	       cif.ccwrite = 0;
	       //cif.cctrans = 0; //CHANGING CODE FOR MERGESORT ------------------------------------------------- REMEMBER THIS CHANGE FOR MERGESORT
	       cif.cctrans = dcif.dmemWEN || dcif.dmemREN;
	    end // case: WB1

	  WB1_SERVICER: 
	    begin
	       snoop_tag_hit = 1'b0;
	       snoop_block_invalid = 1'b0;
	       which_snoop = 1'b0;
	       
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b0;
	       cif.dWEN = 1'b1;
	       cif.daddr = (dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[0].tag == cif.ccsnoopaddr[31:6]) ?
			   {dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[0].tag, cif.ccsnoopaddr[5:3], ~cif.ccsnoopaddr[2], cif.ccsnoopaddr[1:0]} : 
			   {dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[1].tag, cif.ccsnoopaddr[5:3], ~cif.ccsnoopaddr[2], cif.ccsnoopaddr[1:0]};
	       cif.dstore = (dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[0].tag == cif.ccsnoopaddr[31:6]) ? 
			    dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[0].block.words[~cif.ccsnoopaddr[2]] : 
			    dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[1].block.words[~cif.ccsnoopaddr[2]];
	       cif.cctrans = 1'b0;
	       cif.ccwrite = 1'b0;
	    end

	  SNOOP_SERVICER:
	    begin
	       snoop_tag_hit = (dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[0].tag == cif.ccsnoopaddr[31:6]) || (dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[1].tag == cif.ccsnoopaddr[31:6]); //only used for transition back to idle state
	       snoop_block_invalid = ( (dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[0].tag == cif.ccsnoopaddr[31:6]) && (dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[0].valid == 0) ) ||
				     ( (dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[1].tag == cif.ccsnoopaddr[31:6]) && (dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[1].valid == 0) ); //only used for transition back to idle state
	       which_snoop = ( (dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[0].tag == cif.ccsnoopaddr[31:6]) && (dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[0].valid == 1) ) ? 0 : 
			 (( (dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[1].tag == cif.ccsnoopaddr[31:6]) && (dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[1].valid == 1) ) ? 1 : 0);
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b0;
	       cif.dWEN = 1'b0;
	       cif.daddr = 32'b0;
	       cif.dstore = 32'b0;
	       cif.cctrans = 1'b0;
	       cif.ccwrite = /*1'b0;*/ ( (dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[which_snoop].tag == cif.ccsnoopaddr[31:6]) && /*(dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[which_snoop].valid == 1) && */(dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[which_snoop].dirty == 1) ); //this must be to signal whether or not to go to the MEM0 stage or the CACHE0 stage in the memory controller -> ask Tess if she did this
	    end
	  

	  FETCH0:
	    begin
	       snoop_tag_hit = 1'b0;
	       snoop_block_invalid = 1'b0;
	       which_snoop = 1'b0;
	       
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b1;
	       cif.dWEN = 1'b0;
	       cif.daddr = dcif.dmemaddr;
	       cif.dstore = 32'b0;
	       cif.ccwrite = dcif.dmemWEN;
	       cif.cctrans = 1'b1;
	    end

	  FETCH1:
	    begin
	       snoop_tag_hit = 1'b0;
	       snoop_block_invalid = 1'b0;
	       which_snoop = 1'b0;
	       
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b1;
	       cif.dWEN = 1'b0;
	       cif.daddr = {dcif.dmemaddr[31:3], ~block_offset, byte_offset};
	       cif.dstore = 32'b0;
	       cif.ccwrite = dcif.dmemWEN;
	       cif.cctrans = 1'b1;
	    end

	  FLUSH:
	    begin
	       snoop_tag_hit = 1'b0;
	       snoop_block_invalid = 1'b0;
	       which_snoop = 1'b0;
	       
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b0;
	       cif.dWEN = 1'b0;
	       cif.daddr = 32'b0;
	       cif.dstore = 32'b0;
	       cif.ccwrite = 0;
	       cif.cctrans = 0;
	    end

	  ITERATE:
	    begin
	       snoop_tag_hit = 1'b0;
	       snoop_block_invalid = 1'b0;
	       which_snoop = 1'b0;
	       
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b0;
	       cif.dWEN = 1'b0;
	       cif.daddr = 32'h0;
	       cif.dstore = 32'b0;
	       cif.ccwrite = 0;
	       cif.cctrans = 0;
	    end // case: ITERATE


	  FLUSH_WB0:
	    begin
	       snoop_tag_hit = 1'b0;
	       snoop_block_invalid = 1'b0;
	       which_snoop = 1'b0;
	       
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b0;
	       cif.dWEN = 1'b1;
	       cif.daddr = {dcacheset[curr_frame].frameblocks[curr_block].tag, curr_frame[2:0], 1'b0, byte_offset};
	       cif.dstore = dcacheset[curr_frame].frameblocks[curr_block].block.words[0];
	       cif.ccwrite = 0;
	       cif.cctrans = 0;
	    end

	  FLUSH_WB1:
	    begin
	       snoop_tag_hit = 1'b0;
	       snoop_block_invalid = 1'b0;
	       which_snoop = 1'b0;
	       
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b0;
	       cif.dWEN = 1'b1;
	       cif.daddr = {dcacheset[curr_frame].frameblocks[curr_block].tag, curr_frame[2:0], 1'b1, byte_offset};
	       cif.dstore = dcacheset[curr_frame].frameblocks[curr_block].block.words[1];
	       cif.ccwrite = 0;
	       cif.cctrans = 0;
	    end

	  FLUSH_DONE:
	    begin
	       snoop_tag_hit = 1'b0;
	       snoop_block_invalid = 1'b0;
	       which_snoop = 1'b0;
	       
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b1;
	       cif.dREN = 1'b0;
	       cif.dWEN = 1'b0;
	       cif.daddr = 32'b0;
	       cif.dstore = 32'b0;
	       cif.ccwrite = 0;
	       cif.cctrans = 0;
	    end
	endcase // case (curr_state)
     end // always_comb

   
   always_ff @ (posedge CLK, negedge nRST)
     begin
	if(nRST == 1'b0)
	  begin
	     curr_state <= IDLE;
	     dcacheset <= '{default:0};
 
	     link_reg <= 32'b0; //initialize to 0
	     valid_lr <= 1'b0; //initialize to 0
	     
	  end
	else
	  begin
	     //possibly check for halt signals during other states (ex: halt comes in middle of WB1)
	     case(curr_state)

	       
	       IDLE:
		 begin
		    curr_block <= 0;
		    curr_frame <= 0;

		    //beginning of new code for S->M transition ------------------- DO NOT OPTIMIZE NOW
		    /*if ( (tag_match1 && valid1 && ~dirty1 && dcif.dmemWEN)  ) //S->M transition need not require Mem pull
		      begin
			 dcacheset[index].frameblocks[0].dirty <= 1'b1;
		      end
		    else if ( (tag_match2 && valid2 && ~dirty2 && dcif.dmemWEN) ) //S->M transition need not require Mem pull
		      begin
			 dcacheset[index].frameblocks[1].dirty <= 1'b1;
		      end*/
		    //end of new code for S->M transition ------------------- DO NOT OPTIMIZE NOW

		    //new code to fix the friggin LRU problem
		    if (~dcif.dhit && (hit1 || hit2) && dcif.dmemWEN && (next_state == FETCH0) )
		      begin
			 //dcacheset[index].lru <= ~dcacheset[index].lru; //////A MAJOR HACK!!!
			 dcacheset[index].lru <= hit1 ? 1'b0 : 1'b1; //////new code added --- DEBUGGING MERGESORT WITH 15 and MORE ELEMENTS --- might need to remove
		      end 
		    //end of new code to fix the friggin LRU problem


		    //new code to fix the friggin LRU problem with lw while debugging mergesort
		    if (~dcif.dhit && (tag_match1 || tag_match2) && dcif.dmemREN && (next_state == FETCH0) )
		      begin
			 //dcacheset[index].lru <= ~dcacheset[index].lru; //////A MAJOR HACK!!!
			 dcacheset[index].lru <= tag_match1 ? 1'b0 : 1'b1; //////new code added --- DEBUGGING MERGESORT WITH 15 and MORE ELEMENTS ------------- might need to remove 
		      end 
		    //end of new code to fix the friggin LRU problem

		    
		    
		    if(dcif.dhit == 1'b1)
		      begin		
			 //ll-sc code
			 if (dcif.ll == 1'b1 && dcif.datomic == 1'b1) //this will set the valid bit and the link register when there is an ll operation
			   begin
			      link_reg <= dcif.dmemaddr;
			      valid_lr <= 1'b1;
			   end
			 else
			   begin
			      link_reg <= link_reg;
			      valid_lr <= valid_lr;
			   end
	 
			 if(hit1 == 1'b1 && dcacheset[index].lru == 0)
			   begin
			      dcacheset[index].lru <= ~dcacheset[index].lru;
			   end
			 else if(hit2 == 1'b1 && dcacheset[index].lru == 1)
			   begin
			      dcacheset[index].lru <= ~dcacheset[index].lru;
			   end
			 else
			   begin
			      dcacheset[index].lru <= dcacheset[index].lru;
			   end

				   
			 if(dcif.dmemWEN == 1'b1)
			   begin

			      if ( (dcif.sc == 1'b1 && dcif.datomic == 1'b1 && dcif.dhit && (link_reg == dcif.dmemaddr) && valid_lr) || (dcif.dhit && (link_reg == dcif.dmemaddr) && valid_lr) )//new code exclusively for sc ------ adding the sw condition to invalidate valid_lr
				begin
				   valid_lr <= ~valid_lr;

				   dcacheset[index].frameblocks[0].block.words[block_offset] <= dcif.dmemstore;
				   dcacheset[index].frameblocks[0].dirty <= 1'b1;
				end
			      
			      else if(hit1 == 1'b1 && dcif.sc != 1'b1)
				begin
				   dcacheset[index].frameblocks[0].block.words[block_offset] <= dcif.dmemstore;
				   dcacheset[index].frameblocks[0].dirty <= 1'b1;
				end
			      else if (hit2 == 1'b1 && dcif.sc != 1'b1)
				begin
				   dcacheset[index].frameblocks[1].block.words[block_offset] <= dcif.dmemstore;
				   dcacheset[index].frameblocks[1].dirty <= 1'b1;
				end
			      else
				begin
				   dcacheset[index].frameblocks[1].block.words[block_offset] <= dcacheset[index].frameblocks[1].block.words[block_offset];
				   dcacheset[index].frameblocks[1].dirty <= dcacheset[index].frameblocks[1].dirty;
				end

			      if(hit1 == 1'b1 && dcacheset[index].lru == 0)
				begin
				   dcacheset[index].lru <= ~dcacheset[index].lru;
				end
			      else if(hit2 == 1'b1 && dcacheset[index].lru == 1)
				begin
				   dcacheset[index].lru <= ~dcacheset[index].lru;
				end
			      else
				begin
				   dcacheset[index].lru <= dcacheset[index].lru;
				end
			      
			   end // if (dcif.dWEN == 1'b1)
		      end // if (dcif.dhit == 1'b1)

		    //in response to coherence2.asm issue
		    if ( ((tag_match1 && valid1 & ~dirty1) || (tag_match2 && valid2 && ~dirty2)) && (dcif.dmemWEN))
		      begin
			 curr_state <= next_state;
		      end
		    
		    
		    else if( ( hit1 == 0 && hit2 == 0 ) || dcif.halt == 1)
		      begin 
			 curr_state <= next_state;
		      end

		    else if (cif.ccwait == 1'b1)
		      begin
			 curr_state <= next_state; //newly added
		      end
		    
		    else
		      begin
			 curr_state <= curr_state;
		      end
		    
		    
     		 end // case: IDLE

	       SNOOP_SERVICER:
		 begin
		    //changing permissions of servicer
		    if(cif.ccinv == 1'b1 && snoop_tag_hit && ~snoop_block_invalid && cif.ccsnoopaddr != link_reg) //changing to I ---- ADDED NEW SHIT TO FIX EXAMPLE ASM
		      begin
			 dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[which_snoop].dirty <= /*1'b0*/dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[which_snoop].dirty;
			 dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[which_snoop].valid <= 1'b0;
		      end
		    else if(cif.ccinv == 1'b0 && snoop_tag_hit && ~snoop_block_invalid )//changing to S
		      begin
			 dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[which_snoop].dirty <= 1'b0;
			 dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[which_snoop].valid <= 1'b1;
		      end
		    else
		      begin
			 dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[which_snoop].dirty <= dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[which_snoop].dirty;
			 dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[which_snoop].valid <= dcacheset[cif.ccsnoopaddr[5:3]].frameblocks[which_snoop].valid;
		      end


		    if (cif.ccsnoopaddr == link_reg && cif.ccinv == 1'b1) //when there is an sc on the other $ and you have to invalidate your copy of link register
		      //added && ccinv == 1'b0 to only invalidate when the other $ has an sc, not ll
		      begin
			 valid_lr <= 1'b0;
		      end
		    else
		      begin
			 valid_lr <= valid_lr;
		      end
		    
		    curr_state <= next_state;
		 end // case: SNOOP_SERVICER

	       
	       
	       FLUSH:
		 begin
		    curr_state <= next_state;
		 end

	       ITERATE:
		 begin
		    if(curr_block == 1 && next_state != FLUSH_WB0)
		      begin
			 curr_block <= 0;
			 curr_frame <= curr_frame + 1;
		      end
		    else
		      begin
			 if(next_state != FLUSH_WB0)
			   begin
			      curr_block <= 1;
			      curr_frame <= curr_frame;
			   end
			 else
			   begin
			      curr_block <= curr_block;
			      curr_frame <= curr_frame;
			   end
			 
		      end // else: !if(curr_block == 1)
		    
		    //?????
		    curr_state <= next_state;
		 end
	       
	       FLUSH_WB0:
		 begin
		    dcacheset[curr_frame].frameblocks[curr_block].dirty <= 0;
		    if(cif.dwait == 0)
		      begin
			 curr_state <= next_state;
		      end
		 end
	       

	       FLUSH_WB1:
		 begin
		    dcacheset[curr_frame].frameblocks[curr_block].dirty <= 0;
		    
		    if(cif.dwait == 0)
		      begin
			 curr_state <= next_state;
		      end
		 end

	       
	       FLUSH_DONE:
		 begin
		    curr_state <= next_state;
		 end
	       
	       FETCH0:
		 begin
		    if(next_state == FETCH1)
		      begin
			 ///////NEW CODE ADDED TO NOT DIRECTLY WRITE TO THE LRU FRAME - CHECK FOR HIT1 OR HIT2 WHICH MEANS THAT IT IS A SNOOP OPERATION
			 //if (hit1)
			   //begin
			     // dcacheset[index].frameblocks[0].block.words[block_offset] <= cif.dload;
			   //end
			 //else if (hit2)
			   //begin
			      //dcacheset[index].frameblocks[1].block.words[block_offset] <= cif.dload;
			   //end
			 ///////END OF NEW CODE ADDED TO NOT DIRECTLY WRITE TO THE LRU FRAME - CHECK FOR HIT1 OR HIT2 WHICH MEANS THAT IT IS A SNOOP OPERATION
			 //else //the default fetch from previously...this was the only thing there originally
			   //begin
			      dcacheset[index].frameblocks[LRU].block.words[block_offset] <= cif.dload;
			   //end
			 if(cif.dwait == 0)
			   begin
			      curr_state <= next_state;
			   end
		      end
		 end
	       

	       FETCH1:
		 begin
		    if(next_state == IDLE)
		      begin
			 ///////NEW CODE ADDED TO NOT DIRECTLY WRITE TO THE LRU FRAME - CHECK FOR HIT1 OR HIT2 WHICH MEANS THAT IT IS A SNOOP OPERATION
			 //if (hit1)
			   //begin
			      //dcacheset[index].frameblocks[0].block.words[~block_offset] <= cif.dload;
			      //dcacheset[index].frameblocks[0].valid <= 1'b1;
			      //dcacheset[index].frameblocks[0].dirty <= 1'b0;
			      //dcacheset[index].frameblocks[0].tag <= dcif.dmemaddr[31:6];
			      //dcacheset[index].lru <= 1'b1;
			   //end
			 //else if (hit2)
			   //begin
			      //dcacheset[index].frameblocks[1].block.words[~block_offset] <= cif.dload;
			      //dcacheset[index].frameblocks[1].valid <= 1'b1;
			      //dcacheset[index].frameblocks[1].dirty <= 1'b0;
			      //dcacheset[index].frameblocks[1].tag <= dcif.dmemaddr[31:6];
			      //dcacheset[index].lru <= 1'b0;
			   //end
			 ///////END OF NEW CODE ADDED TO NOT DIRECTLY WRITE TO THE LRU FRAME - CHECK FOR HIT1 OR HIT2 WHICH MEANS THAT IT IS A SNOOP OPERATION
			 //else //the default fetch from previously...this was the only thing there originally
			   //begin			 
			      dcacheset[index].frameblocks[LRU].block.words[~block_offset] <= cif.dload;
			      dcacheset[index].frameblocks[LRU].valid <= 1'b1;
			      dcacheset[index].frameblocks[LRU].dirty <= 1'b0;
			      dcacheset[index].frameblocks[LRU].tag <= dcif.dmemaddr[31:6];
			      dcacheset[index].lru <= ~dcacheset[index].lru; //-> might require this back
			   //end

			 //changing permissions for requester
			 if(dcif.dmemWEN && cif.ccwait == 1'b0) //changing to M
			   begin
			      //dcacheset[index].frameblocks[block_offset].dirty <= 1'b1;
			      //dcacheset[index].frameblocks[block_offset].valid <= 1'b1;
			      dcacheset[index].frameblocks[LRU].dirty <= 1'b1;
			   end
			 else if(dcif.dmemREN && cif.ccwait == 1'b0) //changing to S
			   begin
			      //dcacheset[index].frameblocks[block_offset].dirty <= 1'b0;
			      //dcacheset[index].frameblocks[block_offset].valid <= 1'b1;
			      dcacheset[index].frameblocks[LRU].dirty <= 1'b0;
			   end
			 else //not sure this serves any purpose
			   begin
			      //dcacheset[index].frameblocks[block_offset].dirty <= dcacheset[index].frameblocks[block_offset].dirty;
			      //dcacheset[index].frameblocks[block_offset].valid <= dcacheset[index].frameblocks[block_offset].valid;
			      dcacheset[index].frameblocks[LRU].dirty <= dcacheset[index].frameblocks[LRU].dirty;
			      dcacheset[index].frameblocks[LRU].valid <= dcacheset[index].frameblocks[LRU].valid;
			   end
			 
			 if(cif.dwait == 0)
			   begin
			      curr_state <= next_state;
			   end
		      end
		 end

	       WB0:
		 begin
		    if(cif.dwait == 0)
		      begin
			 curr_state <= next_state;
		      end
		 end

	       WB0_SERVICER:
		 begin
		    if(cif.dwait == 0)
		      begin
			 curr_state <= next_state;
		      end
		 end
	       	       
	       WB1:
		 begin
		    dcacheset[index].frameblocks[LRU].dirty <= 1'b0;
		    if(cif.dwait == 0)
		      begin
			 curr_state <= next_state;
		      end
		 end

	       WB1_SERVICER:
		 begin
		    if(cif.dwait == 0)
		      begin
			 curr_state <= next_state;
		      end
		 end
	       
	     endcase // case (curr_state)
	     //curr_state <= next_state;
	     
	  end // else: !if(nRST == 1'b0)
     end // always_ff @
      
   
endmodule // dcache

	  
	       
				      
				  
		  
		  
		       
	    
		    
		    
		    
		    
