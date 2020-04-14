from flask_sqlalchemy import SQLAlchemy
from passlib.hash import argon2
from flask_login import UserMixin
from datetime import timedelta, date, time, datetime
from sqlalchemy import ForeignKey, Integer, String, Column, DateTime, func
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

db = SQLAlchemy()

def hash_my_password(p):
    return argon2.hash(p)

def check_my_password(u,p):
    return argon2.verify(p, u.password_hash)

class Cadastro(db.Model):
    __tablename__ = 'cadastros'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    razao = db.Column(db.String(50))
    fantasia = db.Column(db.String(50))
    cnpj = db.Column(db.Integer())
    inscricaoestadual = db.Column(db.String(14))
    inscricaomunicipal = db.Column(db.String(14))
    telefone = db.Column(db.Integer())
    cep = db.Column(db.Integer())
    rua = db.Column(db.String(50))
    numero = db.Column (db.Integer())
    bairro = db.Column(db.String(20))
    cidade = db.Column(db.String(20))
    estado = db.Column(db.String(30))
    pais = db.Column(db.String(30))
    usuario = db.relationship('Usuario', backref='cadastros')
    cliente = db.relationship('Cliente', backref='cadastros')

    def __init__(self, razao, fantasia, cnpj, inscricaoestadual, inscricaomunicipal, telefone, cep, rua, numero, bairro, cidade, estado, pais):
        self.razao = razao
        self.fantasia = fantasia
        self.cnpj = cnpj
        self.inscricaoestadual = inscricaoestadual
        self.inscricaomunicipal = inscricaomunicipal
        self.telefone = telefone
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.pais = pais

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    email = db.Column(db.String(50))
    password_hash = db.Column(db.String(250))
    cadastro_id = db.Column (db.Integer, db.ForeignKey('cadastros.id'), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.cadastro_id = user_id

class Cliente(db.Model, UserMixin):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    email = db.Column(db.String(50))
    password_hash = db.Column(db.String(250))
    cadastro_id = db.Column(db.Integer, db.ForeignKey('cadastros.id'), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.cadastro_id = user_id

class Equipamento(db.Model):
    __tablename__ = 'equipamentos'
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    nome = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    marca = db.Column(db.String(50))
    placa = db.Column(db.String(50))
    observacoes = db.Column(db.String(1000))
    agenda = db.relationship('Agenda')

class Agenda(db.Model):
    __tablename__ = 'agendas'
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    equipamento_id = db.Column(db.Integer, db.ForeignKey('equipamentos.id'), nullable=False)
    datahora = db.Column(db.DateTime)
    os = db.relationship('Ods')

class Ods(db.Model):
    __tablename__ = 'Odss'
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    agenda_id = db.Column(db.Integer, db.ForeignKey('agendas.id'), nullable=False)
    descricao = db.Column(db.String(1000))
    pecas = db.Column(db.String(1000))
    custo = db.Column(db.String(1000))
    datahorainicio = db.Column(db.DateTime)
    datahoraconclusao = db.Column(db.DateTime)