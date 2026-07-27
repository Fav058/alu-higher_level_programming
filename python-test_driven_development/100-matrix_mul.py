#!/usr/bin/python3
"""Module that multiplies two matrices.
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices (list of lists) and return the result.
    """
    for name, m in (("m_a", m_a), ("m_b", m_b)):
        if not isinstance(m, list):
            raise TypeError("{} must be a list".format(name))
        if not all(isinstance(row, list) for row in m):
            raise TypeError("{} must be a list of lists".format(name))
        if m == [] or m == [[]]:
            raise ValueError("{} can't be empty".format(name))
        for row in m:
            if not all(isinstance(n, (int, float)) and not isinstance(n, bool)
                       for n in row):
                raise TypeError(
                    "{} should contain only integers or floats".format(name))
        row_len = len(m[0])
        if any(len(row) != row_len for row in m):
            raise TypeError(
                "each row of {} must be of the same size".format(name))

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result
