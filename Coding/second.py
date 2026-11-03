with open('example.txt', 'r') as file:
    context = file.read()
    print(context)

with open('example.txt', 'w') as file:
    file.write("hello, world! this is my first code")