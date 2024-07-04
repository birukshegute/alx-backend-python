#!/usr/bin/env python3
"""
Augmenting with the correct duck-typed annotations:
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    returns the first element of lst
    """
    if lst:
        return lst[0]
    else:
        return None
