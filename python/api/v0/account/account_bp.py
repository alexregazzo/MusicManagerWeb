import json

from flask import Blueprint, request, session, Response
from datetime import timedelta
from python.api.utils import ensure_response
import python.database.fastcode as fdb

account_blueprint = Blueprint('account', __name__, url_prefix='/account')


@account_blueprint.route("/login", methods=["POST"])
@ensure_response
def account_login():
    data = request.get_json(force=True)
    username = data["username"]
    password = data["password"]
    user = fdb.selectUserByUsernameValidate(username, password)
    user["use_created_at"] = (user["use_created_at"] + timedelta(hours=3)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    session["id"] = user['use_id']
    del user["use_password"]
    del user["use_password_salt"]
    return Response(json.dumps(user, ensure_ascii=False, indent=4, default=lambda x: x.json()),
                    status=200,
                    content_type='application/json')


@account_blueprint.route("/signup", methods=["POST"])
@ensure_response
def account_signup():
    data = request.get_json(force=True)
    username = data["username"]
    password = data["password"]
    user = fdb.createUser(username, password)
    user["use_created_at"] = (user["use_created_at"] + timedelta(hours=3)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    session["id"] = user['use_id']
    del user["use_password"]
    del user["use_password_salt"]
    return Response(json.dumps(user, ensure_ascii=False, indent=4, default=lambda x: x.json()),
                    status=201,
                    content_type='application/json')
