#Locks ensure that only one thread can access shared resource at a time

#If locks are not there they may result in race conditions and locks ensure mutual exclusion
#Multiple threads can print the documents but only one can printer at time 

import threading
import time 

lock=threading.Lock()

def printdocument(doc):
    with lock:
        print(f"{threading.current_thread().name} printing {doc}")
        time.sleep(1)
        print(f"{threading.current_thread().name} finished {doc}")
threads=[]
for i in range(3):
    t=threading.Thread(target=printdocument,args=(f"Doc:{i+1}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
    
#these Locks are basically the non entrant ones that is they cant be acquired more than once

    