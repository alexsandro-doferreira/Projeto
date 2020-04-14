from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length

class InsereCadastroForm(FlaskForm):
    razao              = StringField('Razão Social', validators=[InputRequired(), Length(min=3)])
    fantasia           = StringField('Nome Fantasia', validators=[InputRequired(), Length(min=3)])
    cnpj               = IntegerField('CNPJ', validators=[InputRequired(), Length(min=3)])
    inscricaoestadual  = StringField('Inscrição Estadual', Length(min=3)])
    inscricaomunicipal = StringField('Inscrição Municipal', Length(min=3)])
    telefone           = IntegerField('Telefone', validators=[InputRequired(), Length(min=3)])
    cep                = IntegerField('CEP')
    rua                = StringField('Logradouro', validators=[InputRequired(), Length(min=3)])
    numero             = IntegerField('Número', validators=[InputRequired(), Length(min=3)])
    bairro             = StringField('Bairro', validators=[InputRequired(), Length(min=3)])
    cidade             = StringField('Cidade', validators=[InputRequired(), Length(min=3)])
    estado             = StringField('Estado', validators=[InputRequired(), Length(min=3)])
    pais               = StringField('País', validators=[InputRequired(), Length(min=3)])
    enviar             = SubmitField('Enviar')