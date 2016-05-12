#ifndef __DFS_SHARED__
#define __DFS_SHARED__

typedef struct dfs_superblock {
  // STUDENT: put superblock internals here
  int valid;
  int dfs_disksize;
  int dfs_blocksize;
  int dfs_blocknum;
  int dfs_inode_start;
  int dfs_num_inodes;
  int dfs_fbv_start;
  int dfs_datablock_start;
} dfs_superblock;

#define DFS_BLOCKSIZE 1024  // Must be an integer multiple of the disk blocksize

typedef struct dfs_block {
  char data[DFS_BLOCKSIZE]; //data[1024]
} dfs_block;


//#define FILE_MAX_FILENAME_LENGTH 79

//#define FILE_MAX_READWRITE_BYTES 4096

typedef struct dfs_inode {
  // STUDENT: put inode structure internals here
  // IMPORTANT: sizeof(dfs_inode) MUST return 128 in order to fit in enough
  // inodes in the filesystem (and to make your life easier).  To do this, 
  // adjust the maximumm length of the filename until the size of the overall inode 
  // is 128 bytes.
  char inuse;
  uint32 max_size;
  char filename[FILE_MAX_FILENAME_LENGTH];
  uint32 vblock_table[10];
  uint32 vblock_index;
} dfs_inode;

#define DFS_MAX_FILESYSTEM_SIZE 0x1000000  // 16MB

#define DFS_FAIL -1
#define DFS_SUCCESS 1

/*
//STUDENT ----
#define DFS_FBV_MAX_NUM_WORDS (DFS_MAX_FILESYSTEM_SIZE / DFS_BLOCKSIZE) / 32
#define DISK_BLOCKSIZE 512
*/
/** STUDENT DEFINES **/
#define FDISK_NUM_INODES      192 
#define DISK_BLOCKSIZE  512
#define DFS_FBV_MAX_NUM_WORDS  DFS_MAX_FILESYSTEM_SIZE/ DFS_BLOCKSIZE/32

#define FDISK_FBV_BLOCK_START 1+ FDISK_NUM_INODES /(2*(DFS_BLOCKSIZE/DISK_BLOCKSIZE)) //STUDENT: define this

/* File descriptor lock create */
void CreateFileLock();

#endif
