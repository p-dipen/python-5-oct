def printGrade(score):
    if score < 0 or score > 100:
        print("Invalid score")
        return # Same as return None
        
    if score >= 90.0:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")

# Special value none: void function/None function
def main():
    score = float(input("Enter a score: "))
    print("The grade is ", end = "")
    printGrade(score) # void function

main() # call the main function