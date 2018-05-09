# Socket-Programming-

Socket programming is a way of connecting two nodes on a network to communicate with each other.
Here we will see how we can establish a communication channel between to systems 
A socket can be viewed as combination of IP address and port number.

For socket programming we have to import socket library

From that we call socket function that has two arguments
socket(<IP address version>,<Communication Protocol>)
  socket.AF_INET means (IPv4 protocol) and socket.AF_INET6 means (IPv6 protocol)
  socket.SOCK_DGRAM means UDP Protocol and ket.SOCK_STREAM means TCP Protocol

Then we have different codes for sender and reciever side
  
On Sender Side
  We send our msg by sendto() function that takes two arguments:
    i.  The message
    ii. A tuple containing IP address and Port No.
    
 To recieve acknowledgement or reply from the reciever we use function recvfrom() that takes accepted no. of characters as argument
    recvfrom(10) #for receiving first 10 characters
    
On receiver side
  We create socket or communication channel by bindin IP address and Port no. using bind() function
  To receive the msg we use recvfrom() in the same way
  Suppose we take A=socket.recvfrom(10)
  then A will take a tuple such that A[0] has the message  and A[1] has the channel
  Then we send the reply to channel A[1]
