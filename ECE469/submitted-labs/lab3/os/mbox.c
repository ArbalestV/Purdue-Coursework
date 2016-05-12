#include "ostraps.h"
#include "dlxos.h"
#include "process.h"
#include "synch.h"
#include "queue.h"
#include "mbox.h"
#include "misc.h"
//#include "usertraps.h"

//-------------------------------------------------------
//
// void MboxModuleInit();
//
// Initialize all mailboxes.  This process does not need
// to worry about synchronization as it is called at boot
// time.  Only initialize necessary items here: you can
// initialize others in MboxCreate.  In other words, 
// don't waste system resources like locks and semaphores
// on unused mailboxes.
//
//-------------------------------------------------------

void MboxModuleInit() {
  //initialize every message box to not use
  int i;
  int j;
  int k;
  //printf("\nin MBoxModuleInit().");
  for (i = 0; i < MBOX_NUM_MBOXES; i++)
    {
      mboxes[i].mbox_inuse = 0;
      mboxes[i].total_msg_inuse = 0;
      mboxes[i].head = 0;
      mboxes[i].tail = 0;
      for (j = 0; j < PROCESS_MAX_PROCS; j++)
	{
	  mboxes[i].proc_mbox_opened[j] = 0;
	}
      
      for (k = 0; k < 10; k++)
	{
	  mboxes[i].which_messages[k] = -1; //initialized to -1
	}
    }
  
  for (j = 0; j < MBOX_MAX_MESSAGE_LENGTH; j++)
    {
      mbox_messages[j].msg_inuse = 0; //all of the 50 available message buffers are initialized to not in use
    }
  //printf("\nMailboxes initialized.");
}

//-------------------------------------------------------
//
// mbox_t MboxCreate();
//
// Allocate an available mailbox structure for use. 
//
// Returns the mailbox handle on success
// Returns MBOX_FAIL on error.
//
//-------------------------------------------------------
mbox_t MboxCreate() {
  uint32 intrval;
  int i;
  intrval = DisableIntrs(); //disable interrrupts because it is a shared entity, and there are no locks yet. afterwards you can use locks.
  
  for (i = 0; i < MBOX_NUM_MBOXES; i++)
    {
      if (mboxes[i].mbox_inuse == 0)
	{
	  mboxes[i].mbox_inuse = 1;
	  break;
	}
    }
  //now that we have received a mailbox, we need to allocate the queue, and the cond variables and the lock
  RestoreIntrs(intrval); //since the mailbox is being allocated now
  if (i == MBOX_NUM_MBOXES) 
    {
      return MBOX_FAIL;
    }
  //now allocate the space for queue
  /*if (AQueueInit(&mboxes[i].messages) == QUEUE_FAIL) 
    {
      return MBOX_FAIL;
      }*/
  //now the queue has been initialized to zero items. now the cv's and the lock.
  //printf("Allocated mailbox no. %d\n", i);
  mboxes[i].lock_for_mbox = LockCreate();
  if (mboxes[i].lock_for_mbox == INVALID_LOCK)
    {
      return MBOX_FAIL;
    }
  //printf("\nDisplaying the lock create value: %d\n", mboxes[i].lock_for_mbox);
  mboxes[i].mbox_isFull = CondCreate(mboxes[i].lock_for_mbox);
  if (mboxes[i].mbox_isFull == INVALID_COND)
    {
      return MBOX_FAIL;
    }
  //printf("\nDisplaying the cond var isFull create value: %d\n", mboxes[i].mbox_isFull);
  mboxes[i].mbox_isEmpty = CondCreate(mboxes[i].lock_for_mbox);
  if (mboxes[i].mbox_isEmpty == INVALID_COND)
    {
      return MBOX_FAIL;
    }  
  //printf("\nDisplaying the cond var isEmpty create value: %d\n", mboxes[i].mbox_isEmpty);
  return i;
}

