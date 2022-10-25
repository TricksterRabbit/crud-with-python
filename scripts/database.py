from app import create_app
from app.databases import db

from app.models.user import User  # noqa: F401


def create_tables():
    app = create_app()

    with app.app_context():
        db.create_all()
