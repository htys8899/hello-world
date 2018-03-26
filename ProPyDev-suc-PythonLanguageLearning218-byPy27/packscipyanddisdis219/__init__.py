# coding=utf-8
from scipy.optimize import fsolve  # 导入求解方程组的函数
import dis


def f(x):  
    x1 = x[0]  
    x2 = x[1]  
    return [2*x1 - x2**2 - 1, x1**2 - x2 - 2]  
result = fsolve(f, [1, 1])  #输入初始值并求解 

def g(x):  
    while 1: 
        pass
    while True: 
        pass

print(result) 

dis.dis(f)
dis.dis(g)

print ("20180219 ok!")