from collections import deque #substitute for a list when:
# double ended queue

d = deque("hello")
d.append("nigel")
d.appendleft("crikey")
d.pop() #removelast by default or an argumented index
d.popleft() #remove first
# d.clear() remove all from deque
print(d)
d.extend('nigel') # breaks down and puts at end
d.extendleft([1,2,3]) # same but front, does it backwards e. g 123 -> 3,2,1
d.rotate(10)  # rotate indexes along mod length
print(d)

r = deque("rabbl", maxlen=5) # maxlen is final, cannot be updated after instance
r.append(1) # removes 1st element and rotates by -1 slots in at end
print(r)