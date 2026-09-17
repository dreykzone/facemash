import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):

    DEBUG = os.getenv("FLASK_DEBUG", "0") == "1"
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///facemash.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False