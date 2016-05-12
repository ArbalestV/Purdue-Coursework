#include "reroot.h"
#include<time.h>
bstack * push(bintree * node, bstack * top)
{
  bstack * bs = malloc(sizeof(bstack));
  bs->node = node;
  if (top == NULL) {
    bs->next = NULL;
    top = bs;
  }
  else {
    bs->next = top;
    top = bs;
  }
  return top;
}
bintree * pop(bstack ** top)
{
  if ((*top) == NULL) {
    return NULL;
  }
  bintree *node_ret = (*top)->node;
  bstack * tmp = *top;
  *top = (*top)->next;
  free(tmp);
  return node_ret;
}
bintree * loadFile(FILE * fp)
{
  char ch;
  fscanf(fp, "%c", &ch);
  bstack * top = NULL;
  do {
    if (ch == '(') {
      char tmp1, tmp2;
      bintree * node = malloc(sizeof(bintree));
      fscanf(fp, "%le%c%le", &(node->width), &tmp1, &(node->height));
      fscanf(fp,"%c", &tmp2);
      node->cutline = 'X';
      node->xcoord = 0.0;
      node->ycoord = 0.0;
      node->left = NULL;
      node->right = NULL;
      top = push(node, top);
    }
    else {
      bintree * par = malloc(sizeof(bintree));
      par->cutline = ch;
      par->right = pop(&top);
      par->left = pop(&top);
      par->xcoord = 0.0;
      par->ycoord = 0.0;
      par->width = 0.0;
      par->ycoord = 0.0;
      top = push(par, top);
    }
    fscanf(fp, "%c", &ch);
  } while(!feof(fp));
  bintree * root = pop(&top);
  fclose(fp);
  return root;
 }

void preOrder(bintree * root)
{
  if (root->cutline == 'X') {
    printf("(");
    printf("%le ", root->width);
    printf(",");
    printf("%le ", root->height);
    printf(")");
  }
  else {
    printf("%c", root->cutline);
  }
  if (root->left != NULL)
    {
      preOrder(root->left); //left subtree
    }
  if (root->right != NULL)
    {
      preOrder(root->right); //right subtree
    }
}
void inOrder(bintree * root)
{
  if (root->left != NULL)
    {
      inOrder(root->left); //left subtree
    }
  if (root->cutline == 'X') {
    printf("(");
    printf("%le ", root->width);
    printf(",");
    printf("%le ", root->height);
    printf(")");
  }
  else {
    printf("%c", root->cutline);
  }
  if (root->right != NULL)
    {
      inOrder(root->right); //right subtree
    }
}
void postOrder(bintree * root)
{
  if (root->left != NULL)
    {
      postOrder(root->left); //left subtree
    }
  if (root->right != NULL)
    {
      postOrder(root->right); //right subtree
    }
  if (root->cutline == 'X') {
    printf("(");
    printf("%le ", root->width);
    printf(",");
    printf("%le ", root->height);
    printf(")");
  }
  else {
    printf("%c", root->cutline);
  }
}
void calcWidth_Height(bintree * root)
{
  if (root->left != NULL) //if left child not a leaf node, calculate width and height -> strictly binary tree
    { 
      calcWidth_Height(root->left); //calculate the width and height of the left child of the current node
    }
  if (root->right != NULL) //if right child not a leaf node, calculate width and height -> strictly binary tree
    {
      calcWidth_Height(root->right); //calculate the width and height of the right child of the current node
    }
  if (root->cutline == 'H') //if horizontal cutline
    {
      root->height = root->left->height + root->right->height; //height of a node = summation of left and right children heights
      //for the width for a horizontal cutline, the width is the larger of the left and right child widths
      if (root->left->width >= root->right->width)
	{
	  root->width = root->left->width;
	}
      else
	{
	  root->width = root->right->width;
	}
    }
  if (root->cutline == 'V') //if vertical cutline
    {
      root->width = root->left->width + root->right->width; //width of a node = summation of left and right children widths
      //for the height for a horizontal cutline, the height is the larger of the left and right child heights
      if (root->left->height >= root->right->height)
	{
	  root->height = root->left->height;
	}
      else
	{
	  root->height = root->right->height;
	}
    }
}
/*void rectInfo(bintree * root)
{
  if (root->cutline == 'X'){
    return;
  }
}*/
  void rectInfo(bintree * root)
  {
    if (root->cutline == 'X'){
      return;
    }
    else if(root->cutline == 'V'){
      root->left->xcoord = root->xcoord;
      root->left->ycoord = root->ycoord;
      root->right->xcoord = root->width + root->xcoord;
      root->right->ycoord = root->ycoord;
    }
    else {
      root->left->xcoord = root->xcoord;
      root->left->ycoord = root->right->height + root->ycoord;
      root->right->xcoord = root->xcoord;
      root->right->ycoord = root->ycoord;
    }
    rectInfo(root->left);
    rectInfo(root->right);
  }


