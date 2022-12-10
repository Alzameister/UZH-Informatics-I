#!/usr/bin/env python3
from unittest import TestCase

from public.script import convert_roman_to_int


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
class ConversionTestSuite(TestCase):

    def _assert(self, roman, expected):
        actual = convert_roman_to_int(roman)
        m = f"should be {expected} but was {actual}"
        self.assertEqual(expected, actual, m)

    def test_simple_numeralI(self):
        self._assert("I", 1)

    def test_simple_numeralV(self):
        self._assert("V", 5)

    def test_simple_numeralX(self):
        self._assert("X", 10)

    def test_simple_numeralL(self):
        self._assert("L", 50)

    def test_simple_numeralC(self):
        self._assert("C", 100)

    def test_simple_numeralD(self):
        self._assert("D", 500)

    def test_simple_numeralM(self):
        self._assert("M", 1000)

    def test_simple_additive1(self):
        self._assert("XI", 11)

    def test_simple_additive2(self):
        self._assert("MD", 1500)

    def test_single_compound(self):
        self._assert("IV", 4)

    def test_double_compound(self):
        self._assert("CDIV", 404)

    def test_longer_additive1(self):
        self._assert("VIII", 8)
    
    def test_longer_additive2(self):
        self._assert("MDC", 1600)

    def test_complex_additive1(self):
        self._assert("CMLX", 960)

    def test_complex_additive_subtraction(self):
        self._assert("XIV", 14)

    def test_invalid_strings(self):
        with self.assertRaises(
            Warning,
            msg="Invalid Input"
        ):
            convert_roman_to_int("XLS")
    
    def test_invalid_pattern(self):
        with self.assertRaises(
            Warning,
            msg="Invalid pattern"
        ):
            convert_roman_to_int("IXIX")

    def test_invalid_system(self):
        with self.assertRaises(
            Warning,
            msg="Invalid system"
        ):
            convert_roman_to_int("VIIII")
    
    def test_invalid_repetition(self):
        with self.assertRaises(
            Warning,
            msg="Invalid repetition"
        ):
            convert_roman_to_int("VV")

    def test_any_number_of_M(self):
        self._assert("MMMMMMMI", 7001)

    def test_CDXC(self):
        self._assert("CDXC", 490)

    def test_XLIX(self):
        self._assert("XLIX", 49)

    def test_VIV(self):
        with self.assertRaises(
            Warning,
            msg="Invalid pattern"
        ):
            convert_roman_to_int("VIV")

    def test_LLX(self):
        with self.assertRaises(
            Warning,
            msg="Invalid pattern"
        ):
            convert_roman_to_int("LLX")