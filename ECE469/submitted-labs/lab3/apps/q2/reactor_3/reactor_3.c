//#include "lab2-api.h"
#include "usertraps.h"
#include "misc.h"
//#include "prod_cons.h"

void main(int argc, char * argv[])
{
  mbox_t h_mbox_h2, h_mbox_o2, h_mbox_so2, h_mbox_h2so4;
  //int counter;
  //int h2_counter,o2_counter;
  sem_t s_procs_completed; // Semaphore to signal the original process that we're done 
  char * msg = NULL;
  *(msg) = 'A'; //the dummy message
  h_mbox_h2 = dstrtol(argv[1], NULL, 10);
  h_mbox_o2 = dstrtol(argv[2],NULL, 10);
  h_mbox_so2 = dstrtol(argv[3],NULL, 10);
  h_mbox_h2so4 = dstrtol(argv[4],NULL,10);

  s_procs_completed = dstrtol(argv[5], NULL, 10);

  //receive h2, o2, so2 once each
  if (mbox_recv(h_mbox_h2, sizeof(msg), (void *) msg) == MBOX_FAIL) {
    Printf("\nCould not receive message in pid = %d!\n", getpid());
    Exit();
  }
  if (mbox_recv(h_mbox_o2, sizeof(msg), (void *) msg) == MBOX_FAIL) {
    Printf("\nCould not receive message in pid = %d!\n", getpid());
    Exit();
  }
  if (mbox_recv(h_mbox_so2, sizeof(msg), (void *) msg) == MBOX_FAIL) {
    Printf("\nCould not receive message in pid = %d!\n", getpid());
    Exit();
  }
 
  Printf("H2SO4 created in reactor 3\n");

  //now send H2SO4 once
  if (mbox_send(h_mbox_h2so4, sizeof(msg), (void *) msg) == MBOX_FAIL) {
    Printf("Could not send message to mailbox %d in (%d)\n", h_mbox_h2so4, getpid());
    Exit();
    }
  
  //Printf("\nreactor_3 is terminated.\n we created %d H2SO4 \n", h2so4_counter);
  if(sem_signal(s_procs_completed) != SYNC_SUCCESS) {
    Printf("Bad semaphore s_procs_completed (%d) in ", s_procs_completed); Printf(argv[0]); Printf(", exiting...\n");
    Exit();
  }

}
