module scl_edge
  (
    input wire clk,
    input wire n_rst,
    input wire scl,
    output wire rising_edge_found,
    output wire falling_edge_found
    );
    
    
    reg nxt_state, cur_state, nxt_state2,cur_state_2;
    always_ff @(posedge clk, negedge n_rst) begin
      if (n_rst == 1'b0) begin
        nxt_state <= 1'b1;
        nxt_state2 <= 1'b1;
      end
      else begin
        
        nxt_state <= cur_state;
        nxt_state2 <= cur_state_2;
      end
    end
    
    always_comb
    begin
        cur_state = scl;
        cur_state_2=nxt_state;
    end
  
    assign rising_edge_found = (!nxt_state2 & nxt_state);
    assign falling_edge_found = (!nxt_state & nxt_state2);
  endmodule
  
        
    
  