#!/usr/bin/env python3
"""This module contains an asynchronous
generator that yields random float values between 0 and 10."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously yields ten random
    float numbers between 0 and 10.
    Each number is yielded after one second delay.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
