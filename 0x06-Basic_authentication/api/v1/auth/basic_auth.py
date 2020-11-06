#!/usr/bin/env python3
""" Module Basic Auth """

from api.v1.auth.auth import Auth
from base64 import b64decode


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
