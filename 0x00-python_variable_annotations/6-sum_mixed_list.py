#!/usr/bin/env python3
""" annotated module """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sums up float & int nums in list & returns sum
    """
    sm: float = 0
    for el in mxd_lst:
        sm += el
    return sm
