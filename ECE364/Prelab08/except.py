#! /usr/local/bin/python3.4
#
# $Author: ee364c10 $:
# $Date: 2015-03-06 21:08:36 -0500 (Fri, 06 Mar 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Prelab08/except.py $:
import os
import math
import sys
import re

vals = input('Please enter some values: ')
l1 = vals.split()
#print(l1)
new_lst = []
for i in range(0,len(l1)):
    try:
        new_lst.append(float(l1[i]))
    except ValueError:
        #print('Cannot convert from string to float...')
        pass
    
sum = 0
for i in range(0, len(new_lst)):
        sum = sum + new_lst[i]
    
print('The sum is: ', sum)

