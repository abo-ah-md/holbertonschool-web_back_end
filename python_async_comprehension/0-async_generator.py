#!/usr/bin/env python3
"""This module implements an asynchronous
generator yielding random numbers."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Yields 10 random float numbers
    between 0 and 10, one per second.

    Each iteration waits one second and
    yields a new number.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
