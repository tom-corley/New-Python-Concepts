li = [ i for i in range(1,11)]
def func(x):
    return x**x

# Without Map function using list comprehension 
print([func(i) for i in li])

#using map
print(list(map(func,li)))
