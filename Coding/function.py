# Chapter = 6: Functions help us organize our code in a way that’s reusable, and accept arguments and defaults where needed.

# sum of integers from 1 to 10, 20 to 37, 35 to 49
# define a function 

# 1. function's name
# 2. Parameters
# 3. body

# syntax -> 
'''
    def functionName(list of parameters):
        # function body 
'''

# void functions and return statement functions 

# Anatomy of a function
# This is the recipe for defining a Python function:

# def: the def keyword, telling Python we’re about to start a function definition
#  a name for the function
# (: opening parenthesis
# (optional) the names of one or more arguments, separated with ,
# (optional) the names and values of one or more default arguments/parameters, separated with (,) note: we’ll see these in the next section
# ) closing parenthesis
# : a colon

# Then, an optional `return` statement can follow, if the function plans on passing data back to the caller.


# declare a function 
def sum(i1, i2=0):
    result = 0
    for i in range(i1, i2+1):
        print("Inside sum i = ", i)
        result += i
        print("Inside sum result = ", result)

        if result >= 5:
            return result

    #  returning the result or not ? 
    return result
# a custom function 
def main():
    sum1 = sum(1, 10)
    print("Sum of integers from 1 to 10 is ", sum1)
    print("Sum of integers from 20 to 37 is ", sum(20, 37))
    print("Sum of integers from 35 to 49 is ", sum(35, 49))

if __name__ == "__main__":
    main()