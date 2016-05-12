#include "pa07.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * Prints a linked-list "head" into the output fie "out"
 *
 * NOTE: we have given the code for this function
 */
void List_print(FILE * out, Node * head)
{
 while(head != NULL)
	{
	    fprintf(out, "%5d: %6d\n", head -> index, head -> value);
	    head = head -> next;
	}
    printf("\n");
}


/**
 * Please fill in the code below
 */

/**
 * Destroys a linked list.
 * Arguments:
 * head    A pointer pointing to the first element of the linked list.
 *
 * Returns:
 * void
 *
 * Destroys (frees memory for) the whole linked list. 
 * You can either use recursion or a while loop.
 */
void List_destroy(Node * head)
{
  if (head == NULL)
    {
      return;
    }
  else
    {
      List_destroy(head->next);
      free(head);
    }
}

/**
 * Create and initialize a linked list. 
 *
 * Arguments:
 * value     The "value" of the new node
 * index     The "index" of the new node
 *
 * Returns:
 * Returns a newly constructed node. The node can be the head of a
 * linked list.
 * 
 * You should allocate memory in this function. 
 */
Node * List_create(int value, int index)
{
  Node * ln;
  ln = malloc(sizeof(Node));
  ln -> value = value;
  ln -> index = index;
  ln -> next = NULL;
  return ln;
}

/**
 * Build a sparse array from the given indices and values with 
 * specific length.
 *
 * Arguments:
 * value    Array of values
 * index    Array of indices
 * length   Length of the above arrays
 *
 * Returns:
 * A sparse array.
 *
 * If a sparse array node has { value = 1000, index = 2 }, then that means that
 * the index "2" caries the value "1000". This is meant to convey an array of 1000 
 * "2s", but instead of creating 1000 nodes in your linked list, you only create
 * 1 node, and that note conceptually has 1000 "copies" of it. Hence 
 * each node in a sparse array has a "value" in addition to its "index".
 *
 * Note that an index can never carry the value of "0", because this would not make
 * any sense; however, negative values are fine. A negative value may seem odd
 * at first blush; however, this is like substraction, and makes sense for certain
 * cases.
 *
 * You need to insert nodes in ascending order by index.
 * See the notes to "List_insert_ascend"
 */
Node * List_build(int * value, int * index, int length)
{
  Node * head = NULL;
  if (length == 0)
    {
      //Node * head = NULL;
      return head;
    }
  int i;
  /*if ( *index != 0)
    {
      Node * head = List_create(* value, * index); //create the first node
    }*/
  //Node * itr = head;
  for (i = 0; i < length; i++)
    { //if (* (index + i) != 0)
	//	{
	  head = List_insert_ascend(head, * (value + i), * (index + i));
      //	}
    }
  return head;
}


/**
 * Inserting "value" and "index" into the correct location in the 
 * sparse array "head"
 * 
 * Arguments: 
 * head      A pointer pointing to the first element of the linked list.
 * value     The "value" of the value
 * index     The "value" of the index
 *
 * Returns:
 * A sparse array
 *
 * This function inserts the node ["value", "index"] into the sparse
 * array "head", and ensures that the nodes remain in ascending order
 * by their "index".
 *
 * Before and after the call to this function, "head" must be in
 * ASCENDING order by the "index" of each node.
 */
