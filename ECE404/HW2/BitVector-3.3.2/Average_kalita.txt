#!/usr/bin/env/python
import sys
#from BitVector import *
sys.path.append( "/home/shay/a/kalita/ece404/HW2/BitVector-3.3.2" )
from BitVector import *
import string
from decimal import Decimal


f = open("Average_results.txt",'w')
#now we will first try to find the effect of changing ciphertext and measuring the the effect on the encrypted text
#keyword = "sherlock"
bv_text1 = BitVector(textstring = "jiuisgod")
#print type(bv_text1)
bv_en_text1 = BitVector(bitstring = '0001000101110001100111001101111101110110001111110000110111010110') #plaintext = "jiuisgod"
bv_text2 = BitVector(textstring = "jiuisgog")
bv_en_text2 = BitVector(bitstring = '0001101011110101010011111001100110000101010101101101011101101001') #plaintext = "jiuisgog"
#now we will find the average bit change 
#first calculate the number of bits that are different in the two texts' bits
diff_t = 0
for i in range(0,64):
    if bv_text1[i] != bv_text2[i]:
        diff_t = diff_t + 1 #no of plaintext bits that are different
#second calculate the number of bits that are different in the two encrypted texts' bits
print "No. of bits changed in plaintext: ", diff_t
f.write("For Diffusion - plaintext\n")
f.write("No. of bits changed in plaintext: " + str(diff_t) + "\n")
diff_et = 0
for i in range(0,64):
    if bv_en_text1[i] != bv_en_text2[i]:
        diff_et = diff_et + 1 #no of encrypted bits that are different
print "No. of bits changed in ciphertext: ", diff_et
f.write("No. of bits changed in ciphertext: " + str(diff_et) + "\n")
print "Average of bit change: ", float(float(diff_et)/float(diff_t)) #The average bits changed in the encrypted output per bit changed in the plaintext
f.write("Average of bit change: " + str(float(float(diff_et)/float(diff_t))) + "\n")

#now we will do the same for the key
#we will use the same plaintext = "jiuisgod" but two different keys
#key1 = "sherlock"
#key2 = "sherlocg"
#then we will do the same thing we did for the plaintext above
key1 = BitVector(textstring = "sherlock")
key2 = BitVector(textstring = "sherlocg")
k_en_text1 = BitVector(bitstring = '0001000101110001100111001101111101110110001111110000110111010110') #key = "sherlock"
k_en_text2 = BitVector(bitstring = '0001011001100011000001001011000011100110100100111010010000000011') #key = "sherlocg"
#now we will find the average bit change 
#first calculate the number of bits that are different in the two keys' bits
diff_k = 0
for i in range(0,64):
    if key1[i] != key2[i]:
        diff_k = diff_k + 1 #no of plaintext bits that are different
#second calculate the number of bits that are different in the two encrypted texts' bits
f.write("For Confusion - key\n")
print "No. of bits changed in plaintext: ", diff_k
f.write("No. of bits changed in plaintext: " + str(diff_k) + "\n")
diff_et = 0
for i in range(0,64):
    if k_en_text1[i] != k_en_text2[i]:
        diff_et = diff_et + 1 #no of encrypted bits that are different
print "No. of bits changed in ciphertext: ", diff_et
f.write("No. of bits changed in ciphertext: " + str(diff_et) + "\n")
print "Average of bit change: ", float(float(diff_et)/float(diff_k)) #The average bits changed in the encrypted output per bit changed in the key
f.write("Average of bit change: " + str(float(float(diff_et)/float(diff_k))) + "\n")

#now for the s-boxes
s_text1 = "0101101101001001000000001000001100111000001111100000111100010000"
s_text2 = "0011011011110011100001010101100111001110010110000011101101110100"
s_text_original = "0001000101110001100111001101111101110110001111110000110111010110"
diff_s_1 = 0
for i in range(0,64):
    if s_text1[i] != s_text_original[i]:
        diff_s_1 = diff_s_1 + 1 #no of encrypted bits that are different for sbox1 with the original sbox
f.write("For Diffusion - S-boxes\n")
print "No. of bits changed in from s-box 1 ciphertext: ", diff_s_1
f.write("No. of bits changed in from s-box 1 ciphertext: " + str(diff_s_1) + "\n")
diff_s_2 = 0
for i in range(0,64):
    if s_text2[i] != s_text_original[i]:
        diff_s_2 = diff_s_2 + 1 #no of encrypted bits that are different for sbox1 with the original sbox
print "No. of bits changed in from s-box 2 ciphertext: ", diff_s_2
f.write("No. of bits changed in from s-box 2 ciphertext: " + str(diff_s_2) + "\n")
f.close()
