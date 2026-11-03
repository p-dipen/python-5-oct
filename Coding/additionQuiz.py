# Generate random numbers 
# in-built namespace or built-in functions
# print(dir(__builtins__))

# standard libraru modules 
from random import choice,randint 

number1 = randint(0,9)
number2 = randint(0,9)
message = f"What is {number1} + {number2}?"

userInput = int(input(message))
print("Sum=",number1 + number2)
print("userInput=",userInput)

if userInput == number1 + number2:
    print("successfully match")
else:
    print("better luck new time")