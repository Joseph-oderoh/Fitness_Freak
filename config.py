import os
class Config:

   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:health@localhost/health'
   SECRET_KEY = os.environ.get('SECRET_KEY')
   
    
class ProdConfig(Config):
   pass   

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:health@localhost/health'


    

class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    # '''
    
    pass

    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig  
} 