#!/usr/bin/env python3
"""
Performs the measure_runtime function
"""

import asyncio
import time
from typing import List, Generator


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    executes async_comprehension four times in parallel
    Also measure the total runtime and return it.
    """
    start_time: float = time.time()
    await asyncio.gather(
        async_comprehension(), async_comprehension(),
        async_comprehension(), async_comprehension()
    )
    end_time: float = time.time()
    return end_time - start_time
