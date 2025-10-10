#!/usr/bin/env python3
"""Module for summing a mixed list of integers and floats."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list
    containing integers and floats, as a float.

    Args:
        mxd_lst (List[Union[int, float]]): The list to sum.

    Returns:
        float: The sum of all numbers in mxd_lst.
    """
    return float(sum(mxd_lst))
