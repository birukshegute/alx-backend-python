#!/usr/bin/env python3
"""
performs the task of the function wait_n
"""

import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns  wait_random function n times
    """

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asynchio.as_completed(tasks)]

    return delays
