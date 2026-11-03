# print('he said', end="anyendingstring")


# some functions will requierd some parameters/request variables/agruments

def myOwnFunc(showOutput, name="system", debug=False):
    if debug:
        print("Hello you are using debug mode")

    #if showOutput:
        print("Calling my own func")
        if name != "":
            print("Function is called by ", name)
        print("End the myOwnFunc Call")
    else:
        print("Cant print anything")

myOwnFunc(True,debug=True, name="Dipen")
