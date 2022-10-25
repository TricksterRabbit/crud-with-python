from app.databases import db
from app.models.user import User

from app.utils import model_utils


def get_users():
    users = User.query.all()
    return model_utils.model_list_to_json(users)


def get_user_by_id(id):
    user = User.query.filter_by(id=id).first()
    return user.to_json()


def add_user(username, email):

    user = User(username=username, email=email)

    db.session.add(user)
    db.session.commit()


def update_user(id, username, email):

    user = User.query.filter_by(id=id).first()

    user.username = username
    user.email = email

    db.session.commit()


def delete_user(id):
    user = User.query.filter_by(id=id).first()

    db.session.delete(user)
    db.session.commit()
