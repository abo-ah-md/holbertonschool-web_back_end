#!/usr/bin/env python3
"""Module for running multiple task_wait_random coroutines
and collecting delays in completion order."""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times and
    returns the list of delays (float values)
    in ascending order—which is the order of completion.

    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay for each random wait.

    Returns:
        List[float]: Delays in ascending order (as finished).
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        delays.append(delay)
    return delays
