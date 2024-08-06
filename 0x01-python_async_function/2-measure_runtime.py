#!/usr/bin/env python3
""" Measures total execution time """

import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measures the total execution time for wait_n
    Args:
        n (int): number of times to wait
        max_delay (int): maximum delay time
    Returns:
        float: total time for execution
    """

    elapsed_time: float

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time / n
