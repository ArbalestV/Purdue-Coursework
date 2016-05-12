module request_unit(
		    input logic CLK, nRST, cu_halt, dR_REQ, dW_REQ, ihit, dhit,
		    output logic halt, imemREN, dmemREN, dmemWEN
		    );
   always_ff @(posedge CLK, negedge nRST)
     begin
	if (!nRST)
	  begin
	     imemREN <= 1'b1; //ihit is perennially 1 once reset
	     dmemREN <= 1'b0;
	     dmemWEN <= 1'b0;
	     halt <= 0;
	  end
	else if (cu_halt == 1'b1)
	  begin
	     imemREN <= 1'b1; //probable source of error, may be 0
	     dmemREN <= 1'b0;
	     dmemWEN <= 1'b0;
	     halt <= cu_halt;
	  end
	else if (dhit == 1'b1)
	  begin
	     dmemREN <= 1'b0;
	     dmemWEN <= 1'b0;
	     halt <= cu_halt;
	  end
	//when ihit and all the other cases, dmemren and dmemwen should take precedence over imemren
	else if (ihit == 1'b1)
	  begin
	     dmemREN <= dR_REQ;
	     dmemWEN <= dW_REQ;
	     halt <= cu_halt;
	  end
	/*else
	  begin
	     dmemREN <= dR_REQ;
	     dmemWEN <= dW_REQ;
	     halt <= cu_halt;
	  end*/
     end // always_ff @

   //assign halt = cu_halt;
endmodule // request_unit




