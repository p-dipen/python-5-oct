from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError,ConnectionFailure

uri = "mongodb://localhost:27017/"
try:
    client = MongoClient(uri,serverSelectionTimeoutMS=2000)
    client.admin.command("ping")
    print("Connected successfully")
    # other application code
except ConnectionFailure:
    print("ConnectionFailure handle properly")
except Exception as e:
    raise Exception("The following error occurred: ", e)


database= client["schooldb"]
cursor = database["students"]

cursor.insert_one({'school':"xyz", "name": "qsdqd"})

for data in cursor.find_one({"school":"xyz"}):
    print(data)