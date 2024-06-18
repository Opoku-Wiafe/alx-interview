#!/usr/bin/python3
"""
calculates the minimum number of operations to achieve a given
number of characters using only 'Copy All' and 'Paste'
"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    operand, root = 0, 2
    while root <= n:
        # divide through evenly by (n)
        if n % root == 0:
            # total even-divisions by root = total operations
            operand += root
            # set n to the remainder
            n = n / root
            # reduce root to find remaining smaller vals that evenly-divide n
            root -= 1
        # increment root until it evenly-divides n
        root += 1
    return operand
