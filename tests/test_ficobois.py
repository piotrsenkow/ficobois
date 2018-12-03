#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ficobois` package."""


import unittest

from ficobois import ficobois as fb


class TestFicobois(unittest.TestCase):
    """Tests for `ficobois` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_sqrt_function(self):
        """Test something."""
        answer = fb.sqrt(25)
        shouldbe = 5.0
        self.assertEqual(answer, shouldbe)

    def test_square_function(self):
        answer = fb.square(4)
        self.assertEqual(answer, 16)

    def test_square_then_sqrt(self):
        answer = fb.square_then_sqrt(3)
        self.assertEqual(answer, 3.0)


if __name__ == '__main__':
    unittest.main()
