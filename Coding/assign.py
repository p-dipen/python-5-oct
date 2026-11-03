radius = 50 # Global scope (global variable)

def area():
    PI = 3.14 # local scope (local variable)
    print("before updating pi", PI)
    PI = 2.14 # in value 
    print("after updating pi", PI)

    area = radius * radius * PI
    
    return area

# print("the value of pi", pi)
print(area())


55 / 60 -> 0.9 is the minute 

190 // 60 -> 3 minutes (round nearest value)