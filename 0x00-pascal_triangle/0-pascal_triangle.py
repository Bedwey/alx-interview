#!/usr/bin/python3
"""This module contains a function that generates Pascal's triangle"""


def pascal_triangle(n):
    """
    Returns A list of lists representing Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j in (0, i):
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle
