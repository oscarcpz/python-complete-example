#!/usr/bin/env python
# -*- coding: utf-8 -*-
from loguru import logger


def operation(element):
    """
    Perform operation over a given element
    :param element: element as String
    :return: '-' if error, else element calculated
    """
    if not element:
        return '-'

    element_cleaned = element.strip()
    if not str(element_cleaned).isnumeric():
        return '-'

    result = int(element_cleaned) * 3
    logger.debug("\t{} -> {}", element_cleaned, result)
    return str(result)
