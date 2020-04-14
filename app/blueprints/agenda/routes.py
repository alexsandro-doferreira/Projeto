from flask import render_template
from flask_login import login_required
from . import agenda

@agenda.route('/agendas')
def lista_agendas():
    return render_template('agenda/agendas.html')

@agenda.route('/agendaadd')
def add_agendas():
    return render_template('agenda/add_agenda.html')

@agenda.route('/agendaedit')
def edit_agendas():
    return render_template('agenda/edit_agenda.html')

@agenda.route('/agendaview')
def view_agendas():
    return render_template('agenda/view_agenda.html')

@agenda.route('/agendadel')
def del_agendas():
    return render_template('agenda/del_agenda.html')