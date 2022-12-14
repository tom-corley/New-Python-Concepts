import threading

# An event can be set off, and can be waited for
event = threading.Event()

def myfunction():
    print("Waiting for event to trigger...")
    event.wait()
    print("Even triggered, peforming...")

t1 = threading.Thread(target=myfunction)
t1.start()

x = input("Do you want to trigger the event? (y/n): ")
if x == "y":
    event.set()

t1.join()
print("done")
