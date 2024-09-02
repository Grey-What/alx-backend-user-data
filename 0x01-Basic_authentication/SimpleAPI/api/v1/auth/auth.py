#!/usr/bin/env python3
"""contains class Auth and it's methods"""

from flask import request
from typing import List, TypeVar


class Auth():
    """
    Authentication class

    Template for all authentications systems
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        returns False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        sets authorization header for basic authentication
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        will return current user

        Return: None
        """
        return None
