# Displaying Prime Numbers

# Key Point
# This section presents a program that displays the first Ten/fifty prime numbers in five lines, each containing ten numbers.
# An integer greater than 1 is prime if its only positive divisor is 1 or itself. For example, 2, 3, 5, and 7 are prime numbers, but 4, 6, 8, and 9 are not.

# The problem can be broken into the following tasks:

# Determine whether a given number is prime.
# For number = 2, 3, 4, 5, 6, …, test whether the number is prime.
# Count the prime numbers.
# Display each prime number, and display ten numbers per line.

# Write steps how the program flow should be - 
# We need use % module if number is not divisible when module will not zero
# 2....number-1
# numberSix = 6



# numberSix = 6
# for deno in range(2, numberSix):
#     if numberSix % deno == 0:
#         print(f"{numberSix} is not a prime number")
#         break


currentNumber = 2
totalNumberOfPrime = 0
currentCountInSingleLine = 0
#tab key
while totalNumberOfPrime < 50:
    isPrime = True
    for deno in range(2, currentNumber):
        if currentNumber % deno == 0:
            # print(f"{currentNumber} is not a prime number")
            isPrime = False
            break

    if isPrime == True:
        currentCountInSingleLine += 1
        print(f"{currentNumber}", end=" ")
        if currentCountInSingleLine == 10:
            print("")
            currentCountInSingleLine = 0
        totalNumberOfPrime += 1

    currentNumber += 1


