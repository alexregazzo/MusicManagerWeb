from flask import Blueprint

from .v0 import v1_blueprint

api = Blueprint('api', __name__, url_prefix='/api')
api.register_blueprint(v1_blueprint)
