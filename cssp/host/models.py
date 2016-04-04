# -*- coding: utf-8 -*-

from sqlalchemy import Column
from ..extension import db
from .constants import HOST_OK

class Host(db.Model):

    __tablename__ = 'hosts'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(128), nullable=False, unique=True)
    username = Column(db.String(32), default='cssp')
    password = Column(db.String(32), default='cssp')
    status_code = Column(db.SmallInteger, default=HOST_OK)
