import threading
import time

myLockerFor1 = threading.Lock()
myLockerFor3 = threading.Lock()
myLockerFor1.acquire()
myLockerFor3.acquire()

def print1():
    myLockerFor1.acquire()
    print('1',end='')

def print2():
    print('2',end='')
    myLockerFor3.release()

def print3():
    myLockerFor3.acquire()
    print('3',end='')
    myLockerFor1.release()

th_3 = threading.Thread(target=print3)
th_2 = threading.Thread(target=print2)
th_1 = threading.Thread(target=print1)

th_1.start()
th_2.start()
th_3.start()