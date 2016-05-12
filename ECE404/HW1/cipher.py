import StringIO
import sys
import string

#Start with three infinite loops to accept the names of the plaintext, key and ciphertext files. These infinite while loop basically makes sure that the names of the files are exactly as mentioned

#check for input file name
while True:
    i_file = raw_input("Enter the name of the plaintext file: ")
    if i_file != 'input.txt':
        print "Wrong name of plaintext file."
    else:
        break
#check for key file name
while True:
    key_file = raw_input("Enter the name of the key file: ")
    if key_file != 'key.txt':
        print "Wrong name of key file."
    else: 
        break
#check for output file name
while True:
    o_file = raw_input("Enter the name of the output file: ")
    if o_file != 'output.txt':
        print "Wrong name of output file."
    else:
        break

#open the input plaintext file for reading and store the plaintext in a string 
f_input = open(i_file, 'r')
for line_i in f_input:
    print line_i

#open the key plaintext file for reading and store the in a string
f_key = open(key_file, 'r')
for line_k in f_key:
    print line_k

#create upper case & lower alphabet strings so we can cross reference position of a specific letter of the alphabet
#we use upper and lower case letters because our plaintext and key letters could be both lower case and upper case
alphabet = "abcdefghijklmnopqrstuvwxyz"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#open the output file for writing
f_output = open(o_file, 'w')
j = 0 #initialize a variable to iterate through the key text length within the loop that iterates through each character of the plaintext
#initialize an empty string to store the cipher text
cstr = "" 

#get length of plaintext 
ilen = len(line_i) - 1
#get length of key
klen = len(line_k) - 1

#now, this for loop is the core of the algorithm.
#Let me explain to you my basis for conversion, especially when dealing with uppercase key text or plaintext letters
#Plaintext Letter      Key Letter     Resulting Cipher Text Letter
#     Lower                Lower             Upper
#     Upper                Lower             Upper
#     Lower                Upper             Lower
#     Upper                Upper             Lower

#for each letter in the plaintext
for i in range(0, (ilen - 1)):
    #basically if the length of the plaintext exceeds that of the key text, then line the key text in a circular manner with the plaintext
    if len(line_i) >= len(line_k) :
    #key text iterator is same as plaintext iterator until plaintext iterator is the last element of the key text length
        if i <= (klen - 1):
            j = i
    #when the plaintext iterator exceeds the langth of the key text, then use the modulo operator to circularly align the keytext to plaintext
        else:
            j = (i % klen)
    #when the key text file is greater than the plaintext file, then simply assign the corresponding elements        
    else:
        j = i
    
    #temporary variable storing current plaintext character  
    tmp_i = line_i[i]
    #temporary variable storing current keyfile character
    tmp_k = line_k[j]

    #find the correct position of the plaintext letter
    if tmp_i.isupper():
        pos_pt = ALPHABET.index(tmp_i)
    else:
        pos_pt = alphabet.index(tmp_i)
    #find the correct position of the keytext letter
    if tmp_k.isupper():
        pos_k = ALPHABET.index(tmp_k)
    else:
        pos_k = alphabet.index(tmp_k)    
            
    #find the correct position of the cipher text letter based on vigenere algorithm
    ct_pos = pos_pt + pos_k
    
    #assign cipher text letter based on position of the letter on the alphabet and its lower/upper caseness based on the case of the key text letter
    if tmp_k.isupper():#if key is lower case cipher text is upper case & vice-versa
        cstr = cstr + alphabet[ct_pos % 26]
    else:
        cstr = cstr + ALPHABET[ct_pos % 26]
    
#output the cipher text string calculated to the output file opened for writing
f_output.write(cstr)   
f_output.close()
f_key.close()
f_input.close()    
        



