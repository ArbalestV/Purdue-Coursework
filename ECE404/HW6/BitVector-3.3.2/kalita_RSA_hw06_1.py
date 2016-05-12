#!/usr/bin/python
import sys
sys.path.append( "/home/shay/a/kalita/ece404/HW4/BitVector-3.3.2" )
from BitVector import *
import string
from PrimeGenerator import *

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
            
e = 65537 #value of e to be used as stated
generator = PrimeGenerator( bits = 128, debug = 0 )
p = generator.findPrime() #prime number p
#print "Prime returned: ", p
generator = PrimeGenerator( bits = 128, debug = 0 )
q = generator.findPrime() #prime number q
#print "Prime returned: ", q
p_bv = BitVector(intVal = p) #bit vector representation of p
#print p_bv
q_bv = BitVector(intVal = q) #bit vector representation of q
#print q_bv
#print "GCD.."
#print gcd(p-1,e)
#print gcd(q-1,e)
#now we check if p and q satisfy the conditions. If not, keep generating them.
while (p_bv[0] != 1 or p_bv[1] != 1 or q_bv[0] != 1 or q_bv[1] != 1 or p == q or gcd(p - 1, e) != 1 or gcd(q - 1, e) != 1):
    print "Regenerating..."
    generator = PrimeGenerator( bits = 128, debug = 0 )
    p = generator.findPrime() #prime number p
    generator = PrimeGenerator( bits = 128, debug = 0 )
    q = generator.findPrime() #prime number q
    p_bv = BitVector(intVal = p) #bit vector representation of p
    q_bv = BitVector(intVal = q) #bit vector representation of q
