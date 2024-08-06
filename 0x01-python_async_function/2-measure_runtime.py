#!/usr/bin/env python3
""" Measures the total execution time for wait_n """

import time
import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """
    Measures the total execution time for wait_n
    Args:
        n (int): number of times to wait
        max_delay (int): maximum delay time
    Returns:
        float: total time for execution
    """
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.time()
    return end - start
