#!/usr/bin/env python3
""" module 0 """
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """ yield random number """
    for _ in range(0, 10):
        yield random.uniform(0, 10)
