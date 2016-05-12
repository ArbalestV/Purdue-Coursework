#!/usr/bin/env/python
import sys
#from BitVector import *
sys.path.append( "/home/shay/a/kalita/ece404/HW2/BitVector-3.3.2" )
from BitVector import *
import string

################################   Initial setup  ################################

# Expansion permutation (See Section 3.3.1):
expansion_permutation = [31, 0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 
9, 10, 11, 12, 11, 12, 13, 14, 15, 16, 15, 16, 17, 18, 19, 20, 19, 
20, 21, 22, 23, 24, 23, 24, 25, 26, 27, 28, 27, 28, 29, 30, 31, 0]

# P-Box permutation (the last step of the Feistel function in Figure 4):
p_box_permutation = [15,6,19,20,28,11,27,16,0,14,22,25,4,17,30,9,
1,7,23,13,31,26,2,8,18,12,29,5,21,10,3,24]

# Initial permutation of the key (See Section 3.3.6):
key_permutation_1 = [56,48,40,32,24,16,8,0,57,49,41,33,25,17,9,1,58,
50,42,34,26,18,10,2,59,51,43,35,62,54,46,38,30,22,14,6,61,53,45,37,
29,21,13,5,60,52,44,36,28,20,12,4,27,19,11,3]

# Contraction permutation of the key (See Section 3.3.7):
key_permutation_2 = [13,16,10,23,0,4,2,27,14,5,20,9,22,18,11,3,25,
7,15,6,26,19,12,1,40,51,30,36,46,54,29,39,50,44,32,47,43,48,38,55,
33,52,45,41,49,35,28,31]

# Each integer here is the how much left-circular shift is applied
# to each half of the 56-bit key in each round (See Section 3.3.5):
shifts_key_halvs = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

#declare an array of round keys
round_keys = []

#get encryption key from the user
def get_encryption_key(): # key                                                     ## ask user for input key
    while True:
        key = raw_input("Enter the 8 character long key: ")
        if len(key) != 8:
            print "Key should be 8 characters in length."
        else:
            break
    ## make sure it satisfies any constraints on the key

    ## next, construct a BitVector from the key 
    #print "Size of key: ", len(key)
    user_key_bv = BitVector(textstring = key)  
    key_bv = user_key_bv.permute( key_permutation_1 )        ## permute() is a BitVector function
    return key_bv #this is now the initial 56-bit key for round 1, which will have to be shifted and then contracted permuted to XOR with the right half

#define the round key for each round
def gen_rnd_key(key_bv, i):
    [left_key,right_key] = key_bv.divide_into_two()
    left_key << shifts_key_halvs[i] #left circular shift the left half
    right_key << shifts_key_halvs[i] #left circular shift the left half
    tmp_bv = left_key + right_key #join the left and right left circular shifted halves
    round_keys.append(tmp_bv)

#This part of the code gets the S-Boxes from the s-box-tables.txt file.
#Please note that the s-box-table.txt has been modified for ease of reading into array purposes
with open('s-box-tables.txt') as f:
    arrays = [line.split() for line in f]
s_box = [] #the array of S-Boxes
for i in range(0,32, 4):
    s_box.append([arrays[k] for k in range(i, i+4)]) # S_BOX

#in this function, we generate 32 bits from 48 bits using the S-Boxes
def gen_from_s_box(right_xor, i, j, k):
    #first of all, decide the S-box applicable -> value of i
    #second of all, decide the row & columnof the s_box applicable
    fir = BitVector(intVal = right_xor[j]) #1st bit 
    six = BitVector(intVal = right_xor[k]) #6th bit
    sec = BitVector(intVal = right_xor[j + 1]) #2nd bit
    thr = BitVector(intVal = right_xor[j + 2]) #3rd bit
    fou = BitVector(intVal = right_xor[j + 3]) #4th bit
    fif = BitVector(intVal = right_xor[j + 4]) #5th bit
    row = fir + six #row is the amalgation of first and sixth bits
    col = sec + thr + fou + fif #column is amalgation of 2nd through 5th bits
    #now that we have found the row and the column, for the s_box[i], we will try to find the exact integer to substitute for the corresponding 4 bits
    #print type(s_box[i][int(row)][int(col)])
    val = int(s_box[i][int(row)][int(col)]) # this is the value it needs to be converted to
    temp_bv = BitVector(intVal = val, size = 4) #since each digit should have a 4-bit representation
    return temp_bv
    
key_bv = get_encryption_key() #get the initial 56 bit key 
#now, we will generate the round keys for rounds 1 through 16, wherein we will basically left shift each half of the overall 56 bits of the generated key based on the shift_value
#key_bv bitvector will serve as the base for each of the rounds
for i in range(0,16):
    gen_rnd_key(key_bv, i)
