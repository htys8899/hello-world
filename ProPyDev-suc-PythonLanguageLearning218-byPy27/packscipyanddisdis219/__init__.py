# coding=utf-8
from scipy.optimize import fsolve  # ������ⷽ����ĺ���
import dis


def f(x):  
    x1 = x[0]  
    x2 = x[1]  
    return [2*x1 - x2**2 - 1, x1**2 - x2 - 2]  
result = fsolve(f, [1, 1])  #�����ʼֵ����� 

def g(x):  
    while 1: 
        pass
    while True: 
        pass

print(result) 

dis.dis(f)
dis.dis(g)

print ("20180219 ok!")