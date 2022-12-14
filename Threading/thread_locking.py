import threading 
import time

x = 8192

# locks access to memory,
lock = threading.Lock()
# Limited exclusive access to memory
semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print(f"{thread_number} is trying to access")
    semaphore.acquire()
    print(f"{thread_number} was granted access!")
    time.sleep(10)
    print(f"{thread_number} is now releasing!")
    semaphore.release()

for thread_number in range(1,11):
    t = threading.Thread(target=access, args = (thread_number,))
    t.start()
    time.sleep(1)

def half():
    global x,lock
    # half takes the lock for himself, stopping other thread
    lock.acquire()
    while x > 1:
        x = 0.5*x
        print(x)
        time.sleep(1)
    print("Reached min")
    lock.release()

def double():
    global x, lock
    # double cannot accquire access to x until the lock
    # is released by half
    lock.acquire()
    while x < 16384:
        x = 2*x
        print(x)
        time.sleep(1)
    print("Reached Max")
    lock.release()

t1 = threading.Thread(target=half)
t2= threading.Thread(target=double)
t1.start()
t2.start()