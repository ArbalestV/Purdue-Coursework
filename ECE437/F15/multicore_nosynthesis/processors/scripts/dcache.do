onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate /dcache_tb/CLK
add wave -noupdate /dcache_tb/nRST
add wave -noupdate /dcache_tb/datacacheif/dmemstore
add wave -noupdate /dcache_tb/datacacheif/dmemaddr
add wave -noupdate /dcache_tb/datacacheif/dmemload
add wave -noupdate /dcache_tb/datacacheif/daddr
add wave -noupdate /dcache_tb/datacacheif/dstore
add wave -noupdate /dcache_tb/datacacheif/dload
add wave -noupdate /dcache_tb/datacacheif/halt
add wave -noupdate /dcache_tb/datacacheif/dmemREN
add wave -noupdate /dcache_tb/datacacheif/dmemWEN
add wave -noupdate /dcache_tb/datacacheif/flushed
add wave -noupdate /dcache_tb/datacacheif/dhit
add wave -noupdate /dcache_tb/datacacheif/dwait
add wave -noupdate /dcache_tb/datacacheif/dREN
add wave -noupdate /dcache_tb/datacacheif/dWEN
add wave -noupdate /dcache_tb/dcif/dhit
add wave -noupdate /dcache_tb/dcif/dmemREN
add wave -noupdate /dcache_tb/dcif/dmemWEN
add wave -noupdate /dcache_tb/dcif/flushed
add wave -noupdate /dcache_tb/dcif/dmemload
add wave -noupdate /dcache_tb/dcif/dmemstore
add wave -noupdate /dcache_tb/dcif/dmemaddr
add wave -noupdate /dcache_tb/ccif/dwait
add wave -noupdate /dcache_tb/ccif/dREN
add wave -noupdate /dcache_tb/ccif/dWEN
add wave -noupdate /dcache_tb/ccif/dload
add wave -noupdate /dcache_tb/ccif/dstore
add wave -noupdate /dcache_tb/ccif/daddr
add wave -noupdate /dcache_tb/DUT/daddr
add wave -noupdate /dcache_tb/DUT/index
add wave -noupdate /dcache_tb/DUT/block_offset
add wave -noupdate /dcache_tb/DUT/next_block_offset
add wave -noupdate /dcache_tb/DUT/byte_offset
add wave -noupdate /dcache_tb/DUT/flushing
add wave -noupdate /dcache_tb/DUT/flushFIdx
add wave -noupdate /dcache_tb/DUT/flushBIdx
add wave -noupdate /dcache_tb/DUT/current_state
add wave -noupdate /dcache_tb/DUT/next_state
add wave -noupdate /dcache_tb/DUT/dirty_bit_set
add wave -noupdate /dcache_tb/DUT/not_least_recently_used
add wave -noupdate /dcache_tb/DUT/least_recently_used
add wave -noupdate -expand /dcache_tb/DUT/frames
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {560 ns} 0}
quietly wave cursor active 1
configure wave -namecolwidth 150
configure wave -valuecolwidth 608
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
WaveRestoreZoom {467 ns} {591 ns}
