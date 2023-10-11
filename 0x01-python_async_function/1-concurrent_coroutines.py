#!/usr/bin/env python3
""" module 1 """
import asyncio
import importlib
import random
from typing import List

wait_random = importlib.import_module('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ spawns wait_random n times with max_delay (random sleep time)
        Return: list of all delays with values in asc (floats)
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
