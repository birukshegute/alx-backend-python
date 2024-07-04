#!/usr/bin/env python3
"""
a string k and an int OR float v as arguments and returns a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    a string k and an int/float v as arguments and returns a tuple.
    """
    return (k, v**2)
