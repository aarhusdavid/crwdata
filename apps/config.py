# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from decouple import config
import os, random, string

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')
    SECRET_KEY  = os.getenv('SECRET_KEY', None)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', None)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', None)
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')
    SECRET_KEY  = os.getenv('SECRET_KEY', None)
    DEBUG = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True

# Load all possible configurations
config_dict = {
    'Production': Config,
    'Debug'     : DevelopmentConfig
}

API_GENERATOR = {
    "books": "Book",
}
