import os
import secrets

from flask import Flask, send_file
from flask_cors import CORS

import settings
from python.api import api

app = Flask(__name__, static_folder=os.path.join(settings.ROOT_PATH, 'build'), static_url_path='')
cors = CORS(app, origins="*")
app.register_blueprint(api)

app.secret_key = secrets.token_hex(20)


@app.route("/")
def index():
    return send_file(os.path.join(settings.ROOT_PATH, 'build/index.html'))


if __name__ == "__main__":
    app.run(port=8855, debug=True)
