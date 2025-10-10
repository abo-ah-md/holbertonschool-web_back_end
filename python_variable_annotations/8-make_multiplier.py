#!/usr/bin/env python3
"""Module for creating a multiplier function."""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies its input by a specified multiplier.

    Args:
        multiplier (float): The value to multiply by.

    Returns:
        Callable[[float], float]: A function that takes a float and returns a float.
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func
