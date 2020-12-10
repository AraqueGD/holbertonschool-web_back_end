#!/usr/bin/env python3
""" Insert New Document With Pymongo """


def insert_school(mongo_collection, **kwargs):
    """ Insert Document """
    document = mongo_collection.insert(kwargs)
    return document