Node * List_insert_ascend(Node * head, int value, int index)
{
  //if (index != 0)
  // {
      Node * node = List_create(value, index);
      if (head == NULL)
	{
	  head = node;
	  return head;
	}
      else if (head -> next == NULL)
	{
	  if (head -> index < index)
	    {
	      head -> next = node;
	      return head;
	    }
	  else if (head -> index > index)
	    {
	      Node * temp = head;
	      head = node;
	      head -> next = temp;
	      return head;
	    }
	  else
	    {
	      free(node);
	      head -> value = head -> value + value;
	      if (head -> value == 0)
		{
		  head = List_delete(head, head -> index);
		  return head;
		}
	    }
	}
      else
	{
	  if (index < head -> index)
	    {
	      Node * temp = head;
	      head = node;
	      head -> next = temp;
	      return head;
	    }
	  else if (index == head -> index)
	    {
	      free(node);
	      head -> value = head -> value + value;
	      if (head -> value == 0)
		{
		  head = List_delete(head, head -> index);
		  return head;
		}
	    }
	  else
	    {
	      Node * itr = head;
	      while (itr -> next != NULL)
		{//printf("\nsughsjkgsfgh");
		  
		  if ((itr -> index < index) && (index < (itr -> next) -> index)) //correct position found
		    {
		      node -> next = (itr -> next); //make node point to where itr was pointing
		      itr -> next = node; //now make itr point to node
		      return head;
		    }
		  else if (index == itr -> index) //if the index is already present, first sum up their values and the final value at that index should be that sum. If the sum come up to be zero, then in that case, delete that node
		    {
		      itr -> value = itr -> value + value;
		      free(node); //the node is no longer required
		      if (itr -> value == 0) //delete the node
			{
			  head = List_delete(head, itr -> index);
			  return head;
			}
		      return head;
		    }
		  else //if the correct spot is not found
		    {
		      itr = itr -> next;
		    }
		} //if it comes out of the while loop, it means that the index passed is larger than any index present in the linked list currently, thus it must be placed at the end
	      if (itr -> index == index)
		{
		  itr -> value = itr -> value + value;
		  free(node);
		  if (itr -> value == 0)
		    {
		      head = List_delete(head, itr -> index);
		      return head;
		    }
		  return head;
		}
	      itr -> next = node; //make the last node point to the newly created node
	    }
	}
      return head;
}
	      //	    }
	  //	}
	      //  }
	      /* else
		 {
		 return NULL;
		 }*/
      //}


/**
 * This function deletes the node with the passed "index"
 * 
 * Arguments: 
 * head      A pointer pointing to the first element of the sparse array.
 * index     The index to be deleted
 *
 * Returns: 
 * A sparse array with the node removed (the one with index)
 */
Node * List_delete(Node * head, int index)
{
  Node * itr = head;
  if (itr == NULL) //empty list, do nothing
    {
      return itr;
    }
  // if the first node is the node to be deleted
  if (itr -> index == index)
    {
      itr = itr -> next;
      free(head);
      return itr;
    }
  //else the node to be deleted is not the first node
  Node * itr2 = itr -> next;
  while ((itr2 != NULL) && ((itr2 -> index) != index))
    {
      /*must check whether itr2 is null before checking q->index*/
      itr = itr -> next;
      itr2 = itr2 -> next;
    }
    if (itr2 != NULL)
      {
	/* find a node whose index is index*/
	itr -> next = itr2 -> next;
	free(itr2);
      }
    return head;
}

/**
 * Copy a list
 *
 * Arguments:
 * head      A pointer pointing to the first element of the sparse array
 *
 * Returns:
 * A copy sparse array
 *
 * This function will copy the sparse array that is passed to it. The
 * copy will be made into new memory. 
 *
 * This is useful, for example, when we want to merge
 * two linked lists together. We can make a copy of one of the linked
 * lists, and then merge the second into the copy. In this way the
 * original copy of the list is not "mutated".
 */
Node * List_copy(Node * head)
{
  if (head == NULL) //if empty list, do nothing
    {
      Node * head2 = NULL;
      return head2;
    }
  Node * head2 = List_create(head -> value, head -> index); //allocate new memory for the head of the new linked list, and its elements should be the same as the elements of head from the first linked list
  Node * p = head2; //as you iterate through the first linked list and copy elemets correspondingly, use p as an iteratative node starting from head2
  head = head -> next;
  while (head != NULL)
    {
      p -> next = List_create(head -> value, head -> index); //create a new node with value taken from the previous linked list at the corresponding position
      p = p -> next;
      head = head -> next;
    }
  return head2;
}


/**
 * Merged two linked list together
 * 
 * Arguments:
 * head1      A pointer pointing to linked list 1
 * head2      A pointer pointing to linked list 2
 *
 * Returns:
 * A merged sparse array
 *
 * This function will merge two linked lists. Before merging, you 
 * should make a copy of "head1" so that you will still have the 
 * original array while modifying (merging) the second linked list. 
 *
 * Please refer to the README file for detailed instructions on how to
 * merge two lists.
 *
 * This function should not modify either "head1" or "head2". You only
 * need to make a clone of "head1".
 */
Node * List_merge(Node * head1, Node * head2)
{
  Node * head1_2 = List_copy(head1); //create the copy of the first sparse array
  //now, merge head1_2 and head2 nodes
  while (head2 != NULL)
    {
      head1_2 = List_insert_ascend(head1_2, head2 -> value, head2 -> index);
      head2 = head2 -> next;
    }
  return head1_2;
}

