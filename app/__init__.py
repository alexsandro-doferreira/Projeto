from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from app.models.models import db, Usuario
from config import app_config
import os
from flask_mail import Mail, Message

migrate = Migrate()
bootstrap = Bootstrap()
login_manager = LoginManager()
config_name = os.environ.get('FLASK_ENV')
mail = Mail()
print(config_name)
def create_app(config_filename='config.py', cfg_name=config_name):      # app factury
    app = Flask('teste', template_folder='app/templates')
    app.config.from_object(app_config[cfg_name])
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    login_manager.login_view = 'auth.login_get'
    
    from .blueprints.auth import auth
    from .blueprints.agenda import agenda
    from .blueprints.cliente import cliente
    from .blueprints.cadastro import cadastro
    from .blueprints.equipamento import equipamento
    from .blueprints.home import home
    from .blueprints.os import os
    
    app.register_blueprint(auth)
    app.register_blueprint(agenda)
    app.register_blueprint(cliente)
    app.register_blueprint(cadastro)
    app.register_blueprint(equipamento)
    app.register_blueprint(home)
    app.register_blueprint(os)
    app.register_error_handler(404, page_not_found)
    
    return app
    
def page_not_found(e):
    return render_template('home/404.html'), 404
        
@login_manager.user_loader
def load_user(user_id):
	return Usuario.query.get(int(user_id))