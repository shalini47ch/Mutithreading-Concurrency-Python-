#creating and destroying multiple threads is expensive so the best way is to create a thread pool with a fixed no of worker threads that reuse themselves for multiple tasks

#python provides threadpool through concurrent.futures import ThreadPoolExecutor this is termed as executor

from concurrent.futures import ThreadPoolExecutor

def task(n):
    return n*n 

with ThreadPoolExecutor(max_workers=3) as executor:
    futures=[]
    for i in range(5):
        futures.append(executor.submit(task,5))
    
    for future in futures:
        print(future.result())
        
#future in simple words means a value that is available in the future
