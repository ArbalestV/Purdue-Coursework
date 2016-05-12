#include <stdlib.h>
#include <stdio.h>
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

Node * List_create(int value) //create the linked list individual nodes
{
  Node * ln;;
  ln = malloc(sizeof(Node));
  ln -> value = value; 
  ln -> next = NULL;
  return ln;
}

List * List_D_create(Node * node) //create the linked list containing the nodes
{
  List * dll = malloc(sizeof(List));
  dll -> int_node = node; //make the node point to the node being inserted
  dll -> prev = NULL;
  dll -> next = NULL;
  return dll;
}

int power(int num, int n) //power function to calculate the nth power of an integer
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

Node * Node_Insert(Node * head, int val) //function to insert a node in the linked list containing integers
{
  if (head == NULL)
    {
      head = List_create(val); //if head is head, then make it the first element
     }
  else
    {
      Node * cur = head;
      while (cur -> next != NULL)
	{
	  cur = cur -> next; //find the correct position
	}
      cur -> next = List_create(val); //create the node at the rear end
    }  
  return head;
}

List * List_Insert(List * dhead, Node * node) //function to insert a linked list node
{
  if (dhead == NULL)
    {
      dhead = List_D_create(node); //make it the first element
    }
  else
    {
      List * cur_d = dhead;
      while (cur_d -> next != NULL)
	{
	  cur_d = cur_d -> next; //find the correct position
	}
      cur_d -> next = List_D_create(node); //create the node at the rear end
      (cur_d -> next) -> prev = cur_d;
    }
  return dhead;
}

Node *Load_File(char *Filename)
{
  FILE * fp = fopen(Filename, "r"); //open file to read
  if (fp == NULL)
    {
      return NULL; //file not opened case
    }
  Node * head = NULL; 
  long val; //individual values
  while (fscanf(fp, "%ld", &val) == 1) //read reading an integer from file
    {
      head = Node_Insert(head, val); //insert the value read from the file into the linked list at the rear end and also increment size
    }
  fclose(fp); //close file pointer
  return head; //return the linked list pointed to by head
}

int Save_File(char *Filename, Node *list)
{
  FILE * fp = fopen(Filename, "w"); //open file for writing
  if (fp == NULL)
    {
      return EXIT_FAILURE; //file not opened
    }
  int success = 0;
  Node * cur = list; //since list points to head
  while (cur != NULL)
    {
      fprintf(fp, "%ld\n", cur -> value); //write each list element onto file
      success++; //increase total no. of successful writes
      cur = cur -> next; //now point to the next node in the linked list
    }
  return success; //return no. of successful writes into the file from linked list
}

int largest_index(int num, int size) //find the largest index of 3 less than or equal to size of integers read
{
  int q = 0;
  while (power(num, q) <= size) //as long as it is less than size or equal to size
    {
      q++; //the highest exponent of 3 less than or equal to the size of the array
    }
  q--; //decrease by one since that'll serve as the height of the triangle of the sequence
  return q; //return the index to create the array sequence from
}

long findSize(Node * list)
{
  long size = 0; //size variable
  while (list != NULL)
    {
      size++; //increment size by 1
      list = list -> next; //iterate until you reach the end of the linked list
    }
  return size; //return the size of the integer list
}

void Insertion_Sort(List * dhead)
{
  List * j = dhead -> next;
  long temp_r;
  while (j != NULL) //implement insertion sort for gaps of 1 using the notes from lecture
    {
      List * i = j;
      temp_r = j -> int_node -> value; //set the current jth node as being the lowest
      while (i -> prev != NULL)
	{
	  if ((i -> prev -> int_node -> value) > temp_r)
	    {
	      i -> int_node -> value = i -> prev -> int_node -> value; //keep pushing the larger elements to right
	    }
	  else
	    {
	      break;
	    }
	  i = i -> prev; //keep decrementing i
	}
      //printf("\n%ld\n", i->int_node->value);
      i -> int_node -> value = temp_r; //insert the smaller elements into the correct positions
      j = j -> next; //keep incrementing j
    }
}

Node * Shell_Sort(Node *list)
{

  long Size; //store the size of the integer list
  Size = findSize(list); //find the size
  int q = largest_index(3, Size); //find the largest value for q less than size
  long j, l;
  int count1;
  Node * head = list;
  int pow1, pow2, k;
  
  for (pow1 = q; pow1 >= 0; pow1--)
    {
      for (pow2 = pow1; pow2 >= 0 ; pow2--)
	{
	  Node * cur = head;
	  k = power(3, pow2) * power(2, pow1 - pow2); //use this formula to calculate the sequence elements
	  for (j = 1; j <= (Size - k); j++)
	    {
	      List * dhead = NULL;
	      dhead = List_Insert(dhead, cur);	//insert starting from the first j'th value
	      Node * tmp1 = cur;     
	      for (l = j + k; l <= Size; l = l + k)
		{ //printf("\nj+k=%ld\n", l);
		  count1 = 0;   
		  while (count1 != k)
		    {  
		      tmp1 = tmp1 -> next; //keep on iterating till you reach the correct node
		      count1++;
		    }
		  dhead = List_Insert(dhead, tmp1); //insert node into the sublist
		}
	      Insertion_Sort(dhead); //implement insertion sort
	      cur = cur -> next; //make current as the next node
	      while (dhead != NULL) //free memory due to each sublist before the next iteration
		{
		  List * tmp = dhead;
		  dhead = dhead -> next;
		  free(tmp);
		}	      
	    }	  
	}
    }
  return head; //return the list of integers that has been sorted
}
	
	 
