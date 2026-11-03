# 1. Import the library 
import pymongo
from pymongo.errors import ConnectionFailure

# 2. Connect to local MongoDB
try:
    host = "localhost"
    port = 27017
    client = pymongo.MongoClient(f"mongodb://{host}:{port}/")
    client.admin.command("ping")
    print("Successfully connected to mongodb!")
except ConnectionFailure:
    print("Network error: General failure connting to mongodb")
    # Hostname - localhost
    # port - 27017
    # username and password
    # database

# 3. Pick a database and collection 
db = client["myFirstDatabase"]

collection = db["collectionName"]

# for document in collection.find():
#     print(document)


# Create, read, update, delete operations
# What is JSON ? key and value 

    # {
    #     "name": "Jones Smith",
    #     "age": 28,
    #     "isStudent": true,
    #     "courses": ["NoSQL", "AI"]
    # }

# In python :
# A json object `{}` is called a Dictionary (dict) in python
# A JSON Array `[]` is called a List (list) in python
student = {
        "name": "Jones Smith",
        "age": 28,
        "isStudent": True,
        "courses": ["NoSQL", "AI"]
    }


collection.insert_one(student)

# more_users = [
#     {"name": "Bob", "age": 30, "role": "Designer"},
#     {"name": "Charlie", "age": 22, "role": "Intern"}
# ]
# collection.insert_many(more_users)
# print("Successfully inserted student into mongo")