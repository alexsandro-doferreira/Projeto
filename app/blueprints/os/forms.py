from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import InputRequired, Length

class InsereOsForm(FlaskForm):
    descricao         = StringField('Descrição', validators=[InputRequired(), Length(min=3)])
    pecas             = StringField('Peças', validators=[InputRequired(), Length(min=3)])
    custo             = StringField('Custo', Length(min=3)])
    datahorainicio    = DateTimeField('Data e hora Iniciais', Length(min=3)])
    datahoraconclusao = DateTimeField('Data e hora Conclusão', Length(min=3)])
    enviar            = SubmitField('Enviar')