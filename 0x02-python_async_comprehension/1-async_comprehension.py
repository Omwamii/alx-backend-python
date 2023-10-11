#!/usr/bin/env python3
""" module 1 """
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ return  values yielded from async fn in list
    """
    result = [i async for i in async_generator()]
    return result
