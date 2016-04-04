#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, redirect, url_for
from .forms import AddUserForm
from .models import User
from ..dbs import db

user = Blueprint('user', __name__, url_prefix='/users')

@user.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        form = AddUserForm()
        user_list = User.query.filter().all()
        return render_template('user/index.html', form=form, user_list=user_list)
    else:
        form = AddUserForm(request.form)
        if form.validate_on_submit():
            user_instance = User()
            form.populate_obj(user_instance)
            db.session.add(user_instance)
            db.session.commit()
        return redirect(url_for('user.index'))

@user.route('/<int:user_id>/delete', methods=['GET'])
def delete_user(user_id):
    user_instance = User.query.filter(User.id == user_id).first()
    if user_instance:
        db.session.delete(user_instance)
        db.session.commit()
    return redirect(url_for('user.index'))
