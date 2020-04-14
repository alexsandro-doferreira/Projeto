from flask import render_template
from flask_login import login_required
from . import equipamento

@equipamento.route('/equipamentos')
def lista_equipamentos():
    return render_template('equipamento/equipamentos.html')

@equipamento.route('/equipamentoadd')
def add_equipamentos():
    return render_template('equipamento/add_equipamento.html')

@equipamento.route('/equipamentoedit')
def edit_equipamentos():
    return render_template('equipamento/edit_equipamento.html')

@equipamento.route('/equipamentoview')
def view_equipamentos():
    return render_template('equipamento/view_equipamento.html')

@equipamento.route('/equipamentodel')
def del_equipamentos():
    return render_template('equipamento/del_equipamento.html')