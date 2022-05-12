from flask import Blueprint
main = Blueprint('main',__name__)

# from app import views
from .views import *