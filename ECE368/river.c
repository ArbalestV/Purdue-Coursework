#include<stdio.h>
#include<stdlib.h>
#include "river.h"


/*
Loads a graph <arr> from input file <fileName>
Args:
fileName: name of input file
Return:
arr: graph loaded from input file
 */
graphNode** LoadFile(char* fileName) 
{
  //printf("asdasd");
  int size;
  int i = 0;
  int j = 0;
  char temp = 0;
  FILE*fin = fopen(fileName,"r");
  fscanf(fin,"%d\n",&size);
  graphNode** arr = malloc(sizeof(graphNode*)*size-1);
  for(i = 0;i < size-1;i++)
    {
      arr[i] = malloc(sizeof(graphNode)*size);
      for(j = 0;j < size;j++)
	{
	  fscanf(fin,"%c",&temp);
	  if(temp == '0')
	    {
	      arr[i][j].weight = 1;
	      arr[i][j].row = i;
	      arr[i][j].col = j;
	      arr[i][j].shortestPath = 0;
	    }
	  else
	    {
	      arr[i][j].weight = 0;
	      arr[i][j].row = i;
	      arr[i][j].col = j;
	      arr[i][j].shortestPath = 0;
	    }
	}
      fscanf(fin,"%c",&temp);
    }
  fclose(fin);
  return arr;
}

/*
 */

int shortestPath(graphNode** arr, int col, int size)
{
  int i = 0;
  int j = 0;
  int min = 0;
  int dist = 0;
  min = size*size;
  printf("col = %d\n",col);
  if(col == size-2)
    {
      for(i = 0;i < size-1;i++)
	{
	  
	  SPATH(arr,i,col) = size*size;
	  for(j = 0;j < size-1;j++)
	    {
	      //printf("sadsd\n");
	      //printf("%d\n",j);
     
	      dist = getDistance(arr,arr[i][col],arr[j][col+1]) + SPATH(arr,j,col+1) + 1;
	      //printf("sad\n");
	      SPATH(arr,i,col) = getMin(SPATH(arr,i,col), dist);
	      printf("dist = %d",dist);
	      printf("hey%d, i = %d, j = %d\n",SPATH(arr,i,col),i,j);
	    }
       
	  min = getMin(SPATH(arr,i,col),min);
	}
      return min;
    }
  shortestPath(arr ,col+1,size);
  for(i = 0;i < size-1;i++)
    {
      SPATH(arr,i,col) = size*size;
      for(j = 0;j < size-1;j++)
	{
	  dist = getDistance(arr,arr[i][col],arr[j][col+1]) + SPATH(arr,j,col+1) ;
	  SPATH(arr,i,col) = getMin(SPATH(arr,i,col), dist);
	  printf("%d\n",dist);
	  printf("hi%d, i = %d, j = %d\n",SPATH(arr,i,col),i,j);
	}
      printf("\nmin1 = %d\n",min);
      min = getMin(SPATH(arr,i,col),min);
      printf("\nmin2 = %d\n",min);
    }
  return min; 
}
/*
 */
int getDistance(graphNode** arr, graphNode node1, graphNode node2)
{
  int  i = 0;
  int j = 0;
  int dist = 0;
  if(node1.row < node2.row)
    {
      for(i = node1.row+1;i <= node2.row; i++)
	{
	  dist = dist + WEIGHT(arr,i,node2.col) + 1; 
	}
      // dist = dist + 
    }
  else if(node1.row > node2.row)
    {
      for(i = node1.row-1; i >= node2.row;i--)
	{
	  dist = dist + WEIGHT(arr,i,node2.col) + 1;
	}
    }
  else
    {
      dist = 1 + node2.weight;
      printf("\nnode2.weight = %d",node2.weight);
      printf("\nnode2.row = %d",node2.row);
      //printf("\nnode1.row = %d",node1.row);
      printf("\nnode2.col = %d",node2.col);
    }
  printf("\nnode = %d\n", dist);
  return dist;
}
/*
 */

int getMin(int a, int b)
{
  if(a < b)
    {
      return a;
    }
  else
    {
      return b;
    }
}

/*
 */
int getBestSource(graphNode** arr, int size)
{
  int i = 0;
  int j = 0;
  int min = size*size;
  for(i = 0; i<size-1;i++)
    {
      min = getMin(SPATH(arr,i,0),min);
    }
  return min;
}

int main(int argc, char** argv)
{
  int i,j;
  int size = 0;
  graphNode** arr = NULL;
  arr = LoadFile(argv[1]);
  
  //int dist = getDistance(arr,arr[2][1],arr[4][2]);
  int dist = shortestPath(arr,0,8);
  for(i = 0;i < 7;i++)
    {
      arr[i][0].shortestPath = arr[i][0].weight + SPATH(arr,i,0);
    }
  dist = getBestSource(arr,8);
  for(i = 0;i < 7;i++)
    {
      for(j = 0;j<8;j++)
	{
	  printf("%d ",arr[i][j].shortestPath);
	}
      printf("\n");
    }
  printf("\ndistance = %d\n",dist);
  return EXIT_SUCCESS;
}
