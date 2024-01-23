#!/usr/bin/env python3
''' Graham S. Paul - 11-schools_by_topics.py
'''


def schools_by_topic(mongo_collection, topic):
    ''' Reinstate list of school having a specific topic.
    '''
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