//-------------------------------------------------------
// 
// void MboxOpen(mbox_t);
//
// Open the mailbox for use by the current process.  Note
// that it is assumed that the internal lock/mutex handle 
// of the mailbox and the inuse flag will not be changed 
// during execution.  This allows us to get the a valid 
// lock handle without a need for synchronization.
//
// Returns MBOX_FAIL on failure.
// Returns MBOX_SUCCESS on success.
//
//-------------------------------------------------------
int MboxOpen(mbox_t handle) {
  int process_id;
  int lr_val;
  if (mboxes[handle].mbox_inuse == 0)
    {
      //printf("\nfailing here in inuse == 0 in mboxopen().\n");
      return MBOX_FAIL;
    }
  //otherwise the mailbox is in use
  //now you will acquire the lock to this mailbox
  if (LockHandleAcquire(mboxes[handle].lock_for_mbox) == SYNC_FAIL) //basically the lock wasnt acquired and the process wasn't put on the wait queue
    {
      printf("\nfailing here in the lock acquire.\n");
      //printf("\nLock handle acquire value: %d\n", LockHandleAcquire(mboxes[handle].lock_for_mbox));
      return MBOX_FAIL;
    }
  //at this point the lock has been acquired
  
  process_id = GetCurrentPid();
  mboxes[handle].proc_mbox_opened[process_id] = 1; //that means this process has opened the mailbox
  
  lr_val = LockHandleRelease(mboxes[handle].lock_for_mbox);
  if (lr_val == SYNC_FAIL)
    {
      printf("\nLock for the mailbox is not getting released.");
      return MBOX_FAIL;
    }
  //now the lock has been released
  return MBOX_SUCCESS;
}

//-------------------------------------------------------
//
// int MboxClose(mbox_t);
//
// Close the mailbox for use to the current process.
// If the number of processes using the given mailbox
// is zero, then disable the mailbox structure and
// return it to the set of available mboxes.
//
// Returns MBOX_FAIL on failure.
// Returns MBOX_SUCCESS on success.
//
//-------------------------------------------------------
int MboxClose(mbox_t handle) {
  int process_id;
  int i;
  int lr_val;
  if (mboxes[handle].mbox_inuse == 0)
    {
      return MBOX_FAIL;
    }
  //otherwise the mailbox is in use
  //now you will acquire the lock to this mailbox
  if (LockHandleAcquire(mboxes[handle].lock_for_mbox) != SYNC_FAIL) //basically the lock wasnt acquired and the process wasn't put on the wait queue
    {
      return MBOX_FAIL;
    }
  //at this point the lock has been acquired
  
  process_id = GetCurrentPid();
  mboxes[handle].proc_mbox_opened[process_id] = 1; //that means this process has closed the mailbox
  //now iterate throught the array of processes using the mailbox to check how many have it opened
  
  for (i = 0; i < PROCESS_MAX_PROCS; i++)
    {
      if (mboxes[handle].proc_mbox_opened[i] == 1)
	{
	  break;
	}
    }
  if (i ==  MBOX_NUM_MBOXES)
    {
      //disable the mailbox structure
      mboxes[handle].mbox_inuse = 0;
    }
  //now release the lock
  
  lr_val = LockHandleRelease(mboxes[handle].lock_for_mbox);
  if (lr_val == SYNC_FAIL)
    {
      printf("\nLock for the mailbox is not getting released.");
      return MBOX_FAIL;
    }
  //now the lock has been released
  return MBOX_SUCCESS;
}

