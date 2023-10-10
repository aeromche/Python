import threading


def sum(max):
    ans = 0;
    print(threading.currentThread().name)
    for i in range(1,max+1):
        ans += i
    print(ans)

sum1000 = threading.Thread(target=sum,args=[10 ** 8],name="thread 1 - 1000")
sum1000.start()

sum100 = threading.Thread(target=sum,args=[100],name="thread 1 - 100")
sum100.start()