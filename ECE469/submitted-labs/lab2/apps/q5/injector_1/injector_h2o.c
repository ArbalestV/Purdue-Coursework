#include "lab2-api.h"
#include "usertraps.h"
#include "misc.h"
#include "prod_cons.h"

void main(int argc, char * argv[])
{
  
  int h2o;
  sem_t h2o_sem;
  sem_t s_procs_completed; // Semaphore to signal the original process that we're done 
  //Printf("Are we in injector1...\n");
  if (argc != 4){
    Printf("must pass three arguments");
    Exit();
  }
  //Printf("finished the if statement\n");
  //Printf(argv[1]);
  //Printf("\n");
  h2o = dstrtol(argv[1], NULL, 10);//integer conversion
  //Printf("1\n");
  h2o_sem = dstrtol(argv[2],NULL, 10);//Printf("21\n");
  s_procs_completed = dstrtol(argv[3], NULL, 10);//Printf("31\n");
  //Printf("finished conversion of string to semophore...\n");
  if (h2o <= 0){
    Printf("less then 0 molecules injected!\n");
  }
  //Printf("about to enter injector_1 while loop...\n");
  while(h2o != 0)
    {
      Printf("H2O was injected \n");
      if(sem_signal(h2o_sem) != SYNC_SUCCESS){
	Printf("Bad semophore created in injector_h20\n");
      }
      h2o--;
    }
  /*if(sem_signal(h2o_sem_empty) != SYNC_SUCCESS){
    Printf("BAD semophore signaled in injector h20\n");
  }*/
  
  if(sem_signal(s_procs_completed) != SYNC_SUCCESS) {
    Printf("Bad semaphore s_procs_completed (%d) in ", s_procs_completed); Printf(argv[0]); Printf(", exiting...\n");
    Exit();
  }

}
  
  
