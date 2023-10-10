#!/usr/bin/env python3
""" annotated module """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return tuple of str and square of number """
    return k, v * v
