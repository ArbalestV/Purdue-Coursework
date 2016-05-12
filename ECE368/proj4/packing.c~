
#include "packing.h"
#include<time.h>

void loadFile(bintree * array_bin, FILE * fp, int num_node, int num_rec)
{
  int i = 0; //the index of the binary tree array
  int j = 0; //counter to make sure that the correct number of leaf nodes are being read
  while (i < num_node) //keep reading for each binary tree structure element
    {
      if (j != num_rec) //while only leaf nodes are being read
	{
	  fscanf(fp, "%d %d %d %d %c %le %le", &array_bin[i].thisnode, &array_bin[i].parnode, &array_bin[i].lcnode, &array_bin[i].rcnode, &array_bin[i].cutline, &array_bin[i].width, &array_bin[i].height); //read into each binary tree element a leaf node
	  j++; //increment the leaf node counter
	}
      
      else //while internal nodes are being read
	{
	  char tempw, temph; //just temporary characters
	  fscanf(fp, "%d %d %d %d %c %c %c", &array_bin[i].thisnode, &array_bin[i].parnode, &array_bin[i].lcnode, &array_bin[i].rcnode, &array_bin[i].cutline, &tempw, &temph); //read into each binary tree element an internal  node
	  array_bin[i].width = 0.0; //initialize widths of internal nodes to 0
	  array_bin[i].height = 0.0; //initialize heights of internal nodes to 0
	}
      i++; //increment the index of the structure array by one
    }
  //now, close fp
  fclose(fp);
}
void preOrder(bintree * array_bin, int index)
{
  printf("%d ", array_bin[index].thisnode); //display the value of node
  if (array_bin[index].lcnode != -1)
    {
      preOrder(array_bin, (array_bin[index].lcnode - 1)); //left subtree
    }
  if (array_bin[index].rcnode != -1)
    {
      preOrder(array_bin, (array_bin[index].rcnode - 1)); //right subtree
    }
}
void inOrder(bintree * array_bin, int index)
{
  if (array_bin[index].lcnode != -1)
    {
      inOrder(array_bin, (array_bin[index].lcnode - 1)); //left subtree
    }
  printf("%d ", array_bin[index].thisnode); //display the value of node
  if (array_bin[index].rcnode != -1)
    {
      inOrder(array_bin, (array_bin[index].rcnode - 1)); //right subtree
    }
}
void postOrder(bintree * array_bin, int index)
{
  if (array_bin[index].lcnode != -1)
    {
      postOrder(array_bin, (array_bin[index].lcnode - 1)); //left subtree
    }
  if (array_bin[index].rcnode != -1)
    {
      postOrder(array_bin, (array_bin[index].rcnode - 1)); //right subtree
    }
  printf("%d ", array_bin[index].thisnode); //display the value of node
}
void calcWidth_Height(bintree * array_bin, int index)
{
  if (array_bin[array_bin[index].lcnode - 1].lcnode != -1) //if left child not a leaf node, calculate width and height -> strictly binary tree
    { 
      calcWidth_Height(array_bin, (array_bin[index].lcnode - 1)); //calculate the width and height of the left child of the current node
    }
  if (array_bin[array_bin[index].rcnode - 1].lcnode != -1) //if right child not a leaf node, calculate width and height -> strictly binary tree
    {
      calcWidth_Height(array_bin, (array_bin[index].rcnode - 1)); //calculate the width and height of the right child of the current node
    }
  if (array_bin[index].cutline == 'H') //if horizontal cutline
    {
      array_bin[index].height = array_bin[array_bin[index].lcnode - 1].height + array_bin[array_bin[index].rcnode - 1].height; //height of a node = summation of left and right children heights
      //for the width for a horizontal cutline, the width is the larger of the left and right child widths
      if (array_bin[array_bin[index].lcnode - 1].width >= array_bin[array_bin[index].rcnode - 1].width)
	{
	  array_bin[index].width = array_bin[array_bin[index].lcnode - 1].width;
	}
      else
	{
	  array_bin[index].width = array_bin[array_bin[index].rcnode - 1].width;
	}
    }
  if (array_bin[index].cutline == 'V') //if vertical cutline
    {
      array_bin[index].width = array_bin[array_bin[index].lcnode - 1].width + array_bin[array_bin[index].rcnode - 1].width; //width of a node = summation of left and right children widths
      //for the height for a horizontal cutline, the height is the larger of the left and right child heights
      if (array_bin[array_bin[index].lcnode - 1].height >= array_bin[array_bin[index].rcnode - 1].height)
	{
	  array_bin[index].height = array_bin[array_bin[index].lcnode - 1].height;
	}
      else
	{
	  array_bin[index].height = array_bin[array_bin[index].rcnode - 1].height;
	}
    }
}

