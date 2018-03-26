# coding=utf-8    
import threading, time, random
count = 0
class Counter(threading.Thread):
    def __init__(self, lock, threadName):
        '''@summary: 初始化对象。
        
        @param lock: 琐对象。
        @param threadName: 线程名称。
        '''
        super(Counter, self).__init__(name = threadName)  #注意：一定要显式的调用父类的初始化函数。
        self.lock = lock
    
    def run(self):
        '''@summary: 重写父类run方法，在线程启动后执行该方法内的代码。
        '''
        global count
        self.lock.acquire()
        for i in xrange(10100):
            count = count + 1
        self.lock.release()
lock = threading.Lock()
for i in range(8): 
    Counter(lock, "thread-" + str(i)).start()
    print Counter.name
time.sleep(2)    #确保线程都执行完毕
print count