from flask import render_template
from flask_login import login_required
from . import home

@home.route('/')
def index():
    return render_template('home/index.html')

@home.route('/painel')
def painel():
    return render_template('home/painel.html')

@home.route('/cliente')
def cliente():
    return render_template('cliente/cliente.html')

@home.route('/equipamento')
def equipamento():
    return render_template('equipamento/equipamentos.html')

@home.route('/agenda')
def agenda():
    return render_template('agenda/agendas.html')

@home.route('/os')
def os():
    return render_template('os/oss.html')

@home.route('/sobre')
def sobre():
    return render_template('home/sobre.html')