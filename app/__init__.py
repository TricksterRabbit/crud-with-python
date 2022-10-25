from flask import Flask

from app import configs, databases
from app.api import user


def create_app():
    app = Flask(__name__)

    configs.init(app)
    databases.init(app)
    user.init(app)

    return app
