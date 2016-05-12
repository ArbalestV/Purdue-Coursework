#!/usr/bin/env/python
import sys
sys.path.append( "/home/shay/a/kalita/ece404/HW4/BitVector-3.3.2" )
from BitVector import *
import string
w = [] #global variable of words to store the key schedules for each round
substitution_table_e = [[0 for x in range(16)] for y in range(16)] #the 16x16 s-table for encryption
substitution_table_d = [[0 for x in range(16)] for y in range(16)] #the 16x16 s-table for decryption
c_e = BitVector(bitstring = '01100011') #this is the constant used for bit scrambling during encryption
d = BitVector(bitstring = '00000101') #this is the constant used for bit scrambling during decryption
RC = [] #the round constants
modulus = BitVector(bitstring = '100011011') #the irreducible polynomial
n = 8 #gf(2^8)
gw = [] #the g() function value for w[3], w[7], w[11], ..., w[39]..there will be 10 of these

def s_table_e(): #make the substitution table for encryption
    #count=0
    #print "encryption"
    for i in range(0, 16):
        row_hex = hex(i)
        row = row_hex.split('x') #to split the x that comes
        for j in range(0, 16):
            col_hex = hex(j)
            col = col_hex.split('x') #to split the x that comes
            #print count + 1        
            rbv = BitVector(hexstring = row[1]) #bit vector representation of row
            cbv = BitVector(hexstring = col[1]) #bit vector representation of column
            tbv = rbv + cbv #join the row and column bits
            #print int(str(rbv),2)
            #print int(str(cbv),2)
            #print tbv
            #now let us find the MI of the tbv bitstring
            if i == 0 and j == 0:
                multi_inverse = BitVector(bitstring = '00000000') #if zero then make it zero
            else:
                multi_inverse = tbv.gf_MI(modulus, n) #find MI
            #print "value of MI: ", multi_inverse
            fin = BitVector(bitstring = '00000000') #just to initialize
            for k in range(0,8):
                fin[k] = multi_inverse[k] ^ multi_inverse[(k+4)%8] ^ multi_inverse[(k+3)%8] ^ multi_inverse[(k+2)%8] ^ multi_inverse[(k+1)%8] ^ c_e[k] #the bit scrambling formula for each bit
            #print fin
            substitution_table_e[int(str(rbv),2)][int(str(cbv),2)] = fin.deep_copy() #perform a deep copy now. Now we have the corresponding byte to be substituted with.
            #print substitution_table_e[int(str(cbv),2)][int(str(rbv),2)]
            #print int(str(substitution_table_e[i][j]),2)
            #count = count + 1
    return

def s_table_d(): #make the substitution table for encryption
    count=0
    #print "decryption"
    for i in range(0, 16):
        row_hex = hex(i)
        row = row_hex.split('x') #to split the x that comes
        for j in range(0, 16):
            col_hex = hex(j)
            col = col_hex.split('x') #to split the x that comes
            #print count + 1                    
            rbv = BitVector(hexstring = row[1]) #bit vector representation of row
            cbv = BitVector(hexstring = col[1]) #bit vector representation of column
            tbv = rbv + cbv #join the row and column bits
            fin = BitVector(bitstring = '00000000') #just to initialize
            for k in range(0,8):
                fin[k] = tbv[(k+2)%8] ^ tbv[(k+5)%8] ^ tbv[(k+7)%8] ^ d[k] #the bit scrambling formula for each bit
            #now let us find the MI of the tbv bitstring
            if str(fin) == '00000000':
                #print "fount 00000000"
                substitution_table_d[int(str(cbv),2)][int(str(rbv),2)] = BitVector(bitstring = '00000000')
                #print int(str(substitution_table_d[j][i]),2)
            else:
                multi_inverse = fin.gf_MI(modulus, n) #find MI  
                #print "jsjsjs:",type(multi_inverse)
                substitution_table_d[int(str(cbv),2)][int(str(rbv),2)] = multi_inverse.deep_copy() #perform a deep copy now. Now we have the corresponding byte to be substituted with.
                #print int(str(substitution_table_d[j][i]),2)
            
    return

def inv_substitute_byte(byte): #the substitute byte function working on one byte
    row = int(str(byte[0:4]), 2) #get the row index
    col = int(str(byte[4:8]), 2)
    return substitution_table_d[row][col]

def substitute_byte(byte): #the substitute byte function working on one byte
    row = int(str(byte[0:4]), 2) #get the row index
    col = int(str(byte[4:8]), 2)
    return substitution_table_e[row][col]
    
