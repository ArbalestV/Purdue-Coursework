#ifndef REROOTING_H
#define REROOTING_H


//Constans
#define TRUE 1
#define FALSE 0

//Stack Error variables
#define UNDERFLOW -1
#define STACK_ERROR -2

//Macros
#define RIGHTC(Tree) (Tree->rc)//Left child
#define LEFTC(Tree) (Tree->lc)//Right child
#define TOP(stack) (stack->top)//Top of stack
#define ISVALID(stack) (stack != NULL)//Check validity of stack

// Helper macros
#define MAX(x,y) ((x) > (y) ? (x) : (y))
#define SUM(x,y) ((x) + (y))
#define MIN(x,y) ((x) < (y) ? (x) : (y))

//structure for most efficient packing
typedef struct _rect{
  double width;
  double height;
  int x;
  int y;
}rect;

//Tree structure
typedef struct _Node{
  struct _Node* lc;
  struct _Node* rc;
  struct _Node* parent;
  char cutline;
  double width;
  double height;

  double x;
  double y;
}Node;

//Stack node structure
typedef struct _Stack_Node{
  Node* tree_node;
  struct _Stack_Node* next;
}Stack_node;

//Global Stack
typedef struct _Stack_t{
  Stack_node* top;
  int size;
}Stack;

//Structure for room
typedef struct _room{
  double width;
  double height;
}room;

Node* stack_pop(Stack_node** stack);//pop top oof stack
Stack_node* stack_push(Stack_node* stack, Node* TreeNode);//Push element at top of stack
int isEmpty(Stack_node* stack);//Chack if stack is empty
Node* Load_file(char* filename);//Load data from input file
void rerooting(char cutline, room par,Node* edge, room*min);//Rerroot the binary tree and calculate most efficient packing
void Cal_coord(Node* arr);
void Inorder(Node* arr);
void Preorder(Node* arr);
void Postorder(Node* arr);
void packing(Node* arr);//calculate packing of current ree representation
int Save_file(char* filename, Node* arr);//Save output to outptufile
room CalWH(room r1, room r2, char cutline);
void CalBestRoom(room r, room* min);
void Cal_Coord(Node* tree);
void StackDestroy(Stack_node*  stack);
#endif
