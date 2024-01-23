#!/usr/bin/env python3
''' Graham S. Paul - 8-all.py
'''


def list_all(mongo_collection):
    ''' Files all documents in a collection.
    '''
    return [doc for doc in mongo_collection.find()]
