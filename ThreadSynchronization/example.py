#Here we will use locks they allow only one thread to enter a critical section
import threading 

counter=0
lock=threading.Lock()

def increment():
    global counter
    for i in range(1000000):
        with lock:
            #so this part is critical section so make sure that no two threads access it at the same time
            counter+=1
threads=[]
for i in range(2):
    t=threading.Thread(target=increment)
    threads.append(t)
    t.start() #means it has moved from the new to the runnable state

for t in threads:
    t.join()
print(counter)

            
        