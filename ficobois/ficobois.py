# -*- coding: utf-8 -*-
import math
"""Main module."""


class MathTool:
    @staticmethod
    def sqrt(x):
        answer = math.sqrt(x)
        return answer

    @staticmethod
    def square(x):
        answer = x**2
        return answer

    @staticmethod
    def square_then_sqrt(x):
        answer = x**2
        square_root = math.sqrt(answer)
        return square_root
