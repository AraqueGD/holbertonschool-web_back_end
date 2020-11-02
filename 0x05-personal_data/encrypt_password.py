#!/usr/bin/env python3
""" Encrypt Password """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Return Password in to Unique Hash """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed
