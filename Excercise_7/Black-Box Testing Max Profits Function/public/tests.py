#!/usr/bin/env python3
from unittest import TestCase
from public.script import max_profit

# Implement this test suite. Make sure that you define test
# methods and that each method _directly_ includes an assertion
# in the body, or -otherwise- the grading will mark the test
# suite as invalid.
class MaxProfitTest(TestCase):
    def _assert(self, prices, expected):
        actual = max_profit(prices)
        m = f"should be {expected} but was {actual}"
        self.assertEqual(expected, actual, m)

    def test_negative(self):
        with self.assertRaises(
            ValueError,
            msg = "Invalid Prices"
        ):
            max_profit([-1,-2])

    def test_mixed_negative(self):
        with self.assertRaises(
            ValueError, 
            msg = "Invalid Prices"
        ):
            max_profit([-1,2])

    def test_wrong_data_type(self):
        with self.assertRaises(
            TypeError
        ):
            max_profit(())

    def test_empty_list(self):
        with self.assertRaises(
            IndexError, 
            msg = "Invalid Prices"
        ):
            max_profit([])

    def test_non_int_list(self):
        with self.assertRaises(
            TypeError, 
            msg = "Invalid Prices"
        ):
            max_profit(["int"])

    def test_one_element(self):
        self._assert([1], 0)

    def test_same_prices(self):
        self._assert([1,1,1,1], 0)

    def test_correct(self):
        self._assert([1, 2, 3, 4, 5], 4)
    
    def test_multiple_same_correct(self):
        self._assert([1,1,2,4], 3)