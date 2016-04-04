# -*- coding: utf-8 -*-

from sqlalchemy import Column
from ..dbs import db

class VM(db.Model):

    __tablename__ = 'vms'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(128), nullable=False, unique=True)
    template_id = Column(db.Integer, db.ForeignKey('templates.id'))
    owner = Column(db.String(32), db.ForeignKey('users.username'))
    create_time = Column(db.DateTime)
