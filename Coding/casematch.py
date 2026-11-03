year = int(input("Enter a year: "))
zodiacYear = year % 12
print(zodiacYear)
match zodiacYear > 5:
    case True: print("True")
    case False: print("false")

match zodiacYear:
    case 0: print("monkey")
    case 1: print("rooster")
    case 2: print("dog")
    case 3: print("pig") 
    case 4: print("rat")
    case 5: print("ox") 
    case 6: print("tiger") 
    case 7: print("rabbit") 
    case 8: print("dragon") 
    case 9: print("snake") 
    case 10: print("horse")
    case 11: print("sheep")
    case _:
        print("default")
# if zodiacYear == 0:
#     print("monkey")
# elif zodiacYear == 1:
#     print("rooster")
# elif zodiacYear == 2:
#     print("dog")
# elif zodiacYear == 3:
#     print("pig")
# elif zodiacYear == 4:
#     print("rat")
# elif zodiacYear == 5:
#     print("ox")
# elif zodiacYear == 6:
#     print("tiger")
# elif zodiacYear == 7:
#     print("rabbit")
# elif zodiacYear == 8:
#     print("dragon")
# elif zodiacYear == 9:
#     print("snake")
# elif zodiacYear == 10:
#     print("horse")
# else:
#     print("sheep")