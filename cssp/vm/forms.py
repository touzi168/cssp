#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import (TextField, SubmitField, IntegerField)

class AddVMForm(Form):

    name = TextField(u'VMName')
    template_id = IntegerField(u'TemplateID')
    owner = TextField(u'Owner')
    create_time = TextField(u'CreateTime')

    submit = SubmitField(u'Add')
