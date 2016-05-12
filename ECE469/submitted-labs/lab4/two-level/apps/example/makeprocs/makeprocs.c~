#include "usertraps.h"
#include "misc.h"
//#include "reqs.h"
#define HELLO_WORLD "hello_world.dlx.obj"
#define STEP1 "step1.dlx.obj"
#define STEP2 "step2.dlx.obj"
#define STEP3 "step3.dlx.obj"
#define STEP4 "step4.dlx.obj"
//#define STEP5 "step5.dlx.obj"
#define STEP6 "step6.dlx.obj"

void main (int argc, char *argv[])
{
  int num_hello_world = 0;             // Used to store number of processes to create
  int i;                               // Loop index variable
  sem_t s_procs_completed;             // Semaphore used to wait until all spawned processes have completed
  char s_procs_completed_str[10];      // Used as command-line argument to pass page_mapped handle to new processes

  if (argc != 2) {
    Printf("Usage: %s <number of hello world processes to create>\n", argv[0]);
    Exit();
  }

  // Convert string from ascii command line argument to integer number
  num_hello_world = dstrtol(argv[1], NULL, 10); // the "10" means base 10
  Printf("makeprocs (%d): Creating %d hello_world processes\n", getpid(), num_hello_world);

  // Create semaphore to not exit this process until all other processes 
  // have signalled that they are complete.
  if ((s_procs_completed = sem_create(0)) == SYNC_FAIL) {
    Printf("makeprocs (%d): Bad sem_create\n", getpid());
    Exit();
  }
  //Printf("\ns_procs_completed: %d\n", s_procs_completed);
  // Setup the command-line arguments for the new processes.  We're going to
  // pass the handles to the semaphore as strings
  // on the command line, so we must first convert them from ints to strings.
  ditoa(s_procs_completed, s_procs_completed_str);

  // Create Hello World processes
  /*
  Printf("-------------------------------------------------------------------------------------\n");
  Printf("makeprocs (%d): Creating %d hello world's in a row, but only one runs at a time\n", getpid(), num_hello_world);
  for(i=0; i<num_hello_world; i++) {
    Printf("makeprocs (%d): Creating hello world #%d\n", getpid(), i);
    process_create(HELLO_WORLD, s_procs_completed_str, NULL);
    if (sem_wait(s_procs_completed) != SYNC_SUCCESS) {
      Printf("Bad semaphore s_procs_completed (%d) in %s\n", s_procs_completed, argv[0]);
      Exit();
    }
  }
  */
  //Printf("\nOut of hello_worlds.\n");
  //this is where we do steps 1-6 one by one
  //now code for calling step1 code

  
  Printf("------------------BEGINNING OF STEP1--------------------------------------\n");
  Printf("makeprocs (%d): Creating 1 program to print hello world and then exit.\n", getpid());
  process_create(STEP1, s_procs_completed_str,  NULL); //create the process
  if (sem_wait(s_procs_completed) != SYNC_SUCCESS) {
      Printf("Bad semaphore s_procs_completed (%d) in %s\n", s_procs_completed, argv[0]);
      Exit();
    }
  Printf("----END OF STEP1--------\n");
  


  //now code for calling step3 code
  
  Printf("--------------------BEGINNING OF STEP3---------------------------------------------\n");
  Printf("makeprocs (%d): Creating 1 program to access memory inside the virtual address space, but outside of currently allocated pages.\n", getpid());
  process_create(STEP3, s_procs_completed_str,  NULL); //create the process
  if (sem_wait(s_procs_completed) != SYNC_SUCCESS) {
      Printf("Bad semaphore s_procs_completed (%d) in %s\n", s_procs_completed, argv[0]);
      Exit();
    }
  Printf("\n----END OF STEP3--------\n");
  
  /*Printf("-------------------BEGINNING OF STEP2--------------------------------------------\n");
  Printf("makeprocs (%d): Creating 1 program to access memory beyond the maximum virtual address.\n", getpid());
  process_create(STEP2, s_procs_completed_str,  NULL); //create the process
  if (sem_wait(s_procs_completed) != SYNC_SUCCESS) {
      Printf("Bad semaphore s_procs_completed (%d) in %s\n", s_procs_completed, argv[0]);
      Exit();
    }
    Printf("----END OF STEP2--------\n");*/

  //now code for calling step4 code
  
  Printf("-------------------BEGINNING OF STEP4---------------------------------------------\n");
  Printf("makeprocs (%d): Creating a process that allocates more than one element for stack.\n", getpid());
  process_create(STEP4, s_procs_completed_str,  NULL); //create the process
  if (sem_wait(s_procs_completed) != SYNC_SUCCESS) {
      Printf("Bad semaphore s_procs_completed (%d) in %s\n", s_procs_completed, argv[0]);
      Exit();
    }
  Printf("----END OF STEP4--------\n");
  

  //now code for calling step5 code
  
  Printf("-------------------BEGINNING OF STEP5---------------------------------------------\n");
  Printf("makeprocs (%d): Calling the Hello World program 100 times, one at a time.\n", getpid());
  for(i=0; i<100; i++) {
    Printf("makeprocs (%d): Creating hello world #%d\n", getpid(), i);
    process_create(HELLO_WORLD, s_procs_completed_str, NULL);
    if (sem_wait(s_procs_completed) != SYNC_SUCCESS) {
      Printf("Bad semaphore s_procs_completed (%d) in %s\n", s_procs_completed, argv[0]);
      Exit();
    }
  }
  Printf("----END OF STEP5--------\n");
  

  //now code for calling step6 code
  
  Printf("------------------BEGINNING OF STEP6---------------------------------------------\n");
  Printf("makeprocs (%d): Spawning 30 simultaneous processes for Step 6.\n", getpid());
  for (i = 0; i < 30; i++)
    {
      Printf("\nSpawning process: %d\n", i);
      process_create(STEP6, s_procs_completed_str,  NULL); //create the process
    }
  
  if (sem_wait(s_procs_completed) != SYNC_SUCCESS) {
      Printf("Bad semaphore s_procs_completed (%d) in %s\n", s_procs_completed, argv[0]);
      Exit();
    }

  Printf("\n----END OF STEP6--------\n");
  
  
  
  //now code for calling step2 code
  /*
  Printf("-------------------BEGINNING OF STEP2--------------------------------------------\n");
  Printf("makeprocs (%d): Creating 1 program to access memory beyond the maximum virtual address.\n", getpid());
  process_create(STEP2, s_procs_completed_str,  NULL); //create the process
  if (sem_wait(s_procs_completed) != SYNC_SUCCESS) {
      Printf("Bad semaphore s_procs_completed (%d) in %s\n", s_procs_completed, argv[0]);
      Exit();
    }
    Printf("----END OF STEP2--------\n");
  */
 


  // And finally, wait until all spawned processes have finished.
  //Printf("\nHere.\n");
  //Printf("\ns_procs_completed: %d\n", s_procs_completed);
  /*if (sem_wait(s_procs_completed) != SYNC_SUCCESS) {
    Printf("Bad semaphore s_procs_completed (%d) in ", s_procs_completed); Printf(argv[0]); Printf("\n");
    Exit();
    }*/
  //Printf("\nOut of here.\n");

  Printf("-------------------------------------------------------------------------------------\n");
  Printf("makeprocs (%d): All other processes completed, exiting main process.\n", getpid());

}
