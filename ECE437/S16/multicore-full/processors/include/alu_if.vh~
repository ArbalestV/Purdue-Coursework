`ifndef ALU_IF_VH
`define ALU_IF_VH

`include "cpu_types_pkg.vh"

interface alu_if;
   // import types
   import cpu_types_pkg::*;

   word_t portA, portB;
   //logic [3:0] aluOP;
   aluop_t aluOP;
   word_t portO;
   logic       nFlag, oFlag, zFlag;

   //alu ports
   modport aluports (
		     input  aluOP, portA, portB,
		     output portO, nFlag, oFlag, zFlag
		     );
   //alu tb
   modport tb (
	       input  portO, nFlag, oFlag, zFlag,
	       output aluOP, portA, portB
	       );
endinterface // alu_if

`endif //  `ifndef ALU_IF_VH
	    
   
  
