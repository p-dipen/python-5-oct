# How to define a variable which you will use to track your repeat count

# count = 1

# start from 0 then when end ? 99 or 100 

# count == 100 or count < 101


# Two type of loops 
# 1. Condition-controlled loop 
# while loop


# 2. count-controlled loop
# for loop


# syntax 

"""

        while loop-continuation-condition:
            #loop body
            Statements

"""

# # count == 100 or count < 101
# count = 0 
# endCount = 51
# while count < endCount:
#     # loop body
#     print("1. Programming is fun ",count)
#     count = count + 5 # Increment by 5

# count = 0
# print("What is the current value of count after updating the value = ",count)
# while endCount > count: 
#     # loop body
#     print("2. Programming is fun ",count)
#     count = count + 5
#     print("Last printing statement in the program",count)
# # End of program
    




# #  range(
# #     start: SupportsIndex,
# #     stop: SupportsIndex,
# #     step: SupportsIndex = 1
# # )
# # Count-Control loop
# # 5, 4 , 3, 2, 1
# # seq < stop

# break -> terminate your loop
# continue -> skip exec of loop code for a particular elements
import sys
a = ["apple", "mongo", "orange", "banana", "pear"]
print(len(a))
seq = range(len(a)) # Start ? = 3 , Stop = 20, Step = 2
for count in seq:
    # print("Print the sequence in the range=",count)
    if a[count] == "orange":
        print("It is in the if condition block code",a[count])
        # continue
        sys.exit() 


    print("THis is ", a[count])


print("End of the loop")


# 1. Standard Division (/)
# 2. Floor / Integer Division (//)
# 3. Modulo (%)



"""

*
**
***
****
*****

1
12
123
1234
12345

"""

# count = 0
# endCount = 5
# for x in range(count, endCount):
#     for y in range(0,x+1):
#         print("*",end="")

#     print(end="\n")
    

# count = 0

# while count < 5:
#     count = count+1
#     print("*" * count)



# sum = 0 # define and declare value zero
# number = 0

# while number < 20:
#     number += 1
#     sum += number
#     if sum >= 100:
#         break

# print("The number is after loop ", number)
# print("the sum is ", sum)