//-------------------------------------------------------
//
// int MboxSend(mbox_t handle,int length, void* message);
//
// Send a message (pointed to by "message") of length
// "length" bytes to the specified mailbox.  Messages of
// length 0 are allowed.  The call 
// blocks when there is not enough space in the mailbox.
// Messages cannot be longer than MBOX_MAX_MESSAGE_LENGTH.
// Note that the calling process must have opened the 
// mailbox via MboxOpen.
//
// Returns MBOX_FAIL on failure.
// Returns MBOX_SUCCESS on success.
//
//-------------------------------------------------------
int MboxSend(mbox_t handle, int length, void* message) {
  int i;
  //char * msg_ptr;
  int empty;
  int lr_val;
  if (length > MBOX_MAX_MESSAGE_LENGTH) //length cannot exceed max message length
    {
      printf("\nMessage length cannot exceed max length.");
      return MBOX_FAIL;
    }
  
  //msg_ptr = (char *)message; //typecasting message to a character array
 
  //now for this particular mailbox, iterate from 0 to 49 on all the available mailbox buffers to find the first message buffer that is not in use
  
  for (i = 0; i < MBOX_NUM_BUFFERS; i++ )
    {
      if (mbox_messages[i].msg_inuse == 0)
	{
	  mbox_messages[i].msg_inuse = 1; //acquire this message buffer
	  break;
	}
    }
  if (i == MBOX_NUM_BUFFERS) //no message buffer found
    {
      return MBOX_FAIL;
    }
  //now in the message buffer characterized by i put the length and the actual message
  //copy byte by byte
  //dstrncpy(mbox_messages[i].msg, msg_ptr, length);
  bcopy((char *) message, mbox_messages[i].msg, length);
  mbox_messages[i].msg_len = length;
  //printf("\nThe sent message is in message id %d:\n", i);
  //printf("\nThe first character of the message coming in: %c\n", msg_ptr[0]);
  //printf("\nThe message coming in: %s\n", msg_ptr);
  //printf("\nThe message in the message buffer: %c\n", mbox_messages[i].msg);
  //now we need to put the message index into the mailbox, which means putting the message inside the mailbox
  empty = 0;
  if (LockHandleAcquire(mboxes[handle].lock_for_mbox) != SYNC_FAIL)
    {
      while ( ((mboxes[handle].head + 1) % 10) == mboxes[handle].tail) 
	{ //if all the mailboxes are taken
	  //printf("\nhead value : %d\n", mboxes[handle].head);
	  //printf("\ntail value : %d\n", mboxes[handle].tail);
	  //printf("\nshould wait for full!!!\n");
	  CondHandleWait(mboxes[handle].mbox_isFull);
	  //CondHandleWait(mboxes[handle].mbox_isEmpty);
	}
      if (mboxes[handle].head == mboxes[handle].tail)
	{
	  empty = 1;
	}
      if ( ( (mboxes[handle].head + 1) % 10) != mboxes[handle].tail) 
	{ //essentially the mailbox is not full
	  //printf("\nHead Before: %d\n", mboxes[handle].head);
	  mboxes[handle].which_messages[mboxes[handle].head] = i;
	  mboxes[handle].head = (mboxes[handle].head + 1) % 10;
	  //printf("Mailbox no. %d message id %d inserted.\n", handle, i);
	  //printf("\nHead After: %d\n", mboxes[handle].head);
	}
      //if (empty)
      //{
      CondHandleSignal(mboxes[handle].mbox_isEmpty);
	  //CondHandleSignal(mboxes[handle].mbox_isFull);
	  //}
      lr_val = LockHandleRelease(mboxes[handle].lock_for_mbox);
      if (lr_val == SYNC_FAIL) 
	{
	  printf("\nLOCK IS NOT GETTING RELEASED FOR MAILBOX NO. %d AND MESSAGE NO. %d.", handle, i);
	}
    }
   return MBOX_SUCCESS;
}

