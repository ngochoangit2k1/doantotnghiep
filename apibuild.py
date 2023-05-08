from  dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())
connection_string = f"mongodb+srv://shopforme34:shopforme34@cluster0.f3g5jcd.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

dbs = client.list_database_names()
test_db = client.test
collections = test_db.list_collection_names()
print(collections)

def insert_test_doc():
    collections = test_db.test
    test_document = {
        "name" : "A",
        "type" : "test"
    }
    inserted_id = collections.insert_one(test_document).inserted_id
    print(inserted_id)

insert_test_doc()