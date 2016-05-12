#! /usr/bin/env python3.4
#
# $Author: ee364c10 $:
# $Date: 2015-02-09 19:46:01 -0500 (Mon, 09 Feb 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Prelab04/dataStructs.py $:
import os
import math
import sys
import glob

def Item_Price_List():  #function to map each item to corresponding price
    it_filename = "purchases/Item List.txt"
    f_i = open(it_filename, 'r')
    count = 0
    it_pr_list = [] #initialize an empty list
    for lines in f_i:
        if count == 0 or count == 1:
            count = count + 1
            continue
        else:
            item_price = lines.strip()
            item_price = item_price.split("$")
            it_pr_list.append(item_price)
            count = count + 1
    f_i.close()
    return it_pr_list

def getPurchaseReport():   
    #purchase files are from 001 to 009
    #now, it_pr_list is a list that stores the name of item and the price in $
    #now create a dictionary with purchase number corresponding to each purchase input file, and the total cost
    it_pr_list = Item_Price_List() #get the list mapping item to respective price
    purID_cost_dict = {}#initialize to empty
    for i in range (0, 10):
        filename = "purchases/purchase_00"+str(i)+".txt"
        #print filename
        f = open(filename, 'r')
        count  = 0
        total = 0.00
        #print "file: ", i
        for lines in f:
            if count == 0 or count == 1:
                count = count + 1
                continue
            else:
                it = lines.split()[0]
                qty = lines.split()[1]
                #now that we have the name of the item and its quantity, all we have to do is iterate through the it_pr_list list and find the price corresponding to each item, and then multiply to get the adding total
                for j in range(0, len(it_pr_list)):
                    if (it_pr_list[j][0].strip() == it):
                        total = total + (int(qty) * float(it_pr_list[j][1]))
                count = count + 1
        #print "File: ", i 
        #print total
        #now, we have to map i to total corresponding to each purchase input file and the total for each input file
        f.close()
        purID_cost_dict.update({i:total})
    return purID_cost_dict

def getTotalSold():
    it_pr_list = Item_Price_List() #get the list mapping item to respective price
    it_sold_dict = {}#empty
    for i in range(0, len(it_pr_list)): #now, we will essentially be comparing for each file name from 0 to 10, if we get the name of the item as similar to the it_pr_list[i][0] -> name of the item, have a counter, and keep counting
        number = 0
        #print "item: "
        #print it_pr_list[i][0].strip()
        for j in range(0, 10):#since the purchase files are from 0 to 9
            filename = "purchases/purchase_00"+str(j)+".txt"
            #print filename
            f = open(filename, 'r') 
            count = 0
            #print "file: "
            #print j
            for lines in f:
                if count == 0 or count == 1:
                    count = count + 1
                    continue
                else:
                    it = lines.split()[0]
                    #print it
                    qty = lines.split()[1]
                    #print qty
                    if (it == it_pr_list[i][0].strip()):
                        #print "Item matched: ", it
                        #print "Quantity: ", qty
                        number = number + int(qty)
                        break #since in each file of purchase an item appears once
                    else:
                        continue
                    count = count + 1
            f.close()
            #end of each purchase file checking
        #end of all the files checked for each item
        #now, here we map each item name to its number sold
        #print type(it_pr_list[i][0].strip())
        it_sold_dict.update({it_pr_list[i][0].strip():int(number)})
    #end of all the items
    return it_sold_dict

def files_get():
    files = []#initialize an empty list
    files = (glob.glob("files/*.txt"))
    return files

def get_file_content():
    files = files_get()
    f_content = [] #a file content list to compare between file contents
    for i in range(0, len(files)):
        #print "File number: ", (i + 1)
        fn = files[i]
        f = open(fn, 'r')
        f_content.append(f.readlines())
        f.close()
    return f_content

def dict_f():
    files = files_get() #list of files
    #print files
    f_content = get_file_content() #list of file content
    #print f_content
    d = {}
    for j in range(0, len(f_content)):
        d.update({str(f_content[j]):str(j)})
    #print d
    for key in d:
        lst = []
        for l in range(0, len(files)):
            if str(key) == str(f_content[l]):
                lst.append(str(files[l]))
            else:
                continue
        #end of for
        lst.sort()
        d.update({str(key):lst})
    #end of key block for loop
    #print d
    return d

def wordCount(fn):
    f = open(fn,'r')
    cont = f.read()
    f.close()
    
    #wordlist = cont.strip("."",")
    wordlist = cont.split()
    #wordlist = wordlist.split()
    l = []
    for words in wordlist:
        words = words.strip(","".")
        l.append(words)
    l = set(l)
    
    return len(l)

def getDuplicates():
    d = dict_f()
    #c=0
    fin_d = {}
    for key in d:
        #print (c+1)
        fn = str(d.get(key))[2:15]
        #print type(fn)
        #print fn
        wc = wordCount(fn)
        #print wc
        #c=c+1
        #print type(d.get(key).split())
        #print type(d.get(key))
        l = d.get(key)
        #print l
        t = (wc,l)
        #print t
        #print t
        fin_d.update({fn:t})
    #print len(fin_d)
    #print fin_d
    return fin_d    
        
def getFreq(words):
    files = files_get() #list of files
    print "Word is: ", words
    for i in range(0, len(files)):
        f = open(files[i], 'r')
        cont = f.read()
        cont = cont.split()
        num = 1
        for words_2 in cont:
            words_2 = words_2.strip(","".")
            if words == words_2:
                num = num + 1
    print num
    return num

  
def getWordFrequency():
    files = files_get() #list of files
    #now, what we will do here, is that for each file, for each word, we will iterate through that file and the remaining other files and try to see if we find match. If match found, then add them
    f_d = {}
    for i in range(0, len(files)):
        #print type(files[i])
        f = open(files[i], 'r')
        cont = f.read()
        #print type(cont)
        cont = cont.split()
        #print cont
        for words in cont:
            words = words.strip(","".")
            #print words
            num = getFreq(words)
            f_d.update({words:num})
    return f_d
            

if __name__ == "__main__":
    purID_cost_dict = getPurchaseReport()
    #print(purID_cost_list.keys())
    #print(purID_cost_list.values())
    print "\n\nNow returning the results of getPurchaseReport() function through the required dictionary..."
    print "\n\nThe Trannsaction ID:Total Cost list is as follows: "
    print(purID_cost_dict)
    it_sold_dict = getTotalSold()
    print "\n\nNow returning the results of getTotalSold() function through the required dictionary..."
    print "\n\nThe Item Name:Total Sold list is as follows: "
    print(it_sold_dict)
    
    files_get()
    get_file_content()
    fin_d = getDuplicates()
    print "\n\nNow printing the results of the getDuplicates funnction..."
    print "\n\nDictionary {(string) : (int, list)}"
    print fin_d
    f_d = getWordFrequency()
    print "\n\nNow printing the results of the getWordFrequency funnction..."
    print "\n\nDictionary {string : int}"
    print f_d
    print type(f_d)
