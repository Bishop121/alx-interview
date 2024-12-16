#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Function that returns the perimeter of the island described in grid
    Args:
        grid (list):  is a list of list of integers
    Returns:
        the perimeter
    """
    rows = len(grid)
    cols = len(grid[0])

    sum_per = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                per = 4
                """Check up"""
                if row > 0:
                    if grid[row - 1][col] == 1:
                        per -= 1
                """Check down"""
                if row < rows - 1:
                    if grid[row + 1][col] == 1:
                        per -= 1
                """Check left"""
                if col > 0:
                    if grid[row][col - 1] == 1:
                        per -= 1
                """Check right"""
                if col < cols - 1:
                    if grid[row][col + 1] == 1:
                        per -= 1
                sum_per += per
    return sum_per
