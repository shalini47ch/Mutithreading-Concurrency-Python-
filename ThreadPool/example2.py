#Threadpool execution using a map
from concurrent.futures import ThreadPoolExecutor

def task(n):
    return n*n 


#
with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(task,[1,2,3,4,5])
print(list(results))