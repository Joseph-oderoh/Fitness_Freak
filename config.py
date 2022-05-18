import os
class Config:

   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:health@localhost/health'
   SECRET_KEY = os.environ.get('SECRET_KEY')
   
    
class ProdConfig(Config):
   pass   

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:health@localhost/health'
    
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig  
} 