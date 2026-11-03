weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
 
if weight > 0 and height > 0:
    bmi = weight / (height * height)
 
    print("Your BMI is: " + str(round(bmi, 2)))
 
    # Determine BMI category
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")

    if bmi >= 30:
        print("Obese")
    elif bmi >= 25:
        print("Overweight")
    elif bmi >= 18.5:
        print("Normal")
    else:
        print("Underweight")


else:
    print("Weight and height invalid.")