#!/usr/bin/env python3
""" Import Modules """

from asyncio import sleep
from random import uniform
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """ Async comprehension """
    num_randoms = [idx async for idx in async_generator()]
    return num_randoms
