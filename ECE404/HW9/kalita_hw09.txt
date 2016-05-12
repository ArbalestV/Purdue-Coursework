#! /bin/bash

iptables -A OUTPUT -j ACCEPT #rule to place no restriction on outbound packets

iptables -A INPUT -p all -s 128.58.0.0/16 -j DROP #block list of ip addresses beginning with 128.58.X.X

iptables -A INPUT -p icmp --icmp-type echo-request -j REJECT #disable pinging by all other hosts

iptables -t nat -A PREROUTING -p tcp -s 0/0 --dport 550 -j REDIRECT --to-port 22 #forward from a random port to port 22 on my computer (127.0.0.1)

iptables -A INPUT -p tcp -s 128.46.0.0/16 --dport 22 -j ACCEPT #accept ssh requests only from ecn.purdue.edu domain
iptables -A INPUT -p tcp --dport 22 -j DROP #reject ssh requests from all the other sources
#iptables -A INPUT -p tcp -s ! ecn.purdue.edu --dport 22 -j DROP #single line command to only accept from ecn.purdue.edu

iptables -A INPUT -p tcp -s 128.46.75.194 --dport 80 -j ACCEPT #only accept HTTP requests on port 80 from ip address 128.72.12.23
iptables -A INPUT -p tcp --dport 80 -j DROP #drop HTTP requests on port 80 from all other hosts
#iptables -A INPUT -p tcp -s ! 128.72.12.23 --dport 80  -j DROP #single line command that only accepts HTTP requests from a particular IP address

iptables -A INPUT -p tcp --dport 113 -j ACCEPT #Permit Auth/Iden port 113 open

