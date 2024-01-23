#!/usr/bin/env python3
''' Graham S. Paul (12-log_stats.py)
'''
from pymongo import MongoClient


def provides_stats():
    """ givess Stats Function """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs.nginx

    print(f"{db.count_documents({})} logs")
    print("Methods:")

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    for method in methods:
        print(f"\tmethod {method}: {db.count_documents({'method': method})}")

    status_get = db.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status_get} status check")


if __name__ == "__main__":
    provides_stats()
