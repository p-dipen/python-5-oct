To create a class, use the keyword `class` 

class MyClass:
    x = 5


Create object -> instance of the class

p1 = MyClass()

print(p1.x)

del p1


class Person:
    pass

    

All classes have a built in method called `__init__()`, which is always executed when the class is being initiated. 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("emil",36)
p2 = Person("dipen",30)
