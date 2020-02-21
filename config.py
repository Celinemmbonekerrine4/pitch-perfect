import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQL_ALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringaschool:Access@localhost/pitches'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    pass

class TestConfig(Config):
    SQL_ALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringaschool:Access@localhost/pitch_test'

class DevConfig(Config):
    '''
    child class for the configuration
    '''
    SQL_ALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringaschool:Access@localhost/pitch'

    DEBUG=True


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}