#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os.path

from loguru import logger

from exceptions.file_exception import FileException
from utils.custom_filename_utility import build_output_file
from utils.line_utility import operation


class CalculatorService:

    def __init__(self, src, dst, encoding, delimiter, date_pattern):
        logger.debug('Init')
        self.src = src
        self.dst = dst
        self.encoding = encoding
        self.delimiter = delimiter
        self.date_pattern = date_pattern

    def action(self):
        """
        Method which contains the main functionality
        :return: true if output file could be wroten
        :raises: FileException
        """
        logger.debug('src: {}', self.src)
        logger.debug('dst: {}', self.dst)
        logger.debug('delimiter: {}', self.delimiter)
        logger.debug('encoding: {}', self.encoding)

        logger.debug("1. Read file from [{}]", self.src)

        logger.debug("1.1 Check if file exists")
        if not os.path.exists(self.src):
            raise FileException(f'File {self.src} does not exist')
        logger.debug("1.2 Check if file is a file")
        if not os.path.isfile(self.src):
            raise FileException(f'File {self.src} is not a file')
        logger.debug("1.3 Check if file can be read")
        if not os.access(self.src, os.R_OK):
            raise FileException(f'File {self.src} can not be read')
        logger.debug("1.4 File is correct")

        lines = None
        with io.open(self.src, mode='r', encoding=self.encoding) as fi:
            lines = fi.readlines()
            if not lines:
                logger.error('File [{}] is empty', self.src)
                return False

        logger.debug("2. [{}] lines have been read", len(lines))
        output_filename = build_output_file(self.dst, self.date_pattern)
        logger.debug("3. Prepare output file: {}", output_filename)

        logger.debug("3. For each line -> make operations")
        lines_result = list()
        for line in lines:
            list_result = list()
            line_spitted = line.strip().split(self.delimiter)
            counter = 0
            for element in line_spitted:
                if counter == 0:
                    list_result.append(element)
                else:
                    list_result.append(operation(element))

                counter += 1

            line_result = self.delimiter.join(list_result)
            logger.debug("3.1 [{}] modified to [{}]", line.strip(), list_result)
            lines_result.append(f'{line_result}\n')

        with io.open(output_filename, mode='w', encoding=self.encoding) as fo:
            fo.writelines(lines_result)
            logger.debug("4. [{}] lines have been wrote to output file", len(lines_result))

        return True
