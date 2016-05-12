/*
  Eric Villasenor
  evillase@gmail.com

  this block is the coherence protocol
  and artibtration for ram
*/

// interface include
`include "cache_control_if.vh"

// memory types
`include "cpu_types_pkg.vh"

module memory_control (
  input CLK, nRST,
  cache_control_if.cc ccif
);   
  // type import
  import cpu_types_pkg::*;

  // number of cpus for cc
   parameter CPUS = 2;
 
   //assign ccif.ramstore = ccif.dstore[0];
   //assign ccif.ramaddr = (ccif.dWEN[0] || ccif.dREN[0])? ccif.daddr[0] : ccif.iaddr[0];
   //assign ccif.ramWEN = ccif.dWEN[0];
   //assign ccif.ramREN = (ccif.dWEN[0])? 0 : ccif.dREN[0] || ccif.iREN[0];
   assign ccif.iload[0] = ccif.ramload;
   assign ccif.iload[1] = ccif.ramload;
   //assign ccif.dload[0] = ccif.ramload;
   //assign ccif.dload[1] = ccif.ramload;   

   
   //assign ccif.dwait[0] = ~((ccif.dREN[0] | ccif.dWEN[0]) & ccif.ramstate == ACCESS) ;
   //assign ccif.iwait[0] = ~(~(ccif.dREN[0] | ccif.dWEN[0]) & ccif.iREN[0] & ccif.ramstate == ACCESS);

   /****************************
    * Coherency Controller
    * 
    * ToDo: --
    * **************************/
   typedef enum logic [3:0] {IDLE, SNOOP, MtoC, CtoC, INVALIDATE, WRITE0, WRITE1, INSTR0, INSTR1, READ0, READ1, NOP} state_t;
   state_t state,nextstate;
   logic 	service, nextservice;
   logic 	clear_dwait;
   


   //for multicore
   logic 	nextprevInstrServed, prevInstrServed;
 
   
   //Next State Logic
   always_comb
     begin
	nextstate = state;
	nextservice = service;
	nextprevInstrServed = 1'b0;
	//clear_dwait = 1'b0;	
	case (state)	  
	  IDLE: 
	    begin // priority logic here
	       if ( ccif.cctrans[0] == 1'b1 ) begin
		  nextstate = SNOOP;
		  nextservice = 0;		  		  
	       end
	       else if ( ccif.cctrans[1] == 1'b1 ) begin
		  nextstate = SNOOP;
		  nextservice = 1;		  
	       end
	       else if ( ccif.dWEN[0] == 1'b1 ) begin
		  nextstate = WRITE0;		  
	       end
	       else if ( ccif.dWEN[1] == 1'b1 ) begin
		  nextstate = WRITE1;		  
	       end
	       else if ( ccif.dREN[0] == 1'b1 ) begin
		  nextstate = READ0;
	       end
	       else if ( ccif.dREN[1] == 1'b1 ) begin
		  nextstate = READ1;		  
	       end
	       else if ( ccif.iREN[0] & ccif.iREN[1] ) begin // dynamic instruction arbitration 
		  if ( prevInstrServed == 1'b1) begin
		     nextstate = INSTR0;
		  end
		  else begin
		     nextstate = INSTR1;		     
		  end
	       end
	       else if ( ccif.iREN[0] == 1'b1 ) begin
		  nextstate = INSTR0;	
		  nextprevInstrServed = 1'b0;		  
	       end
	       else if ( ccif.iREN[1] == 1'b1 ) begin
		  nextstate = INSTR1;	
		  nextprevInstrServed = 1'b1;				       
	       end
	       else begin
		  nextstate = IDLE;		  
	       end
	    end
	  SNOOP:
	    begin
	       if (ccif.cctrans[~service] == 1'b1 && ccif.dWEN[~service] == 0 ) begin
		  nextstate = MtoC;		  
	       end
	       else if ( ccif.cctrans[~service] == 1'b1 && ccif.dWEN[~service] == 1 ) begin
		  nextstate = CtoC;		  
	       end
	       else begin
		  nextstate = SNOOP;
	       end
	    end
	  MtoC:
	    begin
	       if ( ccif.dREN[service] == 0 ) begin
		  nextstate = INVALIDATE;		  
	       end
	       else begin
		  nextstate = MtoC;
	       end
	    end
	  CtoC:
	    begin
	       if ( ccif.dREN[service] == 0 ) begin
		  nextstate = INVALIDATE;
	       end
	       else begin
		  nextstate = CtoC;
	       end
	    end
	  INVALIDATE:
	    begin	  
	       //nextstate = IDLE;	       
	       nextstate = NOP; //dml
	       clear_dwait = 1'b1;	       
	    end
	  NOP: //dml
	    begin
	       nextstate = IDLE;	       
	    end
	  WRITE0:
	    begin
	       if ( ccif.dWEN[0] == 0 ) begin
		  nextstate = IDLE;
	       end
	       else begin
		  nextstate = WRITE0;
	       end
	    end
	  WRITE1:
	    begin
	       if ( ccif.dWEN[1] == 0 ) begin
		  nextstate = IDLE;
	       end
	       else begin
		  nextstate = WRITE1;
	       end
	    end
	  READ0:
	    begin
	       if ( ccif.dREN[0] == 1'b0 ) begin
		  nextstate = IDLE;
	       end
	       else begin
		  nextstate = READ0;
	       end
	    end
	  READ1:
	    begin
	       if ( ccif.dREN[1] == 1'b0 ) begin
		  nextstate = IDLE;		  
	       end
	       else begin
		  nextstate = READ1;
	       end
	    end
	  INSTR0:
	    begin
	       if ( ccif.ramstate == ACCESS ) begin
		  nextstate = IDLE;		  
	       end
	    end
	  INSTR1:
	    begin
	       if ( ccif.ramstate == ACCESS ) begin
		  nextstate = IDLE;		  
	       end
	    end
	  endcase
     end
   
   //State Machine
   always_ff @ (posedge CLK, negedge nRST)
     begin
	if ( ~nRST ) begin
	   state <= IDLE;
	   service <= 0;
	   prevInstrServed <= 0;	   	   
	end
	else begin
	   state <= nextstate;
	   service <= nextservice;
	   prevInstrServed <= nextprevInstrServed;	   
	end
     end // always_ff @

   word_t lastSnoop;
   logic lastCcWrite;   
   
   always_ff @ ( posedge CLK, negedge nRST )
     begin
	if ( ~nRST ) begin
	   lastSnoop <= 0;	 
	   lastCcWrite <= 0;	   
	end
	else begin
	   if ( state == SNOOP && nextstate == SNOOP ) begin 
	      lastSnoop <= ccif.daddr[service];
	      lastCcWrite <= ccif.ccwrite[service];	      
	   end
	   else begin
	      lastSnoop <= lastSnoop;
	      lastCcWrite <= lastCcWrite;	      
	   end
	end
     end
   //Output Logic - Moore
   always_comb
     begin
	ccif.ccwait[0] = 0;
	ccif.ccwait[1] = 0;
	ccif.ccinv[0] = 0;
	ccif.ccinv[1] = 0;
	ccif.ccsnoopaddr[0] = 0;
	ccif.ccsnoopaddr[1] = 0;
	ccif.dwait[0] = 1;
	ccif.dwait[1] = 1;
	ccif.iwait[0] = 1;
	ccif.iwait[1] = 1;

	ccif.dload[0] = ccif.ramload;	
	ccif.dload[1] = ccif.ramload;	
	
	ccif.ramaddr = 0;
	ccif.ramREN = 0;
	ccif.ramWEN = 0;
	ccif.ramstore = 0;
	
	case (state)
	  IDLE:
	    begin
	       ccif.ccsnoopaddr[~service] = lastSnoop; 
	    end
	  SNOOP:
	    begin
	       //ccif.ccwait[0] = 1;
	       //ccif.ccwait[1] = 1;
               ccif.ccwait[~service] = 1;
	       //ccif.ccinv[~service] = lastCcWrite; //dml   
	       ccif.ccinv[~service] = ccif.dWEN[service] && ccif.ccwrite[service];    // <===== not 	       
	       ccif.ccsnoopaddr[~service] = ccif.daddr[service];      
	    end
	  MtoC:
	    begin
	       ccif.dwait[service] = ccif.ramstate == ACCESS ? 0 : 1 ;

               /*pranav asked to comment out the following line*/
	       //ccif.dwait[~service] = ccif.ramstate == ACCESS ? 0 : 1 ; //acc to pranav this has to be commented out
               /*end of pranav asking to comment out the following line*/

	       //ccif.dload[service] = ccif.ramload;
	       ccif.ccwait[~service] = 1; //dml //was 1 	
	       ccif.ramaddr = ccif.daddr[service];
	       ccif.ramWEN = 1'b0;
	       ccif.ramREN = 1'b1;	       
	    end
	  CtoC:
	    begin
	       ccif.dwait[service] = ccif.ramstate == ACCESS ? 0 : 1 ;
	       ccif.dwait[~service] = ccif.ramstate == ACCESS ? 0 : 1 ;
	       ccif.dload[service] = ccif.dstore[~service];
	       ccif.ccwait[~service] = 1;       //dml  //was 1
	       ccif.ccsnoopaddr[~service] = ccif.daddr[service]; //snoop address issues
	       ccif.ramstore = ccif.dstore[~service];
	       ccif.ramaddr = ccif.daddr[~service];
	       ccif.ramWEN = 1'b1;
	       ccif.ramREN = 1'b0;
	    end
	  INVALIDATE:
	    begin
	       ccif.ccwait[~service] = 1;      
	       //ccif.ccinv[~service] = ccif.ccwrite[service]; //<===
	       ccif.ccinv[~service] = lastCcWrite;	       
	       //ccif.ccsnoopaddr[~service] = ccif.daddr[service];//dml3
	       ccif.ccsnoopaddr[~service] = lastSnoop;	       
	       ccif.ccinv[service] = 1'b1; 	       
	    end
	  WRITE0:
	    begin
	       ccif.dwait[0] = ccif.ramstate == ACCESS ? 0 : 1;
	       ccif.dwait[1] = 1;	       
	       ccif.ramaddr = ccif.daddr[0];
	       ccif.ramREN = 1'b0;
	       ccif.ramWEN = 1'b1;
	       ccif.ramstore = ccif.dstore[0];	       
	    end
	  WRITE1:
	    begin
	       ccif.dwait[1] = ccif.ramstate == ACCESS ? 0 : 1;
	       ccif.dwait[0] = 1;	       
	       ccif.ramaddr = ccif.daddr[1];
	       ccif.ramREN = 1'b0;
	       ccif.ramWEN = 1'b1;
	       ccif.ramstore = ccif.dstore[1];	       
	    end
	  READ0:
	    begin
	       ccif.dwait[0] = ccif.ramstate == ACCESS ? 0 : 1;

	       ccif.ramaddr = ccif.daddr[0];
	       ccif.ramREN = 1'b1;
	       ccif.ramWEN = 1'b0;
	       ccif.ramstore = 1'b0;	       
	    end
	  READ1:
	    begin
	       ccif.dwait[1] = ccif.ramstate == ACCESS ? 0 : 1;

	       ccif.ramaddr = ccif.daddr[1];
	       ccif.ramREN = 1'b1;
	       ccif.ramWEN = 1'b0;
	       ccif.ramstore = 1'b0;
	    end
	  INSTR0:
	    begin
	       ccif.iwait[0] = ccif.ramstate == ACCESS ? 0 : 1;
	       
	       ccif.ramaddr = ccif.iaddr[0];
	       ccif.ramREN = 1'b1;
	       ccif.ramWEN = 1'b0;
	       ccif.ramstore = 0;	       
	    end
	  INSTR1:
	    begin
	       ccif.iwait[1] = ccif.ramstate == ACCESS ? 0 : 1;	       
	       ccif.ramaddr = ccif.iaddr[1];	       
	       ccif.ramREN = 1'b1;
	       ccif.ramWEN = 1'b0;
	       ccif.ramstore = 0;
	    end
	  NOP:
	    begin
	       ccif.ccinv[~service] = lastCcWrite;    ////////////dml///////////
	       ccif.ccsnoopaddr[~service] = lastSnoop;
	    end
	endcase // case (state)
     end // always_comb
endmodule
