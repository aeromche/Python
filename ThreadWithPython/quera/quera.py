import threading
import time

def f1():
    time.sleep(3)
    print("f1 finished")

def f2():
    time.sleep(4)
    print("f2 finished")

def f3():
    time.sleep(1)
    print("f3 finished")

def f4():
    time.sleep(2)
    print("f4 finished")



def g1():
    time.sleep(2)
    print("g1 finished")

def g2():
    time.sleep(5)
    print("g2 finished")



def h():
    time.sleep(1)
    print("h finished")


thread_1 = threading.Thread(target=f1,name="f1")
thread_2 = threading.Thread(target=f2,name="f2")
thread_3 = threading.Thread(target=f3,name="f3")
thread_4 = threading.Thread(target=f4,name="f4")

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()


thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

thread_5 = threading.Thread(target=g1,name="g1")
thread_6 = threading.Thread(target=g2,name="g2")

thread_5.start()
thread_6.start()

thread_5.join()
thread_6.join()

thread_7 = threading.Thread(target=h,name="h")

thread_7.start()