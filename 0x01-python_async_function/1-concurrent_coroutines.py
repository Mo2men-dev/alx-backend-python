#!/usr/bin/env python3
""" Takes int arg, waits for random delay """

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """ Waits for random delay max_delay n times, returns list of actual delays """
    delays: List[float] = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    
    return sorted(delays)
