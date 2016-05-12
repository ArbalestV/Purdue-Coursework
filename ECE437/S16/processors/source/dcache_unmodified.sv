
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

   /*
   assign tag_match1 = (dmemaddr == dcacheset[index].frameblocks[0].tag) ? 1'b1 : 1'b0;
   assign tag_match2 = (dmemaddr == dcacheset[index].frameblocks[1].tag) ? 1'b1 : 1'b0;

   assign valid1 = dcacheset[index].frameblocks[0].valid;
   assign valid2 = dcacheset[index].frameblocks[1].valid;

   assign dirty1 = dcacheset[index].frameblocks[0].dirty;
   assign dirty2 = dcacheset[index].frameblocks[1].dirty;
     
   assign hit1 = (tag_match1 == 1'b1) && (valid1 == 1'b1);
   assign hit2 = (tag_match2 == 1'b1) && (valid2 == 1'b1);

   assign LRU = dcacheset[index].lru;
    */
    
   //flushing logic signals
   logic [7:0] 		   curr_frame;
   logic 		   curr_block;
   
   //dhit count
   logic [31:0] 	   dhit_count;

   //snooping signals
   logic 		   M_access, S_access;
   word_t snoopaddr;
   logic [25:0] 	   snoopTag;
   logic [2:0] 		   snoopIndex;
   logic [1:0] 		   snoopByteOff;
   logic 		   snoopBlockOff;
   
   
   //cctrans, ccwrite
   logic 		   ReadHit1, ReadHit2, WriteHit1, WriteHit2;
   
   

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

	ReadHit1 = (dcif.dmemREN && tag_match1 && valid1 && ~dirty1);
	ReadHit2 = (dcif.dmemREN && tag_match2 && valid2 && ~dirty2);
	
	WriteHit1 = (dcif.dmemWEN && tag_match1 && valid1 && dirty1);
	WriteHit2 = (dcif.dmemWEN && tag_match2 && valid2 && dirty2);
	
	LRU = dcacheset[index].lru;
     end // always_comb
   
	
   //next state logic
   always_comb
     begin
	next_state = curr_state;
	case(curr_state)
	  IDLE:
	    begin
	       if(dcif.halt == 1'b1)
		 begin
		    next_state = FLUSH;
		 end
	       else if( cif.ccwait == 1'b0 && ((~tag_match1 && dirty1) && (~tag_match2 && dirty2)) ) //(dcif.dmemWEN == 1 || dcif.dmemREN == 1) && (hit1 == 1'b0 && dirty1 == 1'b1 && LRU == 0) && (hit2 == 1'b0 && dirty2 == 1'b1 && LRU == 1) ) //possible place for change
		 begin
		    next_state = WB0;
		 end
	       /*else if( (dcif.dmemWEN == 1 || dcif.dmemREN == 1) && hit1 == 1'b0 && hit2 == 1'b0 && dcacheset[index].frameblocks[LRU].dirty == 1'b1)
		 begin
		    next_state = WB0;
		 end*/
	       
	       //else if( ~cif.ccwait && ( (dcif.dmemREN && ~ReadHit1) || (dcif.dmemREN && ~ReadHit2) || (dcif.dmemWEN && ~WriteHit1) || (dcif.dmemWEN && ~WriteHit2) ) )  //(dcif.dmemWEN == 1 || dcif.dmemREN == 1) && (hit1 == 1'b0 /*&& dirty1 == 1'b0*/) && (hit2 == 1'b0/* && dirty2 == 1'b0*/) ) //possible place for change
		 //begin
		   // next_state = SNOOP_SERVICER;
		 //end -> 
	       else
		 begin
		    next_state = IDLE;
		 end
	    end // case: IDLE

	  SNOOP_SERVICER:
	    begin
	       if(cif.ccwait == 1'b1 && cif.ccinv == 1'b0)
		 begin
		    next_state = IDLE;
		 end
	       else if(cif.ccwait == 1'b0 && cif.dwait == 1'b0)
		 begin
		    next_state = FETCH0;
		 end
	       else if(cif.ccinv == 1'b1)
		 begin
		    next_state = WB0;
		 end
	       else
		 begin
		    next_state = SNOOP_SERVICER;
		 end
	       
	    end
	  
	  
	  WB0:
	    begin
	       if(cif.dwait == 1'b0)
		 begin
		    next_state = WB1;
		 end
	       else
		 begin
		    next_state = WB0;
		 end
	    end // case: WB0

	  WB1:
	    begin
	       if(cif.dwait == 1'b0)
		 begin
		    next_state = SNOOP_SERVICER;
		 end
	       else if(cif.ccwait == 1'b1)
		 begin
		    next_state = IDLE;
		 end
	       else
		 begin
		    next_state = WB1;
		 end
	    end // case: WB1

	  FETCH0:
	    begin
	       if(cif.dwait == 1'b0)
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
	       if(cif.dwait == 1'b0)
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
	       next_state = ITERATE;
	    end

	  ITERATE:
	    begin
	       if(curr_frame == 8)
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
	       if(cif.dwait == 1'b0)
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
	       if(cif.dwait == 1'b0)
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
	case(curr_state)
	  IDLE:
	    begin
	       dcif.dhit = WriteHit1 || WriteHit2 || ReadHit1 || ReadHit2; //(hit1 || hit2) && ~dcif.halt && (dcif.dmemREN || dcif.dmemWEN);
	       dcif.dmemload = (dcif.dmemREN == 1 && (ReadHit1 || ReadHit2)) ? ((dcif.dmemREN == 1 && ReadHit1) ? dcacheset[index].frameblocks[0].block.words[block_offset] : dcacheset[index].frameblocks[1].block.words[block_offset] ) : 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b0;
	       cif.dWEN = 1'b0;
	       cif.daddr = 32'b0;
	       cif.dstore = 32'b0;
	       cif.ccwrite = ~cif.ccwait && dcif.dmemWEN && ~(WriteHit1 || WriteHit2);
	       cif.cctrans = ~cif.ccwait && ((dcif.dmemREN && ~(ReadHit1 || ReadHit2)) || (dcif.dmemWEN && ~(WriteHit1 || WriteHit2)));
	       
	    end

	  WB0:
	    begin
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b0;
	       cif.dWEN = 1'b1;
	       cif.daddr = {dcacheset[index].frameblocks[LRU].tag, index, block_offset, byte_offset};
	       cif.dstore = dcacheset[index].frameblocks[LRU].block.words[block_offset];
	       
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
	       
	    end

	  SNOOP_SERVICER:
	    begin
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b0;
	       cif.dWEN = 1'b0;
	       cif.daddr = 32'b0;
	       cif.dstore = 32'b0;
	       cif.cctrans = cif.ccwait ? ( (dcacheset[snoopIndex].frameblocks[snoopBlockOff].tag == snoopTag) && (dcacheset[snoopIndex].frameblocks[snoopBlockOff].valid) && (dcacheset[snoopIndex].frameblocks[snoopBlockOff].dirty == 1'b0) ) : cif.cctrans;
	       cif.ccwrite = cif.ccwait ? ( (dcacheset[snoopIndex].frameblocks[snoopBlockOff].tag == snoopTag) && (dcacheset[snoopIndex].frameblocks[snoopBlockOff].valid) && (dcacheset[snoopIndex].frameblocks[snoopBlockOff].dirty) ) : cif.ccwrite;
	       
	    end
	  

	  FETCH0:
	    begin
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b1;
	       cif.dWEN = 1'b0;
	       cif.daddr = dcif.dmemaddr;
	       cif.dstore = 32'b0;
	    end

	  FETCH1:
	    begin
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b1;
	       cif.dWEN = 1'b0;
	       cif.daddr = {dcif.dmemaddr[31:3], ~block_offset, byte_offset};
	       cif.dstore = 32'b0;
	    end

	  FLUSH:
	    begin
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b0;
	       cif.dWEN = 1'b0;
	       cif.daddr = 32'b0;
	       cif.dstore = 32'b0;
	    end

	  ITERATE:
	    begin
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b0;
	       cif.dWEN = 1'b0;
	       cif.daddr = 32'h0;
	       cif.dstore = 32'b0;

	       /*iterate flush signals
	       if(curr_block == 1)
		 begin
		    curr_frame = curr_frame + 1;
		    curr_block = 0;
		 end
	       else
		 begin
		    curr_frame = curr_frame;
		    curr_block = 1;
		 end*/
	       
	    end // case: ITERATE


	  FLUSH_WB0:
	    begin
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b0;
	       cif.dWEN = 1'b1;
	       cif.daddr = {dcacheset[curr_frame].frameblocks[curr_block].tag, curr_frame[2:0], 1'b0, byte_offset};
	       cif.dstore = dcacheset[curr_frame].frameblocks[curr_block].block.words[0];
	    end

	  FLUSH_WB1:
	    begin
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b0;
	       cif.dREN = 1'b0;
	       cif.dWEN = 1'b1;
	       cif.daddr = {dcacheset[curr_frame].frameblocks[curr_block].tag, curr_frame[2:0], 1'b1, byte_offset};
	       cif.dstore = dcacheset[curr_frame].frameblocks[curr_block].block.words[1];
	    end

	  FLUSH_DONE:
	    begin
	       dcif.dhit = 1'b0;
	       dcif.dmemload = 32'b0;
	       dcif.flushed = 1'b1;
	       cif.dREN = 1'b0;
	       cif.dWEN = 1'b0;
	       cif.daddr = 32'b0;
	       cif.dstore = 32'b0;
	    end
	endcase // case (curr_state)
     end // always_comb

   
   always_ff @ (posedge CLK, negedge nRST)
     begin
	if(nRST == 1'b0)
	  begin
	     curr_state <= IDLE;
	     dcacheset <= '{default:0};
	     dhit_count <= 0;
	  end
	else
	  begin
	     //possibly check for halt signals during other states (ex: halt comes in middle of WB1)
	     snoopaddr <= 0;
	     snoopTag <= 0;
	     snoopIndex <= 0;
	     snoopBlockOff <= 0;
	     snoopByteOff <= 0;
	     case(curr_state)

	       
	       IDLE:
		 begin

		    curr_block <= 0;
		    curr_frame <= 0;
		    
		    
		    
		    if(dcif.dhit == 1'b1)
		      begin
			 dhit_count <= dhit_count + 1;
			 
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
			      if(hit1 == 1'b1)
				begin
				   dcacheset[index].frameblocks[0].block.words[block_offset] <= dcif.dmemstore;
				   dcacheset[index].frameblocks[0].dirty <= 1'b1;
				end
			      else
				begin
				   dcacheset[index].frameblocks[1].block.words[block_offset] <= dcif.dmemstore;
				   dcacheset[index].frameblocks[1].dirty <= 1'b1;
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
		    
		    
		    if(next_state == FETCH0)
		      begin
			 dhit_count <= dhit_count - 1;
		      end
		    
		    if( ( hit1 == 0 && hit2 == 0 ) || dcif.halt == 1)
		      begin 
			 curr_state <= next_state;
		      end
		    else
		      begin
			 curr_state <= curr_state;
		      end
		    
		    
     		 end // case: IDLE

	       SNOOP_SERVICER:
		 begin
		    snoopaddr <= cif.ccsnoopaddr;
		    snoopTag <= cif.ccsnoopaddr[31:6];
		    snoopIndex <= cif.ccsnoopaddr[5:3];
		    snoopBlockOff <= cif.ccsnoopaddr[2];
		    snoopByteOff <= cif.ccsnoopaddr[1:0];

		    //changing permissions of servicer
		    if(cif.ccwait == 1'b1 && cif.ccinv == 1'b1) //changing to I
		      begin
			 dcacheset[snoopIndex].frameblocks[snoopBlockOff].dirty <= 1'b0;
			 dcacheset[snoopIndex].frameblocks[snoopBlockOff].valid <= 1'b0;
		      end
		    else if(cif.ccwait == 1'b1 && cif.ccinv == 1'b0)//changing to S
		      begin
			 dcacheset[snoopIndex].frameblocks[snoopBlockOff].dirty <= 1'b0;
			 dcacheset[snoopIndex].frameblocks[snoopBlockOff].valid <= 1'b1;
		      end
		    else
		      begin
			 dcacheset[snoopIndex].frameblocks[snoopBlockOff].dirty <= dcacheset[snoopIndex].frameblocks[snoopBlockOff].dirty;
			 dcacheset[snoopIndex].frameblocks[snoopBlockOff].valid <= dcacheset[snoopIndex].frameblocks[snoopBlockOff].valid;
		      end
		    
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
			 dcacheset[index].frameblocks[LRU].block.words[block_offset] <= cif.dload;
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
			 dcacheset[index].frameblocks[LRU].block.words[~block_offset] <= cif.dload;
			 dcacheset[index].frameblocks[LRU].valid <= 1'b1;
			 dcacheset[index].frameblocks[LRU].dirty <= 1'b0;
			 dcacheset[index].frameblocks[LRU].tag <= dcif.dmemaddr[31:6];
			 dcacheset[index].lru <= ~dcacheset[index].lru;

			 //changing permissions for requester
			 if(dcif.dmemWEN && cif.ccwait == 1'b0) //changing to M
			   begin
			      dcacheset[index].frameblocks[block_offset].dirty <= 1'b1;
			      dcacheset[index].frameblocks[block_offset].valid <= 1'b1;
			   end
			 else if(dcif.dmemREN && cif.ccwait == 1'b0) //changing to S
			   begin
			      dcacheset[index].frameblocks[block_offset].dirty <= 1'b0;
			      dcacheset[index].frameblocks[block_offset].valid <= 1'b1;
			   end
			 else
			   begin
			      dcacheset[index].frameblocks[block_offset].dirty <= dcacheset[index].frameblocks[block_offset].dirty;
			      dcacheset[index].frameblocks[block_offset].valid <= dcacheset[index].frameblocks[block_offset].valid;
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
	       	       
	       WB1:
		 begin
		    dcacheset[index].frameblocks[LRU].dirty <= 1'b0;
		    if(cif.dwait == 0)
		      begin
			 curr_state <= next_state;
		      end

		    if(next_state == FETCH0)
		      begin
			 dhit_count <= dhit_count - 1;
		      end
		 end
	       
	     endcase // case (curr_state)
	     //curr_state <= next_state;
	     
	  end // else: !if(nRST == 1'b0)
     end // always_ff @
      
   
endmodule // dcache

	  
	       
				      
				  
		  
		  
		       
	    
		    
		    
		    
		    
