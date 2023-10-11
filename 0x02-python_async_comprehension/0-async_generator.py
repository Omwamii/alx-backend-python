#!/usr/bin/env python3
""" module 0 """
import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """ yield random number """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
