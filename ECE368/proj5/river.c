#include<stdio.h>
#include<stdlib.h>
#include "river.h"

Node** loadfile(FILE* fin, int *size)
{
  Node** g = NULL;
  int N = 0;
  char temp;
  int r = 0;
  int c = 0;
  fscanf(fin,"%d",&N);
  *size = N;
  g = malloc(sizeof(Node*)*N-1);
  int i;
  
  
  
  
  for(i = 0;i < N-1;i++)
    {
      g[i] = malloc(sizeof(Node)*N);
    }
  fscanf(fin,"%c",&temp);
  int j;
  int dist;
  for(i= 0;i < N-1;i++)
    {
      
      for(j = 0;j<N;j++)
	{
	  fscanf(fin,"%c",&temp);
	  if(temp == '0')
	    {
	      g[i][j].weight = 1;
	      r = i;
	      c = j;
	      dist = 0;  
	    }
	  else
	    {
	      g[i][j].weight = 0;
	      r = i;
	      c = j;
	      dist = 0;
	      
	    }
	  g[i][j].r = r;
	  g[i][j].c = c;
	  g[i][j].dist = dist;
	  
	}
      fscanf(fin,"%c",&temp);
    }
  return g;
}
void shortestPathHelper(Node** g,int size, int col)
{
  int i,j;
  int max_move = size*size;
  int path = 0;
  loc n1;
  loc n2;
  if(col == size-2)
    {
      for(i = 0;i<size-1;i++)
	{
	  ROW(n1) = i;
	  COL(n1) = col;
	  g[i][col].dist = max_move;
	  for(j = 0;j<size-1;j++)
	    {
	      ROW(n2) = j;
	      COL(n2) = col+1;
   
	      path = g[ROW(n2)][COL(n2)].dist + dist(g,i,col,j,col+1)+1;
	      if(g[ROW(n1)][COL(n1)].dist > path)
		{

		  g[ROW(n1)][COL(n1)].dist = path;
		  }
	   
   
	    
	    }
 
	}
      return;
    }

  shortestPathHelper(g,size,col+1);
  for(i = 0;i<size-1;i++)
    {
      g[i][col].dist = max_move;
      COL(n1) = col;
      ROW(n1) = i;
      
      for(j = 0;j<size-1;j++)
	{
	  ROW(n2) = j;
	      COL(n2) = col+1;
   
	      path = g[ROW(n2)][COL(n2)].dist + dist(g,i,col,j,col+1);
	      int prev_best = g[ROW(n1)][COL(n1)].dist;
	      g[ROW(n1)][COL(n1)].dist = MIN(prev_best,path);
	    
	}
    }
}
void shortestPath(Node** g, int size)
{
  shortestPathHelper(g,size,0);
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
  //printf("\ndist = %d",dist);
  return dist;

}


int main(int argc, char** argv)
{
  Node** g  ;
  int i;
  int j;
  int size;
  FILE* f = fopen(argv[1],"r");
  g = loadfile(f, &size);
  
  shortestPath(g,size);
  int min = size*size;
  
  int dist = size*size;
  for(i = 0; i<size-1;i++)
    {
      if(g[i][0].dist<dist)
	{
	  dist = g[i][0].dist;
	}
    }

  fclose(f);
  for(i = 0;i < size-1;i++)
    {
      for(j = 0;j < size;j++)
	{
	  printf("%d",g[i][j].weight);
	}
      printf("\n");
      free(g[i]);
    }
  
  free(g);
  printf("%d\n",dist);
  return EXIT_SUCCESS;

}
