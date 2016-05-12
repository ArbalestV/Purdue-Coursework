#include "lab2-api.h"
#include "usertraps.h"
#include "misc.h"

#include "prod_cons.h"

void main (int argc, char * argv[])
{
  int numprocs = 0; //the total number of producers and consumers
  int i; //loop index
  prod_cons *pc; //used to get address of shared memory page
  uint32 h_mem; //hold the handle to the shared memory page
  sem_t s_procs_completed; //semaphore used to wait until all processes have been completed
  char h_mem_str[10]; //used as a command line argument to pass mem_handle to new processes
  char s_procs_completed_str[10]; //used as command-line argument to pass page mapped handle to new processes


  //uint32 h_lock; //handler for the lock
  //Lock *prod_cons_lock; //used to get the address of the lock structure
  //char h_lock_str[10]; //used as command line argument to pass lock handler to new processes
  lock_t lock_handler;
  char lock_handler_str[10];
  
  
  if (argc != 2) {
    Printf("Usage: "); 
    Printf(argv[0]);
    Printf(" <number of processes to create>\n");
    Exit();
  }

  if (argc != 2) {
    Printf("Usage: "); Printf(argv[0]); Printf(" <number of processes to create>\n");
    Exit();
  }

  // Convert string from ascii command line argument to integer number
  numprocs = dstrtol(argv[1], NULL, 10); // the "10" means base 10
  Printf("Creating %d processes\n", numprocs);

  // Allocate space for a shared memory page, which is exactly 64KB
  // Note that it doesn't matter how much memory we actually need: we 
  // always get 64KB
  if ((h_mem = shmget()) == 0) {
    Printf("ERROR: could not allocate shared memory page in "); Printf(argv[0]); Printf(", exiting...\n");
    Exit();
  }

  // Map shared memory page into this process's memory space
  if ((pc = (prod_cons *)shmat(h_mem)) == NULL) {
    Printf("Could not map the shared page to virtual address in "); Printf(argv[0]); Printf(", exiting..\n");
    Exit();
  }


  /*if ((h_lock = shmget()) == 0) {
    Printf("ERROR: could not allocate shared lock for producer-consumer.");
    Exit();
    }*/
  lock_handler = lock_create();
  

  //Get the value of numprocs in the shared memory space
  pc->numprocs = numprocs;

  // Create semaphore to not exit this process until all other processes 
  // have signalled that they are complete.  To do this, we will initialize
  // the semaphore to (-1) * (number of signals), where "number of signals"
  // should be equal to the number of processes we're spawning - 1.  Once 
  // each of the processes has signaled, the semaphore should be back to
  // zero and the final sem_wait below will return.
  if ((s_procs_completed = sem_create(-(numprocs-1))) == SYNC_FAIL) {
    Printf("Bad sem_create in "); Printf(argv[0]); Printf("\n");
    Exit();
  }

  // Setup the command-line arguments for the new process.  We're going to
  // pass the handles to the shared memory page and the semaphore as strings
  // on the command line, so we must first convert them from ints to strings.
  ditoa(h_mem, h_mem_str);
  ditoa(s_procs_completed, s_procs_completed_str);

  //do the above for the shared lock
  //ditoa(h_lock, h_lock_str);
  ditoa(lock_handler, lock_handler_str);

  //initialize the head and the tail pointer to 0.
  pc->head = 0;
  pc->tail = 0;


  // Now we can create the processes.  Note that you MUST end your call to
  // process_create with a NULL argument so that the operating system
  // knows how many arguments you are sending.
  for(i=0; i<numprocs; i++) {
    process_create(PRODUCER_TO_RUN, h_mem_str, s_procs_completed_str, lock_handler_str, NULL);
    Printf("Producer %d created\n", i);
    process_create(CONSUMER_TO_RUN, h_mem_str, s_procs_completed_str, lock_handler_str, NULL);
    Printf("Consumer %d created\n", i);
  }


  // And finally, wait until all spawned processes have finished.
  if (sem_wait(s_procs_completed) != SYNC_SUCCESS) {
    Printf("Bad semaphore s_procs_completed (%d) in ", s_procs_completed); Printf(argv[0]); Printf("\n");
    Exit();
  }
  Printf("All other processes completed, exiting main process.\n");
}
