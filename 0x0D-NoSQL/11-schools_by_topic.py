#!/usr/bin/env python3
""" Find Results Topics """


def schools_by_topic(mongo_collection, topic):
    """ With PyMongo Find Documents """
    results = mongo_collection.find({"topics": topic})

    for result in results:
        return result
