#!/usr/bin/env python3
""" Module Auth """

from flask import request
from typing import List, TypeVar


class Auth():
    """ Class Auth """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method Require Auth """
        return False

    def authorization_header(self, request=None) -> str:
        """ Method Authorization Header """
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method Current User """
        return request
