onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate /system_tb/CLK
add wave -noupdate /system_tb/nRST
add wave -noupdate -divider States
add wave -noupdate /system_tb/DUT/CPU/CC/req
add wave -noupdate /system_tb/DUT/CPU/CC/serv
add wave -noupdate -expand -group {MEMORY CONTROL} /system_tb/DUT/CPU/CC/curr_state
add wave -noupdate -expand -group {MEMORY CONTROL} /system_tb/DUT/CPU/CC/next_state
add wave -noupdate -divider DP0
add wave -noupdate /system_tb/DUT/CPU/DP0/op_D
add wave -noupdate /system_tb/DUT/CPU/DP0/op_EX
add wave -noupdate /system_tb/DUT/CPU/DP0/op_M
add wave -noupdate /system_tb/DUT/CPU/DP0/op_WB
add wave -noupdate -expand -group ICACHE0 /system_tb/DUT/CPU/CM0/ICACHE/current_state
add wave -noupdate -expand -group ICACHE0 /system_tb/DUT/CPU/CM0/ICACHE/next_state
add wave -noupdate -expand -group DCACHE0 /system_tb/DUT/CPU/CM0/DCACHE/curr_state
add wave -noupdate -expand -group DCACHE0 /system_tb/DUT/CPU/CM0/DCACHE/next_state
add wave -noupdate -divider DP1
add wave -noupdate /system_tb/DUT/CPU/DP1/op_D
add wave -noupdate /system_tb/DUT/CPU/DP1/op_EX
add wave -noupdate /system_tb/DUT/CPU/DP1/op_M
add wave -noupdate /system_tb/DUT/CPU/DP1/op_WB
add wave -noupdate -expand -group ICACHE1 /system_tb/DUT/CPU/CM1/ICACHE/current_state
add wave -noupdate -expand -group ICACHE1 /system_tb/DUT/CPU/CM1/ICACHE/next_state
add wave -noupdate -expand -group DCACHE1 /system_tb/DUT/CPU/CM1/DCACHE/curr_state
add wave -noupdate -expand -group DCACHE1 /system_tb/DUT/CPU/CM1/DCACHE/next_state
add wave -noupdate /system_tb/DUT/CPU/DP1/dpif/dmemWEN
add wave -noupdate /system_tb/DUT/CPU/DP1/dpif/dmemREN
add wave -noupdate /system_tb/DUT/CPU/DP1/dpif/dmemload
add wave -noupdate /system_tb/DUT/CPU/DP1/dpif/dmemstore
add wave -noupdate /system_tb/DUT/CPU/DP1/dpif/dmemaddr
add wave -noupdate -divider MemoryController
add wave -noupdate -expand -group ccif -expand /system_tb/DUT/CPU/CC/ccif/iwait
add wave -noupdate -expand -group ccif -expand /system_tb/DUT/CPU/CC/ccif/dwait
add wave -noupdate -expand -group ccif -expand /system_tb/DUT/CPU/CC/ccif/iREN
add wave -noupdate -expand -group ccif -expand /system_tb/DUT/CPU/CC/ccif/dREN
add wave -noupdate -expand -group ccif -expand /system_tb/DUT/CPU/CC/ccif/dWEN
add wave -noupdate -expand -group ccif /system_tb/DUT/CPU/CC/ccif/iload
add wave -noupdate -expand -group ccif -expand /system_tb/DUT/CPU/CC/ccif/dload
add wave -noupdate -expand -group ccif -expand /system_tb/DUT/CPU/CC/ccif/dstore
add wave -noupdate -expand -group ccif /system_tb/DUT/CPU/CC/ccif/iaddr
add wave -noupdate -expand -group ccif -expand /system_tb/DUT/CPU/CC/ccif/daddr
add wave -noupdate -expand -group ccif -expand /system_tb/DUT/CPU/CC/ccif/ccwait
add wave -noupdate -expand -group ccif /system_tb/DUT/CPU/CC/ccif/ccinv
add wave -noupdate -expand -group ccif /system_tb/DUT/CPU/CC/ccif/ccwrite
add wave -noupdate -expand -group ccif -expand /system_tb/DUT/CPU/CC/ccif/cctrans
add wave -noupdate -expand -group ccif /system_tb/DUT/CPU/CC/ccif/ccsnoopaddr
add wave -noupdate -expand -group ccif /system_tb/DUT/CPU/CC/ccif/ramWEN
add wave -noupdate -expand -group ccif /system_tb/DUT/CPU/CC/ccif/ramREN
add wave -noupdate -expand -group ccif /system_tb/DUT/CPU/CC/ccif/ramstate
add wave -noupdate -expand -group ccif /system_tb/DUT/CPU/CC/ccif/ramaddr
add wave -noupdate -expand -group ccif /system_tb/DUT/CPU/CC/ccif/ramstore
add wave -noupdate -expand -group ccif /system_tb/DUT/CPU/CC/ccif/ramload
add wave -noupdate -expand -group {Memory Control} /system_tb/DUT/CPU/CC/curr_state
add wave -noupdate -expand -group {Memory Control} /system_tb/DUT/CPU/CC/next_state
add wave -noupdate -expand -group {Memory Control} /system_tb/DUT/CPU/CC/req
add wave -noupdate -expand -group {Memory Control} /system_tb/DUT/CPU/CC/serv
add wave -noupdate -divider Core0
add wave -noupdate /system_tb/DUT/CPU/DP0/CLK
add wave -noupdate /system_tb/DUT/CPU/DP0/nRST
add wave -noupdate -expand -group DP0 /system_tb/DUT/CPU/dcif0/halt
add wave -noupdate -expand -group DP0 -group ProgramCounter0 /system_tb/DUT/CPU/DP0/PROGRAM_COUNTER/CLK
add wave -noupdate -expand -group DP0 -group ProgramCounter0 /system_tb/DUT/CPU/DP0/PROGRAM_COUNTER/nRST
add wave -noupdate -expand -group DP0 -group ProgramCounter0 /system_tb/DUT/CPU/DP0/PROGRAM_COUNTER/pc_EN
add wave -noupdate -expand -group DP0 -group ProgramCounter0 /system_tb/DUT/CPU/DP0/PROGRAM_COUNTER/pc_in
add wave -noupdate -expand -group DP0 -group ProgramCounter0 /system_tb/DUT/CPU/DP0/PROGRAM_COUNTER/pc_out
add wave -noupdate -expand -group DP0 /system_tb/DUT/CPU/DP0/pc_next
add wave -noupdate -expand -group DP0 /system_tb/DUT/CPU/DP0/pc
add wave -noupdate -expand -group DP0 /system_tb/DUT/CPU/DP0/dpif/imemaddr
add wave -noupdate -expand -group DP0 /system_tb/DUT/CPU/DP0/instruction
add wave -noupdate -expand -group DP0 /system_tb/DUT/CPU/DP0/instruction_D
add wave -noupdate -expand -group DP0 /system_tb/DUT/CPU/DP0/op_D
add wave -noupdate -expand -group DP0 /system_tb/DUT/CPU/DP0/instruction_EX
add wave -noupdate -expand -group DP0 /system_tb/DUT/CPU/DP0/op_EX
add wave -noupdate -expand -group DP0 /system_tb/DUT/CPU/DP0/instruction_M
add wave -noupdate -expand -group DP0 /system_tb/DUT/CPU/DP0/op_M
add wave -noupdate -expand -group DP0 /system_tb/DUT/CPU/DP0/op_WB
add wave -noupdate -expand -group aluif0 /system_tb/DUT/CPU/DP0/aluif/portA
add wave -noupdate -expand -group aluif0 /system_tb/DUT/CPU/DP0/aluif/portB
add wave -noupdate -expand -group aluif0 /system_tb/DUT/CPU/DP0/aluif/aluOP
add wave -noupdate -expand -group aluif0 /system_tb/DUT/CPU/DP0/aluif/portO
add wave -noupdate -expand -group aluif0 /system_tb/DUT/CPU/DP0/aluif/nFlag
add wave -noupdate -expand -group aluif0 /system_tb/DUT/CPU/DP0/aluif/oFlag
add wave -noupdate -expand -group aluif0 /system_tb/DUT/CPU/DP0/aluif/zFlag
add wave -noupdate -expand -group rfif0 /system_tb/DUT/CPU/DP0/rfif/WEN
add wave -noupdate -expand -group rfif0 /system_tb/DUT/CPU/DP0/rfif/wsel
add wave -noupdate -expand -group rfif0 /system_tb/DUT/CPU/DP0/rfif/rsel1
add wave -noupdate -expand -group rfif0 /system_tb/DUT/CPU/DP0/rfif/rsel2
add wave -noupdate -expand -group rfif0 /system_tb/DUT/CPU/DP0/rfif/wdat
add wave -noupdate -expand -group rfif0 /system_tb/DUT/CPU/DP0/rfif/rdat1
add wave -noupdate -expand -group rfif0 /system_tb/DUT/CPU/DP0/rfif/rdat2
add wave -noupdate -group cuif0 /system_tb/DUT/CPU/DP0/cuif/imemload
add wave -noupdate -group cuif0 /system_tb/DUT/CPU/DP0/cuif/j
add wave -noupdate -group cuif0 /system_tb/DUT/CPU/DP0/cuif/jr
add wave -noupdate -group cuif0 /system_tb/DUT/CPU/DP0/cuif/jal
add wave -noupdate -group cuif0 /system_tb/DUT/CPU/DP0/cuif/beq
add wave -noupdate -group cuif0 /system_tb/DUT/CPU/DP0/cuif/bne
add wave -noupdate -group cuif0 /system_tb/DUT/CPU/DP0/cuif/halt
add wave -noupdate -group cuif0 /system_tb/DUT/CPU/DP0/cuif/RegDst
add wave -noupdate -group cuif0 /system_tb/DUT/CPU/DP0/cuif/ALUSrc
add wave -noupdate -group cuif0 /system_tb/DUT/CPU/DP0/cuif/MemToReg
add wave -noupdate -group cuif0 /system_tb/DUT/CPU/DP0/cuif/RegWrite
add wave -noupdate -group cuif0 /system_tb/DUT/CPU/DP0/cuif/ALUOp
add wave -noupdate -group cuif0 /system_tb/DUT/CPU/DP0/cuif/ExtOp
add wave -noupdate -group cuif0 /system_tb/DUT/CPU/DP0/cuif/ShiftOp
add wave -noupdate -group cuif0 /system_tb/DUT/CPU/DP0/cuif/lui
add wave -noupdate -group cuif0 /system_tb/DUT/CPU/DP0/cuif/dR_REQ
add wave -noupdate -group cuif0 /system_tb/DUT/CPU/DP0/cuif/dW_REQ
add wave -noupdate -expand -group dpif0 /system_tb/DUT/CPU/DP0/dpif/halt
add wave -noupdate -expand -group dpif0 /system_tb/DUT/CPU/DP0/dpif/ihit
add wave -noupdate -expand -group dpif0 /system_tb/DUT/CPU/DP0/dpif/imemREN
add wave -noupdate -expand -group dpif0 /system_tb/DUT/CPU/DP0/dpif/imemload
add wave -noupdate -expand -group dpif0 /system_tb/DUT/CPU/DP0/dpif/imemaddr
add wave -noupdate -expand -group dpif0 /system_tb/DUT/CPU/DP0/dpif/dhit
add wave -noupdate -expand -group dpif0 /system_tb/DUT/CPU/DP0/dpif/datomic
add wave -noupdate -expand -group dpif0 /system_tb/DUT/CPU/DP0/dpif/dmemREN
add wave -noupdate -expand -group dpif0 /system_tb/DUT/CPU/DP0/dpif/dmemWEN
add wave -noupdate -expand -group dpif0 /system_tb/DUT/CPU/DP0/dpif/flushed
add wave -noupdate -expand -group dpif0 /system_tb/DUT/CPU/DP0/dpif/dmemload
add wave -noupdate -expand -group dpif0 /system_tb/DUT/CPU/DP0/dpif/dmemstore
add wave -noupdate -expand -group dpif0 /system_tb/DUT/CPU/DP0/dpif/dmemaddr
add wave -noupdate -expand -group fuif0 /system_tb/DUT/CPU/DP0/fuif/rs_EX
add wave -noupdate -expand -group fuif0 /system_tb/DUT/CPU/DP0/fuif/rt_EX
add wave -noupdate -expand -group fuif0 /system_tb/DUT/CPU/DP0/fuif/wsel_M
add wave -noupdate -expand -group fuif0 /system_tb/DUT/CPU/DP0/fuif/wsel_WB
add wave -noupdate -expand -group fuif0 /system_tb/DUT/CPU/DP0/fuif/WEN_M
add wave -noupdate -expand -group fuif0 /system_tb/DUT/CPU/DP0/fuif/WEN_WB
add wave -noupdate -expand -group fuif0 /system_tb/DUT/CPU/DP0/fuif/forward_A
add wave -noupdate -expand -group fuif0 /system_tb/DUT/CPU/DP0/fuif/forward_B
add wave -noupdate -expand -group fuif0 /system_tb/DUT/CPU/DP0/fuif/is_ITYPE
add wave -noupdate -expand -group fuif0 /system_tb/DUT/CPU/DP0/fuif/is_bne_or_beq_M
add wave -noupdate -expand -group fuif0 /system_tb/DUT/CPU/DP0/fuif/dREN_M
add wave -noupdate -expand -group fuif0 /system_tb/DUT/CPU/DP0/fuif/bubble_lw_f
add wave -noupdate -expand -group sfif0 /system_tb/DUT/CPU/DP0/sfif/dWEN_EX
add wave -noupdate -expand -group sfif0 /system_tb/DUT/CPU/DP0/sfif/rt_EX
add wave -noupdate -expand -group sfif0 /system_tb/DUT/CPU/DP0/sfif/rd_M
add wave -noupdate -expand -group sfif0 /system_tb/DUT/CPU/DP0/sfif/rd_WB
add wave -noupdate -expand -group sfif0 /system_tb/DUT/CPU/DP0/sfif/forwarding_required
add wave -noupdate /system_tb/DUT/CPU/DP0/sw_forwarding_output
add wave -noupdate /system_tb/DUT/CPU/DP0/porto_M
add wave -noupdate /system_tb/DUT/CPU/CM1/DCACHE/which_snoop
add wave -noupdate /system_tb/DUT/CPU/DP0/REGISTER_FILE/rfile
add wave -noupdate -group Icache0 /system_tb/DUT/CPU/CM0/ICACHE/index
add wave -noupdate -group Icache0 /system_tb/DUT/CPU/CM0/ICACHE/ihit
add wave -noupdate -group Icache0 /system_tb/DUT/CPU/CM0/ICACHE/imemload
add wave -noupdate -group Icache0 /system_tb/DUT/CPU/CM0/ICACHE/iREN
add wave -noupdate -group Icache0 /system_tb/DUT/CPU/CM0/ICACHE/current_state
add wave -noupdate -group Icache0 /system_tb/DUT/CPU/CM0/ICACHE/next_state
add wave -noupdate -group Icache0 -expand /system_tb/DUT/CPU/CM0/ICACHE/icacheset
add wave -noupdate -expand -group DCache0 -expand -group cif0 /system_tb/DUT/CPU/CM0/DCACHE/cif/iwait
add wave -noupdate -expand -group DCache0 -expand -group cif0 /system_tb/DUT/CPU/CM0/DCACHE/cif/dwait
add wave -noupdate -expand -group DCache0 -expand -group cif0 /system_tb/DUT/CPU/CM0/DCACHE/cif/iREN
add wave -noupdate -expand -group DCache0 -expand -group cif0 /system_tb/DUT/CPU/CM0/DCACHE/cif/dREN
add wave -noupdate -expand -group DCache0 -expand -group cif0 /system_tb/DUT/CPU/CM0/DCACHE/cif/dWEN
add wave -noupdate -expand -group DCache0 -expand -group cif0 /system_tb/DUT/CPU/CM0/DCACHE/cif/iload
add wave -noupdate -expand -group DCache0 -expand -group cif0 /system_tb/DUT/CPU/CM0/DCACHE/cif/dload
add wave -noupdate -expand -group DCache0 -expand -group cif0 /system_tb/DUT/CPU/CM0/DCACHE/cif/dstore
add wave -noupdate -expand -group DCache0 -expand -group cif0 /system_tb/DUT/CPU/CM0/DCACHE/cif/iaddr
add wave -noupdate -expand -group DCache0 -expand -group cif0 /system_tb/DUT/CPU/CM0/DCACHE/cif/daddr
add wave -noupdate -expand -group DCache0 -expand -group cif0 /system_tb/DUT/CPU/CM0/DCACHE/cif/ccwait
add wave -noupdate -expand -group DCache0 -expand -group cif0 /system_tb/DUT/CPU/CM0/DCACHE/cif/ccinv
add wave -noupdate -expand -group DCache0 -expand -group cif0 /system_tb/DUT/CPU/CM0/DCACHE/cif/ccwrite
add wave -noupdate -expand -group DCache0 -expand -group cif0 /system_tb/DUT/CPU/CM0/DCACHE/cif/cctrans
add wave -noupdate -expand -group DCache0 -expand -group cif0 /system_tb/DUT/CPU/CM0/DCACHE/cif/ccsnoopaddr
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/CLK
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/nRST
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/dcif/dhit
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/dcif/dmemREN
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/dcif/dmemWEN
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/dcif/dmemload
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/curr_state
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/next_state
add wave -noupdate -expand -group DCache0 -expand /system_tb/DUT/CPU/CM0/DCACHE/dcacheset
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/byte_offset
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/block_offset
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/index
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/dmemaddr
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/dcif0/imemREN
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/dcif0/dmemREN
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/dcif0/dmemWEN
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/tag_match1
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/ReadHit1
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/WriteHit1
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/tag_match2
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/ReadHit2
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/WriteHit2
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/valid1
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/valid2
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/dirty1
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/dirty2
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/hit1
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/hit2
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/LRU
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/snoop_tag_hit
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/snoop_block_invalid
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/which_snoop
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/curr_frame
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/curr_block
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/M_access
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/S_access
add wave -noupdate -divider Core1
add wave -noupdate /system_tb/DUT/CPU/DP1/CLK
add wave -noupdate /system_tb/DUT/CPU/DP1/nRST
add wave -noupdate -expand -group DP1 /system_tb/DUT/CPU/dcif1/halt
add wave -noupdate -expand -group DP1 -group ProramCounter1 /system_tb/DUT/CPU/DP1/PROGRAM_COUNTER/CLK
add wave -noupdate -expand -group DP1 -group ProramCounter1 /system_tb/DUT/CPU/DP1/PROGRAM_COUNTER/nRST
add wave -noupdate -expand -group DP1 -group ProramCounter1 /system_tb/DUT/CPU/DP1/PROGRAM_COUNTER/pc_EN
add wave -noupdate -expand -group DP1 -group ProramCounter1 /system_tb/DUT/CPU/DP1/PROGRAM_COUNTER/pc_in
add wave -noupdate -expand -group DP1 -group ProramCounter1 /system_tb/DUT/CPU/DP1/PROGRAM_COUNTER/pc_out
add wave -noupdate -expand -group DP1 /system_tb/DUT/CPU/DP1/pc_next
add wave -noupdate -expand -group DP1 /system_tb/DUT/CPU/DP1/pc
add wave -noupdate -expand -group DP1 /system_tb/DUT/CPU/dcif1/imemaddr
add wave -noupdate -expand -group DP1 /system_tb/DUT/CPU/DP1/instruction
add wave -noupdate -expand -group DP1 /system_tb/DUT/CPU/DP1/instruction_D
add wave -noupdate -expand -group DP1 /system_tb/DUT/CPU/DP1/op_D
add wave -noupdate -expand -group DP1 /system_tb/DUT/CPU/DP1/instruction_EX
add wave -noupdate -expand -group DP1 /system_tb/DUT/CPU/DP1/op_EX
add wave -noupdate -expand -group DP1 /system_tb/DUT/CPU/DP1/instruction_M
add wave -noupdate -expand -group DP1 /system_tb/DUT/CPU/DP1/op_M
add wave -noupdate -expand -group DP1 /system_tb/DUT/CPU/DP1/op_WB
add wave -noupdate -expand -group aluif1 /system_tb/DUT/CPU/DP1/aluif/portA
add wave -noupdate -expand -group aluif1 /system_tb/DUT/CPU/DP1/aluif/portB
add wave -noupdate -expand -group aluif1 /system_tb/DUT/CPU/DP1/aluif/aluOP
add wave -noupdate -expand -group aluif1 /system_tb/DUT/CPU/DP1/aluif/portO
add wave -noupdate -expand -group aluif1 /system_tb/DUT/CPU/DP1/aluif/nFlag
add wave -noupdate -expand -group aluif1 /system_tb/DUT/CPU/DP1/aluif/oFlag
add wave -noupdate -expand -group aluif1 /system_tb/DUT/CPU/DP1/aluif/zFlag
add wave -noupdate -expand -group rfif1 /system_tb/DUT/CPU/DP1/rfif/WEN
add wave -noupdate -expand -group rfif1 /system_tb/DUT/CPU/DP1/rfif/wsel
add wave -noupdate -expand -group rfif1 /system_tb/DUT/CPU/DP1/rfif/rsel1
add wave -noupdate -expand -group rfif1 /system_tb/DUT/CPU/DP1/rfif/rsel2
add wave -noupdate -expand -group rfif1 /system_tb/DUT/CPU/DP1/rfif/wdat
add wave -noupdate -expand -group rfif1 /system_tb/DUT/CPU/DP1/rfif/rdat1
add wave -noupdate -expand -group rfif1 /system_tb/DUT/CPU/DP1/rfif/rdat2
add wave -noupdate -group cuif1 /system_tb/DUT/CPU/DP1/cuif/imemload
add wave -noupdate -group cuif1 /system_tb/DUT/CPU/DP1/cuif/j
add wave -noupdate -group cuif1 /system_tb/DUT/CPU/DP1/cuif/jr
add wave -noupdate -group cuif1 /system_tb/DUT/CPU/DP1/cuif/jal
add wave -noupdate -group cuif1 /system_tb/DUT/CPU/DP1/cuif/beq
add wave -noupdate -group cuif1 /system_tb/DUT/CPU/DP1/cuif/bne
add wave -noupdate -group cuif1 /system_tb/DUT/CPU/DP1/cuif/halt
add wave -noupdate -group cuif1 /system_tb/DUT/CPU/DP1/cuif/RegDst
add wave -noupdate -group cuif1 /system_tb/DUT/CPU/DP1/cuif/ALUSrc
add wave -noupdate -group cuif1 /system_tb/DUT/CPU/DP1/cuif/MemToReg
add wave -noupdate -group cuif1 /system_tb/DUT/CPU/DP1/cuif/RegWrite
add wave -noupdate -group cuif1 /system_tb/DUT/CPU/DP1/cuif/ALUOp
add wave -noupdate -group cuif1 /system_tb/DUT/CPU/DP1/cuif/ExtOp
add wave -noupdate -group cuif1 /system_tb/DUT/CPU/DP1/cuif/ShiftOp
add wave -noupdate -group cuif1 /system_tb/DUT/CPU/DP1/cuif/lui
add wave -noupdate -group cuif1 /system_tb/DUT/CPU/DP1/cuif/dR_REQ
add wave -noupdate -group cuif1 /system_tb/DUT/CPU/DP1/cuif/dW_REQ
add wave -noupdate -expand -group dpif1 /system_tb/DUT/CPU/DP1/dpif/halt
add wave -noupdate -expand -group dpif1 /system_tb/DUT/CPU/DP1/dpif/ihit
add wave -noupdate -expand -group dpif1 /system_tb/DUT/CPU/DP1/dpif/imemREN
add wave -noupdate -expand -group dpif1 /system_tb/DUT/CPU/DP1/dpif/imemload
add wave -noupdate -expand -group dpif1 /system_tb/DUT/CPU/DP1/dpif/imemaddr
add wave -noupdate -expand -group dpif1 /system_tb/DUT/CPU/DP1/dpif/dhit
add wave -noupdate -expand -group dpif1 /system_tb/DUT/CPU/DP1/dpif/datomic
add wave -noupdate -expand -group dpif1 /system_tb/DUT/CPU/DP1/dpif/dmemREN
add wave -noupdate -expand -group dpif1 /system_tb/DUT/CPU/DP1/dpif/dmemWEN
add wave -noupdate -expand -group dpif1 /system_tb/DUT/CPU/DP1/dpif/flushed
add wave -noupdate -expand -group dpif1 /system_tb/DUT/CPU/DP1/dpif/dmemload
add wave -noupdate -expand -group dpif1 /system_tb/DUT/CPU/DP1/dpif/dmemstore
add wave -noupdate -expand -group dpif1 /system_tb/DUT/CPU/DP1/dpif/dmemaddr
add wave -noupdate -expand -group fuif1 /system_tb/DUT/CPU/DP1/fuif/rs_EX
add wave -noupdate -expand -group fuif1 /system_tb/DUT/CPU/DP1/fuif/rt_EX
add wave -noupdate -expand -group fuif1 /system_tb/DUT/CPU/DP1/fuif/wsel_M
add wave -noupdate -expand -group fuif1 /system_tb/DUT/CPU/DP1/fuif/wsel_WB
add wave -noupdate -expand -group fuif1 /system_tb/DUT/CPU/DP1/fuif/WEN_M
add wave -noupdate -expand -group fuif1 /system_tb/DUT/CPU/DP1/fuif/WEN_WB
add wave -noupdate -expand -group fuif1 /system_tb/DUT/CPU/DP1/fuif/forward_A
add wave -noupdate -expand -group fuif1 /system_tb/DUT/CPU/DP1/fuif/forward_B
add wave -noupdate -expand -group fuif1 /system_tb/DUT/CPU/DP1/fuif/is_ITYPE
add wave -noupdate -expand -group fuif1 /system_tb/DUT/CPU/DP1/fuif/is_bne_or_beq_M
add wave -noupdate -expand -group fuif1 /system_tb/DUT/CPU/DP1/fuif/dREN_M
add wave -noupdate -expand -group fuif1 /system_tb/DUT/CPU/DP1/fuif/bubble_lw_f
add wave -noupdate -expand -group sfif1 /system_tb/DUT/CPU/DP1/sfif/dWEN_EX
add wave -noupdate -expand -group sfif1 /system_tb/DUT/CPU/DP1/sfif/rt_EX
add wave -noupdate -expand -group sfif1 /system_tb/DUT/CPU/DP1/sfif/rd_M
add wave -noupdate -expand -group sfif1 /system_tb/DUT/CPU/DP1/sfif/rd_WB
add wave -noupdate -expand -group sfif1 -expand /system_tb/DUT/CPU/DP1/sfif/forwarding_required
add wave -noupdate /system_tb/DUT/CPU/DP1/sw_forwarding_output
add wave -noupdate /system_tb/DUT/CPU/DP1/porto_M
add wave -noupdate /system_tb/DUT/CPU/DP1/rdata2_M
add wave -noupdate /system_tb/DUT/CPU/DP1/REGISTER_FILE/rfile
add wave -noupdate -group Icache1 /system_tb/DUT/CPU/CM1/ICACHE/index
add wave -noupdate -group Icache1 /system_tb/DUT/CPU/CM1/ICACHE/ihit
add wave -noupdate -group Icache1 /system_tb/DUT/CPU/CM1/ICACHE/imemload
add wave -noupdate -group Icache1 /system_tb/DUT/CPU/CM1/ICACHE/iREN
add wave -noupdate -group Icache1 /system_tb/DUT/CPU/CM1/ICACHE/current_state
add wave -noupdate -group Icache1 /system_tb/DUT/CPU/CM1/ICACHE/next_state
add wave -noupdate -group Icache1 -expand /system_tb/DUT/CPU/CM1/ICACHE/icacheset
add wave -noupdate -expand -group DCache1 -expand -group cif1 /system_tb/DUT/CPU/CM1/DCACHE/cif/iwait
add wave -noupdate -expand -group DCache1 -expand -group cif1 /system_tb/DUT/CPU/CM1/DCACHE/cif/dwait
add wave -noupdate -expand -group DCache1 -expand -group cif1 /system_tb/DUT/CPU/CM1/DCACHE/cif/iREN
add wave -noupdate -expand -group DCache1 -expand -group cif1 /system_tb/DUT/CPU/CM1/DCACHE/cif/dREN
add wave -noupdate -expand -group DCache1 -expand -group cif1 /system_tb/DUT/CPU/CM1/DCACHE/cif/dWEN
add wave -noupdate -expand -group DCache1 -expand -group cif1 /system_tb/DUT/CPU/CM1/DCACHE/cif/iload
add wave -noupdate -expand -group DCache1 -expand -group cif1 /system_tb/DUT/CPU/CM1/DCACHE/cif/dload
add wave -noupdate -expand -group DCache1 -expand -group cif1 /system_tb/DUT/CPU/CM1/DCACHE/cif/dstore
add wave -noupdate -expand -group DCache1 -expand -group cif1 /system_tb/DUT/CPU/CM1/DCACHE/cif/iaddr
add wave -noupdate -expand -group DCache1 -expand -group cif1 /system_tb/DUT/CPU/CM1/DCACHE/cif/daddr
add wave -noupdate -expand -group DCache1 -expand -group cif1 /system_tb/DUT/CPU/CM1/DCACHE/cif/ccwait
add wave -noupdate -expand -group DCache1 -expand -group cif1 /system_tb/DUT/CPU/CM1/DCACHE/cif/ccinv
add wave -noupdate -expand -group DCache1 -expand -group cif1 /system_tb/DUT/CPU/CM1/DCACHE/cif/ccwrite
add wave -noupdate -expand -group DCache1 -expand -group cif1 /system_tb/DUT/CPU/CM1/DCACHE/cif/cctrans
add wave -noupdate -expand -group DCache1 -expand -group cif1 /system_tb/DUT/CPU/CM1/DCACHE/cif/ccsnoopaddr
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/CLK
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/nRST
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/dcif/dhit
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/dcif/dmemload
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/cif/dREN
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/cif/dWEN
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/curr_state
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/next_state
add wave -noupdate -expand -group DCache1 -expand /system_tb/DUT/CPU/CM1/DCACHE/dcacheset
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/byte_offset
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/block_offset
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/index
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/dmemaddr
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/dcif1/imemREN
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/dcif1/dmemREN
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/dcif1/dmemWEN
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/tag_match1
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/ReadHit1
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/WriteHit1
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/tag_match2
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/ReadHit2
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/WriteHit2
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/valid1
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/valid2
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/dirty1
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/dirty2
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/hit1
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/hit2
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/LRU
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/snoop_tag_hit
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/snoop_block_invalid
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/curr_frame
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/curr_block
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/M_access
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/S_access
add wave -noupdate /system_tb/DUT/CPU/DP0/rdata2_M
add wave -noupdate -expand -group dcif0 /system_tb/DUT/CPU/CM0/dcif/halt
add wave -noupdate -expand -group dcif0 /system_tb/DUT/CPU/CM0/dcif/ihit
add wave -noupdate -expand -group dcif0 /system_tb/DUT/CPU/CM0/dcif/imemREN
add wave -noupdate -expand -group dcif0 /system_tb/DUT/CPU/CM0/dcif/imemload
add wave -noupdate -expand -group dcif0 /system_tb/DUT/CPU/CM0/dcif/imemaddr
add wave -noupdate -expand -group dcif0 /system_tb/DUT/CPU/CM0/dcif/dhit
add wave -noupdate -expand -group dcif0 /system_tb/DUT/CPU/CM0/dcif/datomic
add wave -noupdate -expand -group dcif0 /system_tb/DUT/CPU/CM0/dcif/dmemREN
add wave -noupdate -expand -group dcif0 /system_tb/DUT/CPU/CM0/dcif/dmemWEN
add wave -noupdate -expand -group dcif0 /system_tb/DUT/CPU/CM0/dcif/flushed
add wave -noupdate -expand -group dcif0 /system_tb/DUT/CPU/CM0/dcif/dmemload
add wave -noupdate -expand -group dcif0 /system_tb/DUT/CPU/CM0/dcif/dmemstore
add wave -noupdate -expand -group dcif0 /system_tb/DUT/CPU/CM0/dcif/dmemaddr
add wave -noupdate -expand -group dcif1 /system_tb/DUT/CPU/CM1/dcif/halt
add wave -noupdate -expand -group dcif1 /system_tb/DUT/CPU/CM1/dcif/ihit
add wave -noupdate -expand -group dcif1 /system_tb/DUT/CPU/CM1/dcif/imemREN
add wave -noupdate -expand -group dcif1 /system_tb/DUT/CPU/CM1/dcif/imemload
add wave -noupdate -expand -group dcif1 /system_tb/DUT/CPU/CM1/dcif/imemaddr
add wave -noupdate -expand -group dcif1 /system_tb/DUT/CPU/CM1/dcif/dhit
add wave -noupdate -expand -group dcif1 /system_tb/DUT/CPU/CM1/dcif/datomic
add wave -noupdate -expand -group dcif1 /system_tb/DUT/CPU/CM1/dcif/dmemREN
add wave -noupdate -expand -group dcif1 /system_tb/DUT/CPU/CM1/dcif/dmemWEN
add wave -noupdate -expand -group dcif1 /system_tb/DUT/CPU/CM1/dcif/flushed
add wave -noupdate -expand -group dcif1 /system_tb/DUT/CPU/CM1/dcif/dmemload
add wave -noupdate -expand -group dcif1 /system_tb/DUT/CPU/CM1/dcif/dmemstore
add wave -noupdate -expand -group dcif1 /system_tb/DUT/CPU/CM1/dcif/dmemaddr
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {2937449 ps} 0}
quietly wave cursor active 1
configure wave -namecolwidth 236
configure wave -valuecolwidth 73
configure wave -justifyvalue left
configure wave -signalnamewidth 1
configure wave -snapdistance 10
configure wave -datasetprefix 0
configure wave -rowmargin 4
configure wave -childrowmargin 2
configure wave -gridoffset 0
configure wave -gridperiod 1
configure wave -griddelta 40
configure wave -timeline 0
configure wave -timelineunits ns
update
WaveRestoreZoom {2876522 ps} {2999993 ps}
