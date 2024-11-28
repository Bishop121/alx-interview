#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """Function to determine the fewest number of coins needed
        to meet a given amount from a given pile of coins
    Arg:
        coins (list): list of the values of the coins in your possession
        total (int): total number to get a change for

    Return:
        fewest number of coins needed to meet total or 0 if None
    """
    if total <= 0:
        return 0

    count = 0
    coins.sort()

    try:
        while total > 0:
            coin = coins.pop()
            if coin <= total:
                num_coin = total // coin
                count += num_coin
                total -= (num_coin * coin)
    except Exception:
        return -1
    return count
