`include "cpu_types_pkg.vh"
`timescale 1 ns / 1 ns
import cpu_types_pkg::*;
module forwarding_unit_tb;
   parameter PERIOD = 10;
   forwarding_unit_if fuif();
   test #(.PERIOD (PERIOD)) PROG 
   (
    .fuif
   );

`ifndef MAPPED
   forwarding_unit DUT(fuif);
`else
   forwarding_unit DUT(
		   .\huif.ex_regRt (fuif.ex_regRt),
		   .\huif.ex_regRs (fuif.ex_regRs),
		   .\huif.mem_regRd (fuif.mem_regRd),
		   .\huif.wb_regRd (fuif.wb_regRd),
		   .\huif.mem_RegWrite (fuif.mem_RegWrite),
		   .\huif.wb_RegWrite (fuif.wb_RegWrite),
		   .\huif.ForwardA (fuif.ForwardA),
		   .\huif.ForwardB (fuif.ForwardB)
		   );
`endif // !`ifndef MAPPED
endmodule // forwarding_unit_tb

program test 
(
 forwarding_unit_if.tb fuif
);
   parameter PERIOD = 10;

  initial
    begin
       //TEST 1
       
       fuif.mem_RegWrite = 1'b1;
       fuif.mem_regRd = 5;
       fuif.ex_regRt = 4;       
       fuif.ex_regRs = 5;
       fuif.wb_RegWrite = 1'b1;
       fuif.wb_regRd = 5;
       #(PERIOD/2)
       if ( fuif.ForwardA == 2'b10 && fuif.ForwardB == 2'b00 )
	 $display("Test 1 Passed!");
       else
	 $error("Test 1 Failed!");
       
       #(PERIOD/2)
       //TEST 2
       
       fuif.ex_regRt = 5;
       #(PERIOD/2)

       if (fuif.ForwardA == 2'b10 && fuif.ForwardB == 2'b10 )
	 $display("Test 2 Passed!");
       else
	 $error("Test 2 Failed!");

       #(PERIOD/2)

       //TEST 3
       fuif.ex_regRs = 4;
       #(PERIOD/2)
       if (fuif.ForwardA == 2'b00 && fuif.ForwardB == 2'b10 )
	 $display("Test 3 Passed!");
       else
	 $error("Test 3 Failed!");
       #(PERIOD/2)

       //TEST 4
       fuif.wb_regRd = 4;
       #(PERIOD/2)
       if (fuif.ForwardA == 2'b01 && fuif.ForwardB == 2'b10 )
	 $display("Test 4 Passed!");
       else
	 $error("Test 4 Failed!");
       #(PERIOD/2)

       //TEST 5
       fuif.ex_regRt = 3;
       fuif.wb_regRd = 3;
       #(PERIOD/2)
       if (fuif.ForwardA == 2'b01 && fuif.ForwardB == 2'b01 )
	 $display("Test 5 Passed!");
       else
	 $error("Test 5 Failed!");
       #(PERIOD/2)

       //TEST 6
       fuif.wb_RegWrite = 0;       
       fuif.mem_RegWrite = 0;
       #(PERIOD/2)
       if (fuif.ForwardA == 2'b00 && fuif.ForwardB == 2'b00 )
	 $display("Test 6 Passed!");
       else
	 $error("Test 6 Failed!");

       #(PERIOD/2)
       fuif.wb_RegWrite = 1;
       fuif.mem_RegWrite = 1;                     
       
    end
   
endprogram // test
   
