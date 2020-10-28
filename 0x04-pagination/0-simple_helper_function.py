#!/usr/bin/env python3
""" Simple Helper FUcntion """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Return Tuple """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
