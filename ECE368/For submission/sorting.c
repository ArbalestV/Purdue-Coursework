#include <stdlib.h>
#include <stdio.h>
#include <string.h>
//#include <process.h>

int power(int num, int n)
{
 int res = 1;
 if (n == 1)
   {
     return num; //if exponent = 1, return number
   }
 if (n == 0)
   {
     return 1; //if exponent = 0, return 1
   }
 int i;
 for(i = 1; i <= n; i++)
   {
     res *= num; //if exponent >=2, use iteration to calculate power
   }
 return res;
}

long *Load_File(char *Filename, int *Size)
{
  FILE * fp = fopen(Filename, "r"); //open file
  if (fp == NULL)
    {
      return NULL; //file not opened case
    }
  long val; //to store the total no. of items in the array 
  fscanf(fp, "%ld", &val); //first line from file
  *Size = val; //size = val
  //  fseek(fp, 0, SEEK_SET);
  long * array = malloc(sizeof(long) * val); //allocate memory for array 
  int i; //loop control variable for following for loop
  for (i = 0; i < val; i++)
    {
      fscanf(fp, "%ld", &array[i]); //read from file & store in array
    }
  fclose(fp); //close file pointer
  return array;
}

int Save_File(char *Filename, long *Array, int Size)
{
  FILE * fp = fopen(Filename, "w"); //open file for writing
  if (fp == NULL)
    {
      return EXIT_FAILURE; //file not opened
    }
  int i, success = 0;
  for (i = 0; i < Size; i++)
    {
      fprintf(fp, "%ld\n", Array[i]); //write each array element onto file
      success++; //increase total no. of successful writes
    }
  return success;
}

int largest_index(int num, int size)
{
  int q = 0;
  while (power(num, q) <= size)
    {
      q++; //the highest exponent of 3 less than or equal to the size of the array
    }
  q--; //decrease by one since that'll serve as the height of the triangle of the sequence
  return q;
}

void array_create(int q, int * k)
{
  int i, j, p = 0;
  for (i = 0; i <= q; i++)
    {
      for (j = 0; j <= i ; j++)
	{
	  k[p] = power(3, j) * power(2, i - j); //use this formula to calculate the sequence elements 
	  p = p + 1; //increment the value for index
	}
    }
}



void Shell_Insertion_Sort(long *Array, int Size, double *N_Comp, double *N_move)
{
  int q = largest_index(3, Size); //find the largest value for q less than size
  int number = ((q + 1) * (q + 2)) / 2; //total number of elements in sequence array
  int * k = malloc(sizeof(int) * number); //allocate memory for sequence array k[]
  array_create(q, k); //create sequence array k[]
  long i, j, l;
  long temp_r;
  *N_Comp = 0; //initialize to 0
  *N_move = 0; //initialize to 0
  //now implement the shell sort for insertion sort as provided in lecture slides
  for (i = number - 1; i >= 0; i--)
    {
      for (j = k[i]; j < Size; j++)
	{
	  temp_r = Array[j];
	  l = j;
	  while (l >= k[i] && Array[l - k[i]] > temp_r)
	    {
	      *N_Comp = *N_Comp + 2.0; //increment no. of comparisons
	      Array[l] = Array[l - k[i]];
	      *N_move += 1.0 ; //increment moves
	      l = l - k[i];
	    }
	  *N_Comp = *N_Comp + 2.0; //increment no. of comparisons
	  Array[l] = temp_r;
	  *N_move += 1.0; //increment moves
	}
    }
  free(k); //free memory for sequence array
}

void Shell_Selection_Sort(long *Array, int Size, double *N_Comp, double *N_move)
{
  int q = largest_index(3, Size); //find the largest value for q less than size
  int number = ((q + 1) * (q + 2)) / 2; //total number of elements in sequence array
  int * k = malloc(sizeof(int) * number); //allocate memory for sequence array k[]
  array_create(q, k); //create sequence array k[]
  long i, j, l;
  long min;
  long temp;
  *N_Comp = 0; //initialize to 0
  *N_move = 0; //initialize to 0
  //now implement the shell sort for insertion sort
  for (i = number - 1; i >= 0; i--)
    {
      for (j = 0; j < Size - k[i]; j++)
	{
	  min = j;
	  for (l = j + k[i]; l < Size; l = l + k[i])
	    {
	      if (Array[l] < Array[min])
		{
		  *N_Comp = *N_Comp + 1.0; //increment no. of comparisons
		  min = l;
		}
	      *N_Comp = *N_Comp + 1.0; //increment no. of comparisons
	    }
	  if (min != j)
	    {	    
	      *N_Comp = *N_Comp + 1.0;  
	      temp = Array[j];
	      //printf("sdfds\n");
	      Array[j] = Array[min];
	      Array[min] = temp;
	      *N_move = *N_move + 3.0; //increment moves	     
	    }
	  *N_Comp = *N_Comp + 1.0;
	}
    }
  free(k); //free memory for sequence array
}

int Print_Seq(char *Filename, int Size)
{
  FILE * fp = fopen(Filename, "w"); //open file to write
  if (fp == NULL)
    {
      return EXIT_FAILURE; //file not opened
    }
  int q = largest_index(3, Size); //find the largest value for q less than size
  int number = ((q + 1) * (q + 2)) / 2; //total number of elements in sequence array
  int * k = malloc(sizeof(int) * number); //allocate memory for sequence array k[]
  array_create(q, k); //create sequence array k[]
  int i;
  fprintf(fp, "%d\n", number); //print the total no. of elements in the sequence as the first number in the file
  for (i = 0; i < number; i++)
    {
      fprintf(fp, "%d\n", k[i]); //print each element of the sequence into the file
    }
  free(k); //deallocate memory held by sequence array
  fclose(fp); //close the file
  return number;
}