def g(w, gw_counter): #define the g(w[i+3]) function, i=gw_counter
    tmp_w = BitVector(bitstring = '00000000') #just to initialize #the temporary word otherwise changes will be reflected in w[3]
    tmp_w = w.deep_copy()
    #print "Inside the g() function: ", w.get_hex_string_from_bitvector()
    #print "inside loop function: "
    #print "the preceding word: ", tmp_w
    #print "Now printing after doing the one byte left circular rotation: "
    tmp_w << 8 #left circular shift the word by 8 bits (one byte) -> STEP 1
    #print tmp_w
    #print "Inside the g() function: ", w.get_hex_string_from_bitvector()
    #now, it's time to perform the byte substitution for each of the 4 bytes of the word from STEP 1 using the substitution_table_e lookup table for encryption round -> STEP 2
    #print "Before the substitution: ", tmp_w
    tmp_w1 = BitVector(bitstring = '00000000')
    tmp_w2 = BitVector(bitstring = '00000000')
    tmp_w3 = BitVector(bitstring = '00000000')
    tmp_w4 = BitVector(bitstring = '00000000')
    tmp_w1 = substitute_byte(tmp_w[0:8]) #substitute the first byte
    tmp_w[0:8] = tmp_w1.deep_copy()
    #print tmp_w[0:8]
    tmp_w2 = substitute_byte(tmp_w[8:16]) #substitute the second byte
    tmp_w[8:16] = tmp_w2.deep_copy()
    #print tmp_w[8:16]
    tmp_w3 = substitute_byte(tmp_w[16:24]) #substitute the third byte
    tmp_w[16:24] = tmp_w3.deep_copy()
    #print tmp_w[16:24]
    tmp_w4 = substitute_byte(tmp_w[24:32]) #substitute the fourth byte
    tmp_w[24:32] = tmp_w4.deep_copy()
    #print tmp_w[24:32]
    #print "After the substitution: ", tmp_w
    #Okay, so now the substitution step (STEP 2) has taken place.
    #time to move to the round constant step -> STEP 3
    temporary = tmp_w[0:8] ^ RC[gw_counter]
    tmp_w[0:8] = temporary.deep_copy()
    #print "The final word gotten of the g() function: ", tmp_w
    #print "round #:", gw_counter
    gw.append(tmp_w)
    return

def generate_word_schedule(): #the method that generates the word schedule..w[4]-w[43]
    gw_counter = 0
    for loop in range(4, 44): #for each word to create from w[4] to w[43]
        if (loop % 4 == 0): #if w[4], w[8], .... the first word of each round
            #print "will go to g() function for: ", loop
            #print "Word i+3: ", w[loop-1].get_hex_string_from_bitvector()
            g(w[loop - 1], gw_counter) #get the g(w[i-1]) equivalent
            #print "Word i+3: ", w[loop-1].get_hex_string_from_bitvector()
            #print "gw[]: ", gw[gw_counter].get_hex_string_from_bitvector()
            #print "loop - 4: ", w[loop-4]
            #print "size of gw[]: ", len(gw)
            #print "corresponding gw[]: ", gw[gw_counter]
            w.append(w[loop - 4] ^ gw[gw_counter]) #xor the function of g() with the fourth last word
            #print "resultant word: ", w[loop]
            gw_counter = gw_counter + 1 #increment so as to reach the next element of gw[] array
        else: #for the non-first words of each round
            #print "loop - 4: ", w[loop-4]
            #print "loop - 1: ", w[loop-1]
            w.append(w[loop - 4] ^ w[loop - 1]) #simply xor the preceding and the 4th last word
            #print "resultant word: ", w[loop]

def inv_sub_each_byte(fin_ip): #the function to substitute each byte
    #fin_ip is 128 bits in length
    for i in range(0, 16):
        #print "i: ", (8*i)
        #print "i+8: ", (8*i+8)
        #print "initially fin_ip[]:", fin_ip[(i*8):(8*i + 8)]
        tmp = inv_substitute_byte(fin_ip[(i*8):(8*i + 8)]) #substitute the first byte
        fin_ip[(i*8):(8*i + 8)] = tmp.deep_copy()
        #print "finally fin_ip[]:", fin_ip[(i*8):(8*i + 8)]
    return fin_ip


