#!/usr/bin/env python3
"""Module for creating a tuple from a string and the square of a number."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of an int or float as a float.

    Args:
        k (str): The string key.
        v (Union[int, float]): The value to square.

    Returns:
        Tuple[str, float]: A tuple where the first element is k, and the second is v squared as a float.
    """
    return (k, float(v * v))
