#!usr/bin/python

import socket

# giving IP version, type of Protocol

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# On sender side
while True :
	v=raw_input("Enter message you want to send")
	s.sendto(v,("192.168.1.14",9999))
	rply= s.recvfrom(10)
	print rply
	while not rply: sleep(3)



#On receiver side

s.bind(("192.168.43.19",5000))

while True:
	data=s.recvfrom(10)
	print (data[1],"has sent a message: ",data[0])
	rply=raw_input("Enter your reply")
	s.sendto(rply,data[1])

