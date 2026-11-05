# Opening and closing files : the `with` statement - file stream 

# f = open("data.txt", "w")
# f.write("Important data")
# print("Is file closed ? ", f.closed)
# f.close()
# print("After Is file closed ? ", f.closed)

# content = ""
# with open("data.txt", "r") as f:
#     content = f.read() # 50 Gb file 
#     print(content)
#     content = content.replace("Dipen","CBC")
#     content = content.replace("Parihar","DSAI")
#     print(content)


# with open("data.txt", "a") as f:
#     f.write(content)



# `open(filename, mode)`


os.path


target_file = "/User/dipenpariahr/d/class/connectivity.py" # Exist doesnt exists

try:
    with open(target_file, 'r') as f:
        data = f.read()
        print(data)
except FileNotFoundError as e:
    print("Missing file doesnt exists")
except PermissionError as e:
    print("Access Denied")
except IsADirectoryError:
    print()
except IOError as io:
    print()
except Exception as e:
    print()





print("This is important statement this need to be printed")