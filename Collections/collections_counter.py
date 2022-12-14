from collections import Counter

# Containers: list,set,tuple(immutable),dictionarry
# new containers from collections:
#Counter

c = Counter('gallad') # input is standard container or a string
d = Counter(['a','b'])
e = Counter({'a':1,'b':2})
f = Counter(cats=4, dogs=5)
print(c,d,e,f, sep = "\n")
print(f['cats'])
print(list(f.elements()))

print(f.most_common(1))

g = Counter(a=4, b=2, c=0, d=2)
h = Counter(['a','b','b','c'])
#g.subtract(h) # subtract them
print(g)
#g.update(h) # add them
print(g)
#g.clear()
print(g)
print("=============")
print(g+h, g-h,g&h,g|h, sep = "\n") # & and | for intersection and unions
