#!/usr/bin/env python3
""" module 3 """
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Takes max_delay & return async Task """
    task = asyncio.create_task(wait_random(max_delay))
    return task
