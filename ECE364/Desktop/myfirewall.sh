#! /bin/bash

############################
#Homework No - 9
#Name - Akash Kumar
#ECN Login - kumar138@purdue.edu
#Due Date - 4/2/2015
############################


##Place No restrictions on out bound packets#####
iptables -A OUTPUT -j ACCEPT
##Allowing all ip addresses in range 128.46.75.0 - 128.46.75.255#####
iptables -A INPUT -p all -s 128.46.75.0/24
##dropping all echo responses to pings###########
iptables -A FORWARD -p icmp --icmp-type echo-request -j DROP
##Forwarding all packets to port 12000 to port 22############
iptables -t nat -A PREROUTING -p tcp -s 0/0 --dport 12000 -j DNAT --to-destination 127.0.0.1:22
##Accepting  an ssh request from ecn.purdue.edu and rejecting requests from all other hosts#####
iptables -A INPUT -p tcp -s ecn.purdue.edu --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j DROP 
##Accepting HTTP requests from 128.46.75.182 , rejecting requests from all other hosts###
iptables -A INPUT -p tcp -s 128.46.75.182 --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j DROP
##Accepting all requests to port 113 for Auth/Ident by SMTP and IRC
iptables -A INPUT -p tcp --dport 113 -j ACCEPT
