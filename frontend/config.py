import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class Config:
    SECRET_KEY='ate530tgjrmkh3gkre[w]gr'
    WTF_CSRF_SECRET_KEY = 'vaergorqmdsa4245trp2lsgsp'

class DevelopmentCOnfig(Config):
    ENV = 'development'
    DEBUG = True

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False