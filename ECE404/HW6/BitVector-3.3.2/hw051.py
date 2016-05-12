#!/usr/bin/env/python
import sys,copy
sys.path.append( "/home/shay/a/kalita/ece404/HW4/BitVector-3.3.2" )
from BitVector import *
import string
S = [] #the state vector S for encryption
S_d = [] #the state vector S for decryption
T = [] #the temporary vector T (same for both encryption and decryption)
K = [] #the key vector 
def initialize_S(): #function to initialize the S[] array for encryption
    for i in range(0, 256): #since it is from 0 to 255
        S.append(hex(i).split('x')[1]) #to split the 'x' that comes
        if len(S[i]) == 1:
            S[i] = "0" + S[i]            
        #print S[i]

def initialize_S_d(): #function to initialize the S[] array for decryption
    for i in range(0, 256): #since it is from 0 to 255
        S_d.append(hex(i).split('x')[1]) #to split the 'x' that comes
        if len(S_d[i]) == 1:
            S_d[i] = "0" + S_d[i]            
        #print S[i]

def initialize_T(): #function to initialize the T[] array
    for i in range(0, 256): #since it is from 0 to 255
        T.append(K[i % len(K)]) #make each element of T[] based on repetition of K

def KSA(): #define the Key Scheduling Algorithm for encryption
    j = 0
    for i in range(0, 256):
        #print "i: ", i+1
        #print "S[i] in hex: ", S[i]
        k = int(S[i], 16) #get S[i] in decimal
        #print "S[i]: in decimal ", k
        #print "T[i] in hex: ", T[i]
        l = int(T[i], 16) #get T[i] in decimal
        #print "T[i] in decimal: ", l
        j = (j + k + l) % 256 #randomize j based on the algorithm
        #print "Final j: ", j
        #print "Before swapping: "
        #print "S[i]: ", S[i]
        #print "S[j]: ", S[j]
        #now swap S[i], S[j]
        tmp = S[i]
        S[i] = S[j]
        S[j] = tmp
        #print "After swapping: "
        #print "S[i]: ", S[i]
        #print "S[j]: ", S[j]

def KSA_d(): #define the Key Scheduling Algorithm for decryption
    j = 0
    for i in range(0, 256):
        #print "i: ", i+1
        #print "S[i] in hex: ", S[i]
        k = int(S_d[i], 16) #get S[i] in decimal
        #print "S[i]: in decimal ", k
        #print "T[i] in hex: ", T[i]
        l = int(T[i], 16) #get T[i] in decimal
        #print "T[i] in decimal: ", l
        j = (j + k + l) % 256 #randomize j based on the algorithm
        #print "Final j: ", j
        #print "Before swapping: "
        #print "S[i]: ", S[i]
        #print "S[j]: ", S[j]
        #now swap S[i], S[j]
        tmp = S_d[i]
        S_d[i] = S_d[j]
        S_d[j] = tmp
        #print "After swapping: "
        #print "S[i]: ", S[i]
        #print "S[j]: ", S[j]

def encrypt_pseudo_random(content):
    i = 0
    j = 0
    count = 0
    f_e = open("encrypt_ppm", 'w')
    for c in range(0, len(content)): #for each line in content
        for d in range(0, len(content[c])): #for each character in the content[c]
            i = (i + 1) % 256
            j = (j + int(S[i], 16) ) % 256
            #swap S[i], Sj[j]
            tmp = S[i]
            S[i] = S[j]
            S[j] = tmp
            k = (int(S[i], 16) + int(S[j], 16)) % 256
            temp = (BitVector(hexstring = S[k]) ^ BitVector(textstring = content[c][d])).get_text_from_bitvector()
            #f_e.write((BitVector(hexstring = S[k]) ^ BitVector(textstring = content[c][d])).get_text_from_bitvector())
            f_e.write(temp)
            #print "Character number: ", str(count+1) 
            #print temp
            count = count + 1
    #print f_e.read()
                      

if __name__ == "__main__":
    f = open("Tiger2.ppm", 'r') #open the .ppm file
    header = "" #to extract the header string
    content = "" #to get the image file contents minus the header
    data = copy.deepcopy(list(f)) #get the image file contents
    header = data[:5] #since header will be in lines 1 to 5
    content = data[5:] #since content will be the rest of the lines
    #print header
    tot = 0 #variable storing total number of characters in header
    tot_h = 0 #variable storing total number of characters in content
    '''
    for i in range(0, len(header)):
        tot_h = tot_h + len(header[i])
    for i in range(0, len(content)):
        #print type(content[0][i])
        tot = tot + len(content[i])
    print "Content # of characters: ", tot
    print "Header # of characters: ", tot_h
    '''
    for i in range(0, len(content)):
        #print type(content[0][i])
        tot = tot + len(content[i])
    print "Content # of characters: ", tot
    #now, we will do the initialization of state vector S
    initialize_S() # for encryption
    print S
    initialize_S_d() # for decryption
    print S_d
    #now, we will initialize the vector T on the basis of S
    #first get the 128-bit (16 characters long key)
    key = "" #first initialize key
    while True: #keey looping until the key itself is 8-characters long
        key = raw_input("Enter the 128-bit long key: ")
        if len(key) != 16:
            print "Key should be 16 characters long."
        else: 
            break
    for i in range(0, 16): #now, convert each byte of key to its equivalent hex representation
        bitstr = BitVector(textstring = key[i]) #get the byte
        #print type(bitstr)
        #print bitstr
        K.append(bitstr.get_hex_string_from_bitvector()) #append it to key
        #print type(K[i])
        #print str(i+1) + ":" +  K[i]
    #print key
    initialize_T()
    #print T
    #print len(T)
    #now, we use the T[] vector to produce the initial permutation of S
    KSA() #Key Scheduling Algorithm for encryption
    #now, we will extract each character from the content list and XOR with the pseudorandom sequence
    encrypt_pseudo_random(content) #call for each character and store it in file
    sys.exit()
