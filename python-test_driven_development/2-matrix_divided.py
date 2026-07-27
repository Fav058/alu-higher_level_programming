#!/usr/bin/python3
"""Module that divides all elements of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix, rounded to 2 decimal places.
    """
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(n, (int, float)) and not isinstance(n, bool)
                   for n in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    if any(len(row) != row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(n / div, 2) for n in row] for row in matrix]
