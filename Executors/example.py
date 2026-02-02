#Here python provides two types of executors one is ThreadPoolExecutor and other is ProcessPoolExecutor

#Example of thread executor in python
from concurrent.futures import ThreadPoolExecutor
import time 

def work(n):
    time.sleep(1)
    return f"Task {n} done"

#now the next step is to create an executor
#three worker threads extra tasks wait in the queue
with ThreadPoolExecutor(max_workers=3) as executor:
    futures=[]
    for i in range(5):
        future=executor.submit(work,i)
        futures.append(future)
    for ele in futures:
        print(ele.result())
        