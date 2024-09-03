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
        if (authorization_header is None
           or not isinstance(authorization_header, str)):
            return None

        if authorization_header.startswith("Basic "):
            return authorization_header.split(' ')[1]
        return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        decode authorization_header from base64 string

        base64_authorization_header (str): Base64 header to decode
        """
        if (base64_authorization_header is None
           or not isinstance(base64_authorization_header, str)):
            return None

        try:
            header = base64_authorization_header.encode('utf-8')
            decoded_header = base64.b64decode(header)
            return decoded_header.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        returns users credentials from decode header

        decoded_base64_authorization_header (str):
        header to extract user credentials from
        """
        if (decoded_base64_authorization_header is None
           or not isinstance(decoded_base64_authorization_header, str)):
            return (None, None)

        if ":" not in decoded_base64_authorization_header:
            return (None, None)

        email, passw = decoded_base64_authorization_header.split(':')

        return (email, passw)
