#!/usr/bin/env python3
"""
Measures the elapsed time of task 1
"""


import asyncio
import random
from typing import List
import time


wait_n: List[float] = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the elapsed time of task 1
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    total_time: float = end_time - start_time

    return total_time/n
