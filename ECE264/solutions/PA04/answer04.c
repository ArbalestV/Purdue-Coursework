/*
 * Please fill the functions in this file.
 * You can add additional functions. 
 *
 * Hint: 
 * You can write additonal functions.
 * You can test your functions with your own input file.
 * See details in README or typing command ./pa04 in terminal after make.
 * See output format examples in any of the files in directory expected.
 * 
 * You may create additional arrays if needed.  The maximum size
 * needed is specified by MAXLENGTH in pa04.h.
 */

#include "pa04.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void printPartition(int * part, int length)
{
  int ind;
  for (ind = 0; ind < length - 1; ind++)
    {
      printf("%d + ", part[ind]);
    }
  printf("%d\n", part[length - 1]);
}

void partition(int * part, int ind, int left)
{
  int val;
  if (left == 0)
    {
      printf("= ");
      printPartition(part, ind);
      return;
    }
  
   for (val = 1; val <= left; val++)
     {
        part[ind] = val;
        partition(part, ind + 1, left - val);
     }
}



/*
 * =================================================================
 * This function prints all partitions of a positive integer value
 * For example, if the value is 3:
 *
 * partitionAll 3
 * = 1 + 1 + 1
 * = 1 + 2
 * = 2 + 1
 * = 3
 */


void partitionAll(int value)
{
  printf("partitionAll %d\n", value);
  int * part;
  part = malloc(sizeof(int) * value);
  partition(part, 0, value);
  free(part); 
}
/*
 * =================================================================
 * This function prints the partitions that use increasing values.
 *
 * For example, if value is 5
 * 2 + 3 and
 * 1 + 4 are valid partitions
 *
 * 5 is a valid partition
 * 
 * 1 + 1 + 3 and
 * 2 + 1 + 2 and
 * 3 + 2 are invalid partitions.
 * 
 * The program should generate only valid partitions.  Do not
 * generates invalid partitions and checks validity before printing.
 *
 */


void partitionInc(int * part, int ind, int left)
{
  int val;
  if (left == 0)
    {
      printf("= ");
      printPartition(part, ind);
      return;
    }
  for (val = 1; val <= left; val++)
    {
      if ((ind == 0) || part[ind - 1] < val)
	{
          part[ind] = val;
          partitionInc(part, ind + 1, left  - val);
	}
    }
}    

void partitionIncreasing(int value)
{

  printf("partitionIncreasing %d\n", value);
  int * part;
  part = malloc(sizeof(int) * value);
  partitionInc(part, 0, value);
  free(part);
}

void partitionDec(int * part, int ind, int left)
{
  int val;
  if (left == 0)
    {
      printf("= ");
      printPartition(part, ind);
      return;
    }
  for (val = 1; val <= left; val++)
    {
      if ((ind == 0) || part[ind - 1] > val)
	{
          part[ind] = val;
          partitionDec(part, ind + 1, left  - val);
	}
    }
}    


/*
 * =================================================================
 * This function prints the partitions that use Decreasing values.
 *
 * For example, if value is 5
 * 3 + 2 and
 * 4 + 1 are valid partitions
 *
 * 5 is a valid partition
 * 
 * 1 + 1 + 3 and
 * 2 + 1 + 2 and
 * 2 + 3 are invalid partitions.
 * 
 * The program should generate only valid partitions.  Do not
 * generates invalid partitions and checks validity before printing.
 *
 */


void partitionDecreasing(int value)
{
  printf("partitionDecreasing %d\n", value);
  int * part;
  part = malloc(sizeof(int) * value);
  partitionDec(part, 0, value);
  free(part);
}

void partitionOddNum(int * part, int ind, int left)
{
  int val;
  if (left == 0)
    {
      printf("= ");
      printPartition(part, ind);
      return;
    }
  for (val = 1; val <= left; val++)
    {
      if ((val % 2) == 1)
	{
          part[ind] = val;
          partitionOddNum(part, ind + 1, left  - val);
	}
    }
}    


/*
 * =================================================================
 * This function prints odd number only partitions of a positive integer value
 * For example, if value is 5
 * 1 + 1 + 1 + 1 + 1 and
 * 1 + 3 + 1 are valid partitions
 *
 * 5 is a valid partition
 * 
 * 1 + 1 + 1 + 2 and
 * 2 + 1 + 2 and
 * 2 + 3 are invalid partitions.
 * 
 * The program should generate only valid partitions.  Do not
 * generates invalid partitions and checks validity before printing.
 */


