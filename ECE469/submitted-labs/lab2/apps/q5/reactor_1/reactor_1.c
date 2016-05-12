#include "lab2-api.h"
#include "usertraps.h"
#include "misc.h"
#include "prod_cons.h"

void main(int argc, char * argv[])
{
  sem_t h2o_sem,h2_sem,o2_sem;
  int counter;
  int h2_counter,o2_counter;
  sem_t s_procs_completed; // Semaphore to signal the original process that we're done 
  h2o_sem = dstrtol(argv[1], NULL, 10);
  h2_sem = dstrtol(argv[2],NULL, 10);
  o2_sem = dstrtol(argv[3],NULL, 10);
  counter = dstrtol(argv[4],NULL,10);

  s_procs_completed = dstrtol(argv[5], NULL, 10);


  while (counter != 0)
    {
      if(sem_wait(h2o_sem) == SYNC_FAIL){Printf("Baad sem_wait in reactor_1\n");}
      if(sem_wait(h2o_sem) == SYNC_FAIL){Printf("Bad sem_wait in reactor_2\n");}
      Printf("H2 created in reactor 1\n");
      Printf("H2 created in reactor 1\n");
      h2_counter = h2_counter + 2;
      o2_counter++;
      Printf("O2 created in reactor 1\n");
      if(sem_signal(h2_sem) == SYNC_FAIL){Printf("bad sem_signal in reactor_1");}
      if(sem_signal(h2_sem) == SYNC_FAIL){Printf("bad sem_signal in reactor_1");}
      if(sem_signal(o2_sem) == SYNC_FAIL){Printf("bad sem_signal in reactor_1");}
      counter--;
    }

  Printf("\nreactor_1 is terminated.\nWe created %d o2, and %d h2\n", o2_counter,h2_counter);
  if(sem_signal(s_procs_completed) != SYNC_SUCCESS) {
    Printf("Bad semaphore s_procs_completed (%d) in ", s_procs_completed); Printf(argv[0]); Printf(", exiting...\n");
    Exit();
  }
}
