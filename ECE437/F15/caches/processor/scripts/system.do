onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate /system_tb/DUT/CPU/DP/instruction
add wave -noupdate /system_tb/DUT/CPU/DP/instruction_D
add wave -noupdate /system_tb/DUT/CPU/DP/instruction_EX
add wave -noupdate /system_tb/DUT/CPU/DP/instruction_M
add wave -noupdate /system_tb/DUT/CPU/DP/pc_plus_4_M
add wave -noupdate /system_tb/DUT/CPU/DP/npc
add wave -noupdate -radix decimal /system_tb/DUT/CPU/CM/DCACHE/dhit_count
add wave -noupdate /system_tb/DUT/CPU/CM/dcif/dhit
add wave -noupdate /system_tb/DUT/CPU/CM/dcif/halt
add wave -noupdate /system_tb/DUT/CPU/CM/dcif/flushed
add wave -noupdate /system_tb/DUT/CPU/CM/ICACHE/current_state
add wave -noupdate /system_tb/DUT/CPU/CM/ICACHE/frames
add wave -noupdate /system_tb/DUT/CPU/CM/dcif/ihit
add wave -noupdate /system_tb/DUT/CPU/CM/dcif/imemREN
add wave -noupdate /system_tb/DUT/CPU/CM/dcif/imemload
add wave -noupdate /system_tb/DUT/CPU/CM/dcif/imemaddr
add wave -noupdate /system_tb/DUT/CPU/CM/dcif/dmemREN
add wave -noupdate /system_tb/DUT/CPU/CM/dcif/dmemWEN
add wave -noupdate /system_tb/DUT/CPU/CM/dcif/dmemload
add wave -noupdate /system_tb/DUT/CPU/CM/dcif/dmemstore
add wave -noupdate /system_tb/DUT/CPU/CM/dcif/dmemaddr
add wave -noupdate /system_tb/DUT/CPU/CM/DCACHE/current_state
add wave -noupdate /system_tb/DUT/CPU/CM/DCACHE/next_state
add wave -noupdate -childformat {{{/system_tb/DUT/CPU/CM/DCACHE/frames[0]} -radix hexadecimal}} -expand -subitemconfig {{/system_tb/DUT/CPU/CM/DCACHE/frames[0]} {-height 17 -radix hexadecimal}} /system_tb/DUT/CPU/CM/DCACHE/frames
add wave -noupdate /system_tb/DUT/CPU/CM/DCACHE/not_least_recently_used
add wave -noupdate /system_tb/DUT/CPU/CM/DCACHE/least_recently_used
add wave -noupdate -expand /system_tb/DUT/CPU/CM/DCACHE/daddr
add wave -noupdate /system_tb/DUT/CPU/CM/DCACHE/flushing
add wave -noupdate /system_tb/DUT/CPU/CM/DCACHE/flushFIdx
add wave -noupdate /system_tb/DUT/CPU/CM/DCACHE/flushBIdx
add wave -noupdate /system_tb/DUT/CPU/CM/DCACHE/index
add wave -noupdate /system_tb/DUT/CPU/CM/DCACHE/block_offset
add wave -noupdate /system_tb/DUT/CPU/CM/DCACHE/next_block_offset
add wave -noupdate /system_tb/DUT/CPU/CM/CLK
add wave -noupdate /system_tb/DUT/CPU/CM/nRST
add wave -noupdate /system_tb/DUT/CPU/DP/pc
add wave -noupdate /system_tb/DUT/CPU/CM/ccif/iwait
add wave -noupdate /system_tb/DUT/CPU/CM/ccif/dwait
add wave -noupdate /system_tb/DUT/CPU/CM/ccif/iREN
add wave -noupdate /system_tb/DUT/CPU/CM/ccif/iload
add wave -noupdate /system_tb/DUT/CPU/CM/ccif/iaddr
add wave -noupdate /system_tb/DUT/CPU/CM/ccif/dREN
add wave -noupdate -expand /system_tb/DUT/CPU/CM/ccif/dWEN
add wave -noupdate /system_tb/DUT/CPU/CM/ccif/daddr
add wave -noupdate /system_tb/DUT/CPU/CM/ccif/dload
add wave -noupdate -radix decimal /system_tb/DUT/CPU/CM/ccif/dstore
add wave -noupdate /system_tb/DUT/CPU/CM/ccif/ramstate
add wave -noupdate /system_tb/DUT/CPU/CM/ccif/ramaddr
add wave -noupdate /system_tb/DUT/CPU/CM/ccif/ramstore
add wave -noupdate -expand /system_tb/DUT/CPU/DP/REGISTER_FILE/rfile
add wave -noupdate /system_tb/DUT/CPU/DP/REGISTER_FILE/rfif/WEN
add wave -noupdate /system_tb/DUT/CPU/DP/REGISTER_FILE/rfif/wsel
add wave -noupdate /system_tb/DUT/CPU/DP/REGISTER_FILE/rfif/rsel1
add wave -noupdate /system_tb/DUT/CPU/DP/REGISTER_FILE/rfif/rsel2
add wave -noupdate /system_tb/DUT/CPU/DP/REGISTER_FILE/rfif/wdat
add wave -noupdate /system_tb/DUT/CPU/DP/REGISTER_FILE/rfif/rdat1
add wave -noupdate /system_tb/DUT/CPU/DP/REGISTER_FILE/rfif/rdat2
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {19657769 ps} 0}
quietly wave cursor active 1
configure wave -namecolwidth 223
configure wave -valuecolwidth 140
configure wave -justifyvalue left
configure wave -signalnamewidth 1
configure wave -snapdistance 10
configure wave -datasetprefix 0
configure wave -rowmargin 4
configure wave -childrowmargin 2
configure wave -gridoffset 0
configure wave -gridperiod 10
configure wave -griddelta 40
configure wave -timeline 0
configure wave -timelineunits ns
update
WaveRestoreZoom {16845993 ps} {20166001 ps}
