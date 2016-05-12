#include "reroot.h"
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<assert.h>
void Preorder(Node* arr)
{
  if(arr->cutline == '-')
    {
      printf("(%le,%le)",arr->width,arr->height);
      return;
    }
  printf("%c ", arr->cutline);
  Preorder(arr->lc);
  Preorder(arr->rc); 
}

Node* TreeNode_create(double w,double h, char cutline)
{
  Node* head = malloc(sizeof(Node));
  head->lc = NULL;
  head->rc = NULL;
  head->parent = NULL;
  head->cutline = cutline;
  head->width = w;
  head->height = h;
  head->x = 0;
    head->y = 0;
    //printf("\nrot = %c",head->cutline);
  return head;
}
int isEmpty(Stack_node* stack)
{
  if(stack != NULL)
    {
      return UNDERFLOW;
    }
  return TRUE;
}
Stack_node* stack_push(Stack_node* stack, Node* root)
{
  //char cut = root->cutline;
  //printf("\ncut = %c",root->cutline);
  //printf("\nwidth = %le",root->width);
  Stack_node* temp = malloc(sizeof(Stack_node));
  //printf("\ncut = %c",root->cutline);

  temp->tree_node = root;
  //temp->tree_node->cutline = cut;

  if(stack != NULL)
    {
      
      temp -> next = stack;
      stack = temp;
      return stack;
    }
  
  temp -> next = NULL;
  
  stack = temp;
  //printf("asdasd\n");
  return stack;  
}

Node* stack_pop(Stack_node** stack)
{

  if((*stack) == NULL)
    {
      printf("\nStack underflow");
      return NULL;
    }
  
  Stack_node* node = (*stack);
  Node* temp = (*stack)->tree_node;
  //printf("\ncutl = %c",temp->cutline);
  (*stack) = (*stack)->next;
  
  free(node);
  
  return temp;
}

Node* CreateParent(Node* Lnode, Node* Rnode, char cutline)
{
  Node* parent = malloc(sizeof(Node));
  parent -> cutline = cutline;
  parent -> lc = Lnode;
  parent -> rc = Rnode;
  return parent;
}
Node* Load_file(char* filename)
{
  FILE* fin  = fopen(filename, "r");
  
  double w = 0;
  double l = 0;
  char dump;
  char dump1;
  char dump2;
  Stack_node* stack = NULL;
  Node* root = NULL;
  //stack->top = NULL;
  if(fin == NULL)
    {
      printf("\nFile failed to open");
      return NULL;
    }
  fscanf(fin,"%c", &dump);
  do
    {
	
      //printf("\nPART 1\n");
      //printf("\n%c",dump);
	  if(dump == '(')
	    {
	      fscanf(fin,"%le%c%le%c", &w,&dump2,&l,&dump1);  
	      Node* node = TreeNode_create(w,l, '-');
		  stack = stack_push(stack, node);
		  // printf("\naa = (%le%c%le%c",w,dump2,l,dump1);
		  // printf("\nPART 2\n");
        
	        
	    }
	
	  else
	    {
	      //printf("\nPART 3\n");
	      
	      Node* node1 = stack_pop(&stack);
	      
	      Node* node2 = stack_pop(&stack);
	      
	      if(node1 != NULL && node2 != NULL)
		{
		  root = CreateParent(node2, node1,dump);
		  //printf("\n%c",root->cutline);
		  
		  stack = stack_push(stack, root);
		  
		}
	      
	    }
	  //printf("\nasdds");
    }
  while(fscanf(fin,"%c", &dump)!=EOF && stack != NULL);
  //printf("\nasdasd");
    StackDestroy(stack);
  return root;
}
	
room CalWH(room r1, room r2, char cutline)
{
  room r3 = {0.0,0.0};
  if(cutline == 'V')
    {
      r3.width = SUM(r1.width,r2.width);
      r3.height = MAX(r1.height, r2.height);
    }
  if(cutline == 'H')
    {
      r3.width = MAX(r1.width, r2.width);
      r3.height = SUM(r1.height,r2.height);
    }
  return r3;
}

void CalBestRoom(room r, room* min)
{
  double area = r.width*r.height;
  double min_area = (min)->width*(min)->height;
  if(area < min_area) {
    min->width = r.width;
    min->height= r.height;
  }
  else if(area == min_area) {
    if(r.width < min->width) {
      min->width = r.width;
      min->height= r.height;
    }
  }

}

void rerooting(char root_cut, room parent_info,Node* edge, room* min)
{
  if(edge -> rc == NULL)
    {
      return;
    }
  room r,parr,parl;
  room rc = {RIGHTC(edge)->width,RIGHTC(edge)->height};

  room lc = {LEFTC(edge)->width,LEFTC(edge)->height};
  
  //ReRooting on Left Child
  parr = CalWH(parent_info,rc,root_cut);
  //printf("\nparl.width = %le",parr.width);
  //printf("\nparl.width = %le",parr.height);
  r = CalWH(lc,parr,edge->cutline);
  //printf("\nrl.width = %le",r.width);
  //printf("\nrl.width = %le",r.height);
  CalBestRoom(r,min);
  
  //ReRooting on Right Child
  parl = CalWH(parent_info,lc,root_cut);
  //printf("\nparr.width = %le",parl.width);
  //printf("\nparr.width = %le",parl.height);
  r = CalWH(rc,parl,edge->cutline);
  //printf("\nrr.width = %le",r.width);
  //printf("\nrr.width = %le",r.height);
  CalBestRoom(r,min);
  //recursive calls
  
  rerooting(edge->cutline,parr,edge->lc,min);
  rerooting(edge->cutline,parl,edge->rc,min);

}

