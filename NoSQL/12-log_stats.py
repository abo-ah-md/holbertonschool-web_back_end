#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    collec = client.logs.nginx

    print(f"{collec.count_documents({})} logs")
    print("Methods:")
