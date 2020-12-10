#!/usr/bin/env python3
""" Change Topics Documents """


def update_topics(mongo_collection, name, topics):
    """ Update Topics """
    q = {"name": name}
    new_q = {"$set": {"topics": topics}}
    mongo_collection.update_many(q, new_q)
