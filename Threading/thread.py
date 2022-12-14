import threading

def func1():
    for x in range(10000):
        print("ONE")

def func2():
    for x in range(10000):
        print("TWO")

def hi():
    for i in range(50):
        print("HI")

def bye():
    for i in range(50):
        print("BYE")

# Create a thread, pass it worker function as target argument
# can create multiple
t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

# Runs thread/s, all are run from main thread
#t1.start()
#t2.start()

t3 = threading.Thread(target=hi)
t4 = threading.Thread(target=bye)
t3.start()

# Means next line cannot run until t3 thread is complete
t3.join() 
t4.start()