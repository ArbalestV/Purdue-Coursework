`ifndef BRANCH_UNIT_IF_VH
`define BRANCH_UNIT_IF_VH

`include "cpu_types_pkg.vh"

interface branch_unit_if;

import cpu_types_pkg::*;

  //declarations
  logic        br, flush_de;//flush the decode stage when there is a branch
  word_t       rs, rt;
  aluop_t     instrOp;
  logic [15:0] imm, brTgt;

  //ports
  modport bu ( 
    input  rs, rt, imm, instrOp,
    output br, brTgt, flush_de
  );

  modport tb (
    input  br, brTgt, flush_de,
    output rs, rt, imm, instrOp
  );

endinterface

`endif
