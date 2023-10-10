import threading
from tasks import clean, invite, drink

cleanThread = threading.Thread(target=clean)
drinkThread = threading.Thread(target=drink)
inviteThread = threading.Thread(target=invite)


cleanThread.start()
drinkThread.start()

cleanThread.join()
drinkThread.join()

inviteThread.start()