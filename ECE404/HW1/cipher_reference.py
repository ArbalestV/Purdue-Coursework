import StringIO
import sys
import string

#Start with an infinite loop to accept the names of the plaintext, key and ciphertext files. This infinite while loop basically makes sure that the names of the files are exactly as mentioned
while True:
    i_file = raw_input("Enter the name of the plaintext file: ")
    if i_file != 'input.txt':
        print "Wrong name of plaintext file."
        #sys.exit(1)
    else:
        break
    #print (i_file)
#print('jiu')
#print (i_file)
#f = open(
#hello = "hello world"
#print hello
while True:
    key_file = raw_input("Enter the name of the key file: ")
    if key_file != 'key.txt':
        print "Wrong name of key file."
        #sys.exit(1)
    else: 
        break
        #print (key_file)
while True:
    o_file = raw_input("Enter the name of the output file: ")
    if o_file != 'output.txt':
        print "Wrong name of output file."
        #sys.exit(1)
    else:
        break
        #print (o_file)

#print "outside while"
f_input = open(i_file, 'r')
for line_i in f_input:
    print line_i
f_key = open(key_file, 'r')
for line_k in f_key:
    print line_k

#print "outside"
#print line_i
#print line_k

#print "length of the plaintext: ", len(line_i)
#print "length of the key: ", len(line_k)
alphabet = "abcdefghijklmnopqrstuvwxyz"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#print "size of alphabet: %d" %len(alphabet)
'''
c=alphabet[9]
print "10th element of alphabet: ", c
'''
'''
d=string.lowercase.index('r')
print d
'''
#print len(alphabet)
f_output = open(o_file, 'w')
j = 0
cstr = "" 
#print line_k[34]
ilen = len(line_i) - 1
klen = len(line_k) - 1
#print ilen
#print klen

for i in range(0, (ilen - 1)):
    #print "i = ", i
    if len(line_i) >= len(line_k) :
    #print "general case"
        if i <= (klen - 1):
            j = i
            #print "i: %d  j: %d" %(i, j)
        else:
            j = (i % klen)
            #print "\n"
            #print "i: %d  j: %d" %(i, j)
    else:
        j = i
       
    tmp_i = line_i[i]
    tmp_k = line_k[j]
    if tmp_i.isupper():
        pos_pt = ALPHABET.index(tmp_i)
    else:
        pos_pt = alphabet.index(tmp_i)
    if tmp_k.isupper():
        pos_k = ALPHABET.index(tmp_k)
    else:
        pos_k = alphabet.index(tmp_k)    
            
    #print "input character: ", tmp_i
    #print "input position: ", pos_pt
    #print "output character: ", tmp_k
    #print "key position: ", pos_k
        
    
    ct_pos = pos_pt + pos_k
    
    #print "ciphertext position of letter: ", ct_pos
    if tmp_k.isupper():#if key is lower case cipher text is upper case & vice-versa
        cstr = cstr + alphabet[ct_pos % 26]
    else:
        cstr = cstr + ALPHABET[ct_pos % 26]
    
    #print "cipher text letter corresponding: ", cstr[i]
    #print len(cstr)

#print cstr
f_output.write(cstr)   
f_output.close()
f_key.close()
f_input.close()    
        



