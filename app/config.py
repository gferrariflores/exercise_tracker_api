import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.getenv('FLASK_ENV') == 'development'
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
