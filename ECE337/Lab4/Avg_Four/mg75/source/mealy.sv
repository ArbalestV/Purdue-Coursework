module mealy
  (
  input wire clk,
  input wire n_rst,
  input wire i,
  output reg o
  );
  typedef enum logic [1:0] {WAITING, RCVa, RCVb, RCVc} state_type;
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
  
  always @ (state, i) 
    begin
    if ((state == RCVc) && (i == 1'b1))
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
          nextstate = RCVa;
        else
          nextstate = WAITING;
        end
        RCVa: begin
          if (i == 1)
            nextstate = RCVb;
          else
            nextstate = WAITING;
        end
        RCVb: begin
          if (i == 0)
            nextstate = RCVc;
          else
            nextstate = RCVb;
        end
        RCVc: begin
          if (i == 1)
            nextstate = RCVa;
          else
            nextstate = WAITING;
        end
        default : nextstate = WAITING;
      endcase
    end
  endmodule