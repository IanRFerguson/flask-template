#!/bin/python3
import os
import logging
from config import Config

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy

logging.basicConfig(level=logging.INFO)


#####

db = SQLAlchemy()
here = os.path.abspath(os.path.dirname(__file__))

###


def create_app(config_class=Config):
    """ """

    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app=app)

    ###

    from app.utilities import bp as utilities

    app.register_blueprint(utilities)

    return app
