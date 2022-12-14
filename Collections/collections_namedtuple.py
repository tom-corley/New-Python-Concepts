from collections import namedtuple

Point = namedtuple('point', 'x y z apple')

newP = Point(3,4,5, True)
print(newP.x, newP.y, newP.z)
# same ops as on basic tuples
print(newP._asdict())
print(newP._fields)

newnewP = newP._replace(z=7)
print(newnewP)

p2 = Point._make(['a','b','c'])
print(p2)