//#include "lab2-api.h"
#include "usertraps.h"
#include "misc.h"
#include "prod_cons.h"
/* Most of this is just copy and pasted from makeprocs in q2, mostly just changed where it said lock to now a cond_t
there are some other small changes as well i noticed we had some useless code around line 33*/
void main (int argc, char * argv[])
{
  int h2o = 0; //the number of h20 injected
  int so4 = 0; //the number of s04 injected
  int num_reactor_1, num_reactor_2, num_reactor_3;
  //char r1_str[10], r2_str[10],r3_str[10];
  //uint32 h_mem;
  //sem_t h2o_sem;//semophore used for h20
  //char  h2o_sem_str[10];//string in argument
  //sem_t so4_sem;//semophore used for s04
  //char  so4_sem_str[10];//string in argument
  //sem_t h2_sem; //semophore used for h2
  //char  h2_sem_str[10];//string in argument line
  //sem_t o2_sem; //semophore used for o2
  //char  o2_sem_str[10];//string in argument line
  //sem_t so2_sem;//semophore used for so2
  //char  so2_sem_str[10];//string in argument line
  //sem_t h2so4_sem;//semophore used for h2so4
  //char  h2so4_sem_str[10];//string in argument line
  // sem_t h2o_sem_empty;
  //char  h2o_sem_empty_str[10];
  mbox_t h_mbox_h2o, h_mbox_h2, h_mbox_o2, h_mbox_so4, h_mbox_so2, h_mbox_h2so4;
  char h_mbox_str_h2o[10];
  char h_mbox_str_h2[10];
  char h_mbox_str_o2[10];
  char h_mbox_str_so4[10];
  char h_mbox_str_so2[10];
  char h_mbox_str_h2so4[10];

  sem_t s_procs_completed;
  char s_procs_completed_str[10];
  int arg1,arg2;
  char argv1[10];
  char argv2[10];

  int num_o2_1;
  int num_o2_2;
  int num_o2_tot;
  
  int total_procs;

  arg1 = dstrtol(argv[1],NULL,10);
  arg2 = dstrtol(argv[2],NULL,10);
  ditoa(arg1, argv1);
  ditoa(arg2, argv2);
  //char h2o_string[1];
  //Printf("we are here...\n");
  //Printf(argv[0]);
  //Printf("%d\n",argc);
  //Printf(argv1);
  //Printf(argv2);
  if (argc != 3) {
    Printf("Usage: "); 
    Printf(argv[0]);
    Printf(" <should control 5 procs with a semaphore for each molecule>\n");
    Exit();
  }

  // Allocate space for a mailbox
  if ((h_mbox_h2o = mbox_create()) == MBOX_FAIL) {
    Printf("makeprocs (%d): ERROR: could not allocate mailbox!", getpid());
    Exit();
  }
  Printf("Mailbox handler number: %d\n", h_mbox_h2o);

  // Allocate space for a mailbox
  if ((h_mbox_h2 = mbox_create()) == MBOX_FAIL) {
    Printf("makeprocs (%d): ERROR: could not allocate mailbox!", getpid());
    Exit();
  }
  Printf("Mailbox handler number: %d\n", h_mbox_h2);

  // Allocate space for a mailbox
  if ((h_mbox_o2 = mbox_create()) == MBOX_FAIL) {
    Printf("makeprocs (%d): ERROR: could not allocate mailbox!", getpid());
    Exit();
  }
  Printf("Mailbox handler number: %d\n", h_mbox_o2);

  // Allocate space for a mailbox
  if ((h_mbox_so4 = mbox_create()) == MBOX_FAIL) {
    Printf("makeprocs (%d): ERROR: could not allocate mailbox!", getpid());
    Exit();
  }
  Printf("Mailbox handler number: %d\n", h_mbox_so4);

  // Allocate space for a mailbox
  if ((h_mbox_so2 = mbox_create()) == MBOX_FAIL) {
    Printf("makeprocs (%d): ERROR: could not allocate mailbox!", getpid());
    Exit();
  }
  Printf("Mailbox handler number: %d\n", h_mbox_so2);

  // Allocate space for a mailbox
  if ((h_mbox_h2so4 = mbox_create()) == MBOX_FAIL) {
    Printf("makeprocs (%d): ERROR: could not allocate mailbox!", getpid());
    Exit();
  }
  Printf("Mailbox handler number: %d\n", h_mbox_h2so4);

  //Printf("converting string from ascii\n");
  // Convert string from ascii command line argument to integer number
  h2o = dstrtol(argv[1], NULL, 10); // h2o integer creation
  so4 = dstrtol(argv[2], NULL, 10); // so4 integer creation

  /*  // Allocate space for a shared memory page, which is exactly 64KB
  // Note that it doesn't matter how much memory we actually need: we 
  // always get 64KB
  if ((h_mem = shmget()) == 0) {
    Printf("ERROR: could not allocate shared memory page in "); Printf(argv[0]); Printf(", exiting...\n");
    Exit();
    }*/
  //math for number of reactions
  num_reactor_1 = h2o / 2;
  num_reactor_2 = so4;
  num_o2_1 = num_reactor_1;
  num_o2_2 = num_reactor_2;
  num_o2_tot = num_o2_1 + num_o2_2;
  Printf("\nTotal number of hydrogen produced: %d", h2o);
  Printf("\nTotal number of oxygen produced: %d", num_o2_tot);
  Printf("\nTotal number of SO2 produced: %d", so4);
  if (h2o < num_o2_tot) {
    num_reactor_3 = num_reactor_1 * 2;
  }
  else {
    num_reactor_3 = num_o2_tot;
  }
  if (num_reactor_3 > so4) {
    num_reactor_3 = so4;
  }
  
  Printf("\nTotal number of H2So4 to be produced: %d\n", num_reactor_3);
  
  //Printf("\nstarting semaphores...\n");
  //start the semophores 
  /*
  if((h2o_sem = sem_create(0)) == SYNC_FAIL){
    Printf("Bad sem_create in h2o \n");
    Exit();}
  if((so4_sem = sem_create(0)) == SYNC_FAIL){
    Printf("Bad sem_create in so4 \n");
    Exit();}
  if((h2_sem = sem_create(0)) == SYNC_FAIL){
    Printf("Bad sem_create in h2 \n");
    Exit();}
  if((o2_sem = sem_create(0)) == SYNC_FAIL){
    Printf("Bad sem_Create in o2 \n");
    Exit();}
  if((so2_sem = sem_create(0)) == SYNC_FAIL){
    Printf("Bad sem_create in s02 \n");
    Exit();}
  if((h2so4_sem = sem_create(0)) == SYNC_FAIL){// probably dont need this
    Printf("Bad sem_create in h2so4 \n");
    Exit();}
  */
  /* if((h2o_sem_empty = sem_create(0)) == SYNC_FAIL){
    Printf("Bad sem_create in h2o empty\n");
    Exit();}*/






  // Create semaphore to not exit this process until all other processes 
  // have signalled that they are complete.  To do this, we will initialize
  // the semaphore to (-1) * (number of signals), where "number of signals"
  // should be equal to the number of processes we're spawning - 1.  Once 
  // each of the processes has signaled, the semaphore should be back to
  // zero and the final sem_wait below will return.
  total_procs = h2o + so4 + num_reactor_1 + num_reactor_2 + num_reactor_3;
  Printf("\nThe total number of processes to be created : %d\n", total_procs);
  if ((s_procs_completed = sem_create(-(total_procs-1))) == SYNC_FAIL) {
    Printf("Bad sem_create in "); Printf(argv[0]); Printf("\n");
    Exit();
  }
  //Printf("setup command line args");
  // Setup the command-line arguments for the new process.  We're going to
  // pass the handles to the shared memory page and the semaphore as strings
  // on the command line, so we must first convert them from ints to strings.
  ditoa(h_mbox_h2o, h_mbox_str_h2o);
  ditoa(h_mbox_h2, h_mbox_str_h2);
  ditoa(h_mbox_o2, h_mbox_str_o2);
  ditoa(h_mbox_so4, h_mbox_str_so4);
  ditoa(h_mbox_so2, h_mbox_str_so2);
  ditoa(h_mbox_h2so4, h_mbox_str_h2so4);

  ditoa(s_procs_completed, s_procs_completed_str);
  sleep(30);




  // Printf("string conversion...\n");
  //lots of string conversion  
  /*
  ditoa(h2o_sem, h2o_sem_str);
  ditoa(so4_sem, so4_sem_str);
  ditoa(h2_sem,h2_sem_str);
  ditoa(o2_sem,o2_sem_str);
  ditoa(so2_sem,so2_sem_str);
  ditoa(h2so4_sem,h2so4_sem_str);
  */
  //ditoa(num_reactor_1,r1_str); 
  //ditoa(num_reactor_2,r2_str);
  //ditoa(num_reactor_3,r3_str);
  Printf("\nstarting injector processes...\n");
  // start the injector processes
  //process_create(INJECTOR_H2O,argv1,h2o_sem_str, s_procs_completed_str, NULL);//argv[1] is h20 string didnt feel like creating new var
  while (h2o > 0)
    {
      process_create(INJECTOR_H2O, 10, 1, h_mbox_str_h2o, s_procs_completed_str, NULL);
      h2o--;
    }
  //process_create(INJECTOR_SO4,argv2,so4_sem_str, s_procs_completed_str, NULL);//argv[2] is so4 string didnt feel like creating a new var
  while (so4 > 0)
    {
      process_create(INJECTOR_SO4, 20, 1, h_mbox_str_so4, s_procs_completed_str, NULL);
      so4--;
    }
  //start the reactor processes
  Printf("starting reactor processes...\n");
  //process_create(REACTOR_1,h2o_sem_str,h2_sem_str,o2_sem_str,r1_str, s_procs_completed_str, NULL);
  while (num_reactor_1 > 0)
    {
      process_create(REACTOR_1, 1, 1, h_mbox_str_h2o, h_mbox_str_h2, h_mbox_str_o2, s_procs_completed_str, NULL);
      num_reactor_1--;
    }
  //process_create(REACTOR_2,so4_sem_str,so2_sem_str,o2_sem_str, r2_str, s_procs_completed_str, NULL);
  while (num_reactor_2 > 0)
    {
      process_create(REACTOR_2, 15, 1, h_mbox_str_so4, h_mbox_str_so2, h_mbox_str_o2, s_procs_completed_str, NULL);
      num_reactor_2--;
    }
  //process_create(REACTOR_3,h2_sem_str,o2_sem_str,so2_sem_str,h2so4_sem_str, r3_str, s_procs_completed_str, NULL);
  while (num_reactor_3 > 0)
    {
      process_create(REACTOR_3, 2, 1, h_mbox_str_h2, h_mbox_str_o2, h_mbox_str_so2, h_mbox_str_h2so4, s_procs_completed_str, NULL);
      num_reactor_3--;
    }


  //now we will be sending the messages inside the mailboxes to each of the wo injectors and the reactors
  

  sleep(200000);

  // And finally, wait until all spawned processes have finished.
  if (sem_wait(s_procs_completed) != SYNC_SUCCESS) {
    Printf("Bad semaphore s_procs_completed (%d) in ", s_procs_completed); Printf(argv[0]); Printf("\n");
    Exit();
  }
  Printf("All other processes completed, exiting main process.\n");
}
