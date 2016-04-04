# -*- coding: utf-8 -*-

from sqlalchemy import Column
from ..dbs import db

class Template(db.Model):

    __tablename__ = 'template'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(128), nullable=False, unique=True)
    vcpu = Column(db.Integer)
    mem = Column(db.Integer)
    disk = Column(db.Integer)
    image_id = Column(db.Integer, db.ForeignKey('images.id'))
