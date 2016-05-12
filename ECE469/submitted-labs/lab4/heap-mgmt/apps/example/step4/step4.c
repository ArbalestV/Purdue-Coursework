#include "usertraps.h"
#include "misc.h"
#include "os/memory_constants.h"
//growing stack size by more than 1 page

int recursive_function(int num)
{
  //Printf("\nCalled function is on : %d", num);
  Printf("\nCalled function is on : %d, address = %d", num, &num);
  if (num == 0)
    {
      return 0;
    }
  return (1 + recursive_function(num - 1));
}

void main (int argc, char *argv[])
{
  sem_t s_procs_completed; // Semaphore to signal the original process that we're done

  int argument_number;
  int answer;
  
  if (argc != 2) { 
    Printf("Usage: %s <handle_to_procs_completed_semaphore>\n"); 
    Exit();
  }
  
  // Convert the command-line strings into integers for use as handles
  s_procs_completed = dstrtol(argv[1], NULL, 10);

  
  
  Printf("\nThe Test Program 4 - growing stack size to more than 1 page..");

  argument_number = 1300;
  Printf("\nBeginning of function call of the recursion...");
  answer = recursive_function(argument_number);

  //number of recursive calls made will be the indication of the stack size
  Printf("\nTotal number of recursive calls made: %d\n", answer);

 // Signal the semaphore to tell the original process that we're done 
  if(sem_signal(s_procs_completed) != SYNC_SUCCESS) {
    Printf("hello_world (%d): Bad semaphore s_procs_completed (%d)!\n", getpid(), s_procs_completed);
    Exit();
  }
  
  Printf("\nEnd of The Test Program 4 - growing stack size to more than 1 page..");
}
