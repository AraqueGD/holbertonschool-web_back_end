#!/usr/bin/env python3
""" List Documents with Pymongo """


def list_all(mongo_collection):
    """ List all """
    documents = mongo_collection.find()

    if (documents.count() == 0):
        return []

    return documents
