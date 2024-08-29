#!/usr/bin/env python3
"""
Module contains function thaty returns log messages obfuscated
"""

import re
from typing import List
import logging


# PII Fields
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        filters values in incoming log records
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Returns log messages obfuscated

    Args:
        fields (List[str]): list of fields
        redaction (str): redaction string
        message (str): log message
        separator (str): log message separator
    """
    return re.sub(rf'({"|".join(fields)})=[^"{separator}"]*',
                  rf'\1={redaction}', message)


def get_logger() -> logging.Logger:
    """
    Returns logger
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))

    logger.addHandler(handler)
    return logger
