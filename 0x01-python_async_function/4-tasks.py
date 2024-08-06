#!/usr/bin/env python3
""" Tasks module for asyncio in Python """

from typing import List
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for a random delay between 0 and max_delay
    Args:
        n (int): number of times to wait
        max_delay (int): maximum delay time
    Returns:
        List[float]: list of delays in ascending order
    """
    delays: List[float] = []
    for i in range(n):
        delays.append(await task_wait_random(max_delay))
    return sorted(delays)
