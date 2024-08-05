#!/usr/bin/python3
"""
Solving the Island Perimeter challenge
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid

    Args:
        grid (list): A list of lists of integers representing an island

    Returns:
        The perimeter of the island
    """

    perim = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if (grid[r][c] == 1):
                # Check up
                if (r == 0 or grid[r-1][c] == 0):
                    perim += 1
                # Check down
                if (r == rows-1 or grid[r+1][c] == 0):
                    perim += 1
                # Check left
                if (c == 0 or grid[r][c-1] == 0):
                    perim += 1
                # Check right
                if (c == cols-1 or grid[r][c+1] == 0):
                    perim += 1
    return perim
