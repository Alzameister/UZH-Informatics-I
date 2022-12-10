#!/usr/bin/env python3

from unittest import TestCase
from script import fac


class PublicTestSuite(TestCase):

    def test1(self):
         self.assertEqual(120, fac(5))
         self.assertEqual(3628800, fac(10))


