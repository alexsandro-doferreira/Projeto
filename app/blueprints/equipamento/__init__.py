from flask import Blueprint

equipamento = Blueprint('equipamento', __name__)

from . import routes