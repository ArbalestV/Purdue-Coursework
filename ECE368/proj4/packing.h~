#ifndef packing_h
#define packing_h
#include<stdio.h>
#include<stdlib.h>

typedef struct btree {
  int thisnode; //node no. of the current node
  int parnode; //node no. of the parent of current node
  int lcnode; //node no. of left child
  int rcnode; //no. of right child
  char cutline; //cutline orientation 
  double width; //width of the rectangle
  double height; //height of the rectangle
} bintree;
typedef struct rectangle 
{
  int thisnode; //node no. of the rectangle
  double width; //width of the rectangle
  double height; //height of the rectangle
  double xcoord; //x-coordinate
  double ycoord; //y-coordinate
} rect;
//void loadFile(bintree *, FILE *, int, int); //the loadfile function
void preOrder(bintree *, int); //the preorder function
void inOrder(bintree *, int); //the inorder function
void postOrder(bintree *, int); //the postorder function
void calcWidth_Height(bintree *, int); //function to calculate width and height
void rectInfo(rect *, bintree *, int, double, double); //call the function to calculate rectangle information
//void saveFile(rect *, File *, int); //the save file function
#endif