/*void rectInfo(bintree * root, double prev_hgt, double prev_wdt)
{
  void Cooder(Node* tree, int n) {
  if(tree->cutline == '-') {
    return;
  }
  else if(tree->cutline == 'H') {
    tree->left->xcoord = tree->xcoord;
    tree->left->ycoord = treeheight + GETN(tree, n).ycoord;
    RIGHTC(tree, n).ycoord = GETN(tree, n).ycoord;
    RIGHTC(tree, n).xcoord = GETN(tree, n).xcoord;
  }
  else {
    RIGHTC(tree, n).ycoord = GETN(tree, n).ycoord;
    RIGHTC(tree, n).xcoord = LEFTC(tree, n).width + GETN(tree, n).xcoord;
    LEFTC(tree, n).ycoord = GETN(tree, n).ycoord;
    LEFTC(tree, n).xcoord = GETN(tree, n).xcoord;
  }

  Cooder(tree, GETN(tree, n).left);
  Cooder(tree, GETN(tree, n).right);
  return;
}
*/

} //end of function

void saveFile(FILE * sf, bintree * root)
{

  if(root->left == NULL)
    {
      fprintf(sf, "%le %le %le %le\n", root->width, root->height, root->xcoord, root->ycoord);
      //fclose(sf);
      return;
    }
  saveFile(sf, root->left);
  saveFile(sf, root->right);
   
}

info change(info ia, info ib, char cutline)
{
  info ret;
  if (cutline == 'V')
    {
      ret.width = ia.width + ib.width;
      if (ia.height >= ib.height){
	ret.height = ia.height;
      }
      else{
	ret.height = ib.height;
      }
    }
  else{
    ret.height = ia.height + ib.height;
    if (ia.width >= ib.width){
      ret.width = ia.width;
    }
    else{
      ret.width = ib.width;
    }
  }
  return ret;
}

void minArea(info cmp, info * min)
{
  double area_min = min->width * min->height;
  double area_cmp = cmp.width * cmp.height;
  if (area_min > area_cmp)
    {
      min->width = cmp.width;
      min->height = cmp.height;
    }
  else if (area_min == area_cmp)
    {
      if (cmp.width < min->width){
	min->width = cmp.width;
	min->height = cmp.height;
      }
      else{
	return;
      }
    }
  else{
    return;
  }
}
void ReRoot(info root_par, char cutline, info * min, bintree * reroot_edge)
{
  if (reroot_edge->left == NULL) //since strictly binary tree, check either left or right
    {
      //printf("\nadasdasdas");
      return;
    }
  //rotate on the left edge
  info rightc;
  rightc.width = reroot_edge->right->width;
  rightc.height = reroot_edge->right->height;
  info leftc;
  leftc.width = reroot_edge->left->width;
  leftc.height = reroot_edge->left->height;
  info parentr;
  info parentl;
  info rect;
  parentr = change(root_par, rightc,cutline);
  rect = change(parentr, leftc, reroot_edge->cutline);
  minArea(rect, min);
  //right child
  parentl = change(root_par,leftc,cutline);
  rect = change(parentl, rightc,reroot_edge->cutline);
  minArea(rect,min);
  ReRoot(parentr, reroot_edge->cutline, min, reroot_edge->left);
  ReRoot(parentl, reroot_edge->cutline, min, reroot_edge->right);
}

void del(bintree * root)
{
  if(root == NULL)
    {
      return;
    }
  del(root->left);
  del(root->right);
  free(root);
}

