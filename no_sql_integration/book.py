# 1. Import the library 
import pymongo
from pymongo.errors import ConnectionFailure
import sys

# 2. Connect to local MongoDB
try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    client.admin.command("ping")
    # Database name
    db = client["myFirstDatabase2"]
    # Collection Name if collection doesnt exits it will create the collection
    collection = db["book"]
    print("Successfully connected to mongodb!")
except ConnectionFailure:
    print("Network error: General failure connting to mongodb")
except Exception as e:
    print(f"Something else went wrong: {e}")
    sys.exit()


# Contact book application 
# 1. Add a new contact
# 2. View all contact
# 3. Search for a contact
# 4. Delete a contact
# 5. exit
while True:
    print("\n---- 📞 My Contact Book ----")
    print("1. Add a new contact")
    print("2. View all contact")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. exit")

    choice = input("Choose an option (1-5):")

    if choice == '1':
        #Create
        name = input("Enter a name: ")
        number = input("Enter a number: ")
        collection.insert_one({"name":name, "number":number})
        print(f"{name} added successfully")
    elif choice == '2':
        print("\n--- All Contacts ----")
        contacts = collection.find()
        for contact in contacts:
            print(f"{contact['name']} - {contact.get('number', 'N/A')}")
    elif choice == '3':
        print("3 is selected")
    elif choice == '4':
        print("4 is selected")
    elif choice == '5':
        print("5 is selected")
        print("GoodBye 👋")
        break
    else:
        print("Invalid choice, Please pick a number from 1 to 5.")