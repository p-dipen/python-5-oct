# Lists  - data type
# A list can store a collection of data of any size. 

# Lists are one of the most powerful data types in python. 

# Container objects 

# Creation of this object -> [], list() for empty list or [1,2,3] for a list with items
# used for storing similar items and in case where items need to be added or removed. 

list1 = [] # Create an empty list
list2 = [2,3,4] # Create a list with elements 2,3,4

list3 = ["red", "green"]

list4 = list(range(3,9))
print(list4)

list5 = list("ABCD")
# ["ABCD"] 
# ['A', 'B', 'C', 'D']
print(list5)

list6 = ["ABCD"]
print(list6)

# s[i] ith element in collection

# each element in list is recognized by index value and it start from 0

# list(dynamic) or Array(how many elements you want to keep)


# Search the item in the list 

list5.index('E')

'D' in list5

# count number of $ in the list 

list5 = list("ABCD######$$$$")
# loop?
count = 0
positionOfSymbolIndex = -1
for index in range(len(list5)):
    if list5[index] == "$":
        count += 1

    if count == 2:
        positionOfSymbolIndex = index
        break

print(positionOfSymbolIndex)
# count += 1 ==> count = count + 1
 

list7 = list(range(15))

# List slicing 
# Syntax list[start:end:step]

# tuple -> () -> immutable (Not add or remove)

# list -> [] -> mutable (add, remove modify)
temp = []
for num in list10:
    if num % 2 == 0:
        temp.append(num)

print(temp)



point1 = ["x1", "y1"]
point2 = ["x2", "y1"]
point3 = ["x2", "y2"]
point4 = ["x1", "y2"]

square = [point1,point2,point3,point4]

print(square)

import random

matrix = [] # Create an empty list
numberOfRows = eval(input("Enter the number of rows: "))
numberOfColumns = eval(input("Enter the number of columns: "))
for row in range(0, numberOfRows):
    matrix.append([]) # Add an empty new row
    for column in range(0, numberOfColumns):
        value = random.randrange(0,100)
        matrix[row].append(value)

print(matrix)

[[1, 2, 3, 4], 
 [5, 6, 7, 8], 
 [9, 10, 11, 12], 
 [13, 14, 15, 16]]





matrix = [
    [46, 48, 57, 69, 46, 13, 70, 38, 26, 59], 
    [31, 34, 10, 84, 0, 37, 41, 96, 81, 74], 
    [44, 98, 90, 10, 77, 22, 52, 67, 28, 28], 
    [92, 62, 84, 90, 6, 53, 31, 90, 46, 51], 
    [14, 87, 80, 10, 43, 45, 96, 1, 71, 2]]


for row in matrix:
    for value in row:
        print(value, end=" ")

    print()

for row in range(0, len(matrix)):
    for col in range(0, len(matrix[row])):
        print(matrix[row][col], end=" ")

    print()