def sub_each_byte(fin_ip): #the function to substitute each byte
    #fin_ip is 128 bits in length
    for i in range(0, 16):
        #print "i: ", (8*i)
        #print "i+8: ", (8*i+8)
        #print "initially fin_ip[]:", fin_ip[(i*8):(8*i + 8)]
        tmp = substitute_byte(fin_ip[(i*8):(8*i + 8)]) #substitute the first byte
        fin_ip[(i*8):(8*i + 8)] = tmp.deep_copy()
        #print "finally fin_ip[]:", fin_ip[(i*8):(8*i + 8)]
    return fin_ip

def shift_rows(fin_ip): #the shift rows method
    tmp = [0 for x in range(4)]
    #print "fin_ip[] before: ", fin_ip
    for i in range(1, 4):
        tmp[0] = fin_ip[(i*8):(i*8)+8].deep_copy() #tmp[0] ->0th of row
        tmp[1] = fin_ip[(i*8)+32:(i*8)+40].deep_copy() #tmp[1] ->1st of row
        tmp[2] = fin_ip[(i*8)+64:(i*8)+72].deep_copy() #tmp[2] ->2nd of row
        tmp[3] = fin_ip[(i*8)+96:(i*8)+104].deep_copy() #tmp[3] ->3rd of row
        if i == 1: #left shift by 1
            fin_ip[(i*8):(i*8)+8] = tmp[1].deep_copy()
            fin_ip[(i*8)+32:(i*8)+40] = tmp[2].deep_copy()
            fin_ip[(i*8)+64:(i*8)+72] = tmp[3].deep_copy()
            fin_ip[(i*8)+96:(i*8)+104] = tmp[0].deep_copy()
        elif i == 2: #left shift by 2
            fin_ip[(i*8):(i*8)+8] = tmp[2].deep_copy()
            fin_ip[(i*8)+32:(i*8)+40] = tmp[3].deep_copy()
            fin_ip[(i*8)+64:(i*8)+72] = tmp[0].deep_copy()
            fin_ip[(i*8)+96:(i*8)+104] = tmp[1].deep_copy()
        else: #left shift by 3
            fin_ip[(i*8):(i*8)+8] = tmp[3].deep_copy()
            fin_ip[(i*8)+32:(i*8)+40] = tmp[0].deep_copy()
            fin_ip[(i*8)+64:(i*8)+72] = tmp[1].deep_copy()
            fin_ip[(i*8)+96:(i*8)+104] = tmp[2].deep_copy()
    #print "fin_ip[] after: ", fin_ip
    return fin_ip
          
def inv_shift_rows(fin_ip): #the inverse shift rows method
    tmp = [0 for x in range(4)]
    #print "fin_ip[] before: ", fin_ip
    for i in range(1, 4):
        tmp[0] = fin_ip[(i*8):(i*8)+8].deep_copy() #tmp[0] ->0th of row
        tmp[1] = fin_ip[(i*8)+32:(i*8)+40].deep_copy() #tmp[1] ->1st of row
        tmp[2] = fin_ip[(i*8)+64:(i*8)+72].deep_copy() #tmp[2] ->2nd of row
        tmp[3] = fin_ip[(i*8)+96:(i*8)+104].deep_copy() #tmp[3] ->3rd of row
        if i == 1: #right shift by 1
            fin_ip[(i*8):(i*8)+8] = tmp[3].deep_copy()
            fin_ip[(i*8)+32:(i*8)+40] = tmp[0].deep_copy()
            fin_ip[(i*8)+64:(i*8)+72] = tmp[1].deep_copy()
            fin_ip[(i*8)+96:(i*8)+104] = tmp[2].deep_copy()
        elif i == 2: #right shift by 2
            fin_ip[(i*8):(i*8)+8] = tmp[2].deep_copy()
            fin_ip[(i*8)+32:(i*8)+40] = tmp[3].deep_copy()
            fin_ip[(i*8)+64:(i*8)+72] = tmp[0].deep_copy()
            fin_ip[(i*8)+96:(i*8)+104] = tmp[1].deep_copy()
        else: #right shift by 3
            fin_ip[(i*8):(i*8)+8] = tmp[1].deep_copy()
            fin_ip[(i*8)+32:(i*8)+40] = tmp[2].deep_copy()
            fin_ip[(i*8)+64:(i*8)+72] = tmp[3].deep_copy()
            fin_ip[(i*8)+96:(i*8)+104] = tmp[0].deep_copy()
    #print "fin_ip[] after: ", fin_ip
    return fin_ip
  
