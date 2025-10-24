#!/usr/bin/env python3
"""
This script provides statistics about Nginx logs stored in MongoDB
by iterating efficiently over the collection.
"""
from pymongo import MongoClient


def log_stats_iterator():
    """
    Iterates over the nginx collection cursor to count stats.
    """
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    total_logs = 0
    method_counts = {
        "GET": 0,
        "POST": 0,
        "PUT": 0,
        "PATCH": 0,
        "DELETE": 0
    }
    status_check = 0

    # Iterate over the cursor directly instead of loading into a list
    # This is much more memory-efficient
    for log_entry in collection.find():
        total_logs += 1
        
        method = log_entry.get("method")
        
        if method in method_counts:
            method_counts[method] += 1
        
        # Check for status check
        if method == "GET" and log_entry.get("path") == "/status":
            status_check += 1

    # Print the stats in the required format
    print(f"{total_logs} logs")
    print("Methods:")
    print(f"\tmethod GET: {method_counts['GET']}")
    print(f"\tmethod POST: {method_counts['POST']}")
    print(f"\tmethod PUT: {method_counts['PUT']}")
    print(f"\tmethod PATCH: {method_counts['PATCH']}")
    print(f"\tmethod DELETE: {method_counts['DELETE']}")
    print(f"{status_check} status check")


if __name__ == "__main__":
