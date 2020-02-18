from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(Config_options[config_name])

    bootstrap.init_app(app)

from .home import home as main_blueprint
app.register_blueprint(main_blueprint)


 return app


from app import views
from app import errors
    
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy

def create_app(config_name):
    app=Flask(__name__)

    bootstrap.init_app(app)
    db.init_app(app)
    
