from flask import Blueprint
main = Blueprint('home',__name__)
from . import views,errors


