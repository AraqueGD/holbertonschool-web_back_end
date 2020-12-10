#!/usr/bin/env python3
""" Find Results Topics """


def schools_by_topic(mongo_collection, topic):
    """ With PyMongo Find Documents """
    results = mongo_collection.find({"topics": topic})
    list_rta = [r for r in results]
    return list_rta
