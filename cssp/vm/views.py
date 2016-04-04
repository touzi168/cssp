#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, redirect, url_for
from .forms import AddVMForm
from .models import VM
from ..dbs import db

vm = Blueprint('vm', __name__, url_prefix='/vms')

@vm.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        form = AddVMForm()
        vm_list = VM.query.filter().all()
        return render_template('vm/index.html', form=form, vm_list=vm_list)
    else:
        form = AddVMForm(request.form)
        if form.validate_on_submit():
            vm_instance = VM()
            form.populate_obj(vm_instance)
            db.session.add(vm_instance)
            db.session.commit()
        return redirect(url_for('vm.index'))

@vm.route('/<int:vm_id>/delete', methods=['GET'])
def delete_vm(vm_id):
    vm_instance = VM.query.filter(VM.id == vm_id).first()
    if vm_instance:
        db.session.delete(vm_instance)
        db.session.commit()
    return redirect(url_for('vm.index'))
