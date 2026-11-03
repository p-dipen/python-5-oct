# Object oriented programming (OOP) - large scale software 


# OOP allows us to represent our code in a different way, organized into classes

#OOP is language model in which properties or behavior are organized into objects

# what is object ? 
# function, a variable, property, a class everything in python is an object. 

#list object -> int object, string object, 

# int object _> contain integer number as value multiple methods (int.float() )

# object -> attributes and methods 
# keyword -> class, self 
class Car:
    runs = True # attribute

    def getStatus(self): # method
        if self.runs:
            print("Car is running. Vroom vromm")
        else:
            print("Car is stop")

    def start(self):
        if self.runs:
            print("Car is already running")
        else:
            self.runs = True
            print("Car is started")

    def stop(self):
        if self.runs:
            self.runs = False
            print("Car is stopped")
        else:
            print("Car is already ideal")


my_car = Car()

my_car.start()