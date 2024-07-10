#!/usr/bin/env python3
"""
performs the task of the function wait_n
"""

import asyncio
import random
from typing import List


wait_random: float = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns  wait_random function n times
    """

    tasks: List[float] = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: List[float] = [await task for task in asyncio.as_completed(tasks)]

    return delays
