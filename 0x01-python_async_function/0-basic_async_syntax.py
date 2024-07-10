#!/usr/bin/env python3
"""
an asynchronous coroutine that completes wait_random function.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    takes in an integer argument that waits
    for a random delay between 0 and the integer
    """
    delay1: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay1)

    return delay1
