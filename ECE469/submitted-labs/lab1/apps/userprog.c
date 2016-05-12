#include "usertraps.h"

void main (int x)
{
  int currentPid = Getpid();
  Printf("Hello World!\n");
  Printf("The current process id = %d", currentPid);
  while(1); // Use CTRL-C to exit the simulator
}
