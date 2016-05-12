module timer
  (
    input wire clk,
    input wire n_rst,
    input wire rising_edge_found,
    input wire falling_edge_found,
    input wire stop_found,
    input wire start_found,
    output reg byte_received,
    output reg ack_prep,
    output reg check_ack,
    output reg ack_done
    );
    reg rollover_flag;
    reg [3:0] count_out;

    flex_counter #(4) CTR (.clk(clk), .n_rst(n_rst), .count_enable(rising_edge_found), 
    .clear(ack_done | start_found), .rollover_val(4'b1001), .count_out(count_out), 
    .rollover_flag(rollover_flag));

    typedef enum logic [2:0] {BEGIN, COUNT, ACK_PREP, ACK_CHECK, ACK_DONE} state_type;
    state_type state, nextstate;
    always@(posedge clk, negedge n_rst)
    begin
      if (n_rst == 0) 
      begin
        state <= BEGIN;
      end
      else begin
        state <= nextstate;
      end
    end
    
    always @(state, falling_edge_found, stop_found, start_found, count_out, rollover_flag) begin
      nextstate = BEGIN;
      byte_received = 1'b0;
      ack_prep = 1'b0;
      check_ack = 1'b0;
      ack_done = 1'b0;
      case(state) 
        BEGIN: begin
          if (start_found == 1'b1)
            nextstate = COUNT;
          else
            nextstate = BEGIN;
        end
        COUNT: begin
          if (stop_found == 1'b1) 
            nextstate = BEGIN;
          if (count_out == 4'b1000) begin
            byte_received = 1'b1;
            nextstate = ACK_PREP;
          end
          else
            nextstate = COUNT;
        end
        ACK_PREP: begin
          //byte_received = 1'b0;
          if (falling_edge_found == 1'b1) begin
            ack_prep = 1'b1;
            nextstate = ACK_CHECK;
          end
          else
            nextstate = ACK_PREP;
        end
        ACK_CHECK: begin
          //ack_prep = 1'b0;
          if (rollover_flag == 1'b1) begin
            check_ack = 1'b1;
            nextstate = ACK_DONE;
          end
          else
            nextstate = ACK_CHECK;
        end
        ACK_DONE: begin
          //check_ack = 1'b0;
          if (falling_edge_found == 1'b1) begin
            ack_done = 1'b1;
            nextstate = COUNT;
          end
          else
            nextstate = ACK_DONE;
        end
      endcase
    end
  endmodule
            
        
