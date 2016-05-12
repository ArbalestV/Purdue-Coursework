#! /usr/local/bin/python3.4
#
# $Author: ee364c10 $:
# $Date: 2015-03-06 19:58:42 -0500 (Fri, 06 Mar 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Prelab08/listmod.py $:
import os
import math
import sys
import re
from lists import find_median

l1 = input('Enter the first list of numbers: ')
l2 = input('Enter the second list of numbers: ')
list1 = l1.split()
list2 = l2.split()
for i in range(0,len(list1)):
    list1[i] = int(list1[i])
for i in range(0,len(list2)):
    list2[i] = int(list2[i])
print('First list: ', list1)
print('Second list: ', list2)
t = find_median(list1, list2)
print('Merged list: ', t[1])
print('Median: ', t[0])
