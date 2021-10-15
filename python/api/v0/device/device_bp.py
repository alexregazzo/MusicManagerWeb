from flask import Blueprint

device_blueprint = Blueprint('device', __name__, url_prefix='/device')


# @device_blueprint.route("/register", methods=["POST"])
# def device_register():
#     return "XDB"


@device_blueprint.route("/disable", methods=["PUT"])
def device_disable():
    return "XDB"
