# -*- coding: utf-8 -*-
import math
"""Main module."""


class A:
    def __init__(self, x):
        self.x = x

    def sqrt(self):
        answer = math.sqrt(self.x)
        return answer

    def square(self):
        answer = self.x**2
        return answer

    def square_then_sqrt(self):
        answer = self.x**2
        square_root = math.sqrt(answer)
        return square_root