//begin from here
void rectInfo(rect * array_rect, bintree * array_bin, int index, double prev_hgt, double prev_wdt)
{
  if (array_bin[index].cutline == 'V') //case for vertical cutline
    {
      if (array_bin[array_bin[index].lcnode - 1].cutline != '-') //left child is an internal node
	{
	  rectInfo(array_rect, array_bin, array_bin[index].lcnode - 1, prev_hgt, prev_wdt);
	}
      else //left child is not an internal node
	{
	  array_rect[array_bin[index].lcnode - 1].thisnode = array_bin[array_bin[index].lcnode - 1].thisnode;
	  array_rect[array_bin[index].lcnode - 1].width = array_bin[array_bin[index].lcnode - 1].width;
	  array_rect[array_bin[index].lcnode - 1].height = array_bin[array_bin[index].lcnode - 1].height;
	  array_rect[array_bin[index].lcnode - 1].xcoord = array_rect[array_bin[index].lcnode - 1].xcoord + prev_wdt;
	  array_rect[array_bin[index].lcnode - 1].ycoord = array_rect[array_bin[index].lcnode - 1].ycoord + prev_hgt;
	}
      prev_wdt = prev_wdt + array_bin[array_bin[index].lcnode - 1].width;//increment the previous width right before we go to the left
      if (array_bin[array_bin[index].rcnode - 1].cutline != '-') //right child is an internal node
	{
	  rectInfo(array_rect, array_bin, array_bin[index].rcnode - 1, prev_hgt, prev_wdt);
	}
      else //right child is not an internal node
	{
	  array_rect[array_bin[index].rcnode - 1].thisnode = array_bin[array_bin[index].rcnode - 1].thisnode;
	  array_rect[array_bin[index].rcnode - 1].width = array_bin[array_bin[index].rcnode - 1].width;
	  array_rect[array_bin[index].rcnode - 1].height = array_bin[array_bin[index].rcnode - 1].height;
	  array_rect[array_bin[index].rcnode - 1].xcoord = array_rect[array_bin[index].rcnode - 1].xcoord + array_bin[array_bin[index].lcnode - 1].width;// + prev_wdt;
	  array_rect[array_bin[index].rcnode - 1].ycoord = array_rect[array_bin[index].rcnode - 1].ycoord + prev_hgt;
	}
    } //end of vertical cutline case
  else //case for horizontal cutline
    {
      //prev_hgt = prev_hgt + array_bin[array_bin[index].rcnode - 1].height; 
      if (array_bin[array_bin[index].rcnode - 1].cutline != '-') //if right child is an internal node
	{
	  rectInfo(array_rect, array_bin, array_bin[index].rcnode - 1, prev_hgt, prev_wdt);
	}
      else //right child is not an internal node
	{
	  array_rect[array_bin[index].rcnode - 1].thisnode = array_bin[array_bin[index].rcnode - 1].thisnode;
	  array_rect[array_bin[index].rcnode - 1].width = array_bin[array_bin[index].rcnode - 1].width;
	  array_rect[array_bin[index].rcnode - 1].height = array_bin[array_bin[index].rcnode - 1].height;
	  array_rect[array_bin[index].rcnode - 1].xcoord = array_rect[array_bin[index].rcnode - 1].xcoord + prev_wdt;
	  array_rect[array_bin[index].rcnode - 1].ycoord = array_rect[array_bin[index].rcnode - 1].ycoord + prev_hgt;
	}
      prev_hgt = prev_hgt + array_bin[array_bin[index].rcnode - 1].height; //increment the previous height right before we go to the left 
      if (array_bin[array_bin[index].lcnode - 1].cutline != '-') //left child is an internal node
	{
	  rectInfo(array_rect, array_bin, array_bin[index].lcnode - 1, prev_hgt, prev_wdt);
	}
      else //left child is not an internal node
	{
	  array_rect[array_bin[index].lcnode - 1].thisnode = array_bin[array_bin[index].lcnode - 1].thisnode;
	  array_rect[array_bin[index].lcnode - 1].width = array_bin[array_bin[index].lcnode - 1].width;
	  array_rect[array_bin[index].lcnode - 1].height = array_bin[array_bin[index].lcnode - 1].height;
	  array_rect[array_bin[index].lcnode - 1].xcoord = array_rect[array_bin[index].lcnode - 1].xcoord + prev_wdt;
	  array_rect[array_bin[index].lcnode - 1].ycoord = array_rect[array_bin[index].lcnode - 1].ycoord + array_bin[array_bin[index].rcnode - 1].height;// + prev_hgt;
	}
    } //end of vertical condition
} //end of function

void saveFile(rect * array_rect, FILE * sf, int num_rec)
{
  fprintf(sf, "%d\n", num_rec); //write the number of rectangles onto file
  int i;
  for (i = 0; i < num_rec; i++)
    {
      fprintf(sf, "%d %le %le %le %le\n", array_rect[i].thisnode, array_rect[i].width, array_rect[i].height, array_rect[i].xcoord, array_rect[i].ycoord);
    }
  fclose(sf);
}

int main(int argc, char** argv)
{
  if (argc != 3)
    {
      return EXIT_FAILURE;
    }
  //now load the input file and each element that you read should be a bintree object
  //also, store the size of the binary tree = the second number from the input file
  //also, store the no. of rectangles = the first number from the input file
  FILE * fp = fopen(argv[1], "r"); //first of all, open the input file, after which take in the sizes of the rectangles and no. of nodes of the binary tree
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


