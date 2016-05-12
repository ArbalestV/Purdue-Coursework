#ifndef RIVER_H
#define RIVER_H


//macros
#define ROW(arr,x,y) arr[x][y].row
#define COL(arr,x,y) arr[x][y].col
#define WEIGHT(arr,x,y) arr[x][y].weight
#define SPATH(arr,x,y) arr[x][y].shortestPath

//structure for graph
typedef struct _graphNode{
  int row;//row index of matrix
  int col;//column index of matrix
  int shortestPath;//shortest path from this node to destination
  int weight;//weight of node
}graphNode;

graphNode** LoadFile(char* fileName);//Load graph from input file
int shortestPath(graphNode** node, int a, int b);//calculate shortest path to cross the river
int shortestPathHelper(graphNode* node, int row);
int getMin(int node1, int node2);//get min to to shortest paths
int getDistance(graphNode** arr, graphNode node1, graphNode node2); //get distance from one node to another

#endif