def mix_cols(fin_ip): #mixing columns step
    m_w = [[0 for x in range(4)] for y in range(4)] #4x4 lhs for mix cols
    m_b = [[0 for x in range(4)] for y in range(4)] #4x4 rhs for mix cols
    #now define each one of them manually
    #m_w
    #row 1
    m_w[0][0] = BitVector(bitstring = '00000010') #02
    m_w[0][1] = BitVector(bitstring = '00000011') #03
    m_w[0][2] = BitVector(bitstring = '00000001') #01
    m_w[0][3] = BitVector(bitstring = '00000001') #01
    #row 2
    m_w[1][0] = BitVector(bitstring = '00000001') #01
    m_w[1][1] = BitVector(bitstring = '00000010') #02
    m_w[1][2] = BitVector(bitstring = '00000011') #03
    m_w[1][3] = BitVector(bitstring = '00000001') #01
    #row 3
    m_w[2][0] = BitVector(bitstring = '00000001') #01
    m_w[2][1] = BitVector(bitstring = '00000001') #01
    m_w[2][2] = BitVector(bitstring = '00000010') #02
    m_w[2][3] = BitVector(bitstring = '00000011') #03
    #row 4
    m_w[3][0] = BitVector(bitstring = '00000011') #03
    m_w[3][1] = BitVector(bitstring = '00000001') #01
    m_w[3][2] = BitVector(bitstring = '00000001') #01
    m_w[3][3] = BitVector(bitstring = '00000010') #02
    
    #m_b
    #row 1
    m_b[0][0] = fin_ip[0:8].deep_copy()
    m_b[0][1] = fin_ip[32:40].deep_copy()
    m_b[0][2] = fin_ip[64:72].deep_copy()
    m_b[0][3] = fin_ip[96:104].deep_copy()
    #row 2
    m_b[1][0] = fin_ip[8:16].deep_copy()
    m_b[1][1] = fin_ip[40:48].deep_copy()
    m_b[1][2] = fin_ip[72:80].deep_copy()
    m_b[1][3] = fin_ip[104:112].deep_copy()
    #row 3
    m_b[2][0] = fin_ip[16:24].deep_copy()
    m_b[2][1] = fin_ip[48:56].deep_copy()
    m_b[2][2] = fin_ip[80:88].deep_copy()
    m_b[2][3] = fin_ip[112:120].deep_copy()
    #row 4
    m_b[3][0] = fin_ip[24:32].deep_copy()
    m_b[3][1] = fin_ip[56:64].deep_copy()
    m_b[3][2] = fin_ip[88:96].deep_copy()
    m_b[3][3] = fin_ip[120:128].deep_copy()
    
    m_r = [[0 for x in range(4)] for y in range(4)] #the resultant matrix
    for i in range(0, 4):
        for j in range(0, 4):
            m_r[i][j] = BitVector(bitstring = '00000000') #just to initialize
    for row in range(0, 4):
        for col in range(0, 4):
            #m_r[i][j] = m_r[i][j] ^ m_w[i][j].gf_multiply_modular(m_b[j][i], modulus, n)
            tmp1 = m_w[row][0].gf_multiply_modular(m_b[0][col], modulus, n)
            tmp2 = m_w[row][1].gf_multiply_modular(m_b[1][col], modulus, n)
            tmp3 = m_w[row][2].gf_multiply_modular(m_b[2][col], modulus, n)
            tmp4 = m_w[row][3].gf_multiply_modular(m_b[3][col], modulus, n)
            m_r[row][col] = tmp1 ^ tmp2 ^ tmp3 ^ tmp4

    #now reassigning to the original state array based on m_r[] results
    #row 1
    fin_ip[0:8] = m_r[0][0].deep_copy()
    fin_ip[32:40] = m_r[0][1].deep_copy()
    fin_ip[64:72] = m_r[0][2].deep_copy()
    fin_ip[96:104] = m_r[0][3].deep_copy()
    #row 2
    fin_ip[8:16] = m_r[1][0].deep_copy()
    fin_ip[40:48] = m_r[1][1].deep_copy()
    fin_ip[72:80] = m_r[1][2].deep_copy()
    fin_ip[104:112] = m_r[1][3].deep_copy()
    #row 3
    fin_ip[16:24] = m_r[2][0].deep_copy()
    fin_ip[48:56] = m_r[2][1].deep_copy()
    fin_ip[80:88] = m_r[2][2].deep_copy()
    fin_ip[112:120] = m_r[2][3].deep_copy()
    #row 4
    fin_ip[24:32] = m_r[3][0].deep_copy()
    fin_ip[56:64] = m_r[3][1].deep_copy()
    fin_ip[88:96] = m_r[3][2].deep_copy()
    fin_ip[120:128] = m_r[3][3].deep_copy()
    
    return fin_ip
  

