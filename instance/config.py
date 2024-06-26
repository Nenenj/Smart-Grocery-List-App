#!/usr/bin/env python3

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get(
            'SECRET_KEY', 'default_secret_key'
    )
    SQLALCHEMY_DATABASE_URI = (
            os.environ.get('DATABASE_URL') or 'sqlite:///../db.sqlite'
            )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
