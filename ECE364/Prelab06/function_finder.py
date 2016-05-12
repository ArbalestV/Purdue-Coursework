#! /usr/bin/env python3.4
#
# $Author: ee364c10 $:
# $Date: 2015-02-22 23:07:39 -0500 (Sun, 22 Feb 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Prelab06/function_finder.py $:

import os
import math
import sys
import re
import os.path

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "There should be two arguments in command line."
        sys.exit()
    else:
        fname = sys.argv[1]
        if (os.path.exists(fname) is False):
            print fname + " does not exist"
            sys.exit()
        if (os.access(fname, os.R_OK) is False):
            print "Could not read " + fname
            sys.exit()
        #if the code reaches here, that means the file exists and is readable
        f = open(fname, "r")
        #print f.read()
        for lines in f:
            #print lines
            if re.match(r"def", lines):
                #print lines
                var = re.search(r"(?P<name>[-\w_]+)\((?P<arg_list>[-\w=_,\s]+)", lines)
                print var.group("name")
                #print var.group("arg_list").split(",")
                arguments = var.group("arg_list").split(",")
                tot_arg = len(arguments)
                #print tot_arg
                for i in range(0, tot_arg):
                    print "Arg" + str(i + 1) + ": " + arguments[i]
