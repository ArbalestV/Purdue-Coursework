#! /usr/bin/env python3.4
#
# $Author: ee364c10 $:
# $Date: 2015-02-22 21:31:30 -0500 (Sun, 22 Feb 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Prelab06/ip_detect.py $:

import os
import math
import sys
import re

if __name__ == "__main__":
    f = open(sys.argv[1],"r")
    for lines in f:
        cnt = lines.strip()
        cont =  lines.split(':')
        cont[1] = cont[1].replace("\n", "")
        #print cont
        pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        #print cont[0]
        if re.match(pattern, cont[0]):
            #print "Vaild IP address"
            #print cont[1]
            '''
            pat2 = r"^([3][2][7][0-6][0-7] | [3][2][0-6][0-9]{2} | [3][0-1][0-9]{3} | [1-2][0-9]{4} | [1-9][0-9]{1,3} | [1,9])"
            if re.match(pat2, cont[1]):
                pat3 = r"^([1][0][2][0-3] | [1][0][0-1][0-9] | [1-9][0-9]{1,2} | [1,9])"
                if re.match(pat3, cont[1]):
                    print cnt + " - " + "Valid (root privileges required)"
                else:
                    print cnt + " - " + "Valid"
            else:
                print cnt + " - " + "Invalid Port Number"
            '''
    
            try:
                if int(cont[1]) > 1 and int(cont[1]) <= 32767:
                    if int(cont[1]) < 1024:
                        print cnt + " - " + "Valid (root privileges required)"
                    else:
                        print cnt + " - " + "Valid"
                else:
                    print cnt + " - " + "Invalid Port Number"
            except ValueError:
                print cnt + " - " + "Invalid Port Number"
            
        else:
            print cnt + " - " + "Invalid IP address"