void partitionOdd(int value)
{
   printf("partitionOdd %d\n", value);
   int * part;
   part = malloc(sizeof(int) * value);
   partitionOddNum(part, 0, value);
   free(part);
}

void partitionEvenNum(int * part, int ind, int left)
{
  int val;
  if (left == 0)
    {
      printf("= ");
      printPartition(part, ind);
      return;
    }
  for (val = 1; val <= left; val++)
    {
      if ((val % 2) == 0)
	{
          part[ind] = val;
          partitionEvenNum(part, ind + 1, left  - val);
	}
    }
}    


/*
 * =================================================================
 * This function prints even number only partitions of a positive integer value
 * For example, if value is 8
 * 2 + 2 + 2 + 2and
 * 2 + 4 + 2 are valid partitions
 *
 * 8 is a valid partition
 *
 * 2 + 1 + 1 + 2 + 2and
 * 2 + 1 + 2 + 3and
 * 5 + 3 are invalid partitions.
 *
 * if the value is 5, there will be no result generated
 * 
 * The program should generate only valid partitions.  Do not
 * generates invalid partitions and checks validity before printing.
 */

void partitionEven(int value)
{
   printf("partitionEven %d\n", value);
   int * part;
   part = malloc(sizeof(int) * value);
   partitionEvenNum(part, 0, value);
   free(part);
}

void partitionOddEven(int * part, int ind, int left, int status)
{
  int val;
  if (left == 0)
    {
      printf("= ");
      printPartition(part, ind);
      return;
    }
  /*for (val = 1; val <= left; val++)
    {
      if ((ind == 0) || (((part[ind - 1] % 2) == 0) && ((val%2) == 1)))
	{
          part[ind] = val;
          partitionOddEven(part, ind + 1, left  - val);
	}
      else if((ind == 0) || ((part[ind - 1] % 2) == 1 && (val%2) == 0))
        {
            part[ind] = val;
            partitionOddEven(part, ind + 1, left  - val);
	}
    }*/
  else
    {
      if (status % 2 == 0)
	{
	  status++;
	  for(val = 1; val <= left; val = val + 2)
	    {
              part[ind] = val;
              partitionOddEven(part, ind + 1, left  - val, status);
	    }
	}
      else
	{
	  status++;
	  for(val = 2; val <= left; val = val + 2)
	    {
	      part[ind] = val;
	      partitionOddEven(part, ind + 1, left - val, status);
	    }
	}
    }




}    

/*
 * =================================================================
 * This function prints alternate ood and even number partitions of a positive integer value. Each partition starts from and odd number, even number, ood number again, even number again...etc.
 *
 * For example, if value is 6
 * 1 + 2 + 1 + 2 and
 * 3 + 2 + 1 are valid partitions
 *
 * 6 is not a valid partition
 *
 * 2 + 1 + 1 + 2 and
 * 2 + 1 + 3and
 * 5 + 1 are invalid partitions.
 * 
 * The program should generate only valid partitions.  Do not
 * generates invalid partitions and checks validity before printing.
 */


void partitionOddAndEven(int value)
{
  printf("partitionOddAndEven %d\n", value);
  int * part;
  part = malloc(sizeof(int) * value);
  partitionOddEven(part, 0, value, 0);
  free(part);
}

/*
 * =================================================================
 * This function prints prime number only partitions of a positive integer value
 * For example, if value is 6
 * 2 + 2 + 2 and
 * 3 + 3 are valid partitions
 *
 * 6 is not a valid partition
 * 
 * 2 + 4 and
 * 1 + 5 are invalid partitions.
 * 
 * The program should generate only valid partitions.  Do not
 * generates invalid partitions and checks validity before printing.
 */

int isPrime(int n)
{
  int count = 0;
  int i;
  for(i = 1; i <= n; i++)
    {
      if((n%i) == 0)
	{
	  count++;
	}
    }
  return count;
}

void partitionPrimeCalc(int * part, int ind, int left)
{
  int val;
  if (left == 0)
    {
      printf("= ");
      printPartition(part, ind);
      return;
    }
  for (val = 1; val <= left; val++)
    {
      if (isPrime(val) < 3 && (val!= 1))
	{
          part[ind] = val;
          partitionPrimeCalc(part, ind + 1, left  - val);
	}
    }
}    


void partitionPrime(int value)
{
  printf("partitionPrime %d\n", value);
  int * part;
  part = malloc(sizeof(int) * value);
  partitionPrimeCalc(part, 0, value);
  free(part);
}
