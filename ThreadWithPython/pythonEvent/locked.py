import threading
import time

count = 0

def increase():
    global count
    lock = threading.Lock()
    for _ in range(500000):
         lock.acquire()
         count += 1
         lock.release()

def count_money():
    global count
    count = 0
    th_1 = threading. Thread(target=increase)
    th_2 = threading. Thread(target=increase)
    th_1.start()
    th_2.start()
    th_1.join()
    th_2.join()
for index in range(1, 6):
    count_money()
    print(f'count must be {500000} but count is {count}')
