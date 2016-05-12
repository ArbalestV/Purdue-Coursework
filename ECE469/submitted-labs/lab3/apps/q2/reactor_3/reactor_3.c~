#include "lab2-api.h"
#include "usertraps.h"
#include "misc.h"
#include "prod_cons.h"

void main(int argc, char * argv[])
{
  sem_t h2_sem,o2_sem,so2_sem,h2so4_sem;
  int counter;
  sem_t s_procs_completed; // Semaphore to signal the original process that we're done 
  int h2so4_counter;

  h2_sem = dstrtol(argv[1], NULL, 10);
  o2_sem = dstrtol(argv[2], NULL, 10);
  so2_sem = dstrtol(argv[3],NULL, 10);
  h2so4_sem = dstrtol(argv[4],NULL,10);
  counter = dstrtol(argv[5],NULL,10);
  s_procs_completed = dstrtol(argv[6], NULL, 10);

  while (counter != 0)
    {
      if(sem_wait(h2_sem) == SYNC_FAIL){Printf("bad semwait in reactor3\n");}
      if(sem_wait(o2_sem) == SYNC_FAIL){Printf("bad semwait in reactor3\n");}
      if(sem_wait(so2_sem)== SYNC_FAIL){Printf("bad semwaitn in reactor2\n");}
      Printf("H2SO4 created in reactor 3\n");
      if(sem_signal(h2so4_sem)== SYNC_FAIL){Printf("bad semsignal in reactor3\n");}
      h2so4_counter++;
      counter--;
    }
  
  Printf("\nreactor_3 is terminated.\n we created %d H2SO4 \n", h2so4_counter);
  if(sem_signal(s_procs_completed) != SYNC_SUCCESS) {
    Printf("Bad semaphore s_procs_completed (%d) in ", s_procs_completed); Printf(argv[0]); Printf(", exiting...\n");
    Exit();
  }

}
