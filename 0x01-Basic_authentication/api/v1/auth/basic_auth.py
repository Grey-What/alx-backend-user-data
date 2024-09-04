#!/usr/bin/env python3
"""
contains class BasicAuth and all it's methods
"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


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

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        return User instance based on credentials
        """
        if (user_email is None or not isinstance(user_email, str)):
            return None
        if (user_pwd is None or not isinstance(user_pwd, str)):
            return None

        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
            return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        overload Auth and return user instance
        """
        auth_header = self.authorization_header(request)
        if auth_header is not None:
            token = self.extract_base64_authorization_header(auth_header)
            if token is not None:
                decoded = self.decode_base64_authorization_header(token)
                if decoded is not None:
                    email, password = self.extract_user_credentials(decoded)
                    if email is not None:
                        return self.user_object_from_credentials(
                            email, password)

        return
