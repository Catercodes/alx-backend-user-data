#!/usr/bin/env python3
""" The Shebang for python"""

import bcrypt


def _hash_password(self, password: str) -> bytes:
    """Hashes a password string using bcrypt"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
