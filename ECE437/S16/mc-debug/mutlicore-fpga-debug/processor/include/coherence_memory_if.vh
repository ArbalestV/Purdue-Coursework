`ifndef COHERENCE_MEMORY_IF_VH
 `define COHERENCE_MEMORY_IF_VH

 `include "cpu_types_pkg.vh"

interface coherence_memory_if;

   import cpu_types_pkg::*;

   word_t dmemaddr_0, dmemaddr_1;
   word_t cacheBlock0, cacheBlock1;

   modport cc (
	       input dmemaddr_0, dmemaddr_1, cacheBlock0, cacheBlock1
	       );

   modport tb (
	       output dmemaddr_0, dmemaddr_1, cacheBlock0, cacheBlock1
	       );

endinterface // coherence_memory_if
`endif //  `ifndef COHERENCE_MEMORY_IF_VH

