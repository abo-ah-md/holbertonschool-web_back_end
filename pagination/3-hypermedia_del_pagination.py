#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset: list[list[str]] | None = None
        self.__indexed_dataset: dict[int, list[str]] | None = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()[:1000]
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Return a dictionary containing pagination info resilient to deletions.
        Ensures that:
        - `index` is within valid range
        - returns `page_size` items (if available)
        - skips deleted indexes
        """
        indexed_data = self.indexed_dataset()
        assert isinstance(index, int) and 0 <= index < len(indexed_data)

        assert isinstance(page_size, int) and page_size > 0

        data: list[list[str]] = []
        current_index = index

        # Keep adding valid rows until page_size is reached or end is hit
        while len(data) < page_size and current_index < len(indexed_data):
            item = indexed_data.get(current_index)
            if item is not None:
                data.append(item)
            current_index += 1

        next_index = current_index if current_index < len(indexed_data) else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
