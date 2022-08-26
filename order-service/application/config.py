from distutils.debug import DEBUG
import os
from unittest import load_tests
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATA_URI = "mysql+pymysql://"
    SQLALCHEMY_ECHO = True

class Production(Config):
    ENV = "production"
    DEBUG = False
    SQLALCHEMY_DATA_URI = 'mysql+pymsql://'
    SQLALCHEMY_ECHO = False
    