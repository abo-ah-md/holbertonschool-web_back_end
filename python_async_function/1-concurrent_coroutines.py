#!/usr/bin/env python3
"""Module for launching multiple async waits and
collecting delays in order."""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times and returns the list of
    all delays (float values) in ascending order.

    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): Maximum delay value for wait_random.

    Returns:
        List[float]: Delays in ascending order (as finished).
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: List[float] = []
    for finished_task in asyncio.as_completed(tasks):
        delay = await finished_task
        delays.append(delay)
    return delays
