#include "pa10.h"
#include "tree.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TRUE 1
#define FALSE 0

/**
 * Returns a pointer to a new empty stack.
 */
Stack * Stack_create()
{
  Stack * head = malloc(sizeof(Stack));
  head -> list = NULL;
  return head;
}

/**
 * Frees all memory associated with the stack. 
 * Don't forget that you _must_ free the entire contained linked-list.
 * Also, you must safely to _nothing_ if stack == NULL. 
 */
void Stack_destroy(Stack * stack)
{
  if (stack == NULL)
    {
      return;
    }
  ListNode * tmp;
  while (stack -> list != NULL)
    {
      tmp = stack -> list;
      stack -> list = stack -> list -> next;
      free(tmp);
    }
  // free(stack -> list);
  free(stack);
}

/**
 * Returns TRUE (something other than zero) if the stack is empty.
 */
int Stack_isEmpty(Stack * stack)
{
  if (stack -> list == NULL)
    {
      return TRUE;
    }
  else
    {
      return FALSE;
    }
}

/**
 * Pop the front 'value' from the stack.
 *
 * More precisely, this function must do two things:
 * (1) Return the value of the head node of the stack's list
 * (2) Remove the head node of the stack's list, freeing it.
 */
int Stack_pop(Stack * stack)
{
  ListNode * p = stack -> list;
  stack -> list = stack -> list -> next;
  int value;
  value = p -> value;
  free(p);
  return value;
}

/**
 * Push an 'value' onto the front of the stack.
 *
 * More precisely, this function must:
 * (1) Create a new ListNode with 'value' for it's value.
 * (2) Push that new ListNode onto the front of the stack's list.
 */
void Stack_push(Stack * stack, int value)
{
  ListNode * p = malloc(sizeof(ListNode));
  p -> value = value;
  if( stack->list != NULL)
    {
      p -> next = stack -> list -> next;
    }
  else
    {
      p->next = NULL ;
    }
  stack -> list = p;
}

/**
 * Sort 'array' of length 'len' using Donald Knuth's "StackSort"
 *
 * To do this, you must implement the following pseudo-code:
 * (1) Maintain a 'write_index'. This is where you'll write values to
 *     as you sort them. It starts off as zero.
 * (2) Initialize an empty stack
 * (3) For each input value 'x':
 *     (3.a) While the stack is nonempty and 'x' is larger than the 
 *           front 'value' on the stack, pop 'value' and:
 *           (3.a.i) Write 'value' to array[write_index], and 
 *                   increment write_index.
 *     (3.b) Push x onto the stack.
 * (4) While the stack is nonempty, pop the front 'value' and follow
 *     step (3.a.i).
 *
 * The output should be a sorted array if, and only if, the array
 * is stack-sortable. You can find files full of stack-sortable and
 * stack-unsortable arrays in the 'expected' folder.
 */
void stackSort(int * array, int len)
{
  int w_ind = 0;
  int * arr = malloc(sizeof(int) * len); 
  Stack * stack = Stack_create();
  int arr_ind = 0;
  for (arr_ind = 0; arr_ind < len; arr_ind++)
    {
      while ( !(Stack_isEmpty(stack)) && (array[arr_ind] > (stack -> list -> value)) )
	{
	  arr[w_ind++] = Stack_pop(stack);
	  //printf("\narray = %d",array[w_ind]);
	}
       
      Stack_push(stack, array[arr_ind]);
   
    }
  while (!Stack_isEmpty(stack))
    {
      arr[w_ind++] = Stack_pop(stack);
    }
  Stack_destroy(stack);	
  memcpy(array, arr, sizeof(int) * len);
  free(arr);
}


 int max(int * arr, int len)
 {
   int maxn = arr[0];
   int i;
   for (i = 0; i < len; i++)
     {
       if (*(arr + i) > maxn)
	 {
	   maxn = *(arr + i);
	 }
     }
   return maxn;
 }

 int min(int * arr, int len)
 {
   int minn = arr[0];
   int i;
   for (i = 0; i < len; i++)
     {
       if (*(arr + i) < minn)
	 {
	   minn = *(arr + i);
	 }
     }
   return minn;
 }



