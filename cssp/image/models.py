# -*- coding: utf-8 -*-

from sqlalchemy import Column
from ..dbs import db

class Image(db.Model):

    __tablename__ = 'images'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(128), nullable=False, unique=True)
    path = Column(db.String(256), nullable=False)
