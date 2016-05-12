module moore
  (
  input wire clk,
  input wire n_rst,
  input wire i,
  output reg o
  );
  typedef enum logic [2:0] {WAITING, RCV1, RCV11, RCV110, RCV1101} state_type;
  state_type state, nextstate;
  
  always@(posedge clk, negedge n_rst)
  begin
    if (n_rst == 0) 
    begin
      state <= WAITING;
    end
    else begin
      state <= nextstate;
    end
  end
  
  //output logic is behavioral
  
   always @ (state) 
    begin
    if ((state == RCV1101))
      begin
        o = 1'b1;
      end
      else
        begin
        o = 1'b0;
      end
    end
  
  always @ (state, i) begin : Next_state
    
    case (state)
      WAITING: begin
        if (i == 1)
          nextstate = RCV1;
        else
          nextstate = WAITING;
        end
        RCV1: begin
          if (i == 1)
            nextstate = RCV11;
          else
            nextstate = WAITING;
        end
        RCV11: begin
          if (i == 0)
            nextstate = RCV110;
          else
            nextstate = RCV11;
        end
        RCV110: begin
          if (i == 1)
            nextstate = RCV1101;
          else
            nextstate = WAITING;
        end
        RCV1101: begin
          if (i == 1)
            nextstate = RCV11;
          else
            nextstate = WAITING;
        end
        default : nextstate = WAITING;
      endcase
    end
  endmodule
        