/**
 * Return TRUE (1) if the 'array' of length 'len' is stack-sortable.
 *
 * To do this you must:
 * (1) If 'len' is less than 3, return TRUE.
 * (2) Find the maximum value in 'array'.
 * (3) Partition array into two parts: left of max, and right of max.
 * (4) The maximum value in left must be smaller than the minimum
 *     value in right. (Otherwise return FALSE.)
 * (5) Return TRUE if both left and right are stack-sortable.
 *
 * The 'expected' directory contains files for all sortable and 
 * unsortable sequences of length len. You must return TRUE for every
 * sequence in the sortable files, and you must return FALSE for every
 * sequence in the unsortable files.
 */
int isStackSortable(int * array, int len)
{
  if (len < 3)
    {
      return TRUE;
    }
  int max_n = 0;
  int i, max_ind;
  for (i = 0; i < len; i++)
    {
      if (array[i] > max_n)
	{
	  max_n = array[i];
	  max_ind = i;
	}
    }
  //printf("\n maxindex = %d",max_ind);
  if ((max_ind == 0) || (max_ind == (len - 1)))
    {
      if (max_ind == 0)
	{
	  int * arr_right = malloc(sizeof(int) * (len - 1));
	  memcpy(arr_right, array + 1, (len - 1) * sizeof(int));
	  if (isStackSortable(arr_right, (len - 1)) == TRUE)
	    {
	      free(arr_right);
	      return TRUE;
	    }
	  else
	    {
	      free(arr_right);
	      return FALSE;
	    }
	}
      else
	{
	  int * arr_left = malloc(sizeof(int) * (len - 1));
	  memcpy(arr_left, array, (len - 1) * sizeof(int));
	  if (isStackSortable(arr_left, (len - 1)) == TRUE)
	    {
	      free(arr_left);
	      return TRUE;
	    }
	  else
	    {
	      free(arr_left);
	      return FALSE;
	    }
	}
    }
  else
    {			    
      int * arr_left = malloc(sizeof(int) * (max_ind));
      int * arr_right = malloc(sizeof(int) * (len - (max_ind + 1)));
      memcpy(arr_left, array, max_ind * sizeof(int));
      memcpy(arr_right, array + (max_ind + 1), (len - (max_ind + 1)) * sizeof(int));
      //printf("\nrightmin = %d",max(arr_left, max_ind));
      //printf("\nleftmax = %d",min(arr_right, (len - (max_ind + 1))));
      if (max(arr_left, max_ind) > min(arr_right, (len - (max_ind + 1))))
	{
	  free(arr_left);
	  free(arr_right);
	  return FALSE;
	}
      
      if ((isStackSortable(arr_left, max_ind) == TRUE) && (isStackSortable(arr_right, (len - (max_ind + 1))) == TRUE))
	{
	  free(arr_left);
	  free(arr_right);
	  return TRUE;
	}
      else
	{
	  free(arr_left);
	  free(arr_right);
	  return FALSE;
	}
    }
}

void swap(int * a, int * b)
{
  int tmp = *a;
  *a = *b;
  *b = tmp;
}


void permute(int * arr, int len, int ind)
{
  TreeNode * root = NULL;
  if (ind == len)
    {
      if((isStackSortable(arr, len)))
	{
	  root = Tree_build(arr, len);
	  Tree_printShape(root);
	  Tree_destroy(root);
	}
      return;
    }
  int i;
  for(i = ind; i < len; i++)
    {
      swap(&arr[i], &arr[ind]);
      permute(arr, len, ind + 1);
      swap(&arr[i], &arr[ind]);
    }
}

 


/**
 * Generates (and prints) all the unique binary tree shapes of size k
 *
 * To do this, you must:
 * (1) Create an array with the elements [0..k-1] inclusive.
 * (2) Find all the permutations of this array.
 * (3) In the base-case of your permute function, you must test if the
 *     permutation is "stack-sortable"
 * (4) If the permutation is "stack-sortable", then build a binary
 *     tree, and print it using the "Tree_printShape(...)" function.
 *
 * Your genShapes() function must NOT produce duplicate tree shapes.
 * The correct outputs for sizes [1..9] are in the 'expected' 
 * directory.
 */
void genShapes(int k)
{
  int * arr = malloc(sizeof(int) * k);
  int ind;
  for (ind = 0; ind < k; ind ++)
    {
      arr[ind] = ind;
    }
  permute(arr, k, 0);
  free(arr);
}




