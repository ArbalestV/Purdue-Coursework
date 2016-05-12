#include "usertraps.h"
#include "misc.h"

void main (int argc, char *argv[])
{
  int i;
  sem_t sem;
  char sem_str[10];

  // Semaphore used to wait until one test completes before starting the next
  if ((sem = sem_create(0)) == SYNC_FAIL) {
    Printf("makeprocs (%d): Bad sem_create\n", getpid());
    Exit();
  }
  ditoa(sem, sem_str);

  //comment the following 2 lines to run test2.
  Printf("\nmakeprocs 1.\n");
  //Printf("\nCreating test1.c\n");
  process_create("test1.dlx.obj", sem_str, NULL);
  //Printf("\nComing out of the first test process before sem_wait(sem).\n");
  sem_wait(sem);
  //Printf("\nComing out of the first test process...\n");
  Printf("\nGoing in to create the second test process.\n");
  process_create("test2.dlx.obj", sem_str, NULL);
  sem_wait(sem);
 
  Printf("------------------Makeprocs complete-------------------\n");

}
