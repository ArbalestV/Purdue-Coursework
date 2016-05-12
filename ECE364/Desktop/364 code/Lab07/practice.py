#! /usr/local/bin/python3.4
f = open("report 69069-29232.txt",'r')
#cont = f.read()
#print cont
c = 0
for lines in f:
    if c == 0 or c==1:
        c = c+1
        continue
    else:
        #print lines
        cnt = lines.split()
        print cnt
        print cnt[0]
        print cnt[1]
        print cnt[2]
        print cnt[3]
        print cnt[4].split('$')[1]
