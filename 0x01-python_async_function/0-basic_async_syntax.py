#!/usr/bin/env python3
""" module 0 """
import random
import asyncio


async def wait_random(max_delay=10):
    """ wait for random time & return wait time
    """
    val = random.uniform(0, max_delay)
    await asyncio.sleep(val)
    return val
