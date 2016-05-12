#ifndef reroot_h
#define reroot_h
#include<stdio.h>
#include<stdlib.h>

typedef struct btree {
  char cutline; //H or V. Else mark as X
  double width; //width
  double height; //height
  double xcoord; //x-coordinate
  double ycoord; //y-coordinate
  struct btree * left;
  struct btree * right;
} bintree;

typedef struct b_stack {
  bintree * node; 
  struct b_stack * next;
} bstack;

typedef struct _info{
  double width;
  double height;
} info;

//void loadFile(bintree *, FILE *, int, int); //the loadfile function
bstack * push(bintree *, bstack *);
bintree * pop(bstack **);
bintree * loadFile(FILE *);
void preOrder(bintree *); //the preorder function
void inOrder(bintree *); //the inorder function
void postOrder(bintree *); //the postorder function
void calcWidth_Height(bintree *); //function to calculate width and height
void rectInfo(bintree *); //call the function to calculate rectangle information
//void rectInfo(bintree *);
void saveFile(FILE *, bintree *);
info change(info, info, char);
void minArea(info, info *);
void ReRoot(info, char, info *, bintree *); //reroot function

//void saveFile(rect *, File *, int); //the save file function
#endif