int main(int argc, char** argv)
{
   if (argc != 3)
    {
      return EXIT_FAILURE;
    }
  FILE * fp = fopen(argv[1], "r"); //first of all, open the input file, after which take in the sizes of the rectangles and no. of nodes of the binary tree
  bintree * root =  loadFile(fp);
  //printf("hiiiii\n");
  info root_parentleft_info, root_parentright_info;
   root_parentleft_info.width = root->left->width;
  root_parentleft_info.height = root->left->height;
  
  root_parentright_info.width = root->right->width;
  root_parentright_info.height = root->right->height;
  
  info * min_info = malloc(sizeof(info));
  
  //printf("\nwidthhhh = %le",root->width);
  clock_t t1, t2, t3;
  //info root_info;
  //root_info.width = 0;
  //root_info.height = 0;
  FILE * sf = fopen(argv[2], "w");
  
  printf("\n\nPreorder: ");
  preOrder(root);
  printf("\n\nInorder: ");
  inOrder(root);
  printf("\n\nPostorder: ");
  postOrder(root);
  t1 = clock();
  calcWidth_Height(root);
  rectInfo(root);
  t2 = clock();
  //rectInfo(root);
  min_info->width = root->width;
  min_info->height = root->height;
  printf("\n\nWidth: %le", root->width);
  printf("\nHeight: %le", root->height);
  
  saveFile(sf, root);
  fclose(sf);
 //calculate the x and y coordinates for the input binary tree

  
  t3 = t2 - t1;
;
  double t_elapsed = (t3 / CLOCKS_PER_SEC);
  printf("\n\nX-coordinate: %le", root->xcoord);
  printf("\nY-coordinate: %le\n", root->ycoord);
  printf("\n\nElapsed time: %le", t_elapsed);
  clock_t t4, t5, t6;
  t4 = clock();
   root_parentleft_info.width = root->left->width;
  root_parentleft_info.height = root->left->height;
  
  root_parentright_info.width = root->right->width;
  root_parentright_info.height = root->right->height;
  ReRoot(root_parentright_info, root->cutline, min_info, root->left);
  ReRoot(root_parentleft_info, root->cutline, min_info, root->right);
  //ReRoot(root_info, root->cutline, min_info, root->right);
  t5 = clock();
  t6 = t5 - t4;
  double t_elapsed_reroot = (t6 / CLOCKS_PER_SEC);
  printf("\n\nBest Width: %le", min_info->width);
  printf("\nBest Height: %le", min_info->height);
  printf("\n\nElapsed time for re-rooting: %le\n", t_elapsed_reroot);
  
  del(root);
  
  return 0;
}












/*
  int num_node; //no. of nodes
  int num_rec; //no. of rectangles
  fscanf(fp, "%d", &num_rec); //now read the no. of rectangles
  fscanf(fp, "%d", &num_node); //now read the no. of nodes
  //now declare the array and called the loadfile function to store the binary tree
  bintree * array_bin = malloc(sizeof(bintree) * num_node); //allocate memory for binary tree, depending on the n. of nodes read from input file
  loadFile(array_bin, fp, num_node, num_rec); //now make the array of binary tree
  //Pre-order display
  printf("%d\n",array_bin[3].rcnode);
  printf("\nPreorder: ");
  preOrder(array_bin, num_node - 1); //display the pre-order traversal, starting with the root node
  //In-order display
  // return 0;
  printf("\nInorder: ");
  inOrder(array_bin, num_node - 1); //display the in-order traversal, starting with the root node
  //Post-order display
  printf("\nPostorder: ");
  postOrder(array_bin, num_node - 1); //display the post-order traversal, starting with the root node
  clock_t t1, t2, t3; //times
  t1 = clock();
  
  calcWidth_Height(array_bin, num_node - 1); //calculate the height and width of each non-leaf node, finally culminating in the root's width & height
  t2 = clock();
  t3 = t2 - t1;
  
  printf("\nWidth: %le", array_bin[num_node - 1].width); //print the width of the packed rectangles
  printf("\nHeight: %le", array_bin[num_node - 1].height); //print the height of the packed rectangles
  //now, we will call the function that creates the information for the rectangles
  
  rect * array_rect = malloc(sizeof(rect) * num_rec); //since no. of elements of rectangle is same as no. of rectangles as given
  double prev_hgt = 0.0; //maintain a variable that stores the height in the coordinate system, since the right rectangle will increase the height for the left rectangle
  double prev_wdt = 0.0; //maintain a variable that stores the width in the coordinate system, since the right rectangle will increase the width for the left rectangle
  clock_t t4, t5, t6, t7;
  t4 = clock();
  int j;

  for(j = 0; j < num_rec; j++)
    {
      array_rect[j].xcoord = 0.0;
      array_rect[j].ycoord = 0.0;
    } 
  rectInfo(array_rect, array_bin, (num_node - 1), prev_hgt, prev_wdt); //call the rectangle information function with the root node's number
  t5 = clock();
  t6 = t5 - t4;
  
  //now, implement the save file function
  printf("\nX-coordinate: %le", array_rect[num_rec - 1].xcoord); //screen dump for x-coordinate
  printf("\nY-coordinate: %le", array_rect[num_rec - 1].ycoord); //screen dump for y-coordinate
  t7 = t6 + t3;
  double t_tot = (t7 / CLOCKS_PER_SEC);
  printf("\nElapsed Time: %le\n", t_tot); //print the elapsed time
  FILE * sf = fopen(argv[2], "w");
  saveFile(array_rect, sf, num_rec); //call the save file function
  free(array_bin);
  free(array_rect);

  return EXIT_SUCCESS;
}
*/

