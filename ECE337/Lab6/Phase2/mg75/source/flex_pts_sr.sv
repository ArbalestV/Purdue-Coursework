module flex_pts_sr
#(
  parameter NUM_BITS = 4,
  parameter SHIFT_MSB = 1
)
(
	input wire clk,
	input wire n_rst,
	input wire shift_enable,
	input wire load_enable,
	input wire [NUM_BITS-1:0] parallel_in,
	output wire serial_out
);
wire [NUM_BITS - 1:0] rev;
genvar i;
generate
  for (i = 0; i < NUM_BITS; i = i + 1) begin
   assign rev[NUM_BITS - 1 - i] = parallel_in[i];
  end
endgenerate
wire [NUM_BITS - 1:0] ip;
assign ip = (SHIFT_MSB == 1'b1) ? parallel_in : rev;
reg [NUM_BITS - 1:0] ip_nxt;
assign serial_out = ip_nxt[NUM_BITS - 1];
always@(posedge clk, negedge n_rst) begin
  if (n_rst == 1'b0)
    ip_nxt[0] <= 1'b1;
  else begin
    if (load_enable == 1'b1) 
      ip_nxt[0] <= ip[0];
    else if (shift_enable == 1'b1) 
      ip_nxt[0] <= 1'b0;
    else 
      ip_nxt[0] <= ip_nxt[0]; 
  end
end

genvar j;
generate
  for (j = 1; j < NUM_BITS; j = j + 1) begin
    always@(posedge clk, negedge n_rst) begin
      if (n_rst == 1'b0)
        ip_nxt[j] <= 1'b1;
      else begin
        if (load_enable == 1'b1) 
          ip_nxt[j] <= ip[j];
        else if (shift_enable == 1'b1) 
          ip_nxt[j] <= ip_nxt[j - 1];
       else 
          ip_nxt[j] <= ip_nxt[j]; 
      end
    end
  end
endgenerate
endmodule
   


