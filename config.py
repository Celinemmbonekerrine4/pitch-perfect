import os

class Config:
    
     SQL_ALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringaschool:Access@localhost/pitches'


class ProdConfig(Config):
    pass

class DevConfig(Config):

    config_options  = {
        'development':DevConfig,
        'production':ProdConfig
        }