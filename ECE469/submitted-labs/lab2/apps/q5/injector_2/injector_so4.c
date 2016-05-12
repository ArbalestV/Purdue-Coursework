#include "lab2-api.h"
#include "usertraps.h"
#include "misc.h"
#include "prod_cons.h"

void main(int argc, char * argv[])
{
  int so4;
  sem_t so4_sem;
  sem_t s_procs_completed; // Semaphore to signal the original process that we're done 
  //Printf("are we in injector 2...\n");
  so4 = dstrtol(argv[1], NULL, 10);//integer conversion
  so4_sem = dstrtol(argv[2], NULL, 10);
  s_procs_completed = dstrtol(argv[3], NULL, 10); 

  if (so4 <= 0){
    Printf("less then 0 molecules injected!\n");
  }
  while(so4 != 0)
    {
      Printf("SO4 was injected \n");
      if(sem_signal(so4_sem) != SYNC_SUCCESS){
	Printf("Bad semophore created in injector_h20\n");
      }
      so4--;
    }

  Printf("\ninjector_2 is terminated.\n");
  if(sem_signal(s_procs_completed) != SYNC_SUCCESS) {
    Printf("Bad semaphore s_procs_completed (%d) in ", s_procs_completed); Printf(argv[0]); Printf(", exiting...\n");
    Exit();
  }

}