def inv_mix_cols(fin_ip): #inverse mixing columns step
    m_w = [[0 for x in range(4)] for y in range(4)] #4x4 lhs for mix cols
    m_b = [[0 for x in range(4)] for y in range(4)] #4x4 rhs for mix cols
    #now define each one of them manually
    #m_w
    #row 1
    m_w[0][0] = BitVector(bitstring = '00001110') #02
    m_w[0][1] = BitVector(bitstring = '00001011') #03
    m_w[0][2] = BitVector(bitstring = '00001101') #01
    m_w[0][3] = BitVector(bitstring = '00001001') #01
    #row 2
    m_w[1][0] = BitVector(bitstring = '00001001') #01
    m_w[1][1] = BitVector(bitstring = '00001110') #02
    m_w[1][2] = BitVector(bitstring = '00001011') #03
    m_w[1][3] = BitVector(bitstring = '00001101') #01
    #row 3
    m_w[2][0] = BitVector(bitstring = '00001101') #01
    m_w[2][1] = BitVector(bitstring = '00001001') #01
    m_w[2][2] = BitVector(bitstring = '00001110') #02
    m_w[2][3] = BitVector(bitstring = '00001011') #03
    #row 4
    m_w[3][0] = BitVector(bitstring = '00001011') #03
    m_w[3][1] = BitVector(bitstring = '00001101') #01
    m_w[3][2] = BitVector(bitstring = '00001001') #01
    m_w[3][3] = BitVector(bitstring = '00001110') #02
    
    #m_b
    #row 1
    m_b[0][0] = fin_ip[0:8].deep_copy()
    m_b[0][1] = fin_ip[32:40].deep_copy()
    m_b[0][2] = fin_ip[64:72].deep_copy()
    m_b[0][3] = fin_ip[96:104].deep_copy()
    #row 2
    m_b[1][0] = fin_ip[8:16].deep_copy()
    m_b[1][1] = fin_ip[40:48].deep_copy()
    m_b[1][2] = fin_ip[72:80].deep_copy()
    m_b[1][3] = fin_ip[104:112].deep_copy()
    #row 3
    m_b[2][0] = fin_ip[16:24].deep_copy()
    m_b[2][1] = fin_ip[48:56].deep_copy()
    m_b[2][2] = fin_ip[80:88].deep_copy()
    m_b[2][3] = fin_ip[112:120].deep_copy()
    #row 4
    m_b[3][0] = fin_ip[24:32].deep_copy()
    m_b[3][1] = fin_ip[56:64].deep_copy()
    m_b[3][2] = fin_ip[88:96].deep_copy()
    m_b[3][3] = fin_ip[120:128].deep_copy()
    
    m_r = [[0 for x in range(4)] for y in range(4)] #the resultant matrix
    for i in range(0, 4):
        for j in range(0, 4):
            m_r[i][j] = BitVector(bitstring = '00000000') #just to initialize
    for row in range(0, 4):
        for col in range(0, 4):
            #m_r[i][j] = m_r[i][j] ^ m_w[i][j].gf_multiply_modular(m_b[j][i], modulus, n)
            tmp1 = m_w[row][0].gf_multiply_modular(m_b[0][col], modulus, n)
            tmp2 = m_w[row][1].gf_multiply_modular(m_b[1][col], modulus, n)
            tmp3 = m_w[row][2].gf_multiply_modular(m_b[2][col], modulus, n)
            tmp4 = m_w[row][3].gf_multiply_modular(m_b[3][col], modulus, n)
            m_r[row][col] = tmp1 ^ tmp2 ^ tmp3 ^ tmp4
    #now reassigning to the original state array based on m_r[] results
    #row 1
    fin_ip[0:8] = m_r[0][0].deep_copy()
    fin_ip[32:40] = m_r[0][1].deep_copy()
    fin_ip[64:72] = m_r[0][2].deep_copy()
    fin_ip[96:104] = m_r[0][3].deep_copy()
    #row 2
    fin_ip[8:16] = m_r[1][0].deep_copy()
    fin_ip[40:48] = m_r[1][1].deep_copy()
    fin_ip[72:80] = m_r[1][2].deep_copy()
    fin_ip[104:112] = m_r[1][3].deep_copy()
    #row 3
    fin_ip[16:24] = m_r[2][0].deep_copy()
    fin_ip[48:56] = m_r[2][1].deep_copy()
    fin_ip[80:88] = m_r[2][2].deep_copy()
    fin_ip[112:120] = m_r[2][3].deep_copy()
    #row 4
    fin_ip[24:32] = m_r[3][0].deep_copy()
    fin_ip[56:64] = m_r[3][1].deep_copy()
    fin_ip[88:96] = m_r[3][2].deep_copy()
    fin_ip[120:128] = m_r[3][3].deep_copy()
    
    return fin_ip          

            
