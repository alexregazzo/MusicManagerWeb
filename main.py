from flask import Flask
import settings

app = Flask(__name__)


@app.route("/")
def index():
    return "Pagina inicial"


if __name__ == "__main__":
    print("Iniciando app")
    app.run()
