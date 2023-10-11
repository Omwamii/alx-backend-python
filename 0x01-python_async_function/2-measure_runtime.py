#!/usr/bin/env python3
""" module 2 """
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measures total exec time for wait_n(n, max_delay)
        returns: total_time / n
    """
    s_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    e_time = time.time()
    t_time = e_time - s_time
    a_time = t_time / n
    return a_time
