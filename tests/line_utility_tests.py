#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from utils.line_utility import operation


class LineUtilityTests(unittest.TestCase):

    def test_operation_element_is_numeric(self):
        self.assertEqual(operation("3"), "9")

    def test_operation_element_is_not_numeric(self):
        self.assertEqual(operation("hi"), "-")

    def test_operation_element_is_none(self):
        self.assertEqual(operation(None), "-")


if __name__ == '__main__':
    unittest.main()
