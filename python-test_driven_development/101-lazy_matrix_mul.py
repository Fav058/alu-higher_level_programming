#!/usr/bin/python3
"""Module that multiplies two matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using numpy.dot.
    """
    return np.dot(m_a, m_b)
