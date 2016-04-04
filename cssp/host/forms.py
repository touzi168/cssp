#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import (TextField, SubmitField, IntegerField)

class AddHostForm(Form):

    name = TextField(u'Address')
    username = TextField(u'Username')
    password = TextField(u'Password')
    status_code = IntegerField(u'Status')

    submit = SubmitField(u'Add')
