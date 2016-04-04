#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import (TextField, SubmitField)

class AddImageForm(Form):

    name = TextField(u'name')
    path = TextField(u'Path')

    submit = SubmitField(u'Add')
