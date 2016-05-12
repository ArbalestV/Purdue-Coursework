//
//	memory.c
//
//	Routines for dealing with memory management.

//static char rcsid[] = "$Id: memory.c,v 1.1 2000/09/20 01:50:19 elm Exp elm $";

#include "ostraps.h"
#include "dlxos.h"
#include "process.h"
#include "memory.h"
#include "queue.h"

// num_pages = size_of_memory / size_of_one_page
static uint32 freemap[MEM_MAX_PAGES / 32]; //= 2^9 / 2^5 = 16. each entry represented by 32 bits, hence division by 32
static uint32 pagestart;
static int nfreepages;
static int freemapmax;
l2_pagetable l2[256];



//----------------------------------------------------------------------
//
//	This silliness is required because the compiler believes that
//	it can invert a number by subtracting it from zero and subtracting
//	an additional 1.  This works unless you try to negate 0x80000000,
//	which causes an overflow when subtracted from 0.  Simply
//	trying to do an XOR with 0xffffffff results in the same code
//	being emitted.
//
//----------------------------------------------------------------------
static int negativeone = 0xFFFFFFFF;
static inline uint32 invert (uint32 n) {
  return (n ^ negativeone); //^ = XOR
}

//----------------------------------------------------------------------
//
//	MemoryGetSize
//
//	Return the total size of memory in the simulator.  This is
//	available by reading a special location.
//
//----------------------------------------------------------------------
int MemoryGetSize() {
  return (*((int *)DLX_MEMSIZE_ADDRESS));
}


//----------------------------------------------------------------------
//
//	MemoryInitModule
//
//	Initialize the memory module of the operating system.
//      Basically just need to setup the freemap for pages, and mark
//      the ones in use by the operating system as "VALID", and mark
//      all the rest as not in use.
//
//----------------------------------------------------------------------
void MemoryModuleInit() {
  int os_reserved_pages; //total number of pages reserved for the OS
  int i, j; //loop variables for iteration
  uint32 mask; //the mask value for each free map element

  //printf("\n\n\nin memory module init()...\n");
  printf("\nlast os address: %d\n", lastosaddress);
  printf("\nMEM_PAGESIZE = %d", MEM_PAGESIZE);
  os_reserved_pages = (lastosaddress / MEM_PAGESIZE); //get the os reserved pages, and they are at the top
  if ((os_reserved_pages % MEM_PAGESIZE) != 0) //reserve one more page for it
    {
      os_reserved_pages = os_reserved_pages + 1;
    }
  //now, we need to keep track of the os_reserved_pages as a decrementing counter
  printf("\nNumber of OS reserved pages: %d\n", os_reserved_pages);
  for (i = 0; i < 16; i++) //size of the freemap[] array
    {
      freemap[i] = 0; //initialize to 0
      mask = 0x1; //how much masking is required for each entry of the freemap
      for (j = 0; j < 32; j++) //for each of the 32 bits representing each of the 512 pages
	{	  
	  if (os_reserved_pages == 0)
	    {
	      freemap[i] = freemap[i] | mask; //orring the values -> the convention is that 1's correspond to available pages in memory, whereas 0 correspond to pages that are given out
	      //os_reserved_pages = os_reserved_pages - 1;
	      mask = mask << 1;
	    }
	  else{
	    //break; //we can simply break since all of the remaining will be zero
	    os_reserved_pages = os_reserved_pages - 1;
	    mask = mask << 1; 
	  }
	}
    }
  //printf("\n\n\nend of in memory module init()...\n");
  preallocateL2PageTables(); 
}


