`include "hazard_detection_unit_if.vh"

module hazard_detection_unit
  (
   hazard_detection_unit_if.hdu hduif
   );

   always_comb
     begin
	//stall logic
	if (hduif.ex_dR_REQ)
	  begin
	     hduif.stall = 1;
	  end
	/*	
	if (hduif.ex_dR_REQ && ( (hduif.ex_regRt == hduif.de_regRs) || (hduif.ex_regRt == hduif.de_regRt) ) )
	  begin
	     hduif.stall = 1;
	  end
	 */
	/*
	else if ( (hduif.ex_dR_REQ && hduif.de_dR_REQ) ||
	          (hduif.ex_dR_REQ && hduif.de_dW_REQ) ||
	          (hduif.ex_dW_REQ && hduif.de_dR_REQ) ||
	          (hduif.ex_dW_REQ && hduif.de_dW_REQ) )
	  begin
	     hduif.stall = 1;
	  end*/ // if ((hduif.ex_dR_REQ && ((hduif.ex_regRt == hduif.de_regRs) || (hduif.ex_regRt == hduif.de_regRt)))...
	else
	  begin
	     hduif.stall = 0;
	  end
     end // always_comb

endmodule // hazard_detection_unit

	     
