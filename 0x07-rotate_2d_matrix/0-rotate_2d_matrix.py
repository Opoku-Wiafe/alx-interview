#!/usr/bin/python3
"""
function Rotate the given n x n 2D matrix
90 degrees clockwise in-place
rotate_2d_matrix([[1,2,3],[4,5,6],[7,8,9]])
"""


def rotate_2d_matrix(matrix):

    n = len(matrix)

    for x in range(n):
        for j in range(x, n):
            matrix[x][j], matrix[j][x] = matrix[j][x], matrix[x][j]

    for x in range(n):
        matrix[x].reverse()
