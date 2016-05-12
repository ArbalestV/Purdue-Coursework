// $Id: $
// File name:   sensor_d.sv
// Created:     9/3/2014
// Author:      Pranjit Kumar Kalita
// Lab Section: 337-02
// Version:     1.0  Initial Design Entry
// Description: data flow sensor code
module sensor_d (
  input wire [3:0] sensors,
  output wire error
  );
  
  assign error = sensors[0] | (sensors[1] & sensors[2]) | (sensors[1] & sensors[3]);

endmodule