def add_round_key(fin_ip, i):
    tmp1 = fin_ip[0:32] ^ w[4*i]
    fin_ip[0:32] = tmp1.deep_copy()
    tmp2 = fin_ip[32:64] ^ w[4*i + 1]
    fin_ip[32:64] = tmp2.deep_copy()
    tmp3 = fin_ip[64:96] ^ w[4*i + 2]
    fin_ip[64:96] = tmp3.deep_copy()
    tmp4 = fin_ip[96:128] ^ w[4*i + 3]
    fin_ip[96:128] = tmp4.deep_copy()
    return fin_ip
    
def inv_add_round_key(fin_ip, i):
    tmp1 = fin_ip[0:32] ^ w[40-(4*i)]
    fin_ip[0:32] = tmp1.deep_copy()
    tmp2 = fin_ip[32:64] ^ w[41-(4*i)]
    fin_ip[32:64] = tmp2.deep_copy()
    tmp3 = fin_ip[64:96] ^ w[42-(4*i)]
    fin_ip[64:96] = tmp3.deep_copy()
    tmp4 = fin_ip[96:128] ^ w[43-(4*i)]
    fin_ip[96:128] = tmp4.deep_copy()
    return fin_ip   

def print_cur(byte_s):
    print "Row 1: " + byte_s[0:8].get_hex_string_from_bitvector() + "," + byte_s[32:40].get_hex_string_from_bitvector() + "," + byte_s[64:72].get_hex_string_from_bitvector() + "," + byte_s[96:104].get_hex_string_from_bitvector()
    print "Row 2: " + byte_s[8:16].get_hex_string_from_bitvector() + "," + byte_s[40:48].get_hex_string_from_bitvector() + "," + byte_s[72:80].get_hex_string_from_bitvector() + "," + byte_s[104:112].get_hex_string_from_bitvector()
    print "Row 3: " + byte_s[16:24].get_hex_string_from_bitvector() + "," + byte_s[48:56].get_hex_string_from_bitvector() + "," + byte_s[80:88].get_hex_string_from_bitvector() + "," + byte_s[112:120].get_hex_string_from_bitvector()
    print "Row 4: " + byte_s[24:32].get_hex_string_from_bitvector() + "," + byte_s[56:64].get_hex_string_from_bitvector() + "," + byte_s[88:96].get_hex_string_from_bitvector() + "," + byte_s[120:128].get_hex_string_from_bitvector()
    return

def encryptAES(fin_ip,cnt):
    #now, we have the input block and the key, lets
    #Step1 -> substitute each byte
    #Step2 -> shift rows
    #Step3 -> mix columns
    #Step4 -> add round key by XORing
    #all these steps repeated 10 times
    #print fin_ip
    #print cnt+1
    #fin_ip = sub_each_byte(fin_ip)
    #print fin_ip
    #fin_ip = shift_rows(fin_ip)
    #print fin_ip
    #print "before performing column mixing: "
    #print fin_ip
    #fin_ip = mix_cols(fin_ip)
    #print "after performing column mixing: "
    #print fin_ip
    #fin_ip = add_round_key(fin_ip, 1)
    #print fin_ip
    for i in range(1, 11): #for 10 rounds
        #print "Round: ", i
        #print "Start of Round: "
        #print_cur(fin_ip)
        fin_ip = sub_each_byte(fin_ip) #perform byte-byte substitution by s_en_lookup
        #print "After SubBytes: "
        #print_cur(fin_ip)
        fin_ip = shift_rows(fin_ip) #perform shifting of rows
        #print "After ShiftRows: "
        #print_cur(fin_ip)
        if i != 10:
            fin_ip = mix_cols(fin_ip) #perform column mixing
            #print "After MixColumns: "
            #print_cur(fin_ip)
        #print "Round Key Value: "
        wtmp2 = w[4*i]+w[(4*i) + 1] + w[(4*i) +2] + w[(4*i) + 3]
        #print_cur(wtmp2)
        fin_ip = add_round_key(fin_ip, i) #lastly perform the XORing with word schedule
        #print "Output from round : ", i
        #print_cur(fin_ip)
        #print "Round:", i
        #print fin_ip
    #print fin_ip
    return fin_ip
    
 
