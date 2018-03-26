# coding=utf-8
import socket              
s8 = socket.socket()        
host = socket.gethostname()   
port = 12345               
s8.bind((host, port))      
s8.listen(5)                 
print "this is server side1017, waiting for client to connect "
while True:
    c, addr = s8.accept()    
    print  "why next connection the addr will add +1??"
    print 'connection address:', addr
    c.send('welcome to cainiao 20171017')
    c.close()   