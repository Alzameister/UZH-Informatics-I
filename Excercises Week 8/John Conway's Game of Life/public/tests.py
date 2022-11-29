#!/usr/bin/env python3
from unittest import TestCase
from public.script import evolve


# You are supposed to develop the functionality in a test-driven way.
# Think about relevant test cases and extend the following test suite
# until all requirements of the description are covered. The test suite
# will be run against various correct and incorrect implementations, so
# make sure that you only test the `move` function and stick strictly
# to its defined signature.
#
# Make sure that you define test methods and that each method
# _directly_ includes an assertion in the body, or -otherwise- the
# grading will mark the test suite as invalid.
class EvolveTestSuite(TestCase):

    def test_glider(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        expected = ((
            "--------------",
            "| ###        |",
            "| #          |",
            "|  #         |",
            "|            |",
            "|            |",
            "--------------"
        ), 5)
        actual = evolve(field, 4)
        self.assertEqual(expected, actual)

    def test_empty(self):
        field = ()
        with self.assertRaises(
            Warning,
            msg = "Field empty"
        ):
            evolve(field, 4)

    def test_non_tuple(self):
        field = []
        with self.assertRaises(
            Warning,
            msg = "Field of incorrect data type"
        ):
            evolve(field, 4)

    def test_wrong_chars(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |s",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(
            Warning,
            msg = "Incorrect chars in field"
        ):
            evolve(field, 4)

    def test_line_dif_len(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #           |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(
            Warning,
            msg = "Field lines have different length"
        ):
            evolve(field, 4)


    def test_field_too_small(self):
        field = (
            "||",
            "||"
        )
        with self.assertRaises(
            Warning,
            msg = "Field not big enough"
        ):
            evolve(field, 4)

    def test_neg_step(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(
            Warning,
            msg = "Evolutionary steps must be positive"
        ):
            evolve(field, -4)