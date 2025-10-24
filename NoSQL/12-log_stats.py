#!/usr/bin/env python3
"""
Provides stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def total_logs(collection):
    """Return total number of logs in the collection."""
    return collection.count_documents({})


def method_stats(collection):
    """Return a dictionary with counts of each HTTP method."""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    stats = {}
    for method in methods:
        stats[method] = collection.count_documents({"method": method})
    return stats


def status_check(collection):
    """Return the count of GET /status requests."""
    return collection.count_documents({"method": "GET", "path": "/status"})


def main():
    """Main function to print Nginx logs statistics."""
    with MongoClient() as client:
        collection = client.logs.nginx

        print(f"{total_logs(collection)} logs")
        print("Methods:")
        for method, count in method_stats(collection).items():
            print(f"\tmethod {method}: {count}")
        print(f"{status_check(collection)} status check")


if __name__ == "__main__":
    main()
