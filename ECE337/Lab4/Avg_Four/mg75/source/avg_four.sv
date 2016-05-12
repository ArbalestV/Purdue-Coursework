module avg_four
  (
    input wire clk,
    input wire n_reset,
    input wire [15:0] sample_data,
    input wire data_ready,
    output wire one_k_samples,
    output wire modwait,
    output wire [15:0] avg_out,
    output wire err
  );
  reg dr; 
    sync sync_main
    (
      .clk(clk),
      .n_rst(n_reset),
      .async_in(data_ready),
      .sync_out(dr)
    );
    reg cnt_up;
    reg [1:0] op;
    reg [3:0] src1;
    reg [3:0] src2;
    reg [3:0] dest;  
    controller control
    (
      .clk(clk),
      .n_reset(n_reset),
      .dr(dr),
      .overflow(overflow),
      .modwait(modwait),
      .err(err),
      .cnt_up(cnt_up),
      .op(op),
      .src1(src1),
      .src2(src2),
      .dest(dest)
      );
  
    
  counter ctr_main
  (
    .clk(clk),
    .n_reset(n_reset),
    .one_k_samples(one_k_samples),
    .cnt_up(cnt_up)
    );
   
    
    
     reg [15:0] sum_tot;
    datapath dp
    (
      .clk(clk),
      .n_reset(n_reset),
      .op(op),
      .src1(src1),
      .src2(src2),
      .dest(dest),
      .ext_data(sample_data),
      .outreg_data(sum_tot),
      .overflow(overflow)
      );
      
      //now assign the divide by 4 by shifting the sum_tot by 2 to right
      assign avg_out = {2'b00, sum_tot[15:2]};
      
    endmodule
      
      
      
  
  