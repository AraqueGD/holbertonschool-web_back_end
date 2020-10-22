#!/usr/bin/env python3
""" Import Modules """

import asyncio
from time import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """ Async Measure Run Time """
    start = time()
    t = [async_comprehension() for i in range(4)]
    await asyncio.gather(*t)
    end = time()
    return (end - start)
