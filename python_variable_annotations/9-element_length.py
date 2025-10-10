#!/usr/bin/env python3
"""Module for list element length pairing."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples for each element in lst and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequence objects (like str, list, tuple, etc.)

    Returns:
        List[Tuple[Sequence, int]]: List of (element, length) tuples.
    """
    return [(i, len(i)) for i in lst]
