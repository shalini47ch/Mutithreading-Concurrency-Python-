#Here we will use reentrant lock to solve this 
#Reentrant lock allows the same thread to acquire it multiple times 
#so we can use a function with lock inside another function and in that case reentrant lock with be useful
import threading 

lock=threading.RLock()

def outer():
    with lock:
        print("outer")
        inner()
def inner():
    with lock:
        print("inner")

#now the next step is to create the thread
t=threading.Thread(target=outer)
t.start()
t.join()
