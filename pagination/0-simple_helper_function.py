#!/usr/bin/env python3
"""this is a helper function for page indexing"""


def index_range(page: int, page_size: int) -> tuple:
    """on every next page the index will incrament to the size"""
    start_index: int
    end_index: int
    if page == 1:
        start_index = 0
    else:
        start_index = (page_size * page) - page_size
    end_index = page_size * page
    return (start_index, end_index)
