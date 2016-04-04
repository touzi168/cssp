# -*- coding: utf-8 -*-

from .host import host
from .user import user
from .image import image
from .template import template
from .vm import vm
from .flask_app import app
from .dbs import db

app.register_blueprint(host)
app.register_blueprint(user)
app.register_blueprint(image)
app.register_blueprint(template)
app.register_blueprint(vm)
