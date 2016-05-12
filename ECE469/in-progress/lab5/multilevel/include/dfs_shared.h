#ifndef __DFS_SHARED__
#define __DFS_SHARED__
typedef unsigned int inode_t;

typedef struct dfs_superblock {
  // STUDENT: put superblock internals here
  char valid;
  unsigned int blocksize;
  unsigned int total_blocks;
  unsigned int inode_start_block;
  unsigned int total_inodes;
  unsigned int fbv_start_block;
  unsigned int fbv_num_words;
  unsigned int fbv_num_blocks;
  unsigned int data_start_block;
} dfs_superblock;

#define DFS_BLOCKSIZE 1024  // Must be an integer multiple of the disk blocksize

typedef struct dfs_block {
  char data[DFS_BLOCKSIZE];
} dfs_block;
#define JUNK_LENGTH 79
typedef struct dfs_inode {
  // STUDENT: put inode structure internals here
  // IMPORTANT: sizeof(dfs_inode) MUST return 128 in order to fit in enough
  // inodes in the filesystem (and to make your life easier).  To do this, 
  // adjust the maximumm length of the filename until the size of the overall inode 
  // is 128 bytes.
unsigned char valid;
unsigned char is_dir;
unsigned char owner_id;
unsigned char permissions;
unsigned int filesize;
unsigned int direct_block_entries[10];
unsigned int indir_block_entry;
char junk[JUNK_LENGTH];
} dfs_inode;

#define DFS_MAX_FILESYSTEM_SIZE 0x1000000  // 16MB

#define DFS_MIN_BLOCKSIZE 64

// DFS_MAX_FILESYSTEM_SIZE / 64 = total_blocks if blocksize is 64
// (total_blocks + 31) / 32 = FBV_NUM_WORDS
#define DFS_FBV_MAX_NUM_WORDS (((DFS_MAX_FILESYSTEM_SIZE / DFS_MIN_BLOCKSIZE) + 31)  / 32)
#define DFS_INODES_MAX_NUM 200

#define DFS_FAIL -1
#define DFS_SUCCESS 1



#endif