//----------------------------------------------------------------------
//
// MemoryTranslateUserToSystem
//
//	Translate a user address (in the process referenced by pcb)
//	into an OS (physical) address.  Return the physical address.
//
//----------------------------------------------------------------------
uint32 MemoryTranslateUserToSystem (PCB *pcb, uint32 addr) {
  uint32 physical_addr;
  uint32 page_offset;
  //uint32 page_number;
  uint32 pte; //the page table entry at page_number that we will then and and or

  uint32 l1_index;
  //l2_pagetable * pt_base;
  uint32 * pt_base;
  uint32 l2_index;
  //uint32 * pte_addr;


  int check_if_valid;
  
  if (addr > MEM_MAX_VIRTUAL_ADDRESS)
    {
      ProcessKill();
    }
  //printf("\naddr = %d", addr);
  //printf("\naddr in hex: %x", (uint32) addr);
  l1_index = addr >> MEM_L1FIELD_FIRST_BITNUM; //to just get the first 2 bits from the 22bit addr
  pt_base = pcb->pagetable[l1_index];
  l2_index = addr << 12; //first left shift by 12 to remove the 2 bit for l1 index
  l2_index = l2_index >> 24; //to remove the first 12 bits corresponding to the page offset
  
  
  page_offset = addr & 0xFFF; //inorder to just get the last 12 bits from the given address that we will then or
  //page_number = addr >> MEM_L1FIELD_FIRST_BITNUM; //since the LSB of the page number starts at bit 12 of the Virtual Address
  //printf("\nPrinting the page number calculated: %d\n", page_number);
  //pte = pcb->pagetable[page_number]; //the value at the particular index of the process's page table
  //pte_addr = pt_base + (l2_index * sizeof(uint32));
  pte = pt_base[l2_index];

  check_if_valid = pte & MEM_PTE_VALID;
  if (check_if_valid == 0) //invalid, hence generate a page fault
    {
      return MemoryPageFaultHandler(pcb);
    }

  physical_addr = pte & 0x3FF000; //to mask out the status bits
  physical_addr = physical_addr | page_offset; //to get the final physical address in memory
  return physical_addr;
}


//----------------------------------------------------------------------
//
//	MemoryMoveBetweenSpaces
//
//	Copy data between user and system spaces.  This is done page by
//	page by:
//	* Translating the user address into system space.
//	* Copying all of the data in that page
//	* Repeating until all of the data is copied.
//	A positive direction means the copy goes from system to user
//	space; negative direction means the copy goes from user to system
//	space.
//
//	This routine returns the number of bytes copied.  Note that this
//	may be less than the number requested if there were unmapped pages
//	in the user range.  If this happens, the copy stops at the
//	first unmapped address.
//
//----------------------------------------------------------------------
int MemoryMoveBetweenSpaces (PCB *pcb, unsigned char *system, unsigned char *user, int n, int dir) {
  unsigned char *curUser;         // Holds current physical address representing user-space virtual address
  int		bytesCopied = 0;  // Running counter
  int		bytesToCopy;      // Used to compute number of bytes left in page to be copied

  while (n > 0) {
    // Translate current user page to system address.  If this fails, return
    // the number of bytes copied so far.
    //printf("\nUser Address before translating to physical address: %x\n", (uint32) user);
    curUser = (unsigned char *)MemoryTranslateUserToSystem (pcb, (uint32)user);

    // If we could not translate address, exit now
    if (curUser == (unsigned char *)0) break;

    // Calculate the number of bytes to copy this time.  If we have more bytes
    // to copy than there are left in the current page, we'll have to just copy to the
    // end of the page and then go through the loop again with the next page.
    // In other words, "bytesToCopy" is the minimum of the bytes left on this page 
    // and the total number of bytes left to copy ("n").

    // First, compute number of bytes left in this page.  This is just
    // the total size of a page minus the current offset part of the physical
    // address.  MEM_PAGESIZE should be the size (in bytes) of 1 page of memory.
    // MEM_ADDRESS_OFFSET_MASK should be the bit mask required to get just the
    // "offset" portion of an address.
    bytesToCopy = MEM_PAGESIZE - ((uint32)curUser & MEM_ADDRESS_OFFSET_MASK);
    
    // Now find minimum of bytes in this page vs. total bytes left to copy
    if (bytesToCopy > n) {
      bytesToCopy = n;
    }

    // Perform the copy.
    if (dir >= 0) {
      bcopy (system, curUser, bytesToCopy);
    } else {
      bcopy (curUser, system, bytesToCopy);
    }

    // Keep track of bytes copied and adjust addresses appropriately.
    n -= bytesToCopy;           // Total number of bytes left to copy
    bytesCopied += bytesToCopy; // Total number of bytes copied thus far
    system += bytesToCopy;      // Current address in system space to copy next bytes from/into
    user += bytesToCopy;        // Current virtual address in user space to copy next bytes from/into
  }
  return (bytesCopied);
}

