#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
int power(int, int);
long *Load_File(char *, int *);
int Save_File(char *, long *, int);
int largest_index(int, int);
void array_create(int, int *);
void Shell_Insertion_Sort(long *, int, double *, double *);
void Shell_Selection_Sort(long *, int, double *, double *);
int Print_Seq(char *, int);
int main(int argc, char** argv)
{
  if (argc != 5)
    {
      return EXIT_FAILURE;
    }
long * Array; //the array that will store the array from the file
int Size = 0; //initialize size to zero
  int success;
double N_Comp, N_Move; //no. of moves and comparisons
  clock_t t1, t2, t3, t4, t5, t6, to1, t_sort, t_i, t_o;
  t3 = clock();
Array = Load_File(argv[2], &Size); //load a file and read the elements into the array
  t1 = clock();
t_i = t1 - t3; //input time
  Print_Seq(argv[3], Size); //print the triangle sequence to output file
  t6 = clock();
to1 = t6 - t1; //output time for printing sequence
  if (strcmp(argv[1], "i") == 0) //insertion sort
    {
Shell_Insertion_Sort(Array, Size, &N_Comp, &N_Move); //call insertion sort
      t2 = clock();
    }
  else //selection sort
    {
Shell_Selection_Sort(Array, Size, &N_Comp, &N_Move); //call selection sort
      t2 = clock();
    }
t_sort = t2 - t1; //time taken to sort only (either insertion or selection)
  float t_sort_sec = (t_sort / CLOCKS_PER_SEC);
  t4 = clock();
success = Save_File(argv[4], Array, Size); //no. of elements successfully read from the sorted array into the output file
  t5 = clock();
  t_o = t5 - t4;
float t_i_sec = (t_i / CLOCKS_PER_SEC); //input time
float t_o_sec = ((t_o + to1)/ CLOCKS_PER_SEC); //output time
float t_io_sec = t_i_sec + t_o_sec ; //total i/o time
printf("\nNumber of comparisons: %le", N_Comp); //display # of comparisons
printf("\nNumber of moves: %le", N_Move); //display # of moves
printf("\nI/O time: %le", t_io_sec); //display input/output time
printf("\nSorting time: %le\n", t_sort_sec); //display time taken to sort
 free(Array);
 return EXIT_SUCCESS;
}
