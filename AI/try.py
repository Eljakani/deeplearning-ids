import pymongo
from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Access the database and collection
db = client['deeplearning_db']
collection = db['valid_packets']

# Query the data
documents = collection.find({})

# Process the retrieved data
for document in documents:
    print(document)
