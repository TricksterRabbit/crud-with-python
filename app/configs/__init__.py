from dotenv import load_dotenv
from os import getenv


def init(app):
    load_dotenv()
    # database configs
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("CONNECTION")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
