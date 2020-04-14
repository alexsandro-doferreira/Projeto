from flask import Blueprint

agenda = Blueprint('agenda', __name__)

from . import routes