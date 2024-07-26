#!/usr/bin/python3

""" 
function that determine the fewest number of coins needed to meet a
given amount total
"""


def makeChange(coin, total):
    """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if not coin or coin is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coin = sorted(coin)[::-1]
    for coin in coin:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
