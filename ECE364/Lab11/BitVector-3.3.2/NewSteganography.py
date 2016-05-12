#! /usr/bin/env python3.4
#
# $Author:$
# $Date:$
# $HeadURL:$

import os
import math
import sys
import re
#sys.path.append('/home/ecegrid/a/ee364c10/Lab11/BitVector-3.3.2')
import BitVector
from BitVector import *
from PIL import Image
from Steganography import *
import base64
import time

class NewSteganography(Steganography):#the NewSteganography class that inherits from Steganography
    def __init__(self, imagePath, direction='horizontal'):#the constructor
        Steganography.__init__(self, imagePath, direction)#call the base class constructor, since this new class has no new data members
        self.imagePath = imagePath #to store the image path
    
    def checkIfMessageExists(self): #the function to check if the medium ctually contains a message
        #first check if the direction that the message is embedded in is horizontal
        if (self.dir == 'horizontal'): #for horizontal rasterization
            pix = list(self.im.getdata()) #get the list of pixels
            #now, we will check if the first line (the first 39 characters are '<?xml version="1.0" encoding="UTF-8"?>\n')
            first_line = '<?xml version="1.0" encoding="UTF-8"?>\n'#the first line to be compared with this
            st1 = '' #the string of bits that will make the first 39 characters extracted out of the medium
            for i in range(0, 312):
                st1 = st1 + bin(pix[i])[2:].rjust(8, '0')[7] #just get the LSB of each pixel 8 bit representation
            bv_comp = BitVector(bitstring = st1)#get the equivalent bitvector representation
            txt = bv_comp.get_text_from_bitvector()#get the equivalent text from the first 39 characters of the medium
            if (txt != first_line):#if the first line is not matched
                tup = (False, None) #the tuple is now (false, None)
                return tup #return the tuple indicating that the medium has no message
            else: #if the first line is as it is supposed to be
                #now, in this case, the next step will be to find out of the underlying message is a Text, GrayImage, or ColorImage)
                #before we proceed with the code, first of all let us note one important observation that the first 39 characters have been consumed by the statement represented byb first_line variable. The next 15 characters is the string '<message type="', and then this implies that the first (39+15)=54 characters are constant at this point. The 55th characters, however, corresponds to a 'C'(ColorImage), 'G'(GrayImage) or 'T'(Text), an this is what we will exploit to find out the type of image
                st2 = ''#the string of bits holding the byte representation of the 55th character
                for i in range(432, 440): #for the 55th character
                    st2 = st2 + bin(pix[i])[2:].rjust(8, '0')[7] #just get the LSB of each pixel 8 bit representation
                bv_comp2 = BitVector(bitstring = st2)#get the equivalent bitvector representation
                txt2 = bv_comp2.get_text_from_bitvector()#get the equivalent text from the first 39 characters of the medium
                if (txt2 == 'C'): #if C, then ColorImage
                    tup = (True, 'ColorImage') #make the corresponding tuple
                    return tup #return the tuple
                elif (txt2 == 'G'): #if G, then GrayImage
                    tup = (True, 'GrayImage') #make the corresponding tuple
                    return tup #return the tuple
                elif (txt2 == 'T'): #if T, then Text
                    tup = (True, 'Text') #make the corresponding tuple
                    return tup #return the tuple
                else:
                    pass
        else: #if vertical rasterization on the medium
            pixels = self.im.load() #2-D array of pixels of the medium image
            pix = []#to store list of pixels in a vertical rasterization format
            for i in range(self.width): #performing a vertical scanning(L-R,T-B)
                for j in range(self.height):
                    p = pixels[i, j] #get the corresponding pixel
                    pix.append(p) #append the number/pixel gotten into the new pixel list
            #now, we will check if the first line (the first 39 characters are '<?xml version="1.0" encoding="UTF-8"?>\n')
            first_line = '<?xml version="1.0" encoding="UTF-8"?>\n'#the first line to be compared with this
            st1 = '' #the string of bits that will make the first 39 characters extracted out of the medium
            for i in range(0, 312):
                st1 = st1 + bin(pix[i])[2:].rjust(8, '0')[7] #just get the LSB of each pixel 8 bit representation
            bv_comp = BitVector(bitstring = st1)#get the equivalent bitvector representation
            txt = bv_comp.get_text_from_bitvector()#get the equivalent text from the first 39 characters of the medium
            if (txt != first_line):#if the first line is not matched
                tup = (False, None) #the tuple is now (false, None)
                return tup #return the tuple indicating that the medium has no message
            else: #if the first line is as it is supposed to be
                #now, in this case, the next step will be to find out of the underlying message is a Text, GrayImage, or ColorImage)
                #before we proceed with the code, first of all let us note one important observation that the first 39 characters have been consumed by the statement represented byb first_line variable. The next 15 characters is the string '<message type="', and then this implies that the first (39+15)=54 characters are constant at this point. The 55th characters, however, corresponds to a 'C'(ColorImage), 'G'(GrayImage) or 'T'(Text), an this is what we will exploit to find out the type of image
                st2 = ''#the string of bits holding the byte representation of the 55th character
                for i in range(432, 440): #for the 55th character
                    st2 = st2 + bin(pix[i])[2:].rjust(8, '0')[7] #just get the LSB of each pixel 8 bit representation
                bv_comp2 = BitVector(bitstring = st2)#get the equivalent bitvector representation
                txt2 = bv_comp2.get_text_from_bitvector()#get the equivalent text from the first 39 characters of the medium
                if (txt2 == 'C'): #if C, then ColorImage
                    tup = (True, 'ColorImage') #make the corresponding tuple
                    return tup #return the tuple
                elif (txt2 == 'G'): #if G, then GrayImage
                    tup = (True, 'GrayImage') #make the corresponding tuple
                    return tup #return the tuple
                elif (txt2 == 'T'): #if T, then Text
                    tup = (True, 'Text') #make the corresponding tuple
                    return tup #return the tuple
                else:
                    pass
            

    def wipeMedium(self): #the function to erase the message from the medium
        #tup = self.checkIfMessageExists() #call the function to check 
        #if (tup[0] == False):#if no message exists in the medium, then no need to do anything
        #    return #come out of the function
        #else: #if message exists, then set all the LSBs to 0
        pix = list(self.im.getdata())#get the list of pixels making the medium image
        fin_pix = []#to store the new pixel values by setting all the LSB's to 0
        for i in range(0, len(pix)): #for all the pixels
            bv = BitVector(intVal = pix[i], size = 8) #byte representation of each pixel
                #now, change the LSB of each pixel to 0
            bv[7] = 0
            newnum = int(bv) #the new number
            fin_pix.append(newnum) #append the new number into the new list
        tup = tuple #make the tuple to store the width and height of medium
        tup = (int(self.width), int(self.height)) 
        im = Image.new('L', tup) #make a new image with the fin_pix pixel list
        im.putdata(fin_pix)
        im.save(self.imagePath) #store the new image on the current image path

'''           
imagePath = '/home/ecegrid/a/ee364c10/Lab11/G7/nature_sunflower_v.png'
#direction = 'horizontal'
direction = 'vertical'
newstegobj = NewSteganography(imagePath, direction)
#tup = newstegobj.checkIfMessageExists()
#print(tup)
newstegobj.wipeMedium()
'''
          
'''
imagePath2 = imagePath
direction2 = 'horizontal'
#direction2 = 'vertical'
newstegobj2 = NewSteganography(imagePath2, direction2)
tup2 = newstegobj2.checkIfMessageExists()
print(tup2)
#direction3 = 'horizontal'
direction3 = 'vertical'
newstegobj3 = NewSteganography(imagePath2, direction3)
tup3 = newstegobj3.checkIfMessageExists()
print(tup3)            
'''
