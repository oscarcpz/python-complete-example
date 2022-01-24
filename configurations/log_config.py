#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

PROJECT_NAME = "pce"

LOG_FORMAT = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {module} | {function} | {message}"

LOG = {
    "handlers": [
        {
            "sink": sys.stdout,
            "format": LOG_FORMAT,
            "level": "DEBUG"
        },
        {
            "sink": "%s_{time:YYYYMMDD}.log" % PROJECT_NAME,
            "serialize": False,  # True - convierte cada linea de log a JSON
            "format": LOG_FORMAT,
            "rotation": "1 days",
            "level": "DEBUG"
        },
    ],

}
