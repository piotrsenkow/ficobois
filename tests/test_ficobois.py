#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ficobois` package."""


import unittest
from click.testing import CliRunner

from ficobois import ficobois
from ficobois import cli


class TestFicobois(unittest.TestCase):
    """Tests for `ficobois` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_sqrt_function(self):
        """Test something."""
        answer = ficobois.sqrt(25)
        shouldbe = 5.0
        self.assertEqual(answer, shouldbe)

    def test_square_function(self):
        answer = ficobois.square(4)
        self.assertEqual(answer, 16)

    def test_square_then_sqrt(self):
        answer = ficobois.square_then_sqrt(3)
        self.assertEqual(answer, 3.0)

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'ficobois.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output


if __name__ == '__main__':
    unittest.main()
