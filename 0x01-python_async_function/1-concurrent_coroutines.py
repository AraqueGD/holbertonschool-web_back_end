#!/usr/bin/env python3
""" Import Modules """
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(max_delay: int, n: int) -> List[float]:
    """ Append Times in Array """
    q, array = [], []
    for _ in range(n):
        q.append(wait_random(max_delay))

    for q in asyncio.as_completed(q):
        rta = await q
        array.append(rta)

    return array
