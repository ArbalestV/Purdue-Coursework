#ifndef __MBOX_OS__
#define __MBOX_OS__

#define MBOX_NUM_MBOXES 16           // Maximum number of mailboxes allowed in the system
#define MBOX_NUM_BUFFERS 50          // Maximum number of message buffers allowed in the system
#define MBOX_MAX_BUFFERS_PER_MBOX 10 // Maximum number of buffer slots available to any given mailbox
#define MBOX_MAX_MESSAGE_LENGTH 50   // Buffer size of 50 for each message

#define MBOX_FAIL -1
#define MBOX_SUCCESS 1

//---------------------------------------------
// Define your mailbox structures here
//--------------------------------------------

typedef struct mbox_message {
  //this is a mailbox message - which means this will just be a buffer of max size defined above

  //what is the size of the message?
  int msg_len; //less than or equal to max length
  //if the particular message is in use or not? -> just use a flag
  int msg_inuse; //inuse = 0 -> not in use, inuse = 1 -> in use
  char msg[MBOX_MAX_MESSAGE_LENGTH]; //msg is the buffer holding each message
} mbox_message;

typedef struct mbox {
  //this is one mailbox - which will consist of maximum allowable number of message buffers
  //Queue messages; //each mailbox will have individual messages  -> maintain a queue instead of an array. Msg going to be read will be first one in the queue

  int which_messages[10]; //each mailbox will store upto 10 messages
  int head; //where the next receive needs to occur from
  int tail; //where the next send has to go to
  //if the mbox is in use or not use
  int mbox_inuse; //1->in use, 0-> not in use 
  //conditional variable isFUll
  cond_t mbox_isFull; //if the mailbox is full -> for the sending processes that will wait on it
  
  //cond var isEmpty
  cond_t mbox_isEmpty; //if the mailbox is empty -> for receiving processes that will wait on it
  //lock reqd -> cond var cant be used without a lock, and mailboxes are shared entities
  lock_t lock_for_mbox; //this lock will be used to access the isFull or isEmpty cv's
  //have a list of processes that have mailbox open -> only those processos that have access to read or write into the mailbox
  //for this, we will just have an array of size PROCESS_MAX_PROCS (ie 32) that will be used to index in based on the pid of the process. 0->not opened the mailbox, 1 -> opened the mailbox
  int proc_mbox_opened[PROCESS_MAX_PROCS];
  //count of total number of messages out of the maximum 
  int total_msg_inuse; 
} mbox;

//acquire the lock before accessing one mbox -> two processes cannot acquire the same mbox at the same time

typedef int mbox_t; // This is the "type" of mailbox handles
mbox mboxes[MBOX_NUM_MBOXES];
mbox_message mbox_messages[MBOX_NUM_BUFFERS];
//-------------------------------------------
// Prototypes for Mbox functions you have to write
//-------------------------------------------

void MboxModuleInit();
mbox_t MboxCreate();
int MboxOpen(mbox_t m);
int MboxClose(mbox_t m);
int MboxSend(mbox_t m, int length, void *message);
int MboxRecv(mbox_t m, int maxlength, void *message);
int MboxCloseAllByPid(int pid);

#ifndef false
#define false 0
#endif

#ifndef true
#define true 1
#endif

#endif
