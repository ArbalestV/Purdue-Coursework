`timescale 1 ns / 1 ns
module request_unit_tb();
   logic CLK, nRST;
   logic cu_halt, dR_REQ, dW_REQ, ihit, dhit;
   logic halt, imemREN, dmemREN, dmemWEN;
   request_unit DUT
     (
      .CLK(CLK),
      .nRST(nRST),
      .cu_halt(cu_halt),
      .dR_REQ(dR_REQ),
      .dW_REQ(dW_REQ),
      .ihit(ihit),
      .dhit(dhit),
      .halt(halt),
      .imemREN(imemREN),
      .dmemREN(dmemREN),
      .dmemWEN(dmemWEN)
      );
   parameter PERIOD = 10;
   parameter delay = 2;
   //always #(PERIOD / 2) CLK++;
   always begin
      CLK = 1'b0;
      #(PERIOD / 2);
      CLK = 1'b1;
      #(PERIOD / 2);
   end
   
   initial begin
      nRST = 0;
      dhit = 1;
      ihit = 1;
      cu_halt = 1;
      dR_REQ = 1;
      dW_REQ = 0;
      #(delay);
      cu_halt = 0;
      dR_REQ = 0;
      dW_REQ = 1;
      #(PERIOD);
      cu_halt = 1;
      dR_REQ = 1;
      #(PERIOD);
      nRST = 1;
      #(PERIOD);
      cu_halt = 0;
      ihit = 1;
      dhit = 0;
      #(PERIOD);
      ihit = 0;
      dhit = 1;
      #(PERIOD);
      dhit = 0;
      dW_REQ = 1;
      #(PERIOD);
      ihit = 1;
      #(PERIOD);
      dhit = 1;
      #(PERIOD);
   end // initial begin
endmodule // request_unit_tb

      
      
      
