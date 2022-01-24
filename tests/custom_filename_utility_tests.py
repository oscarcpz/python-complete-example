#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from datetime import datetime

from configurations.app_config import CALCULATOR
from exceptions.file_exception import FileException
from utils.custom_filename_utility import build_output_file


class CustomFilenameUtilityTests(unittest.TestCase):

    def test_buildOutputFile_ok(self):
        path_built = build_output_file("my/output/path/output-test.file", CALCULATOR['date_pattern'])
        self.assertIsNotNone(path_built)
        now = datetime.now()
        now_str = now.strftime(CALCULATOR['date_pattern'])
        self.assertEqual(path_built, f'my/output/path/output-test_{now_str}.file')

    def test_buildOutputFile_fail_empty_output(self):
        with self.assertRaises(FileException) as cm:
            build_output_file(None, CALCULATOR['date_pattern'])

    def test_buildOutputFile_fail_empty_datePattern(self):
        with self.assertRaises(FileException) as cm:
            build_output_file("", CALCULATOR['date_pattern'])

