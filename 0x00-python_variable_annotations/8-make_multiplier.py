#!/usr/bin/env python3
""" annotated module """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ return a function that multiplies a float by multiplier
    """
    def mult(num: float) -> float:
        """ multiply number by multiplier """
        return multiplier * num
    return mult
