#!/usr/bin/env python3
"""
Module contains function thaty returns log messages obfuscated
"""

import re
from typing import List


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
