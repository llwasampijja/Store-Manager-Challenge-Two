# author = False

import os
import app

basedir = os.path.abspath(os.path.dirname(__file__))
app.secret_key = os.urandom(12)

class Config(object):
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = app.secret_key

class DevelopmentConfig(Config):
    DEVELOPENT = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING =True

runtime_mode = "development"
env_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}