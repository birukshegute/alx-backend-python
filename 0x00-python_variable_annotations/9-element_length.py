#!/usr/bin/env python3
"""
Annotate the function’s parameters and return values
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns length of element
    """
    return [(i, len(i)) for i in lst]
