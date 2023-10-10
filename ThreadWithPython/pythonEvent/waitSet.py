import threading
import time

def inviting(invitingEvent):
    print("inviting Start")
    check = invitingEvent.wait(5)
    if check:
        print('yakhchi')
    else:
        print('bouyour')
    time.sleep(2)
    print("inviting Finish")

def cleaning(cleanEvent):
    print("cleaning Start")
    time.sleep(3)
    print('cleaning finish')
    cleanEvent.set()


myevent = threading.Event()
th_inviting = threading.Thread(target=inviting,args=(myevent,))
th_clean = threading.Thread(target=cleaning,args=(myevent,))


th_inviting.start()
th_clean.start()