#let us now find the MI of d in modulus = (p-1) * (q-1)
totient = (p - 1) * (q - 1) #the totient of n
n = p * q #the modulus
#print totient
bv_totient = BitVector(intVal = totient) #bitvector of totient
#print len(bv_totient)
bv_e = BitVector(intVal = e) #bitvector of e
#print len(bv_e)
bv_d = bv_e.multiplicative_inverse(bv_totient) #find bitvector of d
#print len(bv_d)
d = int(bv_d) #convert to integer for d
#print "integer d: ", d
#print type(d)
#print type(e)
pad_bv = BitVector(bitstring = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000') #the left padding of 128 bit zeroes
#print "Length of pad_bv: ", len(pad_bv)
#print "Type of pad_bv: ", type(pad_bv)
#print "int value of pad_bv: ", int(pad_bv)


def RSA_encrypt(block, et_fh):
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
    C = modular_exp(M, e, n) #perform modular exponentiation 
    #print "C is: ", C
    C_bv = BitVector(intVal = C, size = 256) #get the bitvector of C
    #print "length of C bv: ", len(C_bv)
    #print C_bv
    '''
    rem = len(C_bv) % 4 #check the number of bits C's is not a multiple of 4 by
    if rem == 1: #exceeds by 1 then add 3 0's
        #print "Remainder: ", rem
        C_bv = BitVector(bitstring = '000') + C_bv
        #print "C_bv length now: ", len(C_bv)
        C_hex = C_bv.get_hex_string_from_bitvector() #C in hex form
    elif rem == 2: #exceeds by 2 then add 2 0's
        #print "Remainder: ", rem
        C_bv = BitVector(bitstring = '00') + C_bv
        #print "C_bv length now: ", len(C_bv)
        C_hex = C_bv.get_hex_string_from_bitvector() #C in hex form
    elif rem == 3: #exceeds by 3 then add 1 0's
        #print "Remainder: ", rem
        C_bv = BitVector(bitstring = '0') + C_bv
        #print "C_bv length now: ", len(C_bv)
        C_hex = C_bv.get_hex_string_from_bitvector() #C in hex form
    else:
        #print "Remainder: ", rem
        #print "C_bv length now: ", len(C_bv)
        C_hex = C_bv.get_hex_string_from_bitvector() #C in hex form
    '''
    C_hex = C_bv.get_hex_string_from_bitvector() #C in hex form
    #print "C in hex: ", C_hex
    #print "Length of C_hex: ", len(C_hex)
    #print "type of C in hex: ", type(C_hex)
    #now write to output.txt file
    et_fh.write(C_hex)

def CRT_mod_exp(C, d, n):#function to find the modular exponention using CRT
    Vp = modular_exp(C, d, p)
    Vq = modular_exp(C, d, q)
    Xp = q * int((BitVector(intVal = q).multiplicative_inverse(BitVector(intVal = p))))
    Xq = p * int((BitVector(intVal = p).multiplicative_inverse(BitVector(intVal = q))))
    var = (Vp * Xp) + (Vq * Xq)
    M = var % n
    return M
    
def RSA_decrypt(block, f_d): #decryption in RSA function
    #block is a string of 64 characters in hex format. convert it to int
    C_bv = BitVector(hexstring = block) #get bitvector representation of C
    #print "C in bitvector: ", C_bv
    #print "length of C_bv: ", len(C_bv)
    #now get the int value of C
    C = int(C_bv)
    #print "C: ", C
    #now call M = C^d mod n, but do it using CRT
    M = CRT_mod_exp(C, d, n)
    #print "M: ", M
    M_bv = BitVector(intVal = M, size = 128) #get bitvector representation of M
    #print "Length of M in decrypted: ", len(M_bv)
    #D_bv = M_bv[128:256]
    string = M_bv.get_text_from_bitvector() #get the string from M's bitvector
    f_d.write(string) #append the string to decrypted.txt file

#for arg in sys.argv:
#    print arg

print len(sys.argv)
if len(sys.argv) != 4:
    print "Exiting! Exactly 4 arguments required."
    sys.exit()

else: #
    if sys.argv[1] == '-e': #encryption
        pt_fh = open(sys.argv[2], 'r') #plain text file open
        plntxt = pt_fh.read() #read the text from the and store it in a variable
        pt_fh.close() #close the input file file handler
        tot_len = len(plntxt) #total length of plaintext
        #append a newline to the plntxt since 1 short of 128 bits(16 characters) multiple
        plntxt = plntxt + '\n' #append a newline character
        tot_len = len(plntxt) #160 characters
        #now we will break down the block into 16 characters at a time (128 bits) as an RSA block 
        tot_iter = tot_len / 16 #total number of times it needs to be iterated
        cur_iter = 0 #current iteration number
        #print "Length of p bitvector: ", len(p_bv)
        #print "Length of q bitvector: ", len(q_bv)
        et_fh = open(sys.argv[3], 'w') #output file for encrypted output
        while cur_iter != tot_iter:
            block = plntxt[cur_iter * 16: (cur_iter * 16) + 16] #current block in RSA 
            #print len(block)
            #print "Count: ", cur_iter + 1
            #print block
            RSA_encrypt(block, et_fh) #encrypt the block
            cur_iter = cur_iter + 1 #increment the counter by 1 to get the next block
        #here, we can close the encrypted file handler et_fh
        et_fh.close()
    else: #decryption
        #now begin decryption
        #print sys.argv[2]
        pt_fh = open(sys.argv[2], 'r') #encrypted text file open
        plntxt = pt_fh.read() #the encrypted file contents
        print plntxt
        pt_fh.close() #close the encrypted file handler
        #print "length of encrypted file content: ", len(plntxt)
        #we know that there are 640 characters with each slice being 64 characters in length. 
        tot_len = len(plntxt) #640 characters
        tot_iter = tot_len / 64 #total number of times it needs to be iterated
        cur_iter = 0 #current iteration number
        #print "Decrypting now..."
        f_d = open(sys.argv[3], 'w') #output file for storing decrypted text
        while cur_iter != tot_iter:
            block = plntxt[cur_iter * 64: (cur_iter * 64) + 64] #current block decrypt 
            #print len(block)
            #print "Count: ", cur_iter + 1
            #print block
            RSA_decrypt(block, f_d) #decrypt the block
            cur_iter = cur_iter + 1
        f_d.close() #close the decrypted file handler
