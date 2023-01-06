#!/bin/python3
import os
from dotenv import load_dotenv

#####

here = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(here, ".env"))
db_path = os.path.join(here, "db.sql")

#####


class Config(object):
    """ """

    SECRET_KEY = "end1ngF@scism"
    SESSION_TYPE = "filesystem"
    TESTING = False
    SEND_FILE_MAX_AGE_DEFAULT = 0
    MAX_CONTENT_LENGTH = 1024**3
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDASH_API_KEY = os.getenv("redash_api")
