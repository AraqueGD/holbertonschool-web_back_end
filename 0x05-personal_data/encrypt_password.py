#!/usr/bin/env python3
""" Encrypt Password """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Return Password in to Unique Hash """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Function Valid Data """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hash_password):
        valid = True
    return valid
