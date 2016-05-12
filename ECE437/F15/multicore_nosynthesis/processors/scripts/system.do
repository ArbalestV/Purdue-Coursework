onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate -divider {***Processor 0***}
add wave -noupdate -divider {DATAPATH 0}
add wave -noupdate /system_tb/DUT/CPU/DP0/pc_plus_4_EX
add wave -noupdate /system_tb/DUT/CPU/DP0/pc_plus_4_M
add wave -noupdate /system_tb/DUT/CPU/DP0/pc_plus_4_WB
add wave -noupdate /system_tb/DUT/CPU/DP0/instruction
add wave -noupdate /system_tb/DUT/CPU/DP0/instruction_D
add wave -noupdate /system_tb/DUT/CPU/DP0/instruction_EX
add wave -noupdate /system_tb/DUT/CPU/DP0/instruction_M
add wave -noupdate /system_tb/DUT/CPU/DP0/instr_M
add wave -noupdate /system_tb/DUT/CPU/DP0/instr_WB
add wave -noupdate /system_tb/DUT/CPU/DP0/REGISTER_FILE/rfile
add wave -noupdate /system_tb/DUT/CPU/DP0/pipe_en_others
add wave -noupdate -divider {ICACHE 0}
add wave -noupdate /system_tb/DUT/CPU/CM0/ICACHE/current_state
add wave -noupdate /system_tb/DUT/CPU/CM0/ICACHE/frames
add wave -noupdate /system_tb/DUT/CPU/CM0/ICACHE/index
add wave -noupdate -divider {dcif - inputs}
add wave -noupdate /system_tb/DUT/CPU/CM0/ICACHE/dcif/imemREN
add wave -noupdate /system_tb/DUT/CPU/CM0/ICACHE/dcif/imemaddr
add wave -noupdate -divider {dcif - outputs}
add wave -noupdate /system_tb/DUT/CPU/CM0/ICACHE/dcif/imemload
add wave -noupdate /system_tb/DUT/CPU/CM0/ICACHE/dcif/ihit
add wave -noupdate -divider {ccif 0 - inputs}
add wave -noupdate /system_tb/DUT/CPU/CM0/ICACHE/ccif/iwait
add wave -noupdate /system_tb/DUT/CPU/CM0/ICACHE/ccif/iload
add wave -noupdate -divider {ccif 0 - outputs}
add wave -noupdate /system_tb/DUT/CPU/CM0/ICACHE/ccif/iREN
add wave -noupdate /system_tb/DUT/CPU/CM0/ICACHE/ccif/iaddr
add wave -noupdate -divider DCACHE0
add wave -noupdate /system_tb/DUT/CPU/CM0/DCACHE/current_state
add wave -noupdate /system_tb/DUT/CPU/CM0/DCACHE/oldstate
add wave -noupdate -expand /system_tb/DUT/CPU/CM0/DCACHE/frames
add wave -noupdate /system_tb/DUT/CPU/CM0/DCACHE/index
add wave -noupdate /system_tb/DUT/CPU/CM0/DCACHE/ll_addr
add wave -noupdate /system_tb/DUT/CPU/CM0/DCACHE/ll_valid
add wave -noupdate /system_tb/DUT/CPU/DP0/dpif/halt
add wave -noupdate -divider {dcif - inputs}
add wave -noupdate /system_tb/DUT/CPU/CM0/DCACHE/dcif/dmemaddr
add wave -noupdate /system_tb/DUT/CPU/CM0/DCACHE/dcif/dmemREN
add wave -noupdate /system_tb/DUT/CPU/CM0/DCACHE/dcif/dmemWEN
add wave -noupdate /system_tb/DUT/CPU/CM0/DCACHE/dcif/dmemstore
add wave -noupdate -divider {dcif - outputs}
add wave -noupdate /system_tb/DUT/CPU/CM0/DCACHE/dcif/dmemload
add wave -noupdate /system_tb/DUT/CPU/CM0/DCACHE/dcif/dhit
add wave -noupdate -divider {ccif - inputs}
add wave -noupdate /system_tb/DUT/CPU/CM0/DCACHE/ccif/dload
add wave -noupdate /system_tb/DUT/CPU/CM0/DCACHE/ccif/dwait
add wave -noupdate -divider {ccif - outputs}
add wave -noupdate /system_tb/DUT/CPU/CM0/DCACHE/ccif/daddr
add wave -noupdate /system_tb/DUT/CPU/CM0/DCACHE/ccif/dstore
add wave -noupdate /system_tb/DUT/CPU/CM0/DCACHE/ccif/dWEN
add wave -noupdate /system_tb/DUT/CPU/CM0/DCACHE/ccif/dREN
TreeUpdate [SetDefaultTree]
quietly WaveActivateNextPane
add wave -noupdate -divider ***Processor1***
add wave -noupdate -divider DP1
add wave -noupdate /system_tb/DUT/CPU/DP1/pc_plus_4_EX
add wave -noupdate /system_tb/DUT/CPU/DP1/pc_plus_4_M
add wave -noupdate /system_tb/DUT/CPU/DP1/pc_plus_4_WB
add wave -noupdate /system_tb/DUT/CPU/DP1/instruction
add wave -noupdate /system_tb/DUT/CPU/DP1/instruction_D
add wave -noupdate /system_tb/DUT/CPU/DP1/instruction_EX
add wave -noupdate /system_tb/DUT/CPU/DP1/instruction_M
add wave -noupdate /system_tb/DUT/CPU/DP1/instr_M
add wave -noupdate /system_tb/DUT/CPU/DP1/instr_WB
add wave -noupdate /system_tb/DUT/CPU/DP1/REGISTER_FILE/rfile
add wave -noupdate /system_tb/DUT/CPU/DP1/pipe_en_others
add wave -noupdate -divider {ICACHE 1}
add wave -noupdate /system_tb/DUT/CPU/CM1/ICACHE/current_state
add wave -noupdate /system_tb/DUT/CPU/CM1/ICACHE/frames
add wave -noupdate -divider {dcif - inputs}
add wave -noupdate /system_tb/DUT/CPU/CM1/dcif/imemREN
add wave -noupdate /system_tb/DUT/CPU/CM1/dcif/imemaddr
add wave -noupdate -divider {dcif - outputs}
add wave -noupdate /system_tb/DUT/CPU/CM1/dcif/imemload
add wave -noupdate /system_tb/DUT/CPU/CM1/dcif/ihit
add wave -noupdate -divider {ccif - inputs}
add wave -noupdate {/system_tb/DUT/CPU/CM1/ccif/iwait[1]}
add wave -noupdate {/system_tb/DUT/CPU/CM1/ccif/iload[1]}
add wave -noupdate -divider {ccif - outputs}
add wave -noupdate {/system_tb/DUT/CPU/CM1/ccif/iREN[1]}
add wave -noupdate {/system_tb/DUT/CPU/CM1/ccif/iaddr[1]}
add wave -noupdate -divider DCACHE1
add wave -noupdate /system_tb/DUT/CPU/CM1/DCACHE/current_state
add wave -noupdate /system_tb/DUT/CPU/CM1/DCACHE/oldstate
add wave -noupdate -expand /system_tb/DUT/CPU/CM1/DCACHE/frames
add wave -noupdate /system_tb/DUT/CPU/CM1/DCACHE/ll_addr
add wave -noupdate /system_tb/DUT/CPU/CM1/DCACHE/ll_valid
add wave -noupdate /system_tb/DUT/CPU/DP1/dpif/halt
add wave -noupdate -divider {dcif - inputs}
add wave -noupdate /system_tb/DUT/CPU/CM1/dcif/dmemaddr
add wave -noupdate /system_tb/DUT/CPU/CM1/dcif/dmemREN
add wave -noupdate /system_tb/DUT/CPU/CM1/DCACHE/index
add wave -noupdate /system_tb/DUT/CPU/CM1/dcif/dmemWEN
add wave -noupdate /system_tb/DUT/CPU/CM1/dcif/dmemstore
add wave -noupdate -divider {dcif - outputs}
add wave -noupdate /system_tb/DUT/CPU/CM1/dcif/dmemload
add wave -noupdate /system_tb/DUT/CPU/CM1/dcif/dhit
add wave -noupdate -divider {ccif - inputs}
add wave -noupdate {/system_tb/DUT/CPU/CM1/ccif/dload[1]}
add wave -noupdate {/system_tb/DUT/CPU/CM1/ccif/dwait[1]}
add wave -noupdate -divider {ccif - outputs}
add wave -noupdate {/system_tb/DUT/CPU/CM1/ccif/daddr[1]}
add wave -noupdate {/system_tb/DUT/CPU/CM1/ccif/dstore[1]}
add wave -noupdate {/system_tb/DUT/CPU/CM1/ccif/dWEN[1]}
add wave -noupdate {/system_tb/DUT/CPU/CM1/ccif/dREN[1]}
add wave -noupdate /system_tb/DUT/CPU/ccif/ccsnoopaddr
TreeUpdate [SetDefaultTree]
quietly WaveActivateNextPane
add wave -noupdate -divider {**Cache Controller**}
add wave -noupdate /system_tb/DUT/CPU/CC/state
add wave -noupdate /system_tb/DUT/CPU/CC/service
add wave -noupdate /system_tb/DUT/CPU/CC/prevInstrServed
add wave -noupdate -divider COHERENCY
add wave -noupdate -divider {ccif: to P0}
add wave -noupdate {/system_tb/DUT/CPU/CC/ccif/ccwait[0]}
add wave -noupdate {/system_tb/DUT/CPU/CC/ccif/ccinv[0]}
add wave -noupdate {/system_tb/DUT/CPU/CC/ccif/ccsnoopaddr[0]}
add wave -noupdate -divider {ccif: from P0}
add wave -noupdate {/system_tb/DUT/CPU/CC/ccif/ccwrite[0]}
add wave -noupdate {/system_tb/DUT/CPU/CC/ccif/cctrans[0]}
add wave -noupdate -divider {ccif: to P1}
add wave -noupdate {/system_tb/DUT/CPU/CC/ccif/ccwait[1]}
add wave -noupdate {/system_tb/DUT/CPU/CC/ccif/ccinv[1]}
add wave -noupdate {/system_tb/DUT/CPU/CC/ccif/ccsnoopaddr[1]}
add wave -noupdate -divider {ccif: from P1}
add wave -noupdate {/system_tb/DUT/CPU/CC/ccif/ccwrite[1]}
add wave -noupdate {/system_tb/DUT/CPU/CC/ccif/cctrans[1]}
add wave -noupdate -divider RAM
add wave -noupdate -divider {ramif - inputs}
add wave -noupdate /system_tb/DUT/CPU/CC/ccif/ramaddr
add wave -noupdate /system_tb/DUT/CPU/CC/ccif/ramstore
add wave -noupdate /system_tb/DUT/CPU/CC/ccif/ramWEN
add wave -noupdate /system_tb/DUT/CPU/CC/ccif/ramstate
add wave -noupdate /system_tb/DUT/CPU/CC/ccif/ramREN
add wave -noupdate -divider {ramif - outputs}
add wave -noupdate /system_tb/DUT/CPU/CC/ccif/ramload
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {13609795 ps} 0}
quietly wave cursor active 1
configure wave -namecolwidth 223
configure wave -valuecolwidth 591
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
WaveRestoreZoom {13087097 ps} {14018097 ps}
