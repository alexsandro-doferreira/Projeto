from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length

class InsereEquipamentoForm(FlaskForm):
    nome             = StringField('Nome Equipamento', validators=[InputRequired(), Length(min=3)])
    modelo           = StringField('Modelo', validators=[InputRequired(), Length(min=3)])
    marca            = StringField('Marca', Length(min=3)])
    placa            = StringField('Placa', Length(min=3)])
    observacoes      = StringField('Observações', Length(min=3)])
    enviar           = SubmitField('Enviar')