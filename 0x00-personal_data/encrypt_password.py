#!/usr/bin/env python3
"""module contain function that encrypt password"""

import bcrypt


def hash_password(password: str) -> bytes:
    """hash password"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """check if password is valid"""
    if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
        return True
    return False