def decryptAES(fin_ip,cnt):
    for i in range(1, 11): #for 10 rounds
        #print "Round: ", i
        #print "Start of Round: "
        #print_cur(fin_ip)
        fin_ip = inv_shift_rows(fin_ip) #perform shifting of rows
        #print "After ShiftRows: "
        #print_cur(fin_ip)
        fin_ip = inv_sub_each_byte(fin_ip) #perform byte-byte substitution by s_en_lookup
        #print "After SubBytes: "
        #print_cur(fin_ip)
        #print "Round Key Value: "
        #wtmp2 = w[4*i]+w[(4*i) + 1] + w[(4*i) +2] + w[(4*i) + 3]
        fin_ip = inv_add_round_key(fin_ip, i) #lastly perform the XORing with word schedule
        #print "After XORing round : ", i
        #print_cur(fin_ip)
        if i != 10:
            fin_ip = inv_mix_cols(fin_ip) #perform column mixing
            #print "After MixColumns: "
            #print_cur(fin_ip)
        #print "Round:", i
        #print fin_ip
    #print fin_ip
    return fin_ip

   

pt_fh = open("plaintext.txt", 'r') #plain text file open
plntxt = pt_fh.read() #read the text from the and store it in a variable
#print plntxt
tot_len = len(plntxt) #total length of plaintext
#print tot_len
#now plaintext has 736 characters except the null character. AES block cipher has 128 bits(or 16 characters of input at a time
#let us break it 16 characters at a time. we will feed 16 characters to the AES processing at any time
input_block = "" #this variable will be storing the current input block 16 characters at a time from the plaintext. There will be 737/16 = 47 rounds of processing
i = 0 #variable used to slice the plaintext string 16 characters at a time
#c = 0 #just a counter signifying the round of processing into the AES
key = "lukeimyourfather" #the 16 character(128 bit key)
#key = "2b7e151628aed2a6abf7158809cf4f3c"
#print len(key)
key_bits = BitVector(textstring = key)
#key_bits = BitVector(hexstring = key)
#print len(key_bits)
#print key_bits
#now the key size is 128 
#now, we have the key bits (16 bytes)
#bytes 0-3->w1, 4-7->w2, 8-11->w3, 12-15->w4. Make the division here
#so, we will have 44 words. Let's store them for help during decryption.
#each word is 32 bytes in length.
w.append(key_bits[0:32]) #w[0] create
w.append(key_bits[32:64]) #w[1] create
w.append(key_bits[64:96]) #w[2] create
w.append(key_bits[96:128]) #w[3] create
#print key_bits[96:128]
#print w[3].get_hex_string_from_bitvector()
'''
for i in range(0,44):
    print w[i].get_hex_string_from_bitvector()
'''
#print w
#we now have the initial 4 words
s_table_e() #create the substitution table that we will use for encryption
s_table_d() #create the substitution table that we will use for decryption
RC.append(BitVector(bitstring = '00000001')) #RC[0]
#print type(RC[0])
multiply_fac = BitVector(bitstring = '00000010') #multiply by x each round constant
for loop in range(1,10): #create the 9 remaining round constants
    temp = RC[loop-1].deep_copy()
    RC.append(temp.gf_multiply_modular(multiply_fac, modulus, n)) #multiply the previous RC by 0x02 and keep appending to RC
#so now we have the round constants (all 10 of them). Now we have to generate the key schedules
'''
print "Length of RC[]: ", len(RC)
for loop in range(0, 10):
    print RC[loop]
'''
              
