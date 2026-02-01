
# A thread goes through the following life cycle New=>Runnable=>Running=>Waiting/Blocked=>Terminated

#here is the implementation of the thread lifecycle step by step
import threading 

def workerJob():
    print(f"{threading.current_thread().name} is now running")
    print(f"{threading.current_thread().name} is doing the work")
    print(f"{threading.current_thread().name} is finishing up")


print("==Understanding the thread lifecycle")
thread=threading.Thread(target=workerJob,name="working thread")
print(f"\n This is the new state i.e stage 1")
print(f"\n Thread created:{thread.name}")
print(f"\n Is alive or not:{thread.is_alive()}")


#now the next state is the running or the runnable state that is when we use the .start() method
print(f"\n Stage2:Runnable/Running")
thread.start()
print(f"\n Thread started")
print(f"\n is alive {thread.is_alive()}")


#now when we use .join() that is the part we are waiting for the thread to finish
thread.join()

print(f"\n Stage3:Terminated")
print(f"\n Thread finished!!")
print(f"\n is alive:{thread.is_alive()}")



    

