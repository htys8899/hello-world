# coding=utf-8
# 这是一个简单的网上程序，client端连接后，立刻接收服务器端发过来的字符串，显示后退出了
import socket               # 导入 socket 模块
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口好
#  当client端要连接服务器端时，要保证服务的端是先运行起来的； 
#  如果没有运行服务器端，那么，下一行就会出差，并且，在socket.py line 228中出现一个Exception，错误Errno 为10061；
s.connect((host, port))
print "after s.connect((host,post)), get the chars from server into the buffer reccv"
print s.recv(1024)
s.close()   