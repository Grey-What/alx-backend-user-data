#!/usr/bin/env python3
"""
contains class BasicAuth and all it's methods
"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
    Class for Basic Authentication method
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        return BASE64 of Authorization Header for Basic Authentication

        authorization_header (str): header of request
        """
        if authorization_header is None or type(authorization_header) != str:
            return None

        if authorization_header.startswith("Basic "):
            return authorization_header.split(' ')[1]
        return None
