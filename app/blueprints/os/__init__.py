from flask import Blueprint

os = Blueprint('os', __name__)

from . import routes