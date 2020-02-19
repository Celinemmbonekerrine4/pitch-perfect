import os

class Config:
    
     SQL_ALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringaschool:Access@localhost/pitches'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    '''
    child class for the configuration
    '''
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig
}