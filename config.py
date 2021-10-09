"""
@title: config.py
@title: This is a flask application config file
"""
""" flask configuration"""
from os import environ, path
from dotenv import load_dotenv


class Config:
    """Base config of flask app"""
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class DevConfiguration(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True


class ProdConfiguration(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
