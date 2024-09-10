#!/usr/bin/env python3
"""
This module will contain the Auth class and it's methods
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes a password and return the hash bytes

    Args:
    password: to be hashed
    """

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
