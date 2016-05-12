#include<stdio.h>
#include<stdlib.h>
#include "river.h"

Node** loadfile(char* filename, int *size)
{
  Node** g = NULL;
  char temp;
  FILE* fin = fopen(filename,"r");
  int N = 0;
  fscanf(fin,"%d",&N);
  *size = N;
  fscanf(fin,"%c",&temp);
  int i = 0 ;
  int j = 0;
  
  g = malloc(sizeof(Node*)*N-1);
  for(i= 0;i < N-1;i++)
    {
      g[i] = malloc(sizeof(Node)*N);
      for(j = 0;j<N;j++)
	{
	  fscanf(fin,"%c",&temp);
	  if(atoi(&temp) == 0)
	    {
	      g[i][j].weight = 1;
	    }
	  else
	    {
	      g[i][j].weight = 0;
	    }
	  //g[i][j].weight = atoi(&temp);
	  g[i][j].r = 0;
	  g[i][j].c = 0;
	  g[i][j].dist = 0;
	}
      fscanf(fin,"%c",&temp);
    }
  return g;
}
void shortestPathHelper(Node** g,int size, int col)
{
  int i = 0;
  int j = 0;
 
  int path = 0;
  loc n1;
  loc n2;
  // printf("col = %d",col);
  if(col == size-2)
    {
      for(i = 0;i<size-1;i++)
	{
	  ROW(n1) = i;
	  COL(n1) = col;
	  g[i][col].dist = size*size;
	  for(j = 0;j<size-1;j++)
	    {
	      ROW(n2) = j;
	      COL(n2) = col+1;
   
	      path = g[ROW(n2)][COL(n2)].dist + dist(g,i,col,j,col+1)+1;
	      // printf("\npath1 = %d\n",g[i][col].dist);
	      g[ROW(n1)][COL(n1)].dist = MIN(g[ROW(n1)][COL(n1)].dist,path);
   
	      //printf("\npath2 = %d\n",g[i][col].dist);
	    }
 
	}
      return;
    }
  //printf("asd\n");
  shortestPathHelper(g,size,col+1);
  for(i = 0;i<size-1;i++)
    {
      n1.row = i;
      n1.col = col;
      g[i][col].dist = size*size;
      for(j = 0;j<size-1;j++)
	{
	  ROW(n2) = j;
	      COL(n2) = col+1;
   
	      path = g[ROW(n2)][COL(n2)].dist + dist(g,i,col,j,col+1)+1;
	      // printf("\npath1 = %d\n",g[i][col].dist);
	      g[ROW(n1)][COL(n1)].dist = MIN(g[ROW(n1)][COL(n1)].dist,path);
	}
    }
}
void shortestPath(Node** g, int size)
{
  shortestPathHelper(g,size,0);
}


int getBestSource(Node** g, int size)
{
  int i = 0;
  int j = 0;
  int min = size*size;
  for(i = 0; i<size-1;i++)
    {
      min = MIN(g[i][0].dist,min);
    }
  return min;
}

int dist(Node** g, int r1, int c1, int r2, int c2)
{
  int dist = 0;
  int i = 0;
  if(r1 < r2)
    {
      for(i = r1+1;i<=r2;i++)
	{
	  dist = dist + g[i][c2].weight + 1;
	}
      
    }
  else if(r1>r2)
    {
      for(i = r1-1;i>=r2;i--)
	{
	  dist = dist + g[i][c2].weight + 1;
	}
      
    }
  else
    {
      dist = g[r2][c2].weight + 1;
    
    }
  printf("\ndist = %d",dist);
  return dist;

}


int main(int argc, char** argv)
{
  Node** arr;
  int i = 0;
  int j = 0;
  int size;
  arr = loadfile(argv[1], &size);
  
  shortestPath(arr,size);
  //printf("\n\n\n");
  /*for(i= 0;i < size-1;i++)
  {
  for(j = 0;j <size;j++)
    {
      printf("%d ",arr[i][j].dist);
    }
  printf("\n");
  }*/
//shortestPath(arr,size);
  //printf("sdfsdf\n");
  int dist = getBestSource(arr, size);
  printf("\ndistance = %d\n",dist);
  return EXIT_SUCCESS;

}
