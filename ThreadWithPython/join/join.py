import threading
import time

def cleanHome():
    time.sleep(5)
    print("clean home finished")

def cleanYard():
    time.sleep(3)
    print("clean yard finished")

def invitePeople():
    time.sleep(1)
    print("invite people finished")

homeThread = threading.Thread(target=cleanHome,name="home thread")
yardThread = threading.Thread(target=cleanYard,name="yard thread")
peopleThread = threading.Thread(target=invitePeople,name="invite thread")

homeThread.start()

yardThread.start()

homeThread.join()
yardThread.join()

peopleThread.start()