# -*- coding: utf-8 -*-
import math
"""Main module."""


def sqrt(x):
    answer = math.sqrt(x)
    return answer


def square(x):
    answer = x**2
    return answer


def square_then_sqrt(x):
    answer = x**2
    square_root = sqrt(answer)
    return square_root
