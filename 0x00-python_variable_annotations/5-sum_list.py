#!/usr/bin/env python3
""" annotated module """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ sums up float nums in list & returns sum
    """
    sm: float = 0
    for el in input_list:
        sm += el
    return sm