void Cal_coord(Node* tree) {
  if(tree->cutline == '-') {
    return;
  }
  else if(tree->cutline == 'H') {
    LEFTC(tree)->x = tree->x;
    LEFTC(tree)->y = RIGHTC(tree)->height + tree->y;
    RIGHTC(tree)->y = tree->y;
    RIGHTC(tree)->x = tree->x;
  }
  else {
    RIGHTC(tree)->y = tree->y;
    RIGHTC(tree)->x = tree->width + tree->x;
    LEFTC(tree)->y = tree->y;
    LEFTC(tree)->x = tree->x;
  }

  Cal_coord(LEFTC(tree));
  Cal_coord(RIGHTC(tree));
  return;
}

void packing(Node* tree) {
  if(tree->cutline == '-') {
    return;
  }
  packing(LEFTC(tree));
  packing(RIGHTC(tree));
  if(tree->cutline == 'V') {
    tree->width = SUM(RIGHTC(tree)->width, LEFTC(tree)->width);
    tree->height = MAX(RIGHTC(tree)->height, LEFTC(tree)->height);
  }
  else {
    tree->height = SUM(RIGHTC(tree)->height, LEFTC(tree)->height);
    tree->width = MAX(RIGHTC(tree)->width, LEFTC(tree)->width);
  }
  return;
}
/*
prosorder traversal of binary tree
*/
void Postorder(Node* arr)
{
  if(arr->cutline == '-')
    {
      printf("(%le,%le)",arr->width,arr->height);
      //printf(" width = %le height = %le\n",arr->width,arr->height);
      return;
    }
  Postorder(LEFTC(arr));
  Postorder(RIGHTC(arr)); 
  printf("%c ", arr->cutline);
  //printf(" x = %le y = %le\n",arr->x,arr->y);
}

/*
Inorder traversal of binary tree
*/
void Inorder(Node* arr)
{
  if(arr->cutline == '-')
    {
      printf("(%le,%le)",arr->width,arr->height);
      return;
    }
  Inorder(LEFTC(arr));
  printf("%c ", arr->cutline);
  Inorder(RIGHTC(arr)); 
}
void PostOrderPrint(FILE* fptr, Node*arr)
{
  if(arr->rc == NULL)
    {
      fprintf(fptr,"%le %le %le %le\n",arr->width,arr->height,arr->x,arr->y);
      return;
    }
  PostOrderPrint(fptr,LEFTC(arr));
  PostOrderPrint(fptr,RIGHTC(arr));

}
int Save_file(char*filename, Node* arr)
{
  FILE* fout = fopen(filename, "w");
  //writing data to output file
  PostOrderPrint(fout, arr);
  /*fprintf(fout,"%d\n",rect_num);
  for(i = 1;i <= rect_num;i++)
    {
      fprintf(fout,"%d %le %le %le %le\n",arr[i].this,arr[i].width,arr[i].height,arr[i].x_coord,arr[i].y_coord);
      }*/
  fclose(fout);
  return EXIT_SUCCESS;
}

void TreeDestroy(Node* tree)
{
  if(tree == NULL)
    {
      return;
    }
  TreeDestroy(LEFTC(tree));
  TreeDestroy(RIGHTC(tree));
  free(tree);
}
void StackDestroy(Stack_node* stack)
{
  if(!ISVALID(stack))
    {
      return;
    }
  Stack_node* temp = stack;
  stack = stack->next;
  free(temp);
}
int main(int argc, char** argv)
{
  if(argc != 3)
    {
      return EXIT_FAILURE;
    }
  
  Node*arr = NULL;//Array to store Binart tree
 
  clock_t t1,t2,t3;//time variables
  double t = 0.0;//Elapsed Time
  //loading Binary tree
  arr = Load_file(argv[1]);
  //Clocking elapsed time
  t1 = clock();
  //Packing the binary tree
  packing(arr);//calculating width and height
  Cal_coord(arr);//Calculating the X and Y coordinates of rectangles
  //Cloacking Elapsed Time
  t2 = clock();
  t3 = t2-t1/CLOCKS_PER_SEC;
  t = (double)t3;
  //Printing Screen Dump
  printf("Preorder: ");
  Preorder(arr);
  printf("\n");
  printf("\nInorder: ");
  Inorder(arr);
  printf("\n");
  printf("\nPostorder: ");
  Postorder(arr);
  printf("\n");
  //Saving packed Binary tree to output file
  Save_file(argv[2],arr);
  room min = {arr->width,arr->height};
  room temp = {0.0,0.0};
  
  printf("\nWidth: %le\n",arr->width);
  printf("Height: %le\n\n",arr->height);
  while(arr->rc != NULL)
    {arr=arr->lc;}
  printf("Elapsed Time: %le\n",t);
  t1 = clock();
  rerooting(arr->cutline, temp,arr,&min);
  t2 = clock();
  printf("\nBest Width: %le\n",min.width);
  printf("Best Height: %le\n\n",min.height);
  t3 = (t2-t1)/CLOCKS_PER_SEC;
  t = (double)t3;
  printf("X-coordinate: %le\n",arr->x);
  printf("Y-coordinate: %le\n\n",arr->y);
  printf("Elapsed Time for re-rooting: %le\n",t);
  TreeDestroy(arr);

  
  return EXIT_SUCCESS;
}
