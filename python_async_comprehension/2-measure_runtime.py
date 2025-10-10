#!/usr/bin/env python3
"""Module to measure runtime for parallel async comprehensions."""

import asyncio
import time
from typing import Coroutine

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension 4 times in parallel and measures the total runtime.

    Returns:
        float: The total time taken to run 4 async_comprehension coroutines in parallel.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
