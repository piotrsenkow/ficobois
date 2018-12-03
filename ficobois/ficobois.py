# -*- coding: utf-8 -*-
"""Main module."""
import math


def sqrt(x):
    answer = math.sqrt(x)
    return answer


def square(x):
    answer = x**2
    return answer


def square_then_sqrt(x):
    answer = x**2
    square_root = math.sqrt(answer)
    return square_root


def add(x,y):
    print("Attempting to add {} and {}.".format(x, y))
    return x+y
