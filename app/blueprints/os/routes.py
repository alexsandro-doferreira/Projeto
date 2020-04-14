from flask import render_template
from flask_login import login_required
from . import os

@os.route('/oss')
def lista_oss():
    return render_template('os/oss.html')

@os.route('/osadd')
def add_oss():
    return render_template('os/add_os.html')

@os.route('/osedit')
def edit_oss():
    return render_template('os/edit_os.html')

@os.route('/osview')
def view_oss():
    return render_template('os/view_os.html')

@os.route('/osdel')
def del_oss():
    return render_template('os/del_os.html')