//-------------------------------------------------------
//
// int MboxRecv(mbox_t handle, int maxlength, void* message);
//
// Receive a message from the specified mailbox.  The call 
// blocks when there is no message in the buffer.  Maxlength
// should indicate the maximum number of bytes that can be
// copied from the buffer into the address of "message".  
// An error occurs if the message is larger than maxlength.
// Note that the calling process must have opened the mailbox 
// via MboxOpen.
//   
// Returns MBOX_FAIL on failure.
// Returns number of bytes written into message on success.
//
//-------------------------------------------------------
int MboxRecv(mbox_t handle, int maxlength, void* message) {
  int full;
  int lr_val;
  //char * msg_ptr;
  if (maxlength > MBOX_MAX_MESSAGE_LENGTH) //length cannot exceed max message length
    {
      printf("\nMessage length cannot exceed max length.");
      return MBOX_FAIL;
    }
  //msg_ptr = (char *) message; //typecasting message to a character array  

  full = 0;
  if (LockHandleAcquire(mboxes[handle].lock_for_mbox) != SYNC_FAIL)
    {
      while ( mboxes[handle].head == mboxes[handle].tail) 
	{ //if mailbox is empty
	  //printf("\nhead value : %d\n", mboxes[handle].head);
	  //printf("\ntail value : %d\n", mboxes[handle].tail);
	  //printf("\nshould  wait for empty!!!\n");
	  CondHandleWait(mboxes[handle].mbox_isEmpty);
	  //CondHandleWait(mboxes[handle].mbox_isFull);
	}
      if ( ((mboxes[handle].head + 1) % 10) == mboxes[handle].tail)
	{
	  full = 1;
	}
      if ( mboxes[handle].head != mboxes[handle].tail) 
	{ //essentially the mailbox is not empty
	  //now read the contents of tail pointer message to the message buffer
	  //printf("\nTail Before: %d\n", mboxes[handle].tail);
	  //dstrncpy(msg_ptr, mbox_messages[mboxes[handle].tail].msg, maxlength);
	  bcopy(mbox_messages[mboxes[handle].tail].msg, (char* ) message, maxlength);
	  //printf("Message from message id no. %d and mailbox no %d received.\n", mboxes[handle].tail, handle);
	  //printf("\nThe received message id number: %d\n", mboxes[handle].which_messages[mboxes[handle].tail]);
	  //printf("\nThe current pid: %d\n", GetCurrentPid());
	  //printf("\nThe received message: %s\n", mbox_messages[mboxes[handle].which_messages[mboxes[handle].tail]].msg);
	  mboxes[handle].tail = (mboxes[handle].tail + 1) % 10;	  
	  //printf("\nTail After: %d\n", mboxes[handle].tail);
	}
      //if (full)
	//{
      CondHandleSignal(mboxes[handle].mbox_isFull);
	  //CondHandleSignal(mboxes[handle].mbox_isEmpty);
	  //}
      lr_val = LockHandleRelease(mboxes[handle].lock_for_mbox);
      if (lr_val == SYNC_FAIL) 
	{
	  printf("\nLOCK IS NOT GETTING RELEASED FOR MAILBOX NO. %d.", handle);
	}
    }
  return /*MBOX_SUCCESS*/maxlength;
}

//--------------------------------------------------------------------------------
// 
// int MboxCloseAllByPid(int pid);
//
// Scans through all mailboxes and removes this pid from their "open procs" list.
// If this was the only open process, then it makes the mailbox available.  Call
// this function in ProcessFreeResources in process.c.
//
// Returns MBOX_FAIL on failure.
// Returns MBOX_SUCCESS on success.
//
//--------------------------------------------------------------------------------
int MboxCloseAllByPid(int pid) {
  int handle;
  int lr_val;
  int i;
  int process_id;
  //iterate through all the mailboxes in a for loop
  for (handle = 0; handle < MBOX_NUM_MBOXES; handle++)
    {
      //now you will acquire the lock to this mailbox
      if (LockHandleAcquire(mboxes[handle].lock_for_mbox) != SYNC_FAIL) //basically the lock wasnt acquired and the process wasn't put on the wait queue
	{
	  printf("\nLock for the mailbox %d is not getting acquired.", handle);
	  return MBOX_FAIL;
	}
      //at this point the lock has been acquired
      
      process_id = GetCurrentPid();
      mboxes[handle].proc_mbox_opened[process_id] = 1; //that means this process has closed the mailbox
      //now iterate throught the array of processes using the mailbox to check how many have it opened
      
      for (i = 0; i < PROCESS_MAX_PROCS; i++)
	{
	  if (mboxes[handle].proc_mbox_opened[i] == 1)
	    {
	      break;
	    }
	}
      if (i ==  MBOX_NUM_MBOXES)
	{
	  //disable the mailbox structure
	  mboxes[handle].mbox_inuse = 0;
	}
      //now release the lock
      
      lr_val = LockHandleRelease(mboxes[handle].lock_for_mbox);
      if (lr_val == SYNC_FAIL)
	{
	  printf("\nLock for the mailbox %d is not getting released.", handle);
	  return MBOX_FAIL;
	}
    }
  return MBOX_SUCCESS;
}