#now, let us create the round key schedules
#we initially have w[0]-w[3]
generate_word_schedule() #the function to generate the word schedule
#now, the round word schedules have been generated and the round constants generated
'''
print "Now print the gw[] values..."
for loop in range(0,10):
    print "Number: ", loop
    print gw[loop]
print "Now printing the words..."
countup = 0
for loop in range(4,44):
    if (loop % 4 == 0): 
        print "word number: ", loop
        print gw[countup]
        print w[loop - 4]
        print w[loop]
        countup = countup+1
    else:
        print "word number: ", loop
        print w[loop - 1]
        print w[loop - 4]
        print w[loop]
'''
#print "Size of gw[]: ", len(gw)
#print "Size of w[]: ", len(w)
#print int(str(substitution_table_e[0][2]), 2)
#print int(str(substitution_table_d[2][12]), 2)
'''
for i in range(0,16):
    for j in range(0, 16):
        print "row: ",i
        print "col: ", j
        print int(str(substitution_table_d[i][j]), 2)
'''
'''
for i in range(0,44):
    print i+1
    print w[i].get_hex_string_from_bitvector()
'''
cnt = 0
final_encrypted = BitVector(bitstring = '00000000') #final encrypted bits just initialized
'''
plntxt2 = "3243f6a8885a308d313198a2e0370734"
ip_bv = BitVector(hexstring = plntxt2)
print "Input : "
print_cur(ip_bv)
print "Round Key Value: "
#print w[0:4]
wtmp=w[0]+w[1]+w[2]+w[3]
print_cur(wtmp)
fin_ip = (ip_bv[0:32] ^ w[0]) + (ip_bv[32:64] ^ w[1]) + (ip_bv[64:96] ^ w[2]) + (ip_bv[96:128] ^ w[3])
encrypted_subpart = encryptAES(fin_ip,cnt)
final_encrypted = final_encrypted + encrypted_subpart
'''


while (i + 16) <= (tot_len): #exactly 16 blocks of input data, altogether 46 rounds of processing
    cur_ip = plntxt[i : i + 16] #get the current input
    #let us now XOR the current initial input 128 block with w[0] through w[4]
    ip_bv = BitVector(textstring = cur_ip) #get the bitvector representation of the input block
    fin_ip = (ip_bv[0:32] ^ w[0]) + (ip_bv[32:64] ^ w[1]) + (ip_bv[64:96] ^ w[2]) + (ip_bv[96:128] ^ w[3]) #an array of bits containing the XOR or input bits and w0-w3    
    encrypted_subpart = encryptAES(fin_ip,cnt) #feed it into the AES encryption
    #print "Part: ", cnt+1
    #print encrypted_subpart
    if cnt == 0:
        final_encrypted = encrypted_subpart
    else:
        final_encrypted = final_encrypted + encrypted_subpart
    i = i + 16 #keep incrementing i by 16 characters each time for the next round
    cnt = cnt + 1 #keep incrementing the round counter

#print len(final_encrypted)
encrypted_text = final_encrypted.get_hex_string_from_bitvector() #the encrypted text from the corresponding bitvector
print "Encrypted Text: ", encrypted_text
f_e = open("encryptedtext.txt", 'w') #make a new file for writing to
f_e.write(str(encrypted_text)) #write to encryptedtext.txt
f_e.close() #close file handle
pt_fh.close() #close file handle

f_e = open("encryptedtext.txt", 'r') #open encryptedtext.txt for reading
etxt = f_e.read() #encrypted text in hex stored in a string
#print etxt
#print len(etxt)
etxt_len = len(etxt)
f_e.close() #close file handler
pos = 0
counter = 0
#print etxt_len
final_decrypted = BitVector(bitstring = '00000000') #final decrypted bits just initialized
#print "Decryption Round..."
while (pos + 32) <= (etxt_len):
    #print counter+1
    cur_ip = etxt[pos : pos + 32] #get the current encrypted input
    ip_bv = BitVector(hexstring = cur_ip) #get the bitvector representation of the input encrypted block
    #print ip_bv
    #print len(ip_bv)
    #print type(ip_bv)
    fin_ip = (ip_bv[0:32] ^ w[40]) + (ip_bv[32:64] ^ w[41]) + (ip_bv[64:96] ^ w[42]) + (ip_bv[96:128] ^ w[43]) #an array of bits containing the XOR or input bits and w0-w3
    decrypted_subpart = decryptAES(fin_ip,counter) #feed it into the AES encryption
    if counter == 0:
        final_decrypted = decrypted_subpart
    else:
        final_decrypted = final_decrypted + decrypted_subpart
    counter = counter + 1
    pos = pos + 32
    #print final_decrypted
    #print len(final_decrypted)

decrypted_text = final_decrypted.get_text_from_bitvector() #the decrypted text from the corresponding bitvector
f_d = open("decryptedtext.txt", 'w') #make a new file for writing to
f_d.write(str(decrypted_text)) #write to decryptedtext.txt
print "Decrypted TexT: "
print decrypted_text
f_d.close()
