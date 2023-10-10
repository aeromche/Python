import threading
import time

def getUserLong(name,age,job):
    time.sleep(4)
    print(f"{name}/{age}/{job}")

def getUserMiddle(name,age,job):
    time.sleep(2)
    print(f"{name}/{age}/{job}")

def getUserShort(name,age,job):
    time.sleep(1)
    print(f"{name}/{age}/{job}")

userLong = threading.Thread(target=getUserLong,args=["abbas","32","ML programmer"],name="LongProccess")
userMiddle = threading.Thread(target=getUserMiddle,kwargs={"name":"Hossein","age" :"27","job":"Doctor"},name="MiddleProccess")
userShort = threading.Thread(target=getUserShort,args=("Arian","20","Developer"),name="ShortProccess")

userMiddle.start()
userShort.start()
userLong.start()
