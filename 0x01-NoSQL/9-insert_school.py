#!/usr/bin/env python3
''' Graham S. Paul - 9-insert_school.py
'''


def insert_school(mongo_collection, **kwargs):
    ''' Adds new document in a collection.
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
