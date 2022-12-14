class person(object):
    population = 50 # class variable
    def __init__(self, name, age):
        self.name = name # instance variable
        self.age = age

    @classmethod # call on the class itself 1 or any instance 2 (instance optional)
    def getPopulation(cls):
        return cls.population

    @staticmethod # cannot be called on an instance, is just a feature of the class 3
    # cant use any attributes of the class
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, 'os')

newPerson = person('tim', 18)

print(person.getPopulation()) #1
print(newPerson.getPopulation()) #2
print(person.isAdult(19))