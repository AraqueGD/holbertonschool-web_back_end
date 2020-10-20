#!/usr/bin/env python3
"""string and int/float to tuple"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Return String K and V**2 Tuple """

    return (k, v**2)
