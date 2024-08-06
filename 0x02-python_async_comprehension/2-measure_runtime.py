#!/usr/bin/env python3
"""
Async Comprehensions
"""

from typing import List
import asyncio
from time import time
async_comprehension = __import__('0-async_generator').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime
    Returns:
        float: the runtime
    """
    start: float = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end: float = time()
    return end - start
