#!/usr/bin/env python3
"""
akes a float multiplier as argument and returns
a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies a float by multiplier
    """
    def multiplies(n: float):
        """
        multiply the float with the multiplier
        """
        return n * multiplier
    return multiplies
