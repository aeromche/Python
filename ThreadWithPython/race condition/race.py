import threading
import time

count = 0

def plus():
    global count
    for _ in range(1,101):
        count += 1
    
def plus2():
    global count
    count += 40

plus()
print(count)
plus2()
print(count)