#!/usr/bin/env python3
"""
This script provides statistics about Nginx logs stored in MongoDB
using a single aggregation pipeline for maximum efficiency.
"""
from pymongo import MongoClient


def log_stats_aggregate():
    """
    Uses MongoDB's aggregation framework to get all stats in one query.
    """
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    # Define the aggregation pipeline
    pipeline = [
        {
            "$group": {
                "_id": "$method",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"_id": 1}  # Sort to ensure order, though not strictly needed
        }
    ]

    # Get method counts
    method_counts = {
        "GET": 0,
        "POST": 0,
        "PUT": 0,
        "PATCH": 0,
        "DELETE": 0
    }
    
    results = collection.aggregate(pipeline)
    for result in results:
        if result["_id"] in method_counts:
            method_counts[result["_id"]] = result["count"]

    # Get total logs count
    total_logs = collection.count_documents({})

    # Get status check count
    status_check = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })

    # Print all stats
    print(f"{total_logs} logs")
    print("Methods:")
    print(f"\tmethod GET: {method_counts['GET']}")
    print(f"\tmethod POST: {method_counts['POST']}")
    print(f"\tmethod PUT: {method_counts['PUT']}")
    print(f"\tmethod PATCH: {method_counts['PATCH']}")
    print(f"\tmethod DELETE: {method_counts['DELETE']}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats_aggregate()