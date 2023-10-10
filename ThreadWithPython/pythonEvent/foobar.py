import threading
import time


def fooPrint(num):
    for _ in range(0,num):
        fooLock.acquire()
        print('Foo',end='')
        fooLock.release()
        barLock.release()

def BarPrint(num):
    for _ in range(0,num):
        barLock.acquire()   
        print('Bar',end='')
        barLock.release()   



fooLock = threading.Lock()
barLock = threading.Lock()
# fooLock.acquire()
barLock.acquire()
inp = int(input())    
fooThread = threading.Thread(target=fooPrint,args=(inp,))
barThread = threading.Thread(target=BarPrint,args=(inp,))
barThread.start()
fooThread.start()