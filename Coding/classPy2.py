#initializer 

# class ClassName:
    # initializer
    # method
import math

class Circle:
    #Construct a circle object
    radius = int(input("Enter radius")) 
    def getArea(self):
        return self.radius * self.radius * math.pi


myCircle = Circle()

print(myCircle.getArea())


To make python program which can connect to multiple database depend up the user input you are going work with that database 


I want to make 3 function 

writeData
getSchema
readData

import databaseConnectivity

def putCreditInformation:
    isSuccess = databaseConnectivity.writeData("credit1")