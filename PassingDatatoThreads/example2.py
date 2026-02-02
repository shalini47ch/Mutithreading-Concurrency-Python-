
#here we will see that theads can accept arguments just like regular functions 
import threading 

def greet(name,age):
    print(f"Hello {name}! You are {age} yrs old.")
    print(f"Running on thread:{threading.current_thread().name}")

#now the next step is creation of threads 
#so here we can pass the arguments using args also possible using kwargs
#args means tuple of arguments and kwargs means keyword arguments
thread1=threading.Thread(target=greet,args=("Alice",26),name="Demo thread")
thread2=threading.Thread(target=greet,kwargs={"name":"hanna","age":29})

thread1.start()
thread2.start()

thread1.join()
thread2.join()
    
    
