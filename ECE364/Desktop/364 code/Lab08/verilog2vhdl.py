#! /usr/bin/env python3.4
#
# $Author: ee364c10 $:
# $Date: 2015-03-24 15:29:26 -0400 (Tue, 24 Mar 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Lab08/verilog2vhdl.py $:
import os
import math
import sys
import re
from vtools import is_valid_name, parse_pin_assignment, parse_net
#print(len(sys.argv))
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print('Usage: verilog2vhdl.py [infile] [outfile]')
    exit(1)
try:
    fi = open(sys.argv[1], 'r')
except IOError as e:
    print('Error: %s\n' % (e,))
    exit(2)
if len(sys.argv) == 3:
    #print('will output to file if file opens')
    try:
        fo = open(sys.argv[2], 'w')
    except IOError as e:
        print('Error: %s\n' % (e,))
        exit(3)
    for lines in fi:
        #print(lines)
        lines = lines.lstrip()
        try:
            tup = parse_net(lines)
        #print(tup)
        #print(tup[2])
        #print(len(tup[2]))
        except ValueError as e:
            print('Error: input file is not a valid Verilog port map!')
            print('%s\n' % (e,))
            exit(4)
        instance_name = tup[1]
        component_name = tup[0]
        assignment_list = tup[2]
        len_assignment = len(assignment_list)
        line_str = instance_name + ":" + " " + component_name + " PORT MAP("
        #print(instance_name + ":" + " " + component_name + " PORT MAP(")
        for i in range(0, len_assignment):
            port = tup[2][i][0]
            pin = tup[2][i][1]
            if i != (len_assignment - 1):
                line_str = line_str + port + "=>" + pin + ","
            else:
                line_str = line_str + port + "=>" + pin
        line_str = line_str + ");\n"
        #print(line_str)
        fo.write(line_str)
else:
    #print('will output to stdout')
    for lines in fi:
        #print(lines)
        lines = lines.lstrip()
        try:
            tup = parse_net(lines)
        #print(tup)
        #print(tup[2])
        #print(len(tup[2]))
        except ValueError as e:
            print('Error: input file is not a valid Verilog port map!')
            print('%s\n' % (e,))
            exit(4)
        instance_name = tup[1]
        component_name = tup[0]
        assignment_list = tup[2]
        len_assignment = len(assignment_list)
        line_str = instance_name + ":" + " " + component_name + " PORT MAP("
        #print(instance_name + ":" + " " + component_name + " PORT MAP(")
        for i in range(0, len_assignment):
            port = tup[2][i][0]
            pin = tup[2][i][1]
            if i != (len_assignment - 1):
                line_str = line_str + port + "=>" + pin + ","
            else:
                line_str = line_str + port + "=>" + pin
        line_str = line_str + ");"
        print(line_str)
        
