#!/usr/bin/env python3
"""Module for returning an asyncio.Task for an async function."""

import asyncio
from typing import Any

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task
    for wait_random with the given max_delay.

    Args:
        max_delay (int): The max delay for wait_random.

    Returns:
        asyncio.Task: The created Task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
