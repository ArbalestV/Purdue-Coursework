onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate /system_tb/CLK
add wave -noupdate /system_tb/nRST
add wave -noupdate -expand -group {Control Unit} /system_tb/DUT/CPU/DP/cuif/imemload
add wave -noupdate -expand -group {Control Unit} /system_tb/DUT/CPU/DP/cuif/halt
add wave -noupdate -expand -group {Control Unit} /system_tb/DUT/CPU/DP/cuif/imemload
add wave -noupdate -expand -group {Control Unit} /system_tb/DUT/CPU/DP/cuif/j
add wave -noupdate -expand -group {Control Unit} /system_tb/DUT/CPU/DP/cuif/jr
add wave -noupdate -expand -group {Control Unit} /system_tb/DUT/CPU/DP/cuif/jal
add wave -noupdate -expand -group {Control Unit} /system_tb/DUT/CPU/DP/cuif/beq
add wave -noupdate -expand -group {Control Unit} /system_tb/DUT/CPU/DP/cuif/bne
add wave -noupdate -expand -group {Control Unit} /system_tb/DUT/CPU/DP/cuif/halt
add wave -noupdate -expand -group {Control Unit} /system_tb/DUT/CPU/DP/cuif/RegDst
add wave -noupdate -expand -group {Control Unit} /system_tb/DUT/CPU/DP/cuif/ALUSrc
add wave -noupdate -expand -group {Control Unit} /system_tb/DUT/CPU/DP/cuif/MemToReg
add wave -noupdate -expand -group {Control Unit} /system_tb/DUT/CPU/DP/cuif/RegWrite
add wave -noupdate -expand -group {Control Unit} /system_tb/DUT/CPU/DP/cuif/ALUOp
add wave -noupdate -expand -group {Control Unit} /system_tb/DUT/CPU/DP/cuif/ExtOp
add wave -noupdate -expand -group {Control Unit} /system_tb/DUT/CPU/DP/cuif/ShiftOp
add wave -noupdate -expand -group {Control Unit} /system_tb/DUT/CPU/DP/cuif/lui
add wave -noupdate -expand -group {Control Unit} /system_tb/DUT/CPU/DP/cuif/dR_REQ
add wave -noupdate -expand -group {Control Unit} /system_tb/DUT/CPU/DP/cuif/dW_REQ
add wave -noupdate -expand -group {Instruction opcodes} /system_tb/DUT/CPU/DP/op_D
add wave -noupdate -expand -group {Instruction opcodes} /system_tb/DUT/CPU/DP/op_EX
add wave -noupdate -expand -group {Instruction opcodes} /system_tb/DUT/CPU/DP/op_M
add wave -noupdate -expand -group {Instruction opcodes} /system_tb/DUT/CPU/DP/op_WB
add wave -noupdate -radix hexadecimal /system_tb/DUT/CPU/DP/instruction_D
add wave -noupdate /system_tb/DUT/CPU/dcif/dmemREN
add wave -noupdate -expand -group ihit-dhit /system_tb/DUT/CPU/DP/d_ihit
add wave -noupdate -expand -group ihit-dhit /system_tb/DUT/CPU/DP/d_dhit
add wave -noupdate -expand -group {Program Counter} /system_tb/DUT/CPU/DP/PROGRAM_COUNTER/pc_EN
add wave -noupdate -expand -group {Program Counter} /system_tb/DUT/CPU/DP/pc_next
add wave -noupdate -expand -group {Program Counter} /system_tb/DUT/CPU/DP/pc
add wave -noupdate -expand -group {Program Counter} /system_tb/DUT/CPU/DP/pc_plus_4
add wave -noupdate -expand -group {Program Counter} /system_tb/DUT/CPU/DP/pc_plus_4_D
add wave -noupdate -expand -group {Program Counter} /system_tb/DUT/CPU/DP/pc_plus_4_EX
add wave -noupdate -expand -group {Program Counter} /system_tb/DUT/CPU/DP/pc_plus_4_M
add wave -noupdate -expand -group {Program Counter} /system_tb/DUT/CPU/DP/PROGRAM_COUNTER/pc_in
add wave -noupdate -expand -group {Program Counter} /system_tb/DUT/CPU/DP/PROGRAM_COUNTER/pc_out
add wave -noupdate -expand -group {Cache- I} /system_tb/DUT/CPU/DP/dpif/ihit
add wave -noupdate -expand -group {Cache- I} /system_tb/DUT/CPU/DP/dpif/imemREN
add wave -noupdate -expand -group {Cache- I} /system_tb/DUT/CPU/DP/dpif/imemload
add wave -noupdate -expand -group {Cache- I} /system_tb/DUT/CPU/DP/dpif/imemaddr
add wave -noupdate -radix unsigned /system_tb/DUT/CPU/DP/wsel_WB
add wave -noupdate /system_tb/DUT/CPU/DP/regWrite_WB
add wave -noupdate -expand -group Registers -expand /system_tb/DUT/CPU/DP/REGISTER_FILE/rfile
add wave -noupdate /system_tb/DUT/CPU/DP/jal_EX
add wave -noupdate -radix unsigned /system_tb/DUT/CPU/DP/rt_EX
add wave -noupdate -radix unsigned /system_tb/DUT/CPU/DP/rs_EX
add wave -noupdate /system_tb/DUT/CPU/DP/ALUOp_EX
add wave -noupdate /system_tb/DUT/CPU/DP/RegDst_EX
add wave -noupdate -radix unsigned /system_tb/DUT/CPU/DP/wsel_EX
add wave -noupdate -radix decimal /system_tb/DUT/CPU/DP/wsel_M
add wave -noupdate -radix unsigned /system_tb/DUT/CPU/DP/wsel_WB
add wave -noupdate -expand -group {Forwarding Unit} -radix unsigned /system_tb/DUT/CPU/DP/fuif/rs_EX
add wave -noupdate -expand -group {Forwarding Unit} -radix unsigned /system_tb/DUT/CPU/DP/fuif/rt_EX
add wave -noupdate -expand -group {Forwarding Unit} -radix unsigned /system_tb/DUT/CPU/DP/fuif/wsel_M
add wave -noupdate -expand -group {Forwarding Unit} -radix unsigned /system_tb/DUT/CPU/DP/fuif/wsel_WB
add wave -noupdate -expand -group {Forwarding Unit} /system_tb/DUT/CPU/DP/wdat_WB
add wave -noupdate -expand -group {Forwarding Unit} /system_tb/DUT/CPU/DP/fuif/regWrite_M
add wave -noupdate -expand -group {Forwarding Unit} /system_tb/DUT/CPU/DP/fuif/regWrite_WB
add wave -noupdate -expand -group {Forwarding Unit} -radix unsigned /system_tb/DUT/CPU/DP/fuif/forward_A
add wave -noupdate -expand -group {Forwarding Unit} /system_tb/DUT/CPU/DP/fuif/forward_B
add wave -noupdate -expand -group {Forwarding Unit} /system_tb/DUT/CPU/DP/fuif/is_ITYPE
add wave -noupdate -expand -group {Forwarding Unit} /system_tb/DUT/CPU/DP/fuif/is_bne_or_beq_M
add wave -noupdate -expand -group {Forwarding Unit bubble insertion} /system_tb/DUT/CPU/DP/fuif/dREN_M
add wave -noupdate -expand -group {Forwarding Unit bubble insertion} /system_tb/DUT/CPU/DP/fuif/bubble_lw_f
add wave -noupdate -expand -group {Store Forwarding} /system_tb/DUT/CPU/DP/sfif/dWEN_EX
add wave -noupdate -expand -group {Store Forwarding} /system_tb/DUT/CPU/DP/sfif/rt_EX
add wave -noupdate -expand -group {Store Forwarding} /system_tb/DUT/CPU/DP/sfif/rd_M
add wave -noupdate -expand -group {Store Forwarding} /system_tb/DUT/CPU/DP/sfif/rd_WB
add wave -noupdate -expand -group {Store Forwarding} /system_tb/DUT/CPU/DP/sfif/forwarding_required
add wave -noupdate -expand -group {Register File signals} /system_tb/DUT/CPU/DP/REGISTER_FILE/rfif/WEN
add wave -noupdate -expand -group {Register File signals} -radix unsigned /system_tb/DUT/CPU/DP/REGISTER_FILE/rfif/wsel
add wave -noupdate -expand -group {Register File signals} -radix unsigned /system_tb/DUT/CPU/DP/REGISTER_FILE/rfif/rsel1
add wave -noupdate -expand -group {Register File signals} -radix unsigned /system_tb/DUT/CPU/DP/REGISTER_FILE/rfif/rsel2
add wave -noupdate -expand -group {Register File signals} /system_tb/DUT/CPU/DP/REGISTER_FILE/rfif/wdat
add wave -noupdate -expand -group {Register File signals} /system_tb/DUT/CPU/DP/REGISTER_FILE/rfif/rdat1
add wave -noupdate -expand -group {Register File signals} /system_tb/DUT/CPU/DP/REGISTER_FILE/rfif/rdat2
add wave -noupdate -expand -group ALU /system_tb/DUT/CPU/DP/aluif/portA
add wave -noupdate -expand -group ALU -radix hexadecimal /system_tb/DUT/CPU/DP/aluif/portB
add wave -noupdate -expand -group ALU -radix unsigned /system_tb/DUT/CPU/DP/aluif/aluOP
add wave -noupdate -expand -group ALU /system_tb/DUT/CPU/DP/aluif/portO
add wave -noupdate -expand -group ALU /system_tb/DUT/CPU/DP/aluif/nFlag
add wave -noupdate -expand -group ALU /system_tb/DUT/CPU/DP/aluif/oFlag
add wave -noupdate -expand -group ALU /system_tb/DUT/CPU/DP/aluif/zFlag
add wave -noupdate -expand -group RAM /system_tb/DUT/CPU/DP/dWEN_M
add wave -noupdate -expand -group RAM /system_tb/DUT/CPU/DP/bubble_lw_f
add wave -noupdate -expand -group RAM /system_tb/DUT/CPU/DP/dREN_M
add wave -noupdate -expand -group RAM /system_tb/DUT/RAM/ramif/ramREN
add wave -noupdate -expand -group RAM /system_tb/DUT/RAM/ramif/ramWEN
add wave -noupdate -expand -group RAM /system_tb/DUT/RAM/ramif/ramaddr
add wave -noupdate -expand -group RAM /system_tb/DUT/RAM/ramif/ramstore
add wave -noupdate -expand -group RAM /system_tb/DUT/RAM/ramif/ramload
add wave -noupdate -expand -group RAM /system_tb/DUT/RAM/ramif/ramstate
add wave -noupdate -expand -group RAM /system_tb/DUT/RAM/ramif/memREN
add wave -noupdate -expand -group RAM /system_tb/DUT/RAM/ramif/memWEN
add wave -noupdate -expand -group RAM /system_tb/DUT/RAM/ramif/memaddr
add wave -noupdate -expand -group RAM /system_tb/DUT/RAM/ramif/memstore
add wave -noupdate -expand -group Branch/Jump /system_tb/DUT/CPU/DP/branch_taken
add wave -noupdate -expand -group Branch/Jump /system_tb/DUT/CPU/DP/bne_taken
add wave -noupdate -expand -group Branch/Jump /system_tb/DUT/CPU/DP/beq_taken
add wave -noupdate -expand -group Branch/Jump -radix hexadecimal /system_tb/DUT/CPU/DP/pc_branch_mux
add wave -noupdate -expand -group Branch/Jump -radix hexadecimal /system_tb/DUT/CPU/DP/pc_when_branch
add wave -noupdate -expand -group Branch/Jump /system_tb/DUT/CPU/DP/sign_ext_M
add wave -noupdate -expand -group Branch/Jump /system_tb/DUT/CPU/DP/jr_output
add wave -noupdate -expand -group Branch/Jump /system_tb/DUT/CPU/DP/jal_or_j
add wave -noupdate -expand -group Branch/Jump /system_tb/DUT/CPU/DP/intermediate_jump_op
add wave -noupdate -expand -group Branch/Jump /system_tb/DUT/CPU/DP/jump_address
add wave -noupdate -expand -group Branch/Jump /system_tb/DUT/CPU/DP/jump_taken
add wave -noupdate -expand -group Branch/Jump /system_tb/DUT/CPU/DP/imm16_sign_extended_1
add wave -noupdate -expand -group Branch/Jump /system_tb/DUT/CPU/DP/imm16_sign_extended
add wave -noupdate -expand -group Branch/Jump /system_tb/DUT/CPU/DP/pc_next_branch_jump
add wave -noupdate -expand -group Branch/Jump /system_tb/DUT/CPU/DP/branch_or_jump
add wave -noupdate /system_tb/DUT/CPU/DP/RegDst_EX
add wave -noupdate /system_tb/DUT/CPU/DP/RegDst_output
add wave -noupdate -expand -group {Possible ALU Inputs} /system_tb/DUT/CPU/DP/rdata1_EX
add wave -noupdate -expand -group {Possible ALU Inputs} /system_tb/DUT/CPU/DP/porto_M
add wave -noupdate -expand -group {Possible ALU Inputs} /system_tb/DUT/CPU/DP/wdat_WB
add wave -noupdate -expand -group {Possible ALU Inputs} /system_tb/DUT/CPU/DP/shiftOp_output
add wave -noupdate /system_tb/DUT/CPU/DP/was_forwarding
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {9060444 ps} 0}
quietly wave cursor active 1
configure wave -namecolwidth 236
configure wave -valuecolwidth 97
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
WaveRestoreZoom {1323178498 ps} {1324190606 ps}
