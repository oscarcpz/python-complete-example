#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
from datetime import datetime

from loguru import logger

from exceptions.file_exception import FileException


def build_output_file(output, date_pattern):
    if not output:
        raise FileException('[output] is mandatory')
    if not date_pattern:
        raise FileException('[date_pattern] is mandatory')

    dst_filename = os.path.basename(output)
    logger.debug('dst_filename: {}', dst_filename)
    dst_parent = os.path.dirname(output)
    logger.debug('dst_parent: {}', dst_parent)
    dst_without_extension, dst_extension = os.path.splitext(dst_filename)
    logger.debug('dst_without_extension: {}', dst_without_extension)

    now = datetime.now()
    str_date = now.strftime(date_pattern)

    output_file = f'{dst_without_extension}_{str_date}{dst_extension}'
    logger.debug('output_file: {}', output_file)
    return os.path.join(dst_parent, output_file)
