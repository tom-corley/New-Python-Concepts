import queue

# Structured way of managing multiple threads

numbers = [10*i for i in range(1,11)]
q = queue.Queue()

# 1, 2, 3, 4, 5
#1
# 2, 3, 4, 5
for number in numbers:
    q.put(number)

# gets from front of queue (and removes), 
# FIFO, queue is now shorter
print(q.get())
print(q.get())
print("\n\n")

r = queue.LifoQueue() # Stack
for x in numbers:
    r.put(x)
print(r.get())
print(r.get())
print("\n\n")

s = queue.PriorityQueue()

# elements have attatched priortiy from 1-100, use indexing
s.put((2, "HelloWorld"))
s.put((11,99))
s.put((5,7.5))
s.put((1, True))

while not s.empty(): # s.empty() returns true if queue is empty
    print(s.get()[1])