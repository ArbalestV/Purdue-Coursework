#!/usr/bin/env/python
import sys
#from BitVector import *
sys.path.append( "/home/shay/a/kalita/ece404/HW2/BitVector-3.0" )
from BitVector import *
import string
'''
#get encryption key from the user
def get_encryption_key(): # key                                                     ## ask user for input
    while True:
        key = raw_input("Enter the 8 character long key: ")
        if len(key) != 8:
            print "Key should be 8 characters in length."
        else:
            break
    ## make sure it satisfies any constraints on the key

    ## next, construct a BitVector from the key    
    user_key_bv = BitVector(textstring = "sherlock")   
    print(user_key_bv)
    key_bv = user_key_bv.permute( initial_permutation )        ## permute() is a BitVector function
    #print key_bv
    return key_bv
'''

#key_bv = get_encryption_key()
#print key_bv 
bv3 = BitVector( textstring = "hello" )
print(bv3)
