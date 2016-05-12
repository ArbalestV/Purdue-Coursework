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
   
   //datapath:
   //IN = halt, dmemREN, dmemWEN, datomic, dmemstore, dmemaddr
   //OUT = dhit, dmemload, flushed

   //memory control
   //IN = dwait, dload, ccwait, ccinv, ccsnoopaddr
   //OUT = dREN, dWEN, daddr, dstore, ccwrite, cctrans
   
   //States
   typedef enum 	   logic [2:0] {IDLE, FETCH0, FETCH1, WB0, WB1, FLUSH, WRITE_DHIT_COUNT, SET_FLUSHED} Statetype;
   Statetype curr_state, next_state;

   //frames
   dcacheset_t [7:0] d_frames;

   logic [2:0] 		   idx;
   logic [1:0] 		   byte_offset;
   logic 		   block_offset, next_block_offset;

   logic 		   dhit;
   word_t data;

   logic 		   NRU, LRU;
   logic 		   dirty;
   word_t dhit_count;

   //flushing signals
   logic 		   flushing;
   logic 		   block_idx;
   logic [2:0] 		   frame_idx;
   
   logic 		   begin_flush;

   //STD logic signals
   logic 		   miss;
   assign miss = (dcif.dmemREN == 1 || dcif.dmemWEN == 1 ) && dcif.dhit == 0;
   
   
   assign idx = dcif.dmemaddr[5:3];
   assign byte_offset = dcif.dmemaddr[1:0];
   assign block_offset = dcif.dmemaddr[2];
   assign next_block_offset = ~(dcif.dmemaddr[2]);

   assign LRU = d_frames[idx].lru;
   assign NRU = ~(d_frames[idx].lru);

   /*
   always_ff @ (posedge CLK, negedge nRST)
     begin
	if (~nRST)
	  begin
	     d_frames <= {default:0};
	     dhit_count <= 0;
	     curr_state <= IDLE;
	  end
	else
	  begin
	     if(dcif.halt == 1)
	       begin
		  if( (curr_state == WB1) && (next_state == FLUSH) )
		    begin
		       d_frames[frame_idx].frameblocks[block_idx].dirty <= 0;
		    end
		  curr_state <= next_state;
	       end
	     else if ( (dcif.dmemREN == 1 || dcif.dmemWEN == 1) && cif.dwait = 0)
	       begin
		  if
		       

   

   
   assign idx = dcif.dmemaddr[
    */



endmodule // dcache
