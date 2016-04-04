# -*- coding: utf-8 -*-

import os

class DefaultConfig(object):

    PROJECT = "cssp"

    DEBUG = False
    TESTING = False

    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = 'your secret key'

    # Flask-Sqlalchemy: http://packages.python.org/Flask-SQLAlchemy/config.html
    SQLALCHEMY_ECHO = True
    # MYSQL for production.
    SQLALCHEMY_DATABASE_URI = 'mysql://lc:1qaz@localhost/lc?charset=utf8'

    # Flask-cache: http://pythonhosted.org/Flask-Cache/
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60
