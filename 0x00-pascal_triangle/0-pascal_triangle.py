#!/usr/bin/python3
""" this is a pascal triangle generator file"""


def pascal_triangle(n):
    """
    a function that prints a pascal triangle of n number of rows
    a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n:
     """
    res = []
    if n > 0:
        """executes only if n is greater than 0"""
        for i in range(1, n + 1):
            """loop should run n amount of time"""
            new_list = []
            C = 1
            for j in range(1, i + 1):
                new_list.append(C)
                C = C * (i - j) // j
            res.append(new_list)
    return res
