from http import HTTPStatus

from flask import Blueprint, jsonify, request
from werkzeug.exceptions import HTTPException

from app.services import user_service

user_controller = Blueprint("User", __name__)


@user_controller.route("/users", methods=["GET"])
def get_users():
    user = user_service.get_users()

    return jsonify(user), HTTPStatus.OK


@user_controller.route("/user/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = user_service.get_user_by_id(user_id)

    return jsonify(user), HTTPStatus.OK


@user_controller.route("/user", methods=["POST"])
def new_user():
    email = request.json.get("email")
    name = request.json.get("name")

    user_service.add_user(name, email)

    return jsonify(
        msg="The user has been successfully added"
    ), HTTPStatus.CREATED


@user_controller.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user_service.delete_user(user_id)

    return jsonify(msg="The user has been successfully deleted"), HTTPStatus.OK


@user_controller.route("/user/<int:user_id>", methods=["PUT"])
def upadete_user(user_id):
    email = request.json.get("email")
    name = request.json.get("name")

    user_service.update_user(user_id, name, email)

    return jsonify(msg="The user has been successfully updated"), HTTPStatus.OK


@user_controller.errorhandler(HTTPException)
def http_error_handler(err):
    return jsonify(msg=err.description), err.code


@user_controller.errorhandler(Exception)
def error_handler(err):
    return jsonify(msg="An error ocurred"), HTTPStatus.BAD_REQUEST


def init(app):
    app.register_blueprint(user_controller)
