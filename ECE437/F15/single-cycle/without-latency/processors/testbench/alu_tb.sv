// mapped needs this
`include "alu_if.vh"

//mapped timing needs this. 1 ns is too fast
`timescale 1 ns / 1 ns

module alu_tb;
   parameter PERIOD = 10;

   //interface
   alu_if alpts ();
   //test program
   test #(.PERIOD (PERIOD)) PROG (
				  .alpts
				  );
   // DUT
`ifndef MAPPED
   alu DUT(alpts);
`else
   alu DUT(
	   .\alpts.portA (alpts.portA),
	   .\alpts.portB (alpts.portB),
	   .\alpts.aluOP (alpts.aluOP),
	   .\alpts.portO (alpts.portO),
	   .\alpts.nFlag (alpts.nFlag),
	   .\alpts.oFlag (alpts.oFlag),
	   .\alpts.zFlag (alpts.zFlag)
	   );
`endif // !`ifndef MAPPED
endmodule // alu_tb


program test (
	      alu_if.tb alpts
	      );
   parameter PERIOD = 10;
   initial begin
      //SLL
      alpts.aluOP = 0;
      alpts.portA = 40;
      alpts.portB = 3;
      #(PERIOD * 3)

      //SRL
      alpts.aluOP = 1;
      alpts.portA = 40;
      alpts.portB = 3;
      #(PERIOD * 3)

      //ADD
      alpts.aluOP = 2;
      alpts.portA = 40;
      alpts.portB = 45;
      #(PERIOD * 3)
      alpts.portA = 2147483600;
      alpts.portB = 80000;
      #(PERIOD * 3)
      alpts.portA = 2147483600;
      alpts.portB = -80000;
      #(PERIOD * 3)
      alpts.portB = -2147483600;
      alpts.portA = 80000;
      #(PERIOD * 3)

      //SUB
      alpts.aluOP = 3;
      alpts.portA = 40;
      alpts.portB = 46;
      #(PERIOD * 3)
      alpts.portA = 46;
      alpts.portB = 40;
      #(PERIOD * 3)
      alpts.portA = -2147483600;
      alpts.portB = -80000;
      #(PERIOD * 3)
      alpts.portA = 2147483600;
      alpts.portB = -80000;
      #(PERIOD * 3)
      alpts.portB = -2147483600;
      alpts.portA = 80000;
      #(PERIOD * 3)
      alpts.portA = 46;
      alpts.portB = -40;
      #(PERIOD * 3)

      //AND
      alpts.aluOP = 4;
      alpts.portA = 46;
      alpts.portB = 40;
      #(PERIOD * 3)

      //OR
      alpts.aluOP = 5;
      alpts.portA = 46;
      alpts.portB = 40;
      #(PERIOD * 3)

      //XOR
      alpts.aluOP = 6;
      alpts.portA = 46;
      alpts.portB = 40;
      #(PERIOD * 3)

      //NOR
      alpts.aluOP = 7;
      alpts.portA = 46;
      alpts.portB = 40;
      #(PERIOD * 3)
   
      //SLT
      alpts.aluOP = 10;
      alpts.portA = 46;
      alpts.portB = 40;
      #(PERIOD * 3)
      alpts.portA = 40;
      alpts.portB = 46;
      #(PERIOD * 3)
      alpts.portA = -46;
      alpts.portB = -40;
      #(PERIOD * 3)
      alpts.portA = -40;
      alpts.portB = -46;
      #(PERIOD * 3)
      alpts.portA = 46;
      alpts.portB = -40;
      #(PERIOD * 3)
      alpts.portA = -46;
      alpts.portB = 40;
      #(PERIOD * 3)

      //SLTU
      alpts.aluOP = 11;
      alpts.portA = 46;
      alpts.portB = 40;
      #(PERIOD * 3)
      alpts.portA = 40;
      alpts.portB = 4848;
      #(PERIOD * 3)
      alpts.portA = 20;
      alpts.portB = 3;


   end // initial begin


endprogram // test
   