f_e = open("encrypted.txt", 'w')
f_d = open("decrypted.txt", 'w')
#f_i = open("message.txt", 'r')
## ask user for input encryption string of 8 characters in size
while True:
    txt = raw_input("Enter the 8 character long encryption text: ")
    if len(txt) != 8:
        print "Encryption text should be 8 characters in length."
    else:
        break
#print "Size of encryption text: ", len(txt)
i_bv = BitVector(textstring = txt)

[left,right] = i_bv.divide_into_two() #divide the input string bitvector into two 32bit bitvectors

round_val = 0
while round_val != 16: #basically, do the same thing until 16 rounds have passed
    #print "Round: ", round_val + 1
    right_permute = right.permute(expansion_permutation) #perform expansion permutation for the right half
    #now we will do the contraction permutation step for the key to generate 48 bits from 56 bits
    fin_key_bv = round_keys[round_val].permute(key_permutation_2) #perform the contraction permutation for the round key
    right_xor = right_permute ^ fin_key_bv #XOR right and key 48 bits
    #now we will perform the S-table part that generates 32 bits from 48 bits
    j = 0
    k = 5
    tmp_bv = BitVector(size = 32) #this will store the 32-bit temp
    tmp_bv = gen_from_s_box(right_xor, 0, j, k)
    for i in range(1,8):
        tmp_bv = tmp_bv + gen_from_s_box(right_xor, i, j, k)
        j = j + 6
        k = k + 6
        #Now, assign tmp_bv to right_xor
    right_xor = tmp_bv
    #now, after the substitution step is carried out, we have to do the P-box permutation
    p_permute = right_xor.permute(p_box_permutation)
    #now, the only thing left to do is assigning - the left half for the next round is the initial right half, while the right half for the next round is the XOR of the p-box permutation & left half
    rght_tmp = right
    right = left ^ p_permute
    left = rght_tmp
    round_val = round_val + 1

#now, we have finished the 16 rounds of the Fiestal function
print "Encryption Results"
#encrypted text will just be the left+right remaining
encrypted_bv =  right + left #add the final two halves to generate the encrypted text
print "Encrypted Text BitVector: ", encrypted_bv
#print len(encrypted_bv)
#print type(encrypted_bv)
f_e.write("Key: " + "sherlock\n")
f_e.write("Plaintext: jiuisgod\n")
encrypted_text = encrypted_bv.get_text_from_bitvector() #the encrypted text from the corresponding bitvector
print "Encrypted Text: ", encrypted_text
#print type(encrypted_text)
#print len(encrypted_text)
f_e.write("Encrypted Text: " + str(encrypted_text) + "\n")
f_e.write("Encrypted Text BitVector:" + str(encrypted_bv) + "\n")
#now, let's do the decryption function
#it is essentially the reverse of encryption 16 rounds, except for the round keys being reversed, ie instead of 0 to 16, the round keys should be from 16 to 0
round_val = 15
[left_d,right_d] = encrypted_bv.divide_into_two() #divide the input string bitvector into two 32bit bitvectors
print "Decryption Results"
while round_val != -1: #basically, do the same thing until 16 rounds have passed
    #print "Round: ", round_val + 1
    #print "Left: ", left_d
    #print "Right: ", right_d
    right_permute = right_d.permute(expansion_permutation) #perform expansion permutation for the right half
    #now we will do the contraction permutation step for the key to generate 48 bits from 56 bits
    fin_key_bv = round_keys[round_val].permute(key_permutation_2) #perform the contraction permutation for the round key
    right_xor = right_permute ^ fin_key_bv #XOR right and key 48 bits
    #now we will perform the S-table part that generates 32 bits from 48 bits
    j = 0
    k = 5
    tmp_bv = BitVector(size = 32) #this will store the 32-bit temp
    tmp_bv = gen_from_s_box(right_xor, 0, j, k)
    for i in range(1,8):
        tmp_bv = tmp_bv + gen_from_s_box(right_xor, i, j, k)
        j = j + 6
        k = k + 6
        #Now, assign tmp_bv to right_xor
    right_xor = tmp_bv
    #now, after the substitution step is carried out, we have to do the P-box permutation
    p_permute = right_xor.permute(p_box_permutation)
    #now, the only thing left to do is assigning - the left half for the next round is the initial right half, while the right half for the next round is the XOR of the p-box permutation & left half
    rght_tmp = right_d
    right_d = left_d ^ p_permute
    left_d = rght_tmp
    round_val = round_val - 1

decrypted_bv = right_d + left_d #add the final two halves to generate the decrypted text
print "Decrypted Text Bitvector: ", decrypted_bv 
#print len(decrypted_bv)
#print type(decrypted_bv)
decrypted_text = decrypted_bv.get_text_from_bitvector() #the encrypted text from the corresponding bitvector
print "Decrypted Text: ", decrypted_text
#print len(decrypted_text)
f_d.write("Decrypted Text: " + str(decrypted_text) + "\n")
f_d.write("Decrypted Text BitVector:" + str(decrypted_bv) + "\n")
f_e.close()
f_d.close()
