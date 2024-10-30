#!/usr/bin/python3
"""minimal operation"""


def minOperations(n):
    """ a function that returns minimal operation to produce
        H n amount of times with a given n integer
    """
    if n <= 1:
        return (0)
    operation = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operation += divisor
            n //= divisor
        divisor += 1
    return operation
