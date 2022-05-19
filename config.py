import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moureen:12345@localhost/fitness_freak'
    SECRET_KEY ='qwerty'
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT =587
    MAIL_USE_TLS =True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql://'
    SECRET_KEY = 'qwerty'
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moureen:12345@localhost/fitness_freak_test'


class DevConfig(Config):
    DEBUG = True

config_options= {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}