//----------------------------------------------------------------------
//
//	These two routines copy data between user and system spaces.
//	They call a common routine to do the copying; the only difference
//	between the calls is the actual call to do the copying.  Everything
//	else is identical.
//
//----------------------------------------------------------------------
int MemoryCopySystemToUser (PCB *pcb, unsigned char *from,unsigned char *to, int n) {
  return (MemoryMoveBetweenSpaces (pcb, from, to, n, 1));
}

int MemoryCopyUserToSystem (PCB *pcb, unsigned char *from,unsigned char *to, int n) {
  return (MemoryMoveBetweenSpaces (pcb, to, from, n, -1));
}

//---------------------------------------------------------------------
// MemoryPageFaultHandler is called in traps.c whenever a page fault 
// (better known as a "seg fault" occurs.  If the address that was
// being accessed is on the stack, we need to allocate a new page 
// for the stack.  If it is not on the stack, then this is a legitimate
// seg fault and we should kill the process.  Returns MEM_SUCCESS
// on success, and kills the current process on failure.  Note that
// fault_address is the beginning of the page of the virtual address that 
// caused the page fault, i.e. it is the vaddr with the offset zero-ed
// out.
//
// Note: The existing code is incomplete and only for reference. 
// Feel free to edit.
//---------------------------------------------------------------------
int MemoryPageFaultHandler(PCB *pcb) {
  uint32 faulting_addr;
  uint32 userstack_addr;
  //uint32 page_number;
  uint32 allocated_page;

  //int index, i;
  //l2_pagetable * pt_base;
  uint32 *pt_base;
  uint32 l1_index, l2_index;
  //uint32 * pte_addr;
  /* uint32 addr = pcb->currentSavedFrame[PROCESS_STACK_FAULT]; */

  /* // segfault if the faulting address is not part of the stack */
  /* if (vpagenum < stackpagenum) { */
  /*   dbprintf('m', "addr = %x\nsp = %x\n", addr, pcb->currentSavedFrame[PROCESS_STACK_USER_STACKPOINTER]); */
  /*   printf("FATAL ERROR (%d): segmentation fault at page address %x\n", findpid(pcb), addr); */
  /*   ProcessKill(); */
  /*   return MEM_FAIL; */
  /* } */

  /* ppagenum = MemoryAllocPage(); */
  /* pcb->pagetable[vpagenum] = MemorySetupPte(ppagenum); */
  /* dbprintf('m', "Returning from page fault handler\n"); */
  /* return MEM_SUCCESS; */
  //return MEM_FAIL;
  
  faulting_addr = pcb->currentSavedFrame[PROCESS_STACK_FAULT]; //get the faulting virtual address
  userstack_addr = pcb->currentSavedFrame[PROCESS_STACK_USER_STACKPOINTER]; //the user stack pointer
  //page_number = faulting_addr >> MEM_L1FIELD_FIRST_BITNUM; //get the page offset in case page needs to be allocated
  //now we will have to get the mask out the last 12 bits of the user stack address
  userstack_addr = userstack_addr & 0x3FF000;

  printf("\nINSIDE THE PAGE FAULT HANDLER PROCESS.........\n");
  printf("\nFaulting Address: %x\n", faulting_addr);
  printf("\nUser Stack Address: %x\n", userstack_addr);
  if (faulting_addr < userstack_addr) //case of actual page fault
    {
      //we have to exit simulation
      printf("FATAL ERROR (%d): segmentation fault at page address %x\n",  GetCurrentPid(), faulting_addr);
      ProcessKill();
      //return MEM_FAIL;
    }
  else //not a seg fault, have to allocate a new page
    {
      //printf("\nhere....page fault handler allocate page.\n");
      l1_index = faulting_addr >> MEM_L1FIELD_FIRST_BITNUM;
      pt_base = pcb->pagetable[l1_index];
      l2_index = faulting_addr << 12;
      l2_index = l2_index >> 24;
      //pte_addr = pt_base + (l2_index * sizeof(uint32));
      if ((allocated_page = MemoryAllocPage()) == MEM_FAIL) //page could not be allocated 
	{
	  printf("\nFATAL ERROR : Page could not be allocated.\n");
	  exitsim();
	}
      //*(pte_addr) = MemorySetupPte(allocated_page);
      pt_base[l2_index] = MemorySetupPte(allocated_page);
      
      //printf("\nJust finished allocating a new page..\n");
      //pcb->pagetable[page_number] = MemorySetupPte(allocated_page); //set the new page table entry in the appropriate index
      
    }
  return MEM_SUCCESS;
}


