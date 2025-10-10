#!/usr/bin/env python3
"""Module for async generator that yields random floats."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that asynchronously yields
    10 random numbers between 0 and 10,
    waiting 1s between each.

    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
