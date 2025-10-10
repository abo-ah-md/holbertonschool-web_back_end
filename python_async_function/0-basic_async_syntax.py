#!/usr/bin/env python3
"""Module for async random wait."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0
    and max_delay seconds (float included), then return the delay.

    Args:
        max_delay (int): Maximum delay in seconds. Default is 10.

    Returns:
        float: The actual delay value.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
