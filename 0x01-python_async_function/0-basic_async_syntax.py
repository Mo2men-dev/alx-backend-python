#!/usr/bin/env python3
"""
Basic asynchronous syntax
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> int:
    """
    Aynchronous coroutine that takes in an integer argument
    waits for a random delay and eventually returns it.
    
    Args:
        max_delay (int, optional): The maximum random delay. Defaults to 10.
    
    Returns:
        int: The random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
