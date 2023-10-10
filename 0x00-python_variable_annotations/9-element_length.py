#!/usr/bin/env python3
""" annotated module
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of elements in a list of sequences.

    Args:
        lst (Iterable[Sequence]): A list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains a sequence
        from the input list and its corresponding length as an integer.
    """
    return [(i, len(i)) for i in lst]
