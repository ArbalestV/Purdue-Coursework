// $Id: $
// File name:   sensor_s.sv
// Created:     9/3/2014
// Author:      Pranjit Kumar Kalita
// Lab Section: 337-02
// Version:     1.0  Initial Design Entry
// Description: sensor
module sensor_s(
  input wire [3:0] sensors,
  output wire error
 );
 
 
 wire Y1, Y2, Y3;
 and A1 (Y1, sensors[2], sensors[1]);
 and A2 (Y2, sensors[1], sensors[3]);
 or A3 (Y3, Y1, Y2);
 or A4 (error, sensors[0], Y3);
 
 
 endmodule
 