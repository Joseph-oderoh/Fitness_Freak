import os

class Config:

#    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://carol:lorac1234@localhost/nutrition'
   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
   SECRET_KEY = os.environ.get('SECRET_KEY')
   SQLALCHEMY_TRACK_MODIFICATIONS=False
   
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://carol:lorac1234@localhost/nutrition'
    

class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    # '''
    
    pass
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://carol:lorac1234@localhost/nutrition'
    
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig  
} 