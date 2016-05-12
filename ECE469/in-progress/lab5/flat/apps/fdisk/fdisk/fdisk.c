#include "usertraps.h"
#include "misc.h"

#include "fdisk.h"

dfs_superblock sb;
//dfs_inode inodes[DFS_INODE_MAX_NUM];
dfs_inode inodes[FDISK_NUM_INODES];
uint32 fbv[DFS_FBV_MAX_NUM_WORDS];

int diskblocksize = 0; // These are global in order to speed things up
int disksize = 0;      // (i.e. fewer traps to OS to get the same number)

int FdiskWriteBlock(uint32 blocknum, dfs_block *b); //You can use your own function. This function 
//calls disk_write_block() to write physical blocks to disk

void main (int argc, char *argv[])
{
	// STUDENT: put your code here. Follow the guidelines below. They are just the main steps. 
	// You need to think of the finer details. You can use bzero() to zero out bytes in memory
  dfs_block nb; //new block
  int i;
  int j;
  //Initializations and argc check
  if(argc != 1)
    {
      Printf("Usage issue.....In initialization of fdisk.c.\n");
      Exit();
    }

  // Need to invalidate filesystem before writing to it to make sure that the OS
  // doesn't wipe out what we do here with the old version in memory
  // You can use dfs_invalidate(); but it will be implemented in Problem 2. You can just do 
  // sb.valid = 0
  dfs_invalidate();
  //disksize = 
  //diskblocksize = 
  //num_filesystem_blocks = 
  sb.dfs_disksize = DFS_MAX_FILESYSTEM_SIZE; //16MB
  sb.dfs_blocksize = DFS_BLOCKSIZE; //1024
  sb.dfs_blocknum = DFS_NUMBLOCKS; // 2^24/2^10 = 2^14
  sb.dfs_inode_start = FDISK_INODE_BLOCK_START; //1
  sb.dfs_num_inodes = FDISK_NUM_INODES; //16
  sb.dfs_fbv_start = FDISK_FBV_BLOCK_START; //49
  sb.dfs_datablock_start =  FDISK_FBV_BLOCK_START + DFS_FBV_MAX_NUM_WORDS / (MY_DFS_BLOCKSIZE / 4); //49+512/(1024/4) ----- = 51

  // Make sure the disk exists before doing anything else
  if (disk_create() == DISK_FAIL)
    {
      Printf("\nFailed to create disk.\n");
      Exit();
    }

  // Write all inodes as not in use and empty (all zeros)
  for (i = 0; i < FDISK_NUM_INODES; i++)
    {
      inodes[i].inuse = 0;
      inodes[i],max_size = 0;
      for (j = 0; j < 10; j++)
	{
	  inodes[i].vblock_table[j] = 0;
	}
      inodes[i].block_index = 0;
    }
  // Next, setup free block vector (fbv) and write free block vector to the disk
  // Finally, setup superblock as valid filesystem and write superblock and boot record to disk: 
  sb.valid = 1;
  // boot record is all zeros in the first physical block, and superblock structure goes into the second physical block
  bcopy((char *) &sb, newblock.data, sizeof(dfs_superblock)); //copy superblock
  FdiskWriteBlock(1, &newblock);
  
  for(i = 0; i < FDISK_NUM_INODES; i = i + 2)
    {
      bcopy((char *) (inodes + i), newblock.data, 2 * sizeof(dfs_inode));
      FdiskWriteBlock(2 + (i / 2), &newblock);
    } //copy each inode block 2 at a time
  
  Printf("fdisk (%d): Formatted DFS disk for %d bytes.\n", getpid(), disksize);
}

int FdiskWriteBlock(uint32 blocknum, dfs_block *b) {
  // STUDENT: put your code here
  if (disk_write_block(blocknum, d->data) == DISK_FAIL)
    {
      Printf("\nCould not write to disk the block!!!\n");
      Exit();
    }
  return 0;
}
