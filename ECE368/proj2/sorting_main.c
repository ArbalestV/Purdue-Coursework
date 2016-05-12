#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

typedef struct _node { //define structure
  long value; //store integer
  struct _node *next; //point to the next node
} Node;

typedef struct _list { //define doubly linked list
  Node * int_node; //point to a node that stores the actual integers
  struct _list *prev; //previous node
  struct _list *next; //next node
} List;


int power(int, int);
Node * List_create(int);
Node * Node_Insert(Node *, int);
Node * Load_File(char *);
int Save_File(char *, Node *);
int largest_index(int, int);
long findSize(Node *);
Node * Shell_Sort(Node *);
List * List_D_create(int);
List * List_Insert(List *, Node *);
void Insertion_Sort(List *);

int main(int argc, char** argv)
{
  if (argc != 3)
    {
      printf("\nERROR.");
      return EXIT_FAILURE;
    }
  Node * head; //the linked list that will store the array from the file
  clock_t t1, t2, t3, t4, t5, t6, t_sort, t_i, t_o;
  t3 = clock();
  head = Load_File(argv[1]); //load a file
  t1 = clock();
  t_i = t1 - t3; //input time

  t6 = clock();
  head = Shell_Sort(head); //call insertion sort
  t2 = clock();
  t_sort = t2 - t6; //sorting time
  float t_sort_sec = (t_sort / CLOCKS_PER_SEC);
  t4 = clock();
  int success = Save_File(argv[2], head); //no. of elements successfully read from the sorted array into the output file
  if (success <= 0)
    {
      printf("\nERRORhere.\n");
      return EXIT_FAILURE;
    }
  t5 = clock();
  t_o = t5 - t4;
  float t_i_sec = (t_i / CLOCKS_PER_SEC); //input time
  float t_o_sec = (t_o / CLOCKS_PER_SEC); //output time
  float t_io_sec = t_i_sec + t_o_sec ; //total i/o time
  printf("\nI/O time: %le", t_io_sec); //display input/output time
  printf("\nSorting time: %le\n", t_sort_sec); //display time taken to sort  
  while (head != NULL)
    {   
      Node * tmp = head;
      head = head -> next;
      free(tmp);
    }
  return EXIT_SUCCESS;
}
