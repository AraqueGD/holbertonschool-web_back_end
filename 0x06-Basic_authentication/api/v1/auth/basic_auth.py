#!/usr/bin/env python3
""" Module Basic Auth """

from api.v1.auth.auth import Auth


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
