#!/usr/bin/env python3
"""Simple pagination"""
import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """def get page"""
        assert type(page_size) is int and type(page) is int
        assert page > 0
        assert page_size > 0
        self.dataset()
        i = index_range(page, page_size)
        if i[0] >= len(self.__dataset):
            return []
        else:
            return self.__dataset[i[0] : i[1]]


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
