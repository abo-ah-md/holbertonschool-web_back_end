#!/usr/bin/env python3
"""
Provides stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    collection = client.logs.nginx

    # Total number of documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods stats
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Status check (GET /status)
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")
