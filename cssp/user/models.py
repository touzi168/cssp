# -*- coding: utf-8 -*-

from sqlalchemy import Column
from ..dbs import db

class User(db.Model):

    __tablename__ = 'users'

    id = Column(db.Integer, primary_key=True)
    username = Column(db.String(32), default='cssp')
    password = Column(db.String(32), default='cssp')
    email = Column(db.String(128), default='cssp@cssp.com')
