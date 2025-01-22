# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
import hashlib
import binascii
import jwt
from datetime import datetime
from flask import current_app, request

# Inspiration -> https://www.vitoshacademy.com/hashing-passwords-in-python/

def hash_pass(password):
    """Hash a password for storing."""

    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    
    # Return the combination of salt and hash as a string
    return (salt + pwdhash).decode('ascii')


def verify_pass(provided_password, stored_password):
    """Verify a stored password against one provided by user"""

    # No need to decode here, stored_password is already a string
    salt = stored_password[:64]  # Extract the salt from the string
    stored_pwdhash = stored_password[64:]  # Extract the hashed password

    # Recreate the hash from the provided password and compare
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    
    return pwdhash == stored_pwdhash

# Used in API Generator
def generate_token(aUserId):
    now = int(datetime.utcnow().timestamp())
    api_token = jwt.encode(
        {"user_id": aUserId,
         "init_date": now},
        current_app.config["SECRET_KEY"],
        algorithm="HS256"
    )

    return api_token