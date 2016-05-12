#ifndef __FDISK_H__
#define __FDISK_H__

typedef unsigned int uint32;

#include "dfs_shared.h" // This gets us structures and #define's from main filesystem driver

#define FDISK_INODE_BLOCK_START 1 // Starts after super block (which is in file system block 0, physical block 1)
#define FDISK_INODE_NUM_BLOCKS 16 // Number of file system blocks to use for inodes
#define FDISK_NUM_INODES 192 //STUDENT: define this
#define FDISK_FBV_BLOCK_START 1+ FDISK_NUM_INODES/(2*(DFS_BLOCKSIZE/DISK_BLOCKSIZE))//STUDENT: define this -- 49 is the answer
#define FDISK_BOOT_FILESYSTEM_BLOCKNUM 0 // Where the boot record and superblock reside in the filesystem

#ifndef NULL
#define NULL (void *)0x0
#endif

//STUDENT: define additional parameters here, if any
//DFS_BLOCKSIZE - 1024B - defined in dfs_shared.h
//DFS_FILESYSTEM_SIZE - 16MB - defined in dfs_shared.h
#define DFS_NUMBLOCKS DFS_MAX_FILESYSTEM_SIZE/DFS_BLOCKSIZE// - defined in dfs_shared.h -- 2^24/2^10 = 2^14
#define DFS_FBV_MAX_NUM_WORDS (DFS_MAX_FILESYSTEM_SIZE / DFS_BLOCKSIZE) / 32 //2^24/2^10/32 = 512 = 2^9
#define DISK_BLOCKSIZE 512 //2^9
#endif
