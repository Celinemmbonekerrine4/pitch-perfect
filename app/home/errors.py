from flask import render_template
from app import app
from . import home

@home.app_errorhandler(404)
def four_Ow_four(error):

   return render_template('fourOwfour.html'),404