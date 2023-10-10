#!/usr/bin/env python3
""" Annotated module """
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """ duck-typed annotation """
    if lst:
        return lst[0]
    else:
        return None
