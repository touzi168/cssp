#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import (TextField, SubmitField, IntegerField)

class AddTemplateForm(Form):

    name = TextField(u'Name')
    vcpu = IntegerField(u'Vcpu')
    mem = IntegerField(u'Mem')
    disk = IntegerField(u'disk')
    image_id = IntegerField(u'ImageID')

    submit = SubmitField(u'Add')
