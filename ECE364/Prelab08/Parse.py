#! /usr/local/bin/python3.4
#
# $Author: ee364c10 $:
# $Date: 2015-03-06 22:12:03 -0500 (Fri, 06 Mar 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Prelab08/Parse.py $:
import os
import math
import sys
import re

if len(sys.argv) != 2:
    print('Usage: Parse.py [filename]')
    sys.exit(1)
fn = sys.argv[1]
try:
    fh = open(fn, 'r')
except:
    print(fn + " is not a readable file") 
    sys.exit(1)
count = 0
for lines in fh:
    if count == 0:
        count = count + 1
        #print(lines.split())
        print(lines)
        continue
    lst = lines.split()
    #print(lst)
    str_p = ''
    sum_tot = 0
    tot_char = 0
    for i in range(0, len(lst)):
        try:
            sum_tot = sum_tot + int(lst[i])
        except:
            str_p = str_p + lst[i] + ' '
            tot_char = tot_char + 1
    len_str = len(str_p)
    #str_p[len_str - 1] = ''
    tot_int = len(lst) - tot_char
    median = sum_tot / tot_int
    print('%.3f' %median + ' ' + str_p)
    
    

