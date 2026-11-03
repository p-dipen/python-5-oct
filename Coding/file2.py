import file1

print("file2 __name__2 = %s" %__name__)

if __name__ == "__main__":
    print("file2.py is being run directly")
else:
    print("file2.py is being imported")