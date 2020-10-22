#!/usr/bin/env python3
""" Import Modules """

import random
from asyncio import sleep
from typing import Generator, AsyncGenerator


async def async_generator() -> Generator[float, None, None]:
    """ Async Generator """
    for _ in range(10):
        await sleep(1)
        yield random.uniform(0, 10)
