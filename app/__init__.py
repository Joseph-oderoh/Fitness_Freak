from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    from .nutrition import nutrition as nutrition_blueprint
    app.register_blueprint(nutrition_blueprint)
    

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    

    return app