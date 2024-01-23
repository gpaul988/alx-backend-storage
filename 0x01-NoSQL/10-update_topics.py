#!/usr/bin/env python3
''' Graham S. Paul - 10-update_topics.py
'''


def update_topics(mongo_collection, name, topics):
    ''' Substitutes every topics of a collection's document based on the name.
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
