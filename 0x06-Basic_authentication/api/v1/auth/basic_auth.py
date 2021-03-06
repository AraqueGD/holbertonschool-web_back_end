#!/usr/bin/env python3
""" Module Basic Auth """

from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ Class Basic Auth """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Method Base64 """
        if (authorization_header is None or
            not isinstance(authorization_header, str) or
                not authorization_header.startswith("Basic ")):
            return None
        else:
            encoded = authorization_header.split(' ', 1)[1]

            return encoded

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ Method Base64 Authorization Header """
        if (base64_authorization_header is None or
                not isinstance(base64_authorization_header, str)):
            return None

        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded64 = b64decode(encoded)
            decoded = decoded64.decode('utf-8')
        except BaseException:
            return None
        return decoded

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ Method Extract User Credentials """
        if (decoded_base64_authorization_header is None or
                not isinstance(decoded_base64_authorization_header, str) or
                ":" not in decoded_base64_authorization_header):
            return None, None

        credentials = decoded_base64_authorization_header.split(':', 1)

        return credentials[0], credentials[1]

    def user_object_from_credentials(self, user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        """ Method User Object Credentials """
        if (user_email is None or not isinstance(user_email, str)):
            return None
        if (user_pwd is None or not isinstance(user_pwd, str)):
            return None

        try:
            search_user = User.search({"email": user_email})
        except Exception:
            return None

        for user in search_user:
            if (user.is_valid_password(user_pwd)):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method Current User """
        auth_header = self.authorization_header(request)

        if (not auth_header):
            return None

        encoded = self.extract_base64_authorization_header(auth_header)

        if not encoded:
            return None

        decoded = self.decode_base64_authorization_header(encoded)

        if not decoded:
            return None

        email, pwd = self.extract_user_credentials(decoded)

        if not email or not pwd:
            return None

        user = self.user_object_from_credentials(email, pwd)

        return user
