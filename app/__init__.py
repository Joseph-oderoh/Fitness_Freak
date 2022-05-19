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
    
    
    #
    from .health import health as health_blueprint
    app.register_blueprint(health_blueprint)
  
    
    

  
  
   # initializing flask apps 
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    
    return app    
