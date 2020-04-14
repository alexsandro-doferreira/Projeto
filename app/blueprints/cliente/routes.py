from flask import render_template
from flask_login import login_required
from . import cliente

@cliente.route('/clientes')
def lista_clientes():
    return render_template('cliente/cliente.html')

@cliente.route('/clienteadd')
def add_clientes():
    return render_template('cliente/add_cliente.html')

@cliente.route('/clienteedit')
def edit_clientes():
    return render_template('cliente/edit_cliente.html')

@cliente.route('/clienteview')
def view_clientes():
    return render_template('cliente/view_cliente.html')

@cliente.route('/clientedel')
def del_clientes():
    return render_template('cliente/del_cliente.html')