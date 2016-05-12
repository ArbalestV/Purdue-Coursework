#!/usr/bin/python
import sys
import numpy as np
sys.path.append( "/home/shay/a/kalita/ece404/HW4/BitVector-3.3.2" )
from BitVector import *
import string
from PrimeGenerator import *

def solve_pRoot(p,y):
    p = long(p);
    y = long(y);
    # Initial guess for xk
    try:
        xk = long(pow(y,1.0/p));
    except:
        # Necessary for larger value of y
        # Approximate y as 2^a * y0
        y0 = y;
        a = 0;
        while (y0 > sys.float_info.max):
            y0 = y0 >> 1;
            a += 1;
        # log xk = log2 y / p
        # log xk = (a + log2 y0) / p
        xk = long(pow(2.0, ( a + np.log2(float(y0)) )/ p ));

    # Solve for x using Newton's Method
    err_k = pow(xk,p)-y;
    while (abs(err_k) > 1):
        gk = p*pow(xk,p-1);
        err_k = pow(xk,p)-y;
        xk = -err_k/gk + xk;
    return xk


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

def modular_exp(A, B, n): #modular exponentiation
    result = 1
    while (B > 0):
        if (B & 1): #check the lowest bit of B
            result = (result * A) % n
        B = B >> 1 #shift B by one bit to the right
        A = (A * A) % n
    return result

#generate p1, q1
e = 3 #value of e to be used as stated
generator = PrimeGenerator( bits = 128, debug = 0 )
p1 = generator.findPrime() #prime number p
#print "Prime returned: ", p
generator = PrimeGenerator( bits = 128, debug = 0 )
q1 = generator.findPrime() #prime number q
#print "Prime returned: ", q
p1_bv = BitVector(intVal = p1) #bit vector representation of p
#print p_bv
q1_bv = BitVector(intVal = q1) #bit vector representation of q
while (p1_bv[0] != 1 or p1_bv[1] != 1 or q1_bv[0] != 1 or q1_bv[1] != 1 or p1 == q1 or gcd(p1 - 1, e) != 1 or gcd(q1 - 1, e) != 1):
    #print "Regenerating..."
    generator = PrimeGenerator( bits = 128, debug = 0 )
    p1 = generator.findPrime() #prime number p
    generator = PrimeGenerator( bits = 128, debug = 0 )
    q1 = generator.findPrime() #prime number q
    p1_bv = BitVector(intVal = p1) #bit vector representation of p
    q1_bv = BitVector(intVal = q1) #bit vector representation of q

#generate p2, q2
e = 3 #value of e to be used as stated
generator = PrimeGenerator( bits = 128, debug = 0 )
p2 = generator.findPrime() #prime number p
#print "Prime returned: ", p
generator = PrimeGenerator( bits = 128, debug = 0 )
q2 = generator.findPrime() #prime number q
#print "Prime returned: ", q
p2_bv = BitVector(intVal = p2) #bit vector representation of p
#print p_bv
q2_bv = BitVector(intVal = q2) #bit vector representation of q
while (p2_bv[0] != 1 or p2_bv[1] != 1 or q2_bv[0] != 1 or q2_bv[1] != 1 or p2 == q2 or gcd(p2 - 1, e) != 1 or gcd(q2 - 1, e) != 1):
    #print "Regenerating..."
    generator = PrimeGenerator( bits = 128, debug = 0 )
    p2 = generator.findPrime() #prime number p
    generator = PrimeGenerator( bits = 128, debug = 0 )
    q2 = generator.findPrime() #prime number q
    p2_bv = BitVector(intVal = p2) #bit vector representation of p
    q2_bv = BitVector(intVal = q2) #bit vector representation of q

#generate p3, q3
e = 3 #value of e to be used as stated
generator = PrimeGenerator( bits = 128, debug = 0 )
p3 = generator.findPrime() #prime number p
#print "Prime returned: ", p
generator = PrimeGenerator( bits = 128, debug = 0 )
q3 = generator.findPrime() #prime number q
#print "Prime returned: ", q
p3_bv = BitVector(intVal = p3) #bit vector representation of p
#print p_bv
q3_bv = BitVector(intVal = q3) #bit vector representation of q
while (p3_bv[0] != 1 or p3_bv[1] != 1 or q3_bv[0] != 1 or q3_bv[1] != 1 or p3 == q3 or gcd(p3 - 1, e) != 1 or gcd(q3 - 1, e) != 1):
    #print "Regenerating..."
    generator = PrimeGenerator( bits = 128, debug = 0 )
    p3 = generator.findPrime() #prime number p
    generator = PrimeGenerator( bits = 128, debug = 0 )
    q3 = generator.findPrime() #prime number q
    p3_bv = BitVector(intVal = p3) #bit vector representation of p
    q3_bv = BitVector(intVal = q3) #bit vector representation of q
