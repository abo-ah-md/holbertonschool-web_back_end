#!/usr/bin/env python3
"""This module provides a coroutine to
measure the runtime for running async
comprehensions in parallel."""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in
    parallel and returns the total runtime.

    Returns:
        float: Total time taken to run all four
        async_comprehension coroutines in parallel.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start
