#!/usr/bin/env python
# -*- coding: utf-8 -*-
from loguru import logger

from configurations.app_config import CALCULATOR
from configurations.log_config import LOG
from services.calculator_service import CalculatorService

if __name__ == "__main__":
    logger.remove()  # eliminamos el log por defecto
    logger.configure(**LOG)

    calculator_service = CalculatorService(**CALCULATOR)
    if calculator_service.action():
        logger.info('Success')
    else:
        logger.error('Error')