'''
print "p1: ", p1
print "q1: ", q1
print "p2: ", p2
print "q2: ", q2
print "p3: ", p3
print "q3: ", q3
'''
n1 = p1 * q1 #the modulus
n2 = p2 * q2 #the modulus
n3 = p3 * q3 #the modulus
M = n1 * n2 * n3 
pad_bv = BitVector(bitstring = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000') #the left padding of 128 bit zeroes


e1 = [] #for convenience sakes let us make a list storing cipherblocks
e2 = [] #for convenience sakes let us make a list storing cipherblocks
e3 = [] #for convenience sakes let us make a list storing cipherblocks
def RSA_encrypt(block):
    #get the bitvector representation of block - 128 bits
    bv_block = BitVector(textstring = block)
    #print "Size of block bitvector: ", len(bv_block)
    #print bv_block
    #now add the 128-bit zero padding on the left
    bv_block = pad_bv + bv_block
    #print "Size of block bitvector: ", len(bv_block)
    #print "Type of block bitvector: ", type(bv_block)
    #print "int value of block bitvector: ", int(bv_block)
    #print bv_block[0:127]
    #print bv_block
    M = int(bv_block) #get the 256 bit integer value
    #print "M is: ", M
    #now get C for this particular M: C = M^e mod n
    C1 = modular_exp(M, e, n1) #perform modular exponentiation 
    C2 = modular_exp(M, e, n2) #perform modular exponentiation 
    C3 = modular_exp(M, e, n3) #perform modular exponentiation 
    #print "C is: ", C
    C1_bv = BitVector(intVal = C1, size = 256) #get the bitvector of C
    C2_bv = BitVector(intVal = C2, size = 256) #get the bitvector of C
    C3_bv = BitVector(intVal = C3, size = 256) #get the bitvector of C
    #print "length of C bv: ", len(C_bv)
    #print C_bv
    C1_hex = C1_bv.get_hex_string_from_bitvector() #C in hex form
    C2_hex = C2_bv.get_hex_string_from_bitvector() #C in hex form
    C3_hex = C3_bv.get_hex_string_from_bitvector() #C in hex form
    #print "C in hex: ", C_hex
    #print "Length of C_hex: ", len(C_hex)
    #print "type of C in hex: ", type(C_hex)
    e1.append(C1_hex)
    e2.append(C2_hex)
    e3.append(C3_hex)
    

pt_fh = open(sys.argv[1], 'r') #plain text file open
plntxt = pt_fh.read() #read the text from the and store it in a variable
pt_fh.close() #close the input file file handler
tot_len = len(plntxt) #total length of plaintext
plntxt = plntxt + '\n' #append a newline character
tot_len = len(plntxt) #160 characters
#now we will break down the block into 16 characters at a time (128 bits) as an RSA block 
tot_iter = tot_len / 16 #total number of times it needs to be iterated
cur_iter = 0 #current iteration number
while cur_iter != tot_iter:
    block = plntxt[cur_iter * 16: (cur_iter * 16) + 16]
    RSA_encrypt(block) #encrypt the block
    cur_iter = cur_iter + 1 #increment the counter by 1 to get the next block

#print "now printing the three encrypted texts..."
#print len(e1)
#print len(e2)
#print len(e3[5])

#now, let us generate the decrypted text using CRT
#make ci's and Mi's
Mi = []
m1 = (n2 * n3)
#print "m1: ", m1
m2 = (n1 * n3)
#print "m2: ", m2
m3 = (n1 * n2)
#print "m3: ", m3
Mi.append(m1)
Mi.append(m2)
Mi.append(m3)
#print Mi
c = []
c_1 = Mi[0] * int((BitVector(intVal = Mi[0]).multiplicative_inverse(BitVector(intVal = n1))))
#print "c1: ",c_1
c_2 = Mi[1] * int((BitVector(intVal = Mi[1]).multiplicative_inverse(BitVector(intVal = n2))))
#print "c2: ",c_2
c_3 = Mi[2] * int((BitVector(intVal = Mi[2]).multiplicative_inverse(BitVector(intVal = n3))))
#print "c3: ",c_3
c.append(c_1)
c.append(c_2)
c.append(c_3)
out_fh = open(sys.argv[2], 'w')
for i in range(0, len(e1)): #for all the ciphertext blocks(0 to 10 in this case)
    #generate a1, a2, a3, which are just int values of c1, c2, c3
    c1_bitvec =  BitVector(hexstring = e1[i]) #get bitvector representation
    c2_bitvec =  BitVector(hexstring = e2[i]) #get bitvector representation
    c3_bitvec =  BitVector(hexstring = e3[i]) #get bitvector representation
    c1_int = int(c1_bitvec)
    c2_int = int(c2_bitvec)
    c3_int = int(c3_bitvec)
    a1 = c1_int
    a2 = c2_int
    a3 = c3_int
    #print "i: ", i+1
    #print "a1: ",  a1
    #print "a2: ", a2
    #print "a3: ", a3
    tot = (a1 * c[0]) + (a2 * c[1]) + (a3 * c[2])
    M_cube = tot % M
    M = solve_pRoot(3, M_cube)
    #print "M: ", M
    M_bv = BitVector(intVal = M, size = 128)
    #print len(M_bv)
    string = M_bv.get_text_from_bitvector()
    #print string
    out_fh.write(string)
    
    
