#!/usr/bin/python
import StringIO
import sys
import string

#Euclid's Binary GCD algorithm defined here
def gcd(a,n):
    if n > a: #if the RHS argument is greater than LHS argument, then flip the arguments
        return gcd(n,a);
    else:
        if n == 0: # if the RHS argument is zero, then return the LHS number
            return a;
        elif n == a: #if both numbers are equal then return the number
            return a;
        else:
            return gcd(n, (a%n)); #otherwise gcd(a,n)=gcd(n,(a%n)) -> recursive implementation
        

#accept an integer and keep looping until the number is less than 50
while True:
    n = int(input("Enter an integer smaller than 50: "))
    if n >= 50:
        print "Number should be less than 50." #User output statement to get the correct integer
    else:
        break

#create a file to store the output for the particular number
name_file = str(n)+".txt" #for each number that the user enters create a text output file that will either contain if it is a ring or a field
#print name_file
f_output = open(name_file, 'w') #file output handler
#check if Zn is a field
#create a for loop from 2 to (n-1), and check if for any of these integers the gcb(a, n) is not 1. The moment it is not 1, we can directly say that it is a ring, otherwise at the end of the loop iteration it is a field
for i in range(2, n):
    #print i
    if (gcd(i,n) != 1 ): #if the gcd is not 1, break immediately and also exit the program with the appropriate file output
        f_output.write("Ring")
        sys.exit()
    else:
        continue #keep looping until the end of the loop

f_output.write("Field") #if we reach this point, then we know its a field
f_output.close() #close the file handler
