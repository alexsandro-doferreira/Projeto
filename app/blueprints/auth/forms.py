from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo

class FormRegistro(FlaskForm):
	nome =StringField('Nome', validators=[InputRequired()])
	email =StringField('Email', validators=[InputRequired(), Email(message='Email Inválido')])
	password = PasswordField('Senha', validators=[InputRequired(), Length(min=8)])
	password2 = PasswordField ('Confirme sua Senha', validators=[InputRequired(),EqualTo('password')])
	submit = SubmitField('Enviar')
	
class FormLogin(FlaskForm):
	email = StringField ('Email', validators = [InputRequired(), Email(message='Email invalido!')])
	password = PasswordField ('Senha', validators=[InputRequired(),EqualTo('password')])
	submit = SubmitField('Log in')

class InsereUsuarioForm(FlaskForm):
    nome      = StringField('Nome',validators=[InputRequired(),Length(min=3)])
    email     = StringField('Email',validators=[InputRequired(),Email(message='Insira um email válido.')])
    password  = PasswordField('Senha',validators=[InputRequired(),Length(min=6)])
    password1 = PasswordField('Confirme a senha',validators=[InputRequired(), EqualTo('password')])
    enviar    = SubmitField('Enviar')