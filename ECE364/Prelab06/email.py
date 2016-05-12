#! /usr/bin/env python3.4
#
# $Author: ee364c10 $:
# $Date: 2015-02-22 21:32:01 -0500 (Sun, 22 Feb 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Prelab06/email.py $:

import os
import math
import sys
import re

if __name__ == "__main__":
    f = open(sys.argv[1],"r")
    #contents = f.read()
    #print contents
    #lst = []
    #i = 0
    for lines in f:
        cont =  lines.split()
        #print cont
        if re.search(r"(ecn.)", cont[0]):
            print cont[0] + "\t" + re.sub(r"([\d]+)(\.)([\d]+)", r"\1\2\3/100", cont[1])
            continue
        else:
            print re.sub(r"(purdue.edu)", r"ecn.\1", cont[0]) + "\t" + re.sub(r"([\d]+)(\.)([\d]+)", r"\1\2\3/100", cont[1])
        #print re.sub(r"(purdue.edu)",  r"ecn.\1", r"([\d]+)(\.)([\d]+)", r"\1\2\3/100", cont)
        #print re.sub(r"([\d]+)(\.)([\d]+)", r"\1\2\3/100", cont[1])
        #print type(cont)
        #lst.append(cont)
        #lst[i].append(cont[1])
        #print type(lst[i])
        #i += 1
    #for i in range(0, len(lst)):
        
