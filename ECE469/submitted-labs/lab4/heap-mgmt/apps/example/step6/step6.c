#include "usertraps.h"
#include "misc.h"

//spawn me step with looping a large number of times to facilitate 30 different processes running at the same time
void main (int argc, char *argv[])
{
  sem_t s_procs_completed; // Semaphore to signal the original process that we're done
  int i;
  
  if (argc != 2) { 
    Printf("Usage: %s <handle_to_procs_completed_semaphore>\n"); 
    Exit();
  }
  
  // Convert the command-line strings into integers for use as handles
  s_procs_completed = dstrtol(argv[1], NULL, 10);
  

  
   Printf("\nThe Test Program 5 - loop for a large number of times..");
   for (i = 0; i < 1000000; i++)
     {
       //Printf("\ni = %d, pid = %d", i, getpid());
     }

   Printf("\nEnd of looping in spawning for process id: %d", getpid()); 
   Printf("\nEnd of The Test Program 5 - loop for a large number of times..\n");
   // Signal the semaphore to tell the original process that we're done 
  if(sem_signal(s_procs_completed) != SYNC_SUCCESS) {
    Printf("hello_world (%d): Bad semaphore s_procs_completed (%d)!\n", getpid(), s_procs_completed);
    Exit();
  }
  
}
