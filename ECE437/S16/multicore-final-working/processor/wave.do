onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate /system_tb/CLK
add wave -noupdate /system_tb/nRST
add wave -noupdate -divider States
add wave -noupdate -divider DP0
add wave -noupdate /system_tb/DUT/CPU/DP0/instruction_D
add wave -noupdate /system_tb/DUT/CPU/DP0/op_D
add wave -noupdate /system_tb/DUT/CPU/DP0/instruction_EX
add wave -noupdate /system_tb/DUT/CPU/DP0/op_EX
add wave -noupdate /system_tb/DUT/CPU/DP0/instruction_M
add wave -noupdate /system_tb/DUT/CPU/DP0/op_M
add wave -noupdate -divider DP1
add wave -noupdate /system_tb/DUT/CPU/DP1/instruction_D
add wave -noupdate /system_tb/DUT/CPU/DP1/op_D
add wave -noupdate /system_tb/DUT/CPU/DP1/instruction_EX
add wave -noupdate /system_tb/DUT/CPU/DP1/op_EX
add wave -noupdate /system_tb/DUT/CPU/DP1/instruction_M
add wave -noupdate /system_tb/DUT/CPU/DP1/op_M
add wave -noupdate -divider MemoryController
add wave -noupdate -divider Core0
add wave -noupdate /system_tb/DUT/CPU/DP0/nRST
add wave -noupdate -expand -group DP0 -group ProgramCounter0 /system_tb/DUT/CPU/DP0/PROGRAM_COUNTER/nRST
add wave -noupdate -expand -group DP0 /system_tb/DUT/CPU/DP0/instruction_D
add wave -noupdate -expand -group DP0 /system_tb/DUT/CPU/DP0/op_D
add wave -noupdate -expand -group DP0 /system_tb/DUT/CPU/DP0/instruction_EX
add wave -noupdate -expand -group DP0 /system_tb/DUT/CPU/DP0/op_EX
add wave -noupdate -expand -group DP0 /system_tb/DUT/CPU/DP0/instruction_M
add wave -noupdate -expand -group DP0 /system_tb/DUT/CPU/DP0/op_M
add wave -noupdate /system_tb/DUT/CPU/DP0/rdata2_EX
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/CLK
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/nRST
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/link_reg
add wave -noupdate -expand -group DCache0 /system_tb/DUT/CPU/CM0/DCACHE/curr_frame
add wave -noupdate -divider Core1
add wave -noupdate /system_tb/DUT/CPU/DP1/nRST
add wave -noupdate -expand -group DP1 -group ProramCounter1 /system_tb/DUT/CPU/DP1/PROGRAM_COUNTER/nRST
add wave -noupdate -expand -group DP1 /system_tb/DUT/CPU/DP1/instruction_D
add wave -noupdate -expand -group DP1 /system_tb/DUT/CPU/DP1/op_D
add wave -noupdate -expand -group DP1 /system_tb/DUT/CPU/DP1/instruction_EX
add wave -noupdate -expand -group DP1 /system_tb/DUT/CPU/DP1/op_EX
add wave -noupdate -expand -group DP1 /system_tb/DUT/CPU/DP1/instruction_M
add wave -noupdate -expand -group DP1 /system_tb/DUT/CPU/DP1/op_M
add wave -noupdate /system_tb/DUT/CPU/CM1/DCACHE/dcifdhit
add wave -noupdate -expand -group MC-States {/system_tb/DUT/CPU/CC/\curr_state.IDLE~q }
add wave -noupdate -expand -group MC-States /system_tb/DUT/CPU/CC/curr_stateSNOOP
add wave -noupdate -expand -group MC-States /system_tb/DUT/CPU/CM1/DCACHE/curr_stateSNOOP
add wave -noupdate -expand -group MC-States /system_tb/DUT/CPU/CC/curr_stateiREQ
add wave -noupdate -expand -group MC-States /system_tb/DUT/CPU/CC/curr_stateWB1
add wave -noupdate -expand -group MC-States /system_tb/DUT/CPU/CC/curr_stateWB0
add wave -noupdate -expand -group MC-States /system_tb/DUT/CPU/CC/curr_stateFETCH1
add wave -noupdate -expand -group MC-States /system_tb/DUT/CPU/CC/curr_stateFETCH0
add wave -noupdate -expand -group MC-States {/system_tb/DUT/CPU/CC/\curr_state.MEM1~q }
add wave -noupdate -expand -group MC-States {/system_tb/DUT/CPU/CC/\curr_state.MEM0~q }
add wave -noupdate -expand -group MC-States {/system_tb/DUT/CPU/CC/\curr_state.CACHE1~q }
add wave -noupdate -expand -group MC-States {/system_tb/DUT/CPU/CC/\curr_state.CACHE0~q }
add wave -noupdate -expand -group {D$1-States} /system_tb/DUT/CPU/CM1/DCACHE/curr_stateFLUSH_DONE
add wave -noupdate -expand -group {D$1-States} {/system_tb/DUT/CPU/CM1/DCACHE/\curr_state.WB1~q }
add wave -noupdate -expand -group {D$1-States} {/system_tb/DUT/CPU/CM1/DCACHE/\curr_state.WB1_SERVICER~q }
add wave -noupdate -expand -group {D$1-States} {/system_tb/DUT/CPU/CM1/DCACHE/\curr_state.WB0~q }
add wave -noupdate -expand -group {D$1-States} {/system_tb/DUT/CPU/CM1/DCACHE/\curr_state.WB0_SERVICER~q }
add wave -noupdate -expand -group {D$1-States} {/system_tb/DUT/CPU/CM1/DCACHE/\curr_state.SNOOP_SERVICER~q }
add wave -noupdate -expand -group {D$1-States} {/system_tb/DUT/CPU/CM1/DCACHE/\curr_state.ITERATE~q }
add wave -noupdate -expand -group {D$1-States} {/system_tb/DUT/CPU/CM1/DCACHE/\curr_state.IDLE~q }
add wave -noupdate -expand -group {D$1-States} {/system_tb/DUT/CPU/CM1/DCACHE/\curr_state.FLUSH~q }
add wave -noupdate -expand -group {D$1-States} {/system_tb/DUT/CPU/CM1/DCACHE/\curr_state.FLUSH_WB1~q }
add wave -noupdate -expand -group {D$1-States} {/system_tb/DUT/CPU/CM1/DCACHE/\curr_state.FLUSH_WB0~q }
add wave -noupdate -expand -group {D$1-States} {/system_tb/DUT/CPU/CM1/DCACHE/\curr_state.FETCH0~q }
add wave -noupdate -expand -group {D$1-States} {/system_tb/DUT/CPU/CM1/DCACHE/\curr_state.FETCH1~q }
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/CLK
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/nRST
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/link_reg
add wave -noupdate -expand -group DCache1 /system_tb/DUT/CPU/CM1/DCACHE/curr_frame
add wave -noupdate {/system_tb/DUT/CPU/CM1/DCACHE/\curr_state.FETCH1~0_combout }
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {2000000 ps} 0}
quietly wave cursor active 1
configure wave -namecolwidth 236
configure wave -valuecolwidth 124
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
WaveRestoreZoom {1705214 ps} {2606315 ps}