//---------------------------------------------------------------------
// You may need to implement the following functions and access them from process.c
// Feel free to edit/remove them
//---------------------------------------------------------------------

int MemoryAllocPage(void) {
  // return -1;
  int i, j;
  uint32 mask;
  int return_val;
  uint32 check_val_and; //this is strictly a stand value that checks if something is > 0
  //printf("\nIn the MemoyAllocPage() function...");
  for (i = 0; i < 16; i++) //each element of freemap
    {
      mask = 0x1; //this will keep on updating until you get the appropriate value
      if (freemap[i] != 0) //i.e, it is available
	{
	  for (j = 0; j < 32; j++)
	    {
	      check_val_and = freemap[i] & mask; //this should not be zero, or strictly, greater than 0
	      if (check_val_and > 0) //check if it is not 0
		{
		  //that means jth bit of ith index is the appropriate page number in memory
		  //first of all, set the freemap
		  freemap[i] = freemap[i] ^ mask;
		  return_val = (i * 32) + j;
		  //printf("\nValue to be returned is : %d\n", return_val);
		  return return_val; //function returns
		}
	      else
		{
		  //check the next one and move the mask such that 1 gets to the next bit on the left
		  mask = mask << 1;
		}
	    }
	}
    }
  //if it reaches this point then we obviously have no physical pages as being empty
  return MEM_FAIL;
}


uint32 MemorySetupPte (uint32 page) {
  //return -1;
  page = page << MEM_L2FIELD_FIRST_BITNUM; //since 12th bit onwards actual physical addresses begin
  page = page | MEM_PTE_VALID; //now the status bit will be set to 1
  //printf("\nPage = %x", page);
  return page; //return the appropriate form of physical address + valid bit set PTE
}


void MemoryFreePage(uint32 page) { //function to free a physical memory page, i.e., set the corresponding freemap to 1
  int freemap_index;
  int index_bit_position;
  uint32 mask;
  page = page & 0x3ff000; //mask out the status bits
  page = page >> MEM_L2FIELD_FIRST_BITNUM; //since 12th bit onwards actual physical addresses begin -> reverse of the previous function's operation
  freemap_index = page / 32;
  index_bit_position = page % 32;
  mask = 0x1 << index_bit_position; //the appropriate position of the bit set it to 1 so it can becomes 1 in the freemap value by XORing since it will be 0 now since page is in use
  //printf("\nFreed index = %d, index_bit_position = %d", freemap_index, index_bit_position);
  freemap[freemap_index] = freemap[freemap_index] ^ mask; //make it 1 indicating it is free again and could be allocated
  //printf("\nFreemap[index] = %x", freemap[freemap_index]);
  return;
}

void preallocateL2PageTables() //function to preallocate L2 page tables
{
  int i;
  for (i = 0; i < 256; i++)
    {
      preallocateOneL2PageTable(i);
    }
}

void preallocateOneL2PageTable(int i)
{
  l2[i].inuse = 0; //make it 0 to initialize signifying it is in the pool
}
  
