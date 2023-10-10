from threading import Thread
import threading


class Greet:
    def __init__(self):
        self.helloLock = threading.Lock()
        self.byeLock = threading.Lock()
        self.byeLock.acquire()

    def hello(self):
        self.helloLock.acquire()
        print('hello', end=' ')
        self.byeLock.release()
    def bye(self):
        self.byeLock.acquire()
        print('bye', end=' ')
        self.helloLock.release()

greet = Greet()

th_1 = Thread(target=greet.bye)
th_2 = Thread(target=greet.bye)
th_3 = Thread(target=greet.hello)
th_4 = Thread(target=greet.hello)


th_1.start()
th_2.start()
th_3.start()
th_4.start()