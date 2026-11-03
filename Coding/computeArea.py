# Radius 
#radius =  None # this will work or not 
# integer 
# #
# FUNCTION FOR DATA TYPE CONVERSION
# float(/*Any data type as input parameter*/)  covert any string or number to float data type 
# str() convert any number float boolean to string data type
stringInputResult = input("Enter radius:")
radius = float(stringInputResult) # IS ALWAYS GOING TO RETURN STRING DATA TYPE 

# Condition if radius is positive then only execute thiscode/
if radius > 0 :
    radiusInStr = str(radius)
    print("data type of variable radius:",type(radius))
    print("data type of variable radiusInStr:",type(radiusInStr))

    # area = radius * radis * pi 
    area = radius * radius * 3.14

    print("the area of the circle of radius ", radius, "is", area)
else:
    print("No negative radius")