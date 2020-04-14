from flask import render_template
from flask_login import login_required
from . import cadastro

@cadastro.route('/cadastros')
def lista_cadastros():
    return render_template('cadastro/cadastros.tpl')