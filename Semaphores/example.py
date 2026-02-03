#Semaphores control how many resources can access a thread at once
import threading 
import time 

sem=threading.Semaphore(2)
def task(name):
    with sem:
        print(f"{name} entered")
        time.sleep(1)
        print(f"{name} ending")
for i in range(5):
    threading.Thread(target=task,args=("hello",)).start()

