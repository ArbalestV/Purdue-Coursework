`include "cache_control_if.vh"
`include "datapath_cache_if.vh"
`include "cpu_types_pkg.vh"

module dcache (
	       input logic CLK, nRST,
	       datapath_cache_if dcif,
	       cache_control_if ccif
	       );
   
   parameter CPUID = 0;

   //import types
   import cpu_types_pkg::*;

   typedef enum 	   logic [3:0] {IDLE, FETCH0, FETCH1, WB0, WB1, FLUSH, WRITE_DHIT_COUNT, SET_FLUSHED, SNOOP, SNOOP_WB0, SNOOP_WB1, INVALIDATE, INVALIDATE_NOWRITE} StateType;
   dcacheset_t [7:0] frames; //since there are 8 frames in total, index is 3 bits long
   dcachef_t daddr; //to compare with the frames within the dcache
   assign daddr = dcif.dmemaddr; //the memory address that is being checked for
   logic [2:0] 		   index; //since the index is from 0-7
   assign index = daddr.idx; //get the address to compare it with
   logic 		   block_offset, next_block_offset;
   assign block_offset = daddr.blkoff; //get the block offset (0 or 1)
   assign next_block_offset = (block_offset == 0) ? 1 : 0;
   logic [1:0]		   byte_offset;
   assign byte_offset = daddr.bytoff;
   logic 		   setTrans; //set ccif.cctrans signal to memory controller
		   
   
   logic 		   flushing;
   logic [2:0] 		   flushFIdx;
   logic 		   flushBIdx;
   logic 		   prevCcWait; //dml   
   logic 		   goto_dhit_write;
   logic 		   snoopFrameReg, next_snoopFrameReg;
   logic 		   isSC;		   
   logic 		   clearDirty;
   logic 		   clearValid;   
   StateType current_state, next_state;
   logic 		   dirty_bit_set; //we check in the idle state if this is a 0 or a 1

   logic 		   not_least_recently_used, least_recently_used;
   assign least_recently_used = frames[index] .lru; //can be either 0 or 1. 0 by default
   assign not_least_recently_used = (frames[index].lru == 0) ? 1: 0; //can be either 0 or 1

   

   //now for hit counter
   logic [31:0] 	   dhit_count;

   //for multicore
   StateType oldstate;
   //for multi-core - ll-sc
   logic sc_fail;

   always_comb
     begin
	dirty_bit_set = frames[index].frameblocks[frames[index].lru].dirty; //dirty bit set will only be on the lru frame block
     end

   logic wasInFetch;
   word_t prevAddr;

   always_ff @ ( posedge CLK, negedge nRST ) 
     begin
	if ( ~nRST ) begin
	   wasInFetch <= 1'b0;
	   prevAddr <= 0;
	end
	else begin
	   if ( dcif.dmemWEN && current_state == FETCH1 && next_state == IDLE ) begin
	      wasInFetch <= 1'b1;	      
	   end
	   else begin
	      wasInFetch <= 0;	      
	   end

	   if ( dcif.dmemWEN && current_state == IDLE && next_state == INVALIDATE_NOWRITE ) begin
	      prevAddr <= dcif.dmemaddr;	      
	   end
	   else begin
	      prevAddr <= prevAddr;
	   end
	end
     end // always_ff @   
	 
   
   //next state logic
   always_comb
     begin
	next_state = current_state; //to avoid latch
	next_snoopFrameReg = snoopFrameReg;	
	setTrans = 1'b0;
	
	case (current_state)
	  IDLE:
	    begin
	       if (dcif.halt == 1 /*&!nRST*/) //if it is a halt then first priority
		 begin
		    next_state = FLUSH;
		    //dcif.dhit = 0; //override the dhit signal
		 end
	       else if ( (dcif.dmemWEN == 1) && (dcif.dhit == 1) && wasInFetch == 1'b0 )
		 begin
		    next_state = INVALIDATE_NOWRITE;		    
		 end
	       else if ( (dcif.dmemREN == 1 || dcif.dmemWEN == 1) && dcif.dhit == 0 && dirty_bit_set == 0 /*&!nRST*/) //if it is just a read and not write, and the data to be read is not found in the data cache, and the dirty bit is set to 0 -> replacement without write back
		 begin
		    next_state = FETCH0;
		 end
	       else if ( (dcif.dmemREN == 1 || dcif.dmemWEN == 1) && dcif.dhit == 0 && dirty_bit_set == 1 /*&!nRST*/) //if it is just a read and not write, and the data to be read is not found in the data cache, and the dirty bit is set to 1 -> replacement with writeback
		 begin
		    next_state = WB0;
		 end
	       else //otherwise there was a dhit then stay in the IDLE state
		 begin
		    next_state = next_state;
		 end
	    end // case: IDLE
	  FLUSH: //this is a trap state, so put it in this state forever
	    begin
	       if (flushing == 1'b1) begin
		  next_state = WB0;
	       end
	       else begin
		  next_state = FLUSH;
	       end
	       if (goto_dhit_write == 1'b1) begin
		  //next_state = WRITE_DHIT_COUNT; not writing count
		  next_state = SET_FLUSHED;
	       end
	    end

	  
	  WRITE_DHIT_COUNT:
	    begin
	       if (ccif.dwait[CPUID] == 0)
		 begin
		    next_state = SET_FLUSHED;
		 end
	       else
		 begin
		    next_state = WRITE_DHIT_COUNT;
		 end
	    end // case: WRITE_DHIT_COUNT

	  SET_FLUSHED:
	    begin
	       next_state = SET_FLUSHED;
	    end
	   
  
	  FETCH0: //the first word is fetched
	    begin
	       /*
	       if (dirty_bit_set == 1)
		 begin
		    frames[index].frameblocks[frames[index].lru].dirty = 0; //make the dirty bit of the lru frame to be 0 only if it was set to 1 earlier, mostly will be used after it comes from the WB1 state
		 end
		*/
	       //dirty_bit_set = 0; //explicitly set it to zero, if it directly goes from the idle state tofetch0, then this will be 0. otherwise when it come from wb1 state to fetch0, that is when this explicit override becomes useful
	       if (ccif.dwait[CPUID] == 0) //signalling the first word has been loaded into the correct frame
		 begin
		    next_state = FETCH1; //go to fetch the next word
		 end
	       else
		 begin
		    next_state = FETCH0; //stay in this state until the first word is loaded from the RAM
		 end
	    end // case: FETCH0
	  FETCH1: //the second word is fetched
	    begin
	       if (ccif.dwait[CPUID] == 0) //signalling the second word has been loaded into the correct frame
		 begin
		    next_state = IDLE; //now go to the idle state where there will be a dhit generated upon the proper comparisons
		 end
               else if ( (dcif.dmemWEN == 1) && (dcif.dhit == 1) )
		 begin
		    next_state = INVALIDATE_NOWRITE;		    
		 end
	       else
		 begin
		    next_state = FETCH1; //stay in this state until the second word is loaded from the RAM
		 end
	    end // case: FETCH1
	  WB0: //in the write back state, write the first word into the RAM
	    begin
	       if (ccif.dwait[CPUID] == 0) //signalling the first word has been written to the memory
		 begin
		    next_state = WB1; //go to write the second word
		 end
	       else //still written to memory yet, keep in the same state
		 begin
		    next_state = WB0;
		 end
	    end // case: WB0
	  WB1: //in the write back state, write the second word into the RAM
	    begin
	       if (flushing == 1 && ccif.dwait[CPUID] == 0) begin
		  next_state = FLUSH;
	       end
	       else if (ccif.dwait[CPUID] == 0) //signalling the second word has been written to the memory
		 begin
		    next_state = FETCH0; //go to fetching from the memory
		 end
	       else //still written to memory yet, keep in the same state
		 begin
		    next_state = WB1;
		 end
	    end // case: WB1
	  SNOOP:
	    begin
	       next_state = oldstate;	       
	       // snoop logic - tag search
	       if ( (ccif.ccsnoopaddr[CPUID][31:6] == frames[ccif.ccsnoopaddr[CPUID][5:3]].frameblocks[0].tag) && (frames[ccif.ccsnoopaddr[CPUID][5:3]].frameblocks[0].valid == 1'b1) ) begin //tag match //dml9
		  
		  if ( ccif.ccinv[CPUID] == 1'b1 ) begin //invalidate signal, $[!service] <= Modified 
		     next_state = INVALIDATE;
		     next_snoopFrameReg = 1'b0; //dml8		     
		     //pranav's doubt with regards to setTrans that is supposedly causing all the problems
		     setTrans = 1'b1; 	     //pranav->david: why is setTrans == 1 here????????? might be causing something to fail. Halt signal is not reaching the WB stage at 13609.795 ns.
		     //end of pranav's question///

		  end
	       
		  else if ( frames[ccif.ccsnoopaddr[CPUID][5:3]].frameblocks[0].valid == 1'b1 ) begin // ccMSI : Modified or Shared
		     next_state = SNOOP_WB0; //wb and set dirty bit to 1'b0; ccMSI <= Shared
		     next_snoopFrameReg = 1'b0; 
		     clearDirty = 1'b1;		     
		  end
		  else begin // dont care any other case
		     if (ccif.ccwait == 1'b0) begin
			next_state = oldstate;
			setTrans = 0; // ? 			
		     end
		     else begin
			next_state = SNOOP;
			setTrans = 1'b1;			
		     end	     
		     //setTrans = 1'b1
		  end
	       end 
	       // snoop logic - tag search
	       else if ( (ccif.ccsnoopaddr[CPUID][31:6] == frames[ccif.ccsnoopaddr[CPUID][5:3]].frameblocks[1].tag) && (frames[ccif.ccsnoopaddr[CPUID][5:3]].frameblocks[1].valid == 1'b1) ) begin //tag match //dml9
		  if ( ccif.ccinv[CPUID] == 1'b1 ) begin //invalidate signal, $[!service] <= Modified 
		     next_state = INVALIDATE;
		     next_snoopFrameReg = 1'b1; //dml8		     
		     setTrans = 1'b1; 		     
		  end
		  else if ( frames[ccif.ccsnoopaddr[CPUID][5:3]].frameblocks[1].valid == 1'b1 ) begin // ccMSI : Modified or Shared
		     next_state = SNOOP_WB0; //wb and set dirty bit to 1'b0; ccMSI <= Shared
		     next_snoopFrameReg = 1'b1;	
		     clearDirty = 1'b1;		     
		  end
		  else begin // dont care any other case
		     if ( ccif.ccwait == 1'b0 ) begin			
			next_state = oldstate;
			setTrans = 1'b0; // ? 			
		     end
		     else begin
			next_state = SNOOP;			
			setTrans = 1'b1; // ? 
		     end
		     //setTrans = 1'b1;
		  end
	       end
	       else begin //no match
		  if ( ccif.ccwait == 1'b0 ) begin
		     next_state = oldstate;
		  end
		  else begin
		     next_state = SNOOP;
		  end		  
		  setTrans = 1'b1;		  
	       end		 
	    end
	  SNOOP_WB0:
	    begin
	       if (ccif.dwait[CPUID] == 0) //signalling the first word has been written to the memory
		 begin
		    next_state = SNOOP_WB1; //go to write the second word
		 end
	       else //still written to memory yet, keep in the same state
		 begin
		    next_state = SNOOP_WB0;
		 end	       
	    end
	  SNOOP_WB1:
	    begin
	       if (ccif.dwait[CPUID] == 0) //signalling the second word has been written to the memory
		 begin
		    next_state = INVALIDATE; //go to fetching from the memory
		 end
	       else //still written to memory yet, keep in the same state
		 begin
		    next_state = SNOOP_WB1;
		 end
	    end
	  INVALIDATE:
	    begin
	       if ( ccif.ccwait[CPUID] == 1'b0 ) begin		  
		  next_state = oldstate;
	       end
	       else begin
		  next_state = INVALIDATE;
	       end
	    end
	  INVALIDATE_NOWRITE: //dml
	    begin
	       if ( ccif.ccinv[CPUID] == 1'b1 ) begin		  
		  next_state = IDLE;
	       end
	       else begin
		  next_state = INVALIDATE_NOWRITE;
	       end
	    end
	endcase // case (current_state)

	if ( ( ccif.ccwait[CPUID] == 1'b1 && prevCcWait == 1'b0 ) && ((current_state != SNOOP) && (current_state != SNOOP_WB0) && (current_state != SNOOP_WB1) && (current_state != INVALIDATE)) && (current_state != INVALIDATE_NOWRITE)) begin //could be a potential source of error -> why is INVALID_NOWRITE not included
	   next_state = SNOOP;	   
	end
     end // always_comb

   //dml
   
   always_ff @ (posedge CLK, negedge nRST)
     begin
	if ( nRST == 0 ) begin
	   prevCcWait <= 0;
	end
	else begin
	   prevCcWait <= ccif.ccwait[CPUID];	   
	end	
     end
   
   //old state register
   always_ff @ (posedge CLK, negedge nRST)
     begin
	if ( nRST == 0 )
          begin
            oldstate <= IDLE;
          end 
	else begin
          oldstate <= oldstate;
          if ( ccif.ccwait[CPUID] == 1'b1 && ((current_state != SNOOP) && (current_state != SNOOP_WB0) && (current_state != SNOOP_WB1) && (current_state != INVALIDATE) )) begin //could be a potential source of error -> why is INVALID_NOWRITE not included
	     oldstate <= current_state;	   
	  end
        end
     end

   
   always_ff @ (posedge CLK, negedge nRST)
     begin
	if ( nRST == 0 )
	  begin
	     snoopFrameReg <= 0;
	  end
	else
	  begin
	     snoopFrameReg <= next_snoopFrameReg;
	  end
     end
   
   always_ff @ (posedge CLK, negedge nRST)
     begin
	current_state <= next_state;	
	if (nRST == 0)
	  begin
	     frames <= '{default:0}/*0*/;
	     current_state <= IDLE;
	     //flushFIdx <= 0; //not flushing
	     //flushBIdx <= 0; //not flushing
	     //flushing <= 0; //not flushing
	     //dcif.flushed <= 0; //will be set once all the dirty bits have been set to zero
	     
	     //for dhit counter
	     dhit_count <= 0;  	     
	  end
	else
	  begin
	     if (dcif.halt == 1) //basically a halt signal
	       begin
		  //frames <= 0; //flush. Maybe will have to write to the ram individually where all the dirty bits are set
	       if ((current_state == WB1) && (next_state == FLUSH))
		 begin
		    frames[flushFIdx].frameblocks[flushBIdx].dirty <= 0;
		    //flushing <= 0;   
		 end
		  current_state <= next_state;
	       end
	     else if ( (dcif.dmemREN == 1 || dcif.dmemWEN == 1) && ccif.dwait[CPUID] == 0 /*&& dirty_bit_set == 0*/) //no more wait when read request if generated, then load whatever is on the dload to the right frameblock of the frame
	       begin
		  //can be in either FETCH0 or FETCH1, WB0 or WB1
		  //these three following statements will be common for one frameblock - namely the valid bit, the tag and the dirty bit set value
		  
		  if (next_state == FETCH1 /*&& dcif.dhit == 0*/) //this will only happen if current_state == WB1 or IDLE
		    begin
		       //set for block offset for fetch0
		       frames[index].frameblocks[frames[index].lru].block.words[block_offset] <= ccif.dload[CPUID];
		       frames[index].frameblocks[frames[index].lru].dirty <= 0; //explicitly set the dirty bit to zero

		       //dhit counter logic to decrement
		       if (dcif.halt == 0) //to not do it while halting
			 begin
			    dhit_count <= dhit_count - 1;
			 end
		       

		    end
		  else if (next_state == IDLE /*&& dcif.dhit == 0*/) //this will only happen if current_state == FETCH0
		    begin
		       //set for block offset for fetch1	
		       frames[index].frameblocks[frames[index].lru].valid <= 1;
		       frames[index].frameblocks[frames[index].lru].tag <= daddr.tag;
		       frames[index].frameblocks[frames[index].lru].dirty <= 0; //if the dirty bit was set to zero from before in which case it wouldn't have gone IDLE->WB0->WB1->FETCH0, it wouldn't still hurt to overwrite this bit with a 0
		       frames[index].frameblocks[frames[index].lru].block.words[next_block_offset] <= ccif.dload[CPUID];
		       frames[index].lru <= ~frames[index].lru; //reverse the lru bit every time there is a load from RAM
		    end
		  current_state <= next_state;
		  //end of loading from the RAM
		  		  
	       end // if (dcif.dmemREN == 1 && dcif.dwait == 0 && dirty_bit_set == 0)
	     

	     else if (dcif.dhit == 1) //if there is a dhit, can only happen in the IDLE state
	       begin

		  //dhit counter addition
		  dhit_count <= dhit_count + 1;
		  
		  
		  if ( dcif.dmemWEN == 1 && ~sc_fail ) //only if there was a write enable, we will have to replace the frame
			 begin
			    if ( (frames[index].frameblocks[0].valid == 1) && (frames[index].frameblocks[0].tag == daddr.tag) )
			      begin
				 
				 frames[index].frameblocks[0].block.words[block_offset] <= dcif.dmemstore;
				 frames[index].frameblocks[0].dirty <= 1; //set dirty bit value high
			      end
			    else
			      begin
				 
				 frames[index].frameblocks[1].block.words[block_offset] <= dcif.dmemstore;
				 frames[index].frameblocks[1].dirty <= 1; //set dirty bit value high
			      end
			 end
		  
		  else if ( (frames[index].frameblocks[frames[index].lru].valid == 1) && (frames[index].frameblocks[frames[index].lru].tag == daddr.tag) ) //to change the lru if applicable, applies to both read or write requests
		    begin
		       frames[index].lru <= ~frames[index].lru;
		    end
		  //if the hit comes due to the lru frame, then make the other frame the lru frame
		  
	       end // if (dcif.dhit == 1)

	     
	     
	     
	     else //there wasnt a dhit or there wasnt a flush or there wasn't a need for replacement, which means that there might not have been a change to the lru
	       begin
		  frames <= frames;
		  current_state <= next_state;
	       end // else: !if(dcif.dhit == 1)
	     
	  end // else: !if(nRST == 0)
	if ( clearDirty == 1'b1 ) begin
	   frames[ccif.ccsnoopaddr[CPUID][5:3]].frameblocks[snoopFrameReg].dirty <= 0;	   
	end
	if ( clearValid == 1'b1 ) begin
	   frames[ccif.ccsnoopaddr[CPUID][5:3]].frameblocks[~snoopFrameReg].valid <= 0; //dml8
	   frames[ccif.ccsnoopaddr[CPUID][5:3]].frameblocks[snoopFrameReg].valid <= 0;
	end
     end // always_ff @
   


	//flush ff logic by david
		
	//FLUSH LOGIC
	//added for flushing setting the dirty bit to zero
   always_ff @ (posedge CLK, negedge nRST)
     begin
	if (nRST == 0)
	  begin
	     //frames <= '{default:0}/*0*/;
	     flushFIdx <= 0; //not flushing
	     flushBIdx <= 0; //not flushing
	     flushing <= 0; //not flushing
	     dcif.flushed <= 0; //will be set once all the dirty bits have been set to zero

	     goto_dhit_write <= 0;
	     
	  end
	else
	  begin
	     if ((current_state == WB1) && (next_state == FLUSH))
	       begin
		  //frames[flushFIdx].frameblocks[flushBIdx].dirty <= 0;
		  flushing <= 0;   
	       end
	     //end of flush addition
	     
	     if (current_state == FLUSH) begin
		
		if (frames[0].frameblocks[0].dirty == 1'b1) begin
		   flushFIdx <= 0;
		   flushBIdx <= 0;
		   flushing <= 1;
		   dcif.flushed <= 0;
		end
		else if (frames[0].frameblocks[1].dirty == 1'b1) begin
		   flushFIdx <= 0;
		   flushBIdx <= 1;
		   flushing <= 1;
		   dcif.flushed <= 0;
		end
		else if (frames[1].frameblocks[0].dirty == 1'b1) begin
		   flushFIdx <= 1;
		   flushBIdx <= 0;
		   flushing <= 1;
		   dcif.flushed <= 0;
		end
		else if (frames[1].frameblocks[1].dirty == 1'b1) begin
		   flushFIdx <= 1;
		   flushBIdx <= 1;
		   flushing <= 1;
		   dcif.flushed <= 0;
		end
		else if (frames[2].frameblocks[0].dirty == 1'b1) begin
		   flushFIdx <= 2;
		   flushBIdx <= 0;
		   flushing <= 1;
		   dcif.flushed <= 0;
		end
		else if (frames[2].frameblocks[1].dirty == 1'b1) begin
		   flushFIdx <= 2;
		   flushBIdx <= 1;
		   flushing <= 1;
		   dcif.flushed <= 0;
		end
		else if (frames[3].frameblocks[0].dirty == 1'b1) begin
		   flushFIdx <= 3;
		   flushBIdx <= 0;
		   flushing <= 1;
		   dcif.flushed <= 0;
		end
		else if (frames[3].frameblocks[1].dirty == 1'b1) begin
		   flushFIdx <= 3;
		   flushBIdx <= 1;
		   flushing <= 1;
		   dcif.flushed <= 0;
		end
		else if (frames[4].frameblocks[0].dirty == 1'b1) begin
		   flushFIdx <= 4;
		   flushBIdx <= 0;
		   flushing <= 1;
		   dcif.flushed <= 0;
		end
		else if (frames[4].frameblocks[1].dirty == 1'b1) begin
		   flushFIdx <= 4;
		   flushBIdx <= 1;
		   flushing <= 1;
		   dcif.flushed <= 0;
		end
		else if (frames[5].frameblocks[0].dirty == 1'b1) begin
		   flushFIdx <= 5;
		   flushBIdx <= 0;
		   flushing <= 1;
		   dcif.flushed <= 0;
		end
		else if (frames[5].frameblocks[1].dirty == 1'b1) begin
		   flushFIdx <= 5;
		   flushBIdx <= 1;
		   flushing <= 1;
		   dcif.flushed <= 0;
		end
		else if (frames[6].frameblocks[0].dirty == 1'b1) begin
		   flushFIdx <= 6;
		   flushBIdx <= 0;
		   flushing <= 1;
		   dcif.flushed <= 0;
		end
		else if (frames[6].frameblocks[1].dirty == 1'b1) begin
		   flushFIdx <= 6;
		   flushBIdx <= 1;
		   flushing <= 1;
		   dcif.flushed <= 0;
		end
		else if (frames[7].frameblocks[0].dirty == 1'b1) begin
		   flushFIdx <= 7;
		   flushBIdx <= 0;
		   flushing <= 1;
		   dcif.flushed <= 0;
		end
		else if (frames[7].frameblocks[1].dirty == 1'b1) begin
		   flushFIdx <= 7;
		   flushBIdx <= 1;
		   flushing <= 1;
		   dcif.flushed <= 0;
		end
		else begin
		   flushFIdx <= 0;
		   flushBIdx <= 0;
		   flushing <= 0;
		   //frames <= '{default:0}/*0*/;
		   //dcif.flushed <= 1;

		   
		   dcif.flushed <= 0;
		   //current_state <= WRITE_DHIT_COUNT;
		   goto_dhit_write <= 1;
		   
		end	  
	     end // if (current_state == FLUSH)
	     
	     
	     if (current_state == SET_FLUSHED)
	       begin
		  dcif.flushed <= 1;
		  goto_dhit_write <= 0;
		  
	       end
	      
	    
	  end // else: !if(nRST == 0)
	
     end // always_ff @
   



   
   //output combinational logic
   always_comb
     begin
	case(current_state)
	  IDLE:
	    begin
	       dcif.dhit = ( ( (frames[index].frameblocks[frames[index].lru].valid == 1) && (frames[index].frameblocks[frames[index].lru].tag == daddr.tag) ) ||
				  ( (frames[index].frameblocks[not_least_recently_used].valid == 1) && (frames[index].frameblocks[not_least_recently_used].tag == daddr.tag) ) ) && ~dcif.halt && ( dcif.dmemREN || dcif.dmemWEN ); //basically check if there is a dhit
	       
	       dcif.dmemload = (dcif.dmemWEN == 1) ? 0 : ( (dcif.dmemREN == 0) ? 0 : ( ((frames[index].frameblocks[0].valid == 1) && (frames[index].frameblocks[0].tag == daddr.tag)) ? frames[index].frameblocks[0].block.words[block_offset] : frames[index].frameblocks[1].block.words[block_offset]));

	       //dcif.flushed = 0;
	       ccif.dREN[CPUID] = 0;
	       ccif.dWEN[CPUID] = 0;
	       //ccif.daddr[CPUID] = dcif.dmemaddr; //does not matter <---
	       ccif.daddr[CPUID] = prevAddr;	 
	       ccif.dstore[CPUID] = dcif.dmemstore; //does not matter
	       ccif.ccwrite[CPUID] = 0;
	       ccif.cctrans[CPUID] = 0;	       
	    end // case: IDLE
	  
	  FETCH0:
	    begin
	       dcif.dhit = 0;
	       dcif.dmemload = 0;
	       //dcif.flushed = 0;
	       ccif.dREN[CPUID] = 1;
	       ccif.dWEN[CPUID] = 0;
	       ccif.daddr[CPUID] = dcif.dmemaddr;
	       ccif.dstore[CPUID] = 0;
	       ccif.ccwrite[CPUID] = dcif.dmemWEN; //MSI: to Modified, cache hit therefore no dWEN, dREN
	       ccif.cctrans[CPUID] = 1; //dcif.dmemWEN; //dml9
	    end

	  FETCH1:
	    begin
	       dcif.dhit = 0;
	       dcif.dmemload = 0;
	       //dcif.flushed = 0;
	       ccif.dREN[CPUID] = 1;
	       ccif.dWEN[CPUID] = 0;
	       ccif.daddr[CPUID] = {dcif.dmemaddr[31:3],next_block_offset,dcif.dmemaddr[1:0]};
	       ccif.dstore[CPUID] = 0;
	       ccif.ccwrite[CPUID] = 0;
	       ccif.cctrans[CPUID] = 0;
	    end

	  WB0:
	    begin
	       dcif.dhit = 0;
	       dcif.dmemload = 0;
	       //dcif.flushed = 0;
	       ccif.dREN[CPUID] = 0;
	       ccif.dWEN[CPUID] = 1;
	       ccif.daddr[CPUID] = flushing ? {frames[flushFIdx].frameblocks[flushBIdx].tag, flushFIdx, 1'b0, byte_offset} : {frames[index].frameblocks[frames[index].lru].tag,index,block_offset,byte_offset};
	       ccif.dstore[CPUID] = flushing ? frames[flushFIdx].frameblocks[flushBIdx].block.words[0] : frames[index].frameblocks[frames[index].lru].block.words[block_offset];
	       ccif.ccwrite[CPUID] = 0;
	       ccif.cctrans[CPUID] = 0;
	    end

	  WB1:
	    begin
	       dcif.dhit = 0;
	       dcif.dmemload = 0;
	       //dcif.flushed = 0;
	       ccif.dREN[CPUID] = 0;
	       ccif.dWEN[CPUID] = 1;
	       ccif.daddr[CPUID] = flushing ? {frames[flushFIdx].frameblocks[flushBIdx].tag, flushFIdx, 1'b1, byte_offset} : {frames[index].frameblocks[frames[index].lru].tag,index,next_block_offset,byte_offset};
	       ccif.dstore[CPUID] = flushing ? frames[flushFIdx].frameblocks[flushBIdx].block.words[1] : frames[index].frameblocks[frames[index].lru].block.words[next_block_offset];
	       ccif.ccwrite[CPUID] = 0;
	       ccif.cctrans[CPUID] = 0;
	    end

	   FLUSH:
	    begin
	       dcif.dhit = 0;
	       dcif.dmemload = 0;
	       //dcif.flushed = 1;
	       ccif.dREN[CPUID] = 0;
	       ccif.dWEN[CPUID] = 0;
	       ccif.daddr[CPUID] = 0;
	       ccif.dstore[CPUID] = 0;
	       ccif.ccwrite[CPUID] = 0;
	       ccif.cctrans[CPUID] = 0;
	    end
	  
	  WRITE_DHIT_COUNT:
	    begin
	       dcif.dhit = 0;
	       dcif.dmemload = 0;
	       ccif.dREN[CPUID] = 0;
	       ccif.dWEN[CPUID] = 1;
	       ccif.daddr[CPUID] = 32'h3100;
	       ccif.dstore[CPUID] = dhit_count;
	       ccif.ccwrite[CPUID] = 0;
	       ccif.cctrans[CPUID] = 0;
	    end

	  SET_FLUSHED:
	    begin
	       dcif.dhit = 0;
	       dcif.dmemload = 0;
	       ccif.dREN[CPUID] = 0;
	       ccif.dWEN[CPUID] = 0;
	       ccif.daddr[CPUID] = 0;
	       ccif.dstore[CPUID] = 0;
	       ccif.ccwrite[CPUID] = 0;
	       ccif.cctrans[CPUID] = 0;
	    end
	  
	  SNOOP:
	    begin
	       dcif.dhit = 0;
	       dcif.dmemload = 0;
	       ccif.dREN[CPUID] = 0;
	       ccif.dWEN[CPUID] = 0;
	       ccif.daddr[CPUID] = 0;
	       ccif.dstore[CPUID] = 0;
	       ccif.ccwrite[CPUID] = 0;
	       ccif.cctrans[CPUID] = 0;
	    end
	  SNOOP_WB0:
	    begin
	       dcif.dhit = 0;
	       dcif.dmemload = 0;
	       //dcif.flushed = 0;
	       ccif.dREN[CPUID] = 0;
	       ccif.dWEN[CPUID] = 1;
	       //ccif.daddr[CPUID] = {frames[ccif.ccsnoopaddr[CPUID][5:3]].frameblocks[snoopFrameReg].tag,ccif.ccsnoopaddr[CPUID][5:3],1'b0,2'b00};
	       ccif.daddr[CPUID] = {frames[ccif.ccsnoopaddr[CPUID][5:3]].frameblocks[snoopFrameReg].tag,ccif.ccsnoopaddr[CPUID][5:3],ccif.ccsnoopaddr[CPUID][2],/*2'b00*/ccif.ccsnoopaddr[CPUID][1:0]};
	       ccif.dstore[CPUID] = frames[ccif.ccsnoopaddr[CPUID][5:3]].frameblocks[snoopFrameReg].block.words[ccif.ccsnoopaddr[CPUID][2]];	  //blk_offset
	       ccif.ccwrite[CPUID] = 0;
	       ccif.cctrans[CPUID] = 1; // to CC if CtoC or MtoC
	    end
	  SNOOP_WB1:
	    begin
	       dcif.dhit = 0;
	       dcif.dmemload = 0;
	       //dcif.flushed = 0;
	       ccif.dREN[CPUID] = 0;
	       ccif.dWEN[CPUID] = 1;
	       //ccif.daddr[CPUID] = {frames[ccif.ccsnoopaddr[CPUID][5:3]].frameblocks[snoopFrameReg].tag,ccif.ccsnoopaddr[CPUID][5:3],1'b1,2'b00};
	       ccif.daddr[CPUID] = {frames[ccif.ccsnoopaddr[CPUID][5:3]].frameblocks[snoopFrameReg].tag,ccif.ccsnoopaddr[CPUID][5:3],~ccif.ccsnoopaddr[CPUID][2],/*2'b00*/ccif.ccsnoopaddr[CPUID][1:0]};
	       ccif.dstore[CPUID] = frames[ccif.ccsnoopaddr[CPUID][5:3]].frameblocks[snoopFrameReg].block.words[~ccif.ccsnoopaddr[CPUID][2]];   //blk_offset
	       ccif.ccwrite[CPUID] = 0;
	       ccif.cctrans[CPUID] = 0;
	    end
	  INVALIDATE:
	    begin
	       dcif.dhit = 0;
	       dcif.dmemload = 0;
	       ccif.dREN[CPUID] = 0;
	       ccif.dWEN[CPUID] = 0;
	       ccif.daddr[CPUID] = 0;
	       ccif.dstore[CPUID] = 0;	  
	       ccif.ccwrite[CPUID] = 0;
	       ccif.cctrans[CPUID] = 0;	       
	       //ccif.cctrans[CPUID] = 1; // to CC if CtoC or MtoC     
	    end
	  INVALIDATE_NOWRITE:
	    begin
	       dcif.dhit = 0;
	       dcif.dmemload = 0;
	       ccif.dREN[CPUID] = 0;
	       ccif.dWEN[CPUID] = 1;
	       ccif.daddr[CPUID] = prevAddr;
	       ccif.dstore[CPUID] = 0;
	       ccif.ccwrite[CPUID] = 1;
	       ccif.cctrans[CPUID] = 1;	       
	    end
	endcase // case (current_state)
	if (isSC) begin
	   dcif.dmemload = (sc_fail == 1) ? 0 : 1;	   
	end
	if ( setTrans ) begin
	   ccif.cctrans[CPUID] = 1'b1;
	end
     end // always_comb


   word_t ll_addr, next_ll_addr;
   
   always_comb
     begin
	clearValid = 1'b0;

	if ( current_state == SNOOP ) begin	   //////////////////////////////////////////////////////////dml
	   if ( ll_addr == ccif.ccsnoopaddr[CPUID] && ccif.ccinv[CPUID] == 1'b1 ) begin
	      clearValid = 1'b1;	      
	   end
	end
	//if ( current_state == SNOOP_WB1 && next_state == INVALIDATE) begin
	if ( current_state == INVALIDATE && next_state == IDLE ) begin       //dml-------
	//if ( current_state == SNOOP && next_state == INVALIDATE ) begin
	   //clearValid = 1'b1;
	   clearValid = ccif.ccinv[CPUID]; //dml9	   
	end
     end
   

   /* ******************************************************
    * Load Linked (LL) Register
    * 
    * stores daddr on a LL instruction
    * clears validity bit on SW, SC, or Snoop Invalidate
    * *****************************************************/

   //word_t ll_addr, next_ll_addr;
   logic ll_valid, next_ll_valid;
   
   
   always_ff @ ( posedge CLK, negedge nRST)
     begin
	if ( nRST == 1'b0 ) begin
	   ll_addr <= 0;
	   ll_valid <= 0;	   
	end
	else begin
	   ll_addr <= next_ll_addr;
	   ll_valid <= next_ll_valid;
	end
     end

   always_comb
     begin
	sc_fail = 0;
	isSC = 1'b0;
	next_ll_valid = ll_valid;
	next_ll_addr = ll_addr;
	
	if ( dcif.datomic & dcif.dmemREN ) begin
	   next_ll_addr = dcif.dmemaddr;
	   next_ll_valid = 1'b1;	   
	end

	/* On a SC, need to set dcif.dmemload == whether SC passed or failed 
	 *   isSC : means dmemload will take the value of !sc_fail
	 *   sc_fail : whether or not the SC condition passed */

	if ( dcif.datomic == 1'b1 && dcif.dmemWEN == 1'b1 ) begin //if SC, then
	   isSC = 1'b1;	   
	   if ( dcif.dmemaddr == ll_addr && ll_valid == 1'b1 ) begin //check address match & valid
	      next_ll_valid = 0;	   //invalidate
	   end
	   else begin
	      /* TODO : Don't store dmemstore into cache if this condition fails*/
	      sc_fail = 1; /* if ( match && ll_fail == 0 ) then store */
	   end	   
	end
	if ( dcif.dmemWEN ) begin
	   if ( dcif.dmemaddr == ll_addr ) begin
	      next_ll_valid = 1'b0;	      
	   end	   
	   /* Store into cache, regardless */
	end
	if ( current_state == SNOOP ) begin	   
	   if ( ll_addr == ccif.ccsnoopaddr[CPUID] && ccif.ccinv[CPUID] == 1'b1 ) begin
	      next_ll_valid = 1'b0;	      
	   end
	end
     end // always_comb
   
   
endmodule // dcache

	  
	       
				      
				  
		  
		  
		       
	    
		    
		    
		    
		    
