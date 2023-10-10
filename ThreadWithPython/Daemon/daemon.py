import threading
import time

def printHello():
    time.sleep(5)
    print("Hello")


myThread = threading.Thread(target=printHello,name="sayHello")
myThread.setDaemon(True)
myThread.start()



print("\nend")

print(myThread.is_alive())