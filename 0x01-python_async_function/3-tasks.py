#!/usr/bin/env python3
""" Import Modules """
from asyncio import Task, create_task

wait_random = wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ Return Async Task """
    task = create_task(wait_random(max_delay))
    return task
