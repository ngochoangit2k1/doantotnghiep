# import pymongo
import threading

import pymongo
from  dotenv import load_dotenv, find_dotenv
import os
import pprint
from queue import Queue
import time
from  bson.objectid import ObjectId
from pymongo import MongoClient, DESCENDING
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

test = client.production
products = test.timekeepings
MAX_QUEUE_SIZE = 10
def create_documents(first_name,last_name,ages):


    # first_name = ["a", 'b', "c"]
    # last_name = ['x','y','z']
    # ages =  [1,2,3]
    docs = []
    flag = True
    for first_name, last_name, ages in zip(first_name, last_name, ages):
        if flag:
            time.sleep(0.1)
            doc = {"fist": first_name, "last": last_name, "age": ages}
            docs.append(doc)
        else:
            time.sleep(1)

    products.insert_one(docs)



printer = pprint.PrettyPrinter()

MAX_QUEUE_SIZE = 5

def worker():
        while True:
            if not q.empty():
                data = q.get()
            # Thực hiện xử lý dữ liệu
                print(f"Processing data {data}...")
                time.sleep(1)
                q.task_done()

q = Queue(maxsize=MAX_QUEUE_SIZE)
worker_thread = threading.Thread(target=worker, daemon=True)
worker_thread.start()
first_name = ["a", 'b', "c","a", 'b', "c","a", 'b', "c","a", 'b', "c"]
last_name = ['x', 'y', 'z',"a", 'b', "c","a", 'b', "c","a", 'b', "c"]
ages = [1, 2, 3,1, 2, 3,1, 2, 3,1, 2, 3]
for first_name, last_name, ages in zip(first_name, last_name, ages):
        create_documents(first_name, last_name, str(ages))

# Đợi cho các dữ liệu trong queue được thực hiện xong
q.join()
print("All data processed.")

def find_all_people():
    people = products.find()
    # print(list(people))

    for person in people:
        printer.pprint(person)

find_all_people()
#
# test1x = test.test1
# test1x.create_index([("id", 1)], unique=True)

# tạo hàm để lấy giá trị sequence tiếp theo


# thêm document mới với _id tự động tăng dần
# def create_documents():
#     first_name = ["a",'b',"c"]
#     last_name = ['x','y','z']
#     ages =  [1,2,3]
#     docs = []
#
#     for first_name, last_name , ages in zip(first_name, last_name, ages):
#         doc = {"fist": first_name, "last": last_name, "age": ages}
#         docs.append(doc)
#
#     products.insert_many(docs)
# create_documents()
# in ra tất cả document trong collection
# for doc in test1x.find():
#     print(doc)