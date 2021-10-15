from flask import Blueprint

from .account import account_blueprint
from .device import device_blueprint
from .spotify import spotify_blueprint

v1_blueprint = Blueprint('v0', __name__, url_prefix='/v0')
v1_blueprint.register_blueprint(account_blueprint)
v1_blueprint.register_blueprint(device_blueprint)
v1_blueprint.register_blueprint(spotify_blueprint)
