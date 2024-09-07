#!/usr/bin/env python3
"""contains class Auth and it's methods"""

from flask import request
from typing import List, TypeVar
import os


class Auth():
    """
    Authentication class

    Template for all authentications systems
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determine if route do not need authenitcation

        Return: bool
        """
        if (path is None or excluded_paths is None
           or len(excluded_paths) == 0):
            return True

        basic_path = path.rstrip('/')

        for excluded in excluded_paths:
            basic_excluded = excluded.rstrip('/')

            if basic_path == basic_excluded:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        sets authorization header for basic authentication

        Args:
        request: request object
        """
        if request is None or "Authorization" not in request.headers:
            return None
        else:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        will return current user

        Return: None
        """
        return None

    def session_cookie(self, request=None):
        """returns cookie value from request"""
        if request is None:
            return None

        session_name = os.environ.get('SESSION_NAME')
        return request.cookies.get(session_name)
