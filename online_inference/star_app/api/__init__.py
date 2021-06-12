from flask import Blueprint

bp = Blueprint('api', __name__)

from star_app.api import predict