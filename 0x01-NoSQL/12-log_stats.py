#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB"""


import pymongo


if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    db_collection = client.logs.nginx
    
    print("{} logs".format(db_collection.count_documents({})))
    print("Methods:")
    print("\tmethod GET: {}".format(db_collection.count_documents({"method": "GET"})))
    print("\tmethod POST: {}".format(db_collection.count_documents({"method": "POST"})))
    print("\tmethod PUT: {}".format(db_collection.count_documents({"method": "PUT"})))
    print("\tmethod PATCH: {}".format(db_collection.count_documents({"method": "PATCH"})))
    print("\tmethod DELETE: {}".format(db_collection.count_documents({"method": "DELETE"})))
    print("{} status check".format(db_collection.count_documents({"method": "GET", "path": "/status"})))
