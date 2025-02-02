#!/usr/bin/env python3
"""
performs the task of task_wait_n function
"""

import asyncio
import random
from typing import List


task_wait_rand: float = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns  task_wait_random function n times
    """

    tasks: List[asyncio.Task] = [(task_wait_rand(max_delay)) for _ in range(n)]
    delays: List[float] = [await task for task in asyncio.as_completed(tasks)]

    return delays
