module flex_stp_sr
#(
  parameter NUM_BITS = 4,
  parameter SHIFT_MSB = 1
)
(
	input wire clk,
	input wire n_rst,
	input wire shift_enable,
	input wire serial_in,
	output reg [NUM_BITS-1:0] parallel_out
);
//assign serial_in = 1'b1;
reg [NUM_BITS-1:0] f, NEXT;
integer i,k;

always_comb  begin //reset is 1
    if (SHIFT_MSB == 1'b1) begin
      if (shift_enable == 1'b0) begin
        NEXT<=f;
      end
      else begin
        NEXT[0] <= serial_in;
        for(i = 1; i <= NUM_BITS - 1; i = i + 1)
          begin 
            NEXT[i]<=f[i-1];
        end      
      end
    end
    else begin //SHIFT_MSB=0
      if (shift_enable == 1'b0) begin
        NEXT<=f;
      end
      else begin
        NEXT[NUM_BITS-1] <= serial_in;
        for(k = NUM_BITS-1; k > 0; k = k - 1)
          begin 
            NEXT[k-1]<=f[k];
        end      
      end
    end
  end

always_ff @ (posedge clk, negedge n_rst) begin
  if (n_rst == 0) begin
    f[NUM_BITS-1:0] <= '1;
  end
  else begin
    f <= NEXT;
  end
end
always_comb begin
   parallel_out=f;
 end
endmodule
