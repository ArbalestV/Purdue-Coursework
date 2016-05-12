#include<stdio.h>
#include<stdlib.h>
#define ARRAY_SIZE 4
void printPartition(int * part, int length)
{
  int ind = 0;
  for(ind = 0; ind < length - 1; ind++)
    {
      printf("%d + ", part[ind]);
    }
  printf("%d\n", part[length - 1]);
}

void partition(int * result, int ind, int left)
{
  int val = 0;
  if (left == 0)
    {
      printPartition(result, ind);
    }
  for (val = 1; val < =left; val++)
    {
      result[ind] = val;
      partition(result, ind + 1, left - val);
    }
}

void partHelp(int left)
{
  int arr[ARRAY_SIZE] = {0};
  partition(arr,0,left);
}

int main(int argc, char * argv[])
{
  partHelp(3);
  return EXIT_SUCCESS;
}
