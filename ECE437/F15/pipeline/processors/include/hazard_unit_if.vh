`ifndef HAZARD_UNIT_IF_VH
`define HAZARD_UNIT_IF_VH

`include "cpu_types_pkg.vh"

interface hazard_unit_if;

import cpu_types_pkg::*;

  //declarations
  logic     ex_memread, ex_memwrite, nop;
  regbits_t de_regRs, de_regRt, ex_regRd, ex_regRt, ex_wsel, mem_regRd;

  //ports
  modport hu ( 
    input  ex_memread, ex_memwrite, ex_regRt, ex_regRd, ex_wsel, de_regRt, de_regRs, mem_regRd, 
    output nop //this is going to the first 3 latches and works along with the enable latches signal
  );

  modport tb (
    input  nop,
    output ex_memread, ex_memwrite, ex_regRt, ex_regRd, ex_wsel, de_regRt, de_regRs, mem_regRd
  );
  
endinterface

`endif
