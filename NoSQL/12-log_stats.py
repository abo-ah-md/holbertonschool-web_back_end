#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def total_logs(collection):
    """Return total number of documents in the collection."""
    return collection.count_documents({})


def method_stats(collection):
    """Return a dictionary with counts of each HTTP method."""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    stats = {}
    for method in methods:
        stats[method] = collection.count_documents({"method": method})
    return stats


def status_check(collection):
    """Return the number of GET /status requests."""
    return collection.count_documents({"method": "GET", "path": "/status"})


def main():
    """Print Nginx logs statistics."""
    client = MongoClient()
    collection = client.logs.nginx

    # Total logs
    print(f"{total_logs(collection)} logs")

    # Methods stats
    print("Methods:")
    for method, count in method_stats(collection).items():
        print(f"\tmethod {method}: {count}")

    # GET /status requests
    print(f"{status_check(collection)} status check")


if __name__ == "__main__":
    main()
