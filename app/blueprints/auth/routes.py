from flask import render_template, redirect, flash
from . import auth
from .forms import FormRegistro, FormLogin
from ... import db
from ... models.models import Usuario, check_my_password
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bootstrap import Bootstrap

#from...import db


#@auth.route('/')
#def index():
#    return 'Hello from auth.index'

@auth.route('/registrar', methods=['GET'])
def registrar_get():
    form=FormRegistro()
    return render_template('auth/registro.html', form=form)

    
@auth.route('/registrar', methods=['POST'])
def registrar_post():
    form= FormRegistro(request.form)
    if form.validate_on_submit():
        print (form.nome.data, form.email.data, form.password.data)
        try:
            novo_usuario=Usuario( nome     = form.nome.data,
                                  email    = form.email.data,
                                  password = form.password.data) 
            db.session.add(novo_usuario)
            db.session.commit()
            flash ('Usuário inserido com sucesso', 'success')
            return redirect('/login')
        except Exception as e:
            flash ('Ferrou' + str(e), 'danger')
            return redirect ('/registrar')
    else: 
        print (form.errors)
        flash ('Dados inválidos' +str(form.errors), 'danger')
        return redirect ('/registrar')

@auth.route('/login', methods=['GET'])
def login_get():
    form=FormLogin()
    return render_template('auth/login.html', form=form)
        
@auth.route('/login', methods=['POST'])
def login_post():
    form=FormLogin()
    
    if form.validate_on_submit():
        try:
            usuario=Usuario.query.filter_by(email=form.email.data).first()
            print('ok', usuario)
            if usuario is not None and check_password_hash(usuario.password_hash, form.password.data):
                
                login_user(usuario)
                flash ('Beleza', 'success')
                return redirect('/')        
            else:
                flash ('Dados invalidos!2' +str(e), 'danger')
                return redirect('/login')
           
        except Exception as e:
            flash ('Ferrou' +str(e), 'danger')
            return redirect ('/login')
    else: 
        print (form.errors)
        flash ('Dados inválidos' +str(form.errors), 'danger')
        return redirect ('/login')

@auth.route('/logout', methods=['GET'])
def logout():
    logout_user()
    flash('Desconectado', 'success')
    return redirect('/login')

@auth.route('/password', methods=['GET'])
def password_get():
    form=FormRegistro()
    return render_template('auth/password.html', form=form)