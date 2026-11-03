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

def getAllData():
    db = client["myFirstDatabase2"]
    collection = db["book"]
    return collection.find()