#!/usr/bin/env python3
"""
This script provides statistics about Nginx logs stored in MongoDB.
It connects to the 'logs' database and 'nginx' collection.
"""
from pymongo import MongoClient


def log_stats():
    """
    Connects to MongoDB and prints statistics for the nginx logs
    using count_documents for efficiency.
    """
    # Connect to the MongoDB client
    client = MongoClient("mongodb://127.0.0.1:27017")

    # Access the logs.nginx collection
    collection = client.logs.nginx

    # 1. Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Methods
    print("Methods:")

    methods_list = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods_list:
        count = collection.count_documents({"method": method})
        # Note: The \t is a literal tab character for precise formatting
        print(f"\tmethod {method}: {count}")

    # 3. Status check (method=GET, path=/status)
    status_check_count = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
