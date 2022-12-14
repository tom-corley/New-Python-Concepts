a = [i for i in range(1,11)]

b = list(filter(lambda x: x%2==1,a)) # removes elements for which is odd does not return true
print(b)

c = list(map(lambda x: x+7, b)) # can use lambda function as argument for function
print(c)

print(list(map(lambda x: x**3+2*x,a)))