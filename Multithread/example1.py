import threading 

def cookPasta():
    print(f"[{threading.current_thread().name}] Boiling Water")
    print(f"[{threading.current_thread().name}] Add pasta veggies")
    print(f"[{threading.current_thread().name}] Add sauce")
    print(f"[{threading.current_thread().name}] Pasta is ready")
    
#similarly create a helper function to makesalad and then two separate threads will be created and these specific methods will be passed as target

def makeSalad():
    print(f"[{threading.current_thread().name}] Washing vegetables")
    print(f"[{threading.current_thread().name}] cutting vegetables")
    print(f"[{threading.current_thread().name}] adding salt")
    print(f"[{threading.current_thread().name}] Salad is ready")

chef1=threading.Thread(target=cookPasta,name="Chef Pasta")
chef2=threading.Thread(target=makeSalad,name="Chef Salad")

chef1.start()
chef2.start()

#using .join() for waiting both of them to finish
chef1.join()
chef2.join()

print("All done !!")
 
    