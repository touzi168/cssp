#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import (TextField, SubmitField)

class AddUserForm(Form):

    username = TextField(u'Username')
    password = TextField(u'Password')
    email = TextField(u'Email')

    submit = SubmitField(u'Add')
