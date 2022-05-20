import os
class Config:

   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:health@localhost/health'
   SECRET_KEY = os.environ.get('SECRET_KEY')
   
    
class ProdConfig(Config):
    URI= os.getenv('DATABASE_URL')
    if URI and URI.startswith('postgres://'):
        URI = URI.replace('postgres://', 'postgresql://', 1)
        
    SQLALCHEMY_DATABASE_URI = URI

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
