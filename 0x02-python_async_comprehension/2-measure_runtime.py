#!/usr/bin/env python3
""" module 2 """
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure avg time for 4 loops of async_comprehension
    """
    s_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    e_time = time.time()
    return e_time - s_time
