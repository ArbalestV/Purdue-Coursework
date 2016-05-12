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


   typedef enum logic [3:0] {IDLE, iREQ, SNOOP, MEM0, MEM1, CACHE0, CACHE1, WB0, WB1} StateType;
   StateType curr_state, next_state;

   logic 	req, serv;

   logic 	first_cycle_SNOOP;

   word_t dummy_load;


   logic 	WB1_SNOOP_high; //very specific to what the name described. Part of Mergesort debugging
   

   
   always_ff @ (posedge CLK, negedge nRST)
     begin
	//first_cycle_SNOOP <= ( (curr_state == IDLE) && (next_state == SNOOP) ) /*|| ( (curr_state == WB1) && (next_state == SNOOP) )*/; //----- ADDING NEW CODE FOR MERGESORT DEBUGGING. TO HAVE THE DWAIT ASSERTED WHERN THE MEMORY CONTROLLER GOES FROM WB1->SNOOP. WHEN MEM CONTROLLER GOES FROM WB1-SNOOP EVEN THEN YOU HAVE TO HAVE THE DWAIT SIGNAL ON HENCE YOU NEED AN OR CONDITION.
	if (nRST == 1'b0)
	  begin
	     first_cycle_SNOOP <= 1'b0;
	  end
	else
	  begin
	     first_cycle_SNOOP <= ( (curr_state == IDLE) && (next_state == SNOOP) ) /*|| ( (curr_state == WB1) && (next_state == SNOOP) )*/; //----- ADDING NEW CODE FOR MERGESORT DEBUGGING. TO HAVE THE DWAIT ASSERTED WHERN THE MEMORY CONTROLLER GOES FROM WB1->SNOOP. WHEN MEM CONTROLLER GOES FROM WB1-SNOOP EVEN THEN YOU HAVE TO HAVE THE DWAIT SIGNAL ON HENCE YOU NEED AN OR CONDITION.
	  end
     end

   //very specific to what the name described. Part of Mergesort debugging
   always_ff @ (posedge CLK, negedge nRST)
     begin
	/*WB1_SNOOP_high <= 1'b0;
	if ( (curr_state == WB1) && (next_state == SNOOP) )
	  begin
	     WB1_SNOOP_high <= 1'b1;
	  end
	else if (curr_state == SNOOP)
	  begin
	     WB1_SNOOP_high <= WB1_SNOOP_high;
	  end
	else
	  begin
	     WB1_SNOOP_high <= 1'b0;
	  end*/ // always_ff @
	if (nRST == 1'b0)
	  begin
	     WB1_SNOOP_high <= 1'b0;
	  end
	else
	  begin
	     if ( (curr_state == WB1) && (next_state == SNOOP) )
	       begin
		  WB1_SNOOP_high <= 1'b1;
	       end
	     else if (curr_state == SNOOP)
	       begin
		  WB1_SNOOP_high <= WB1_SNOOP_high; //before synthesis bug
		  //WB1_SNOOP_high <= WB1_SNOOP_high_tmp; //SYNTHESIS BUG
	       end
	     else
	       begin
		  WB1_SNOOP_high <= 1'b0;
	       end
	  end
     end // always_ff @
   //end of a very specific to what the name described. Part of Mergesort debugging
   
   
   //next state logic
   always_comb
     begin
	next_state = curr_state;
	case(curr_state)
	  IDLE:
	    begin
	       if( (ccif.iREN[0] || ccif.iREN[1]) && ~ccif.cctrans[0] && ~ccif.cctrans[1] && ~ccif.dWEN[0] && ~ccif.dWEN[1] && ~ccif.dREN[0] && ~ccif.dREN[1] )
		 begin
		    next_state = iREQ;
		 end
	       else if(ccif.dWEN[0] || ccif.dWEN[1])
		 begin
		    next_state = WB0;
		 end
	       else if( ccif.cctrans[0] || ccif.cctrans[1] )
		 begin
		    next_state = SNOOP;
		 end
	       else
		 begin
		    next_state = IDLE;
		 end
	    end // case: IDLE

	  iREQ:
	    begin
	       //experimentation ------ new if condition. originally was only the below two
	       /*if( ccif.cctrans[0] || ccif.cctrans[1] )
		 begin
		    next_state = SNOOP;
		 end
	       
	       
	       else */if( ccif.ramstate == ACCESS )
		 begin
		    next_state = IDLE;
		 end
	       else
		 begin
		    next_state = iREQ;
		 end
	    end // case: iREQ

	  SNOOP:
	    begin
	       //let me just stall for one extra cycle, since ccwrite[serv] will be determined only after that cycle. otherwise it goes to the MEM0 state regardless.
	       if (first_cycle_SNOOP == 1'b1)
		 begin
		    next_state = SNOOP;
		 end
	       else if(ccif.ccwrite[serv] == 0 /*|| (ccif.ccwrite[serv] == 1 && ccif.ccwrite[req] == 1)*/ ) //basically if he requestor is going to overwrite, then no point in writing back to and fetching from memory. Directly fetch something from memory and overwrite on top of that while invalidating the servicer's copy if it had earlier writen to the same block.
		 begin
		    next_state = MEM0;
		 end
	       else if(ccif.ccwrite[serv] == 1 /*&& ccif.ccwrite[req] == 0*/)
		 begin
		    next_state = CACHE0;
		 end
	       else
		 begin
		    next_state = SNOOP;
		 end
	    end // case: SNOOP

	  MEM0:
	    begin
	       if(ccif.ramstate == ACCESS)
		 begin
		    next_state = MEM1;
		 end
	       else
		 begin
		    next_state = MEM0;
		 end
	    end // case: MEM0

	  MEM1:
	    begin
	       if(ccif.ramstate == ACCESS)
		 begin
		    next_state = IDLE;
		 end
	       else
		 begin
		    next_state = MEM1;
		 end
	    end // case: MEM1

	  CACHE0:
	    begin
	       if(ccif.ramstate == ACCESS)
		 begin
		    next_state = CACHE1;
		 end
	       else
		 begin
		    next_state = CACHE0;
		 end
	    end // case: CACHE0

	  CACHE1:
	    begin
	       if(ccif.ramstate == ACCESS)
		 begin
		    next_state = IDLE;
		 end
	       else
		 begin
		    next_state = CACHE1;
		 end
	    end // case: CACHE1

	  WB0:
	    begin
	       if(ccif.ramstate == ACCESS)
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
	       if(ccif.ramstate == ACCESS && ccif.cctrans[req] == 0) //the flushing case -> very specific case
		 begin
		    next_state = IDLE;
		 end
	       else if(ccif.ramstate == ACCESS && ccif.cctrans[req] == 1)
		 begin
		    next_state = SNOOP;
		 end
	    end // case: WB1

	endcase // case (curr_state)
     end // always_comb begin
   

   //output logic
   always_comb
     begin
	ccif.iwait[0] = 1;
	ccif.iwait[1] = 1;
	ccif.dwait[0] = 1;
	ccif.dwait[1] = 1;
	ccif.iload[0] = 32'b0;
	ccif.iload[1] = 32'b0;
	ccif.dload[0] = 32'b0;
	ccif.dload[1] = 32'b0;
	ccif.ccwait[0] = 0;
	ccif.ccwait[1] = 0;
	ccif.ccinv[0] = 0;
	ccif.ccinv[1] = 0;
	ccif.ccsnoopaddr[0] = 32'b0;
	ccif.ccsnoopaddr[1] = 32'b0;
	ccif.ramstore = 32'b0;
	ccif.ramaddr = 32'b0;
	ccif.ramWEN = 0;
	ccif.ramREN = 0;
	
	case(curr_state)
	  IDLE:
	    begin
	       ccif.iwait[req] = 1;
	       ccif.iwait[serv] = 1;
	       ccif.dwait[req] = 1;
	       ccif.dwait[serv] = 1;
	       ccif.iload[req] = 32'b0;
	       ccif.iload[serv] = 32'b0;
	       ccif.dload[req] = 32'b0;
	       ccif.dload[serv] = 32'b0;
	       ccif.ccwait[req] = 0;
	       ccif.ccwait[serv] = 0;
	       ccif.ccinv[req] = 0;
	       ccif.ccinv[serv] = 0;
	       ccif.ccsnoopaddr[req] = 32'b0;
	       ccif.ccsnoopaddr[serv] = 32'b0;
	       ccif.ramstore = 32'b0;
	       ccif.ramaddr = 32'b0;
	       ccif.ramWEN = 0;
	       ccif.ramREN = 0;
	    end // case: IDLE

	  iREQ:
	    begin
	       ccif.iwait[req] = (ccif.ramstate != ACCESS);
	       ccif.iwait[serv] = 1;
	       ccif.dwait[req] = 1;
	       ccif.dwait[serv] = 1;
	       ccif.iload[req] = ccif.ramload;
	       ccif.iload[serv] = 32'b0;
	       ccif.dload[req] = 32'b0;
	       ccif.dload[serv] = 32'b0;
	       ccif.ccwait[req] = 0;
	       ccif.ccwait[serv] = 0;
	       ccif.ccinv[req] = 0;
	       ccif.ccinv[serv] = 0;
	       ccif.ccsnoopaddr[req] = 32'b0;
	       ccif.ccsnoopaddr[serv] = 32'b0;
	       ccif.ramstore = 32'b0;
	       ccif.ramaddr = ccif.iaddr[req];
	       ccif.ramWEN = 0;
	       ccif.ramREN = 1;
	    end // case: iREQ

	  SNOOP:
	    begin
	       ccif.iwait[req] = 1;
	       ccif.iwait[serv] = 1;
	       ccif.dwait[req] = /*1;*/(first_cycle_SNOOP) || (WB1_SNOOP_high);//change to 0 so requestor will go to next state and servicer will go to snoop_servicer -> not sure if thats true -- ADDED WB1_SNOOP_high for mergesort
	       ccif.dwait[serv] = 1;
	       ccif.iload[req] = 32'b0;
	       ccif.iload[serv] = 32'b0;
	       ccif.dload[req] = 32'b0;
	       ccif.dload[serv] = 32'b0;
	       ccif.ccwait[req] = 0;
	       ccif.ccwait[serv] = 1;
	       ccif.ccinv[req] = 0;
	       ccif.ccinv[serv] = ccif.ccwrite[req];
	       ccif.ccsnoopaddr[req] = 32'b0;
	       ccif.ccsnoopaddr[serv] = ccif.daddr[req];
	       ccif.ramstore = 32'b0;
	       ccif.ramaddr = 32'b0;
	       ccif.ramWEN = 0;
	       ccif.ramREN = 0;
	    end // case: SNOOP

	  MEM0:
	    begin
	       ccif.iwait[req] = 1;
	       ccif.iwait[serv] = 1;
	       ccif.dwait[req] = ccif.ramstate != ACCESS;
	       ccif.dwait[serv] = 1;
	       ccif.iload[req] = 32'b0;
	       ccif.iload[serv] = 32'b0;
	       ccif.dload[req] = ccif.ramload/*dummy_load*/;
	       ccif.dload[serv] = 32'b0;
	       ccif.ccwait[req] = 0;
	       ccif.ccwait[serv] = 0;
	       ccif.ccinv[req] = 0;
	       ccif.ccinv[serv] = 0;
	       ccif.ccsnoopaddr[req] = 32'b0;
	       ccif.ccsnoopaddr[serv] = 32'b0;
	       ccif.ramstore = 32'b0;
	       ccif.ramaddr = ccif.daddr[req];
	       ccif.ramWEN = 0;
	       ccif.ramREN = 1;
	    end // case: MEM0

	  MEM1:
	    begin
	       ccif.iwait[req] = 1;
	       ccif.iwait[serv] = 1;
	       ccif.dwait[req] = ccif.ramstate != ACCESS;
	       ccif.dwait[serv] = 1;
	       ccif.iload[req] = 32'b0;
	       ccif.iload[serv] = 32'b0;
	       ccif.dload[req] = ccif.ramload/*dummy_load*/;
	       ccif.dload[serv] = 32'b0;
	       ccif.ccwait[req] = 0;
	       ccif.ccwait[serv] = 0;
	       ccif.ccinv[req] = 0;
	       ccif.ccinv[serv] = 0;
	       ccif.ccsnoopaddr[req] = 32'b0;
	       ccif.ccsnoopaddr[serv] = 32'b0;
	       ccif.ramstore = 32'b0;
	       ccif.ramaddr = ccif.daddr[req];
	       ccif.ramWEN = 0;
	       ccif.ramREN = 1;
	    end // case: MEM1

	  CACHE0:
	    begin
	       ccif.iwait[req] = 1;
	       ccif.iwait[serv] = 1;
	       ccif.dwait[req] = ccif.ramstate != ACCESS;
	       ccif.dwait[serv] = ccif.ramstate != ACCESS;
	       ccif.iload[req] = 32'b0;
	       ccif.iload[serv] = 32'b0;
	       ccif.dload[req] = ccif.dstore[serv]/*dummy_load*/;
	       ccif.dload[serv] = 32'b0;
	       ccif.ccwait[req] = 0;
	       ccif.ccwait[serv] = 0;
	       ccif.ccinv[req] = 0;
	       ccif.ccinv[serv] = (ccif.ccwrite[req] == 1'b1) ? 1 : 0;
	       ccif.ccsnoopaddr[req] = 32'b0;
	       ccif.ccsnoopaddr[serv] = ccif.daddr[req];
	       ccif.ramstore = ccif.dstore[serv];
	       ccif.ramaddr = ccif.daddr[serv];
	       ccif.ramWEN = 1;
	       ccif.ramREN = 0;
	    end // case: CACHE0

	  CACHE1:
	    begin
	       ccif.iwait[req] = 1;
	       ccif.iwait[serv] = 1;
	       ccif.dwait[req] = ccif.ramstate != ACCESS;
	       ccif.dwait[serv] = ccif.ramstate != ACCESS;
	       ccif.iload[req] = 32'b0;
	       ccif.iload[serv] = 32'b0;
	       ccif.dload[req] = ccif.dstore[serv]/*dummy_load*/;
	       ccif.dload[serv] = 32'b0;
	       ccif.ccwait[req] = 0;
	       ccif.ccwait[serv] = 0;
	       ccif.ccinv[req] = 0;
	       ccif.ccinv[serv] = (ccif.ccwrite[req] == 1'b1) ? 1 : 0;
	       ccif.ccsnoopaddr[req] = 32'b0;
	       ccif.ccsnoopaddr[serv] = {ccif.daddr[req][31:3], !ccif.daddr[req][2], ccif.daddr[req][1:0]};
	       ccif.ramstore = ccif.dstore[serv];
	       ccif.ramaddr = ccif.daddr[serv];
	       ccif.ramWEN = 1;
	       ccif.ramREN = 0;
	    end // case: CACHE1

	  WB0:
	    begin
	       ccif.iwait[req] = 1;
	       ccif.iwait[serv] = 1;
	       ccif.dwait[req] = ccif.ramstate != ACCESS;
	       ccif.dwait[serv] = 1;
	       ccif.iload[req] = 32'b0;
	       ccif.iload[serv] = 32'b0;
	       ccif.dload[req] = 32'b0;
	       ccif.dload[serv] = 32'b0;
	       ccif.ccwait[req] = 0; //req is in the WB0 stage
	       ccif.ccwait[serv] = 0; //serv goes to SNOOP only after the memory controller gets to the SNOOP state thereby asserting ccwait[serv]
	       ccif.ccinv[req] = 0;
	       ccif.ccinv[serv] = 0;
	       ccif.ccsnoopaddr[req] = 32'b0;
	       ccif.ccsnoopaddr[serv] = 32'b0;
	       ccif.ramstore = ccif.dstore[req];
	       ccif.ramaddr = ccif.daddr[req];
	       ccif.ramWEN = 1;
	       ccif.ramREN = 0;
	    end // case: WB0

	  WB1:
	    begin
	       ccif.iwait[req] = 1;
	       ccif.iwait[serv] = 1;
	       ccif.dwait[req] = ccif.ramstate != ACCESS;
	       ccif.dwait[serv] = 1;
	       ccif.iload[req] = 32'b0;
	       ccif.iload[serv] = 32'b0;
	       ccif.dload[req] = 32'b0;
	       ccif.dload[serv] = 32'b0;
	       ccif.ccwait[req] = 0; //req is in the WB0 stage
	       ccif.ccwait[serv] = 0; //serv goes to SNOOP only after the memory controller gets to the SNOOP state thereby asserting ccwait[serv]
	       ccif.ccinv[req] = 0;
	       ccif.ccinv[serv] = 0;
	       ccif.ccsnoopaddr[req] = 32'b0;
	       ccif.ccsnoopaddr[serv] = 32'b0;
	       ccif.ramstore = ccif.dstore[req];
	       ccif.ramaddr = ccif.daddr[req];
	       ccif.ramWEN = 1;
	       ccif.ramREN = 0;
	    end // case: WB1	

	endcase // case (curr_state)
     end // always_comb begin

   always_ff @ (posedge CLK, negedge nRST)
     begin
	//ccif.dload[req] <= 32'b0;
	//ccif.dload[serv] <= 32'b0;
	dummy_load <= 32'b0;
	if (nRST == 1'b0)
	  begin
	     //ccif.dload[req] <= 32'b0;
	     //ccif.dload[serv] <= 32'b0;
	    
	     dummy_load <= 32'b0;
	  end
	else
	  begin
	     if (curr_state == MEM0)
	       begin
		  //ccif.dload[req] <= ccif.ramload;
		  //ccif.dload[serv] <= 32'b0;
		  if(ccif.ramstate == ACCESS)
		    begin
		       dummy_load <= ccif.ramload;
		    end
	       end
	     else if (curr_state == MEM1)
	       begin
		  //ccif.dload[req] <= ccif.ramload;
		  //ccif.iload[serv] <= 32'b0;
		  if(ccif.ramstate == ACCESS)
		    begin
		       dummy_load <= ccif.ramload;
		    end
	       end
	     else if (curr_state == CACHE0)
	       begin
		  //ccif.dload[req] <= ccif.dload[serv];
		  //ccif.dload[serv] <= 32'b0;
		  dummy_load <= ccif.dstore[serv];
	       end
	     else if (curr_state == CACHE1)
	       begin
		  //ccif.dload[req] <= ccif.dload[serv];
		  //ccif.dload[serv] <= 32'b0;
		  dummy_load <= ccif.dstore[serv];
	       end
	     else
	       begin
		  //ccif.dload[req] <= 32'b0;
		  //ccif.iload[serv] <= 32'b0;
		  dummy_load <= 32'b0;
	       end
	  end
     end // always_ff @
   
   
   always_ff @ (posedge CLK, negedge nRST)
     begin
	if(nRST == 1'b0)
	  begin
	     curr_state <= IDLE;
	     req <= 0;
	     serv <= 1;
	  end
	else
	  begin	     
	     if(curr_state == IDLE)
	       begin
		  if(ccif.cctrans[0] == 1'b1)
		    begin
		       req <= 0;
		       serv <= 1;
		    end
		  else if(ccif.cctrans[1] == 1'b1)
		    begin
		       req <= 1;
		       serv <= 0;
		    end
		  else if(ccif.dWEN[0] == 1'b1 || ccif.dREN[0] == 1'b1)
		    begin
		       req <= 0;
		       serv <= 1;
		    end
		  else if(ccif.dWEN[1] == 1'b1 || ccif.dREN[1] == 1'b1)
		    begin
		       req <= 1;
		       serv <= 0;
		    end
		  else if( (ccif.iREN[0] == 1'b1) && (ccif.iREN[1] == 1'b1))
		    begin
		       req <= ~req;
		       serv <= ~serv;
		    end
		  else if( (ccif.iREN[0] == 1'b1) && (ccif.iREN[1] == 1'b0))
		    begin
		       req <= 0;
		       serv <= 1;
		    end
		  else if( (ccif.iREN[1] == 1'b1) && (ccif.iREN[0] == 1'b0))
		    begin
		       req <= 1;
		       serv <= 0;
		    end
		  else
		    begin
		       req <= 0;
		       //req <= ~req;
		       serv <= 1;
		       //serv <= ~serv;
		    end		  
	       end // if (curr_state == IDLE)

	     
	     
	     else if (curr_state == SNOOP)
	       begin
		  req <= req; //these two should serve well for every case except for iREQ->IDLE
		  serv <= serv;
	       end
	     else if (curr_state == MEM0)
	       begin
		  req <= req; //these two should serve well for every case except for iREQ->IDLE
		  serv <= serv;
	       end
	     else if (curr_state == MEM1)
	       begin
		  req <= req; //these two should serve well for every case except for iREQ->IDLE
		  serv <= serv;
	       end
	     else if (curr_state == CACHE0)
	       begin
		  req <= req; //these two should serve well for every case except for iREQ->IDLE
		  serv <= serv;
	       end
	     else if (curr_state == CACHE1)
	       begin
		  req <= req; //these two should serve well for every case except for iREQ->IDLE
		  serv <= serv;
	       end
	     else if (curr_state == WB0)
	       begin
		  req <= req; //these two should serve well for every case except for iREQ->IDLE
		  serv <= serv;
	       end
	     else if (curr_state == WB1)
	       begin
		  req <= req; //these two should serve well for every case except for iREQ->IDLE
		  serv <= serv;
	       end
	     else if (curr_state == iREQ)
	       begin
		  req <= req; //these two should serve well for every case except for iREQ->IDLE
		  serv <= serv;
	       end
	     
	     curr_state <= next_state;
	     
	  end // else: !if(nRST == 1'b0)
     end // always_ff @ (posedge CLK, negedge nRST)
   
endmodule
