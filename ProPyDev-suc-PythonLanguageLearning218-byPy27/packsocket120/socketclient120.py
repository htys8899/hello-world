# coding=utf-8
# ����һ���򵥵����ϳ���client�����Ӻ����̽��շ������˷��������ַ�������ʾ���˳���
import socket               # ���� socket ģ��
s = socket.socket()         # ���� socket ����
host = socket.gethostname() # ��ȡ����������
port = 12345                # ���ö˿ں�
#  ��client��Ҫ���ӷ�������ʱ��Ҫ��֤����Ķ��������������ģ� 
#  ���û�����з������ˣ���ô����һ�оͻ������ң���socket.py line 228�г���һ��Exception������Errno Ϊ10061��
s.connect((host, port))
print "after s.connect((host,post)), get the chars from server into the buffer reccv"
print s.recv(1024)